//---------------------------------------------------------------------------------------
//  jepCovertBlock, 2026-11-12, built by jep for Idi (ruling K1).
//  jepFixes lists nine covert actions under Covert Infiltration's CovertActionsPreventRandomSpawn, yet three of
//  them were offered and completed in the live campaign (Launch logs 11-10, 11-11). Cause unknown.
//  This mod does not depend on that filter:
//   1. Every time the world map opens or regains focus, it removes every UNSTARTED covert action whose template
//      is on its own list, strips those names from each faction's pool of pending draws, and (bReplace) lets
//      the faction draw a replacement from what is left, through the game's own AddNewCovertActions.
//   2. Once per map load it logs each faction's offered actions and pending pool, and runs the console
//      commands in ProbeCommands. The pool tells whether Covert Infiltration's filter ran at all (its own
//      blocked names absent) and whether jepFixes' names reached it (jep's names absent).
//  Started actions are never touched. Base-game API only; no Highlander or Covert Infiltration compile dependency.
//---------------------------------------------------------------------------------------
class UISL_jepCovertBlock extends UIScreenListener config(jepCovertBlock);

var config array<name> BlockedActions;
var config bool bReplace;
var config bool bLogState;
var config array<string> ProbeCommands;

event OnInit(UIScreen Screen)
{
	if (UIStrategyMap(Screen) != none)
	{
		RunProbes(Screen);
		LogState();
		Sweep("map init");
	}
	else if (Screen.IsA('UICovertActionsGeoscape') || Screen.IsA('UICovertActions'))
	{
		ReportLeftovers();
	}
}

event OnReceiveFocus(UIScreen Screen)
{
	if (UIStrategyMap(Screen) != none)
	{
		Sweep("map focus");
	}
}

function RunProbes(UIScreen Screen)
{
	local string Cmd, Result;
	local int Part;

	foreach default.ProbeCommands(Cmd)
	{
		Result = Screen.ConsoleCommand(Cmd, false);
		`log("probe [" $ Cmd $ "] returned" @ Len(Result) @ "chars", , 'jepCovertBlock');
		// long values are logged in pieces so no log line is cut
		for (Part = 0; Part * 800 < Len(Result) && Part < 12; Part++)
		{
			`log("probe part" @ Part $ ":" @ Mid(Result, Part * 800, 800), , 'jepCovertBlock');
		}
	}
}

function LogState()
{
	local XComGameStateHistory History;
	local XComGameState_ResistanceFaction FactionState;
	local XComGameState_CovertAction ActionState;
	local StateObjectReference ActionRef;
	local string Offered, Pool;
	local name N;

	if (!default.bLogState)
	{
		return;
	}
	`log("list holds" @ default.BlockedActions.Length @ "blocked names, replace" @ default.bReplace, , 'jepCovertBlock');
	History = `XCOMHISTORY;
	foreach History.IterateByClassType(class'XComGameState_ResistanceFaction', FactionState)
	{
		Offered = "";
		foreach FactionState.CovertActions(ActionRef)
		{
			ActionState = XComGameState_CovertAction(History.GetGameStateForObjectID(ActionRef.ObjectID));
			if (ActionState != none)
			{
				Offered $= string(ActionState.GetMyTemplateName()) $ (ActionState.bStarted ? "(started) " : " ");
			}
		}
		Pool = "";
		foreach FactionState.AvailableCovertActions(N)
		{
			Pool $= string(N) $ " ";
		}
		`log("state" @ FactionState.GetMyTemplateName() @ "met" @ FactionState.bMetXCom @ "| offered:" @ Offered @ "| pool:" @ Pool, , 'jepCovertBlock');
	}
}

function ReportLeftovers()
{
	local XComGameStateHistory History;
	local XComGameState_ResistanceFaction FactionState;
	local XComGameState_CovertAction ActionState;
	local StateObjectReference ActionRef;

	History = `XCOMHISTORY;
	foreach History.IterateByClassType(class'XComGameState_ResistanceFaction', FactionState)
	{
		foreach FactionState.CovertActions(ActionRef)
		{
			ActionState = XComGameState_CovertAction(History.GetGameStateForObjectID(ActionRef.ObjectID));
			if (ActionState != none && !ActionState.bStarted && default.BlockedActions.Find(ActionState.GetMyTemplateName()) != INDEX_NONE)
			{
				`log("LEFTOVER on the covert screen (a path the sweep missed):" @ ActionState.GetMyTemplateName() @ "at" @ FactionState.GetMyTemplateName(), , 'jepCovertBlock');
			}
		}
	}
}

function Sweep(string Tag)
{
	local XComGameStateHistory History;
	local XComGameState NewGameState;
	local XComGameState_ResistanceFaction FactionState;
	local XComGameState_CovertAction ActionState;
	local XComGameState_HeadquartersResistance ResHQ;
	local StateObjectReference ActionRef;
	local array<StateObjectReference> ToRemove, FactionRefs;
	local array<int> PerFaction;
	local array<name> ExclusionList;
	local name N;
	local bool bStale;
	local int i, k, Before;

	if (default.BlockedActions.Length == 0)
	{
		return;
	}
	History = `XCOMHISTORY;
	foreach History.IterateByClassType(class'XComGameState_ResistanceFaction', FactionState)
	{
		k = 0;
		foreach FactionState.CovertActions(ActionRef)
		{
			ActionState = XComGameState_CovertAction(History.GetGameStateForObjectID(ActionRef.ObjectID));
			if (ActionState != none && !ActionState.bStarted && !ActionState.bCompleted
				&& default.BlockedActions.Find(ActionState.GetMyTemplateName()) != INDEX_NONE)
			{
				ToRemove.AddItem(ActionRef);
				k++;
			}
		}
		bStale = false;
		foreach default.BlockedActions(N)
		{
			if (FactionState.AvailableCovertActions.Find(N) != INDEX_NONE)
			{
				bStale = true;
			}
		}
		if (k > 0 || bStale)
		{
			FactionRefs.AddItem(FactionState.GetReference());
			PerFaction.AddItem(k);
		}
	}
	if (FactionRefs.Length == 0)
	{
		return;
	}

	NewGameState = class'XComGameStateContext_ChangeContainer'.static.CreateChangeState("jepCovertBlock sweep");
	for (i = 0; i < ToRemove.Length; i++)
	{
		ActionState = XComGameState_CovertAction(NewGameState.ModifyStateObject(class'XComGameState_CovertAction', ToRemove[i].ObjectID));
		`log(Tag $ ": removing" @ ActionState.GetMyTemplateName(), , 'jepCovertBlock');
		ActionState.RemoveEntity(NewGameState);
	}

	ResHQ = XComGameState_HeadquartersResistance(History.GetSingleGameStateObjectForClass(class'XComGameState_HeadquartersResistance'));
	ResHQ = XComGameState_HeadquartersResistance(NewGameState.ModifyStateObject(class'XComGameState_HeadquartersResistance', ResHQ.ObjectID));
	ExclusionList = ResHQ.CovertActionExclusionList;
	for (i = 0; i < FactionRefs.Length; i++)
	{
		FactionState = XComGameState_ResistanceFaction(NewGameState.ModifyStateObject(class'XComGameState_ResistanceFaction', FactionRefs[i].ObjectID));
		foreach default.BlockedActions(N)
		{
			FactionState.AvailableCovertActions.RemoveItem(N);
		}
		if (default.bReplace && PerFaction[i] > 0)
		{
			Before = FactionState.CovertActions.Length;
			FactionState.AddNewCovertActions(NewGameState, PerFaction[i], ExclusionList);
			`log(Tag $ ":" @ FactionState.GetMyTemplateName() @ "removed" @ PerFaction[i] @ "drew" @ (FactionState.CovertActions.Length - Before) @ "replacement(s), pool left" @ FactionState.AvailableCovertActions.Length, , 'jepCovertBlock');
		}
		else
		{
			`log(Tag $ ":" @ FactionState.GetMyTemplateName() @ "removed" @ PerFaction[i] @ "and cleaned its pool", , 'jepCovertBlock');
		}
	}
	ResHQ.CovertActionExclusionList = ExclusionList;
	`XCOMGAME.GameRuleset.SubmitGameState(NewGameState);
}

defaultproperties
{
	ScreenClass = none
}
