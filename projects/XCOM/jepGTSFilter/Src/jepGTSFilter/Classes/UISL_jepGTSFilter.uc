//---------------------------------------------------------------------------------------
//  jepGTSFilter, 2026-09-28, built by jep for Idi.
//  The Amalgamation Promotion Assistant's GTS alternative (UISL_AmalGTS, 3313946064) rebuilds the GTS
//  class list from its own hash and never checks NumInDeck, so classes switched off with Amalgamation's
//  DisableClass (NumInDeck 0; jepFixes P1c) can still be offered for rookie training.
//  One frame after the list is built, this swaps every Amalgamation class (name Primary_Secondary_Tertiary)
//  with NumInDeck 0 for an allowed class of the same primary (stable per soldier), or drops it when the
//  primary has none left. Non-Amalgamation classes (Keeper etc.) are never touched.
//---------------------------------------------------------------------------------------
class UISL_jepGTSFilter extends UIScreenListener;

var UIChooseClass PendingScreen;

event OnInit(UIScreen Screen)
{
	if (!Screen.IsA('UIChooseClass')
		|| Screen.IsA('UIChooseClass_WOTC_ChooseMyClass')
		|| Screen.IsA('UIChooseClass_ConditionSoldier')
		|| Screen.IsA('UI_SelectSparkClasses_CMC'))
	{
		return;
	}
	PendingScreen = UIChooseClass(Screen);
	// run after every OnInit listener, including UISL_AmalGTS which rebuilds the list synchronously
	Screen.SetTimer(0.05f, false, nameof(FilterPending), self);
}

static function bool IsAmalgamationName(name ClassName)
{
	local array<string> Parts;
	Parts = SplitString(string(ClassName), "_", false);
	return Parts.Length == 3;
}

static function string PrimaryOf(name ClassName)
{
	local array<string> Parts;
	Parts = SplitString(string(ClassName), "_", false);
	return Parts.Length > 0 ? Parts[0] : "";
}

static function bool Offerable(X2SoldierClassTemplate T)
{
	return T != none && T.NumInDeck > 0 && !T.bMultiplayerOnly;
}

function FilterPending()
{
	local UIChooseClass Screen;
	local X2SoldierClassTemplateManager Mgr;
	local X2DataTemplate DataTemplate;
	local X2SoldierClassTemplate T, Pick;
	local array<X2SoldierClassTemplate> NewList, Candidates;
	local XComGameState_HeadquartersXCom XComHQ;
	local array<Commodity> Commodities;
	local Commodity ClassComm;
	local string Primary;
	local int i, Swapped, Dropped;

	Screen = PendingScreen;
	PendingScreen = none;
	if (Screen == none || Screen.m_arrClasses.Length == 0)
		return;

	Mgr = class'X2SoldierClassTemplateManager'.static.GetSoldierClassTemplateManager();

	foreach Screen.m_arrClasses(T)
	{
		if (T == none || Offerable(T) || !IsAmalgamationName(T.DataName))
		{
			NewList.AddItem(T);
			continue;
		}
		// disabled Amalgamation class: find an allowed class with the same primary
		Primary = PrimaryOf(T.DataName);
		Candidates.Length = 0;
		foreach Mgr.IterateTemplates(DataTemplate, none)
		{
			Pick = X2SoldierClassTemplate(DataTemplate);
			if (Pick != none && Offerable(Pick) && IsAmalgamationName(Pick.DataName) && PrimaryOf(Pick.DataName) ~= Primary
				&& NewList.Find(Pick) == INDEX_NONE && Screen.m_arrClasses.Find(Pick) == INDEX_NONE)
			{
				Candidates.AddItem(Pick);
			}
		}
		if (Candidates.Length == 0)
		{
			Dropped++;
			`log("dropped" @ T.DataName @ "(no allowed class left for primary" @ Primary $ ")", , 'jepGTSFilter');
			continue;
		}
		Candidates.Sort(class'UIChooseClass'.static.SortClassesByName);
		Pick = Candidates[(Screen.m_UnitRef.ObjectID * 59 + Swapped) % Candidates.Length];
		NewList.AddItem(Pick);
		Swapped++;
		`log("swapped" @ T.DataName @ "->" @ Pick.DataName, , 'jepGTSFilter');
	}

	if (Swapped == 0 && Dropped == 0)
	{
		`log("GTS list clean," @ Screen.m_arrClasses.Length @ "classes", , 'jepGTSFilter');
		return;
	}

	NewList.Sort(class'UIChooseClass'.static.SortClassesByName);
	XComHQ = `XCOMHQ;
	for (i = 0; i < NewList.Length; i++)
	{
		T = NewList[i];
		ClassComm.Title = T.DisplayName;
		ClassComm.Image = T.IconImage;
		ClassComm.Desc = T.ClassSummary;
		ClassComm.OrderHours = XComHQ.GetTrainRookieDays() * 24;
		Commodities.AddItem(ClassComm);
	}
	Screen.List.ClearItems();
	Screen.m_arrClasses = NewList;
	Screen.arrItems = Commodities;
	Screen.PopulateData();
	`log("GTS list filtered: swapped" @ Swapped @ "dropped" @ Dropped @ "->" @ NewList.Length @ "classes", , 'jepGTSFilter');
}

defaultproperties
{
	ScreenClass = none
}
