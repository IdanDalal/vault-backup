//---------------------------------------------------------------------------------------
//  jepReusePCS, 2026-09-27, built by jep for Idi.
//  PCS behave like weapon upgrades once RequiredTech (default ModularWeapons) is researched:
//  removing or replacing a PCS returns it to storage, no confirm popups, Remove All PCS button on.
//  Mechanism = the vanilla breakthrough's own flag, XComHQ.bReusePCS
//  (X2StrategyElement_XpackTechs.uc:1258-1264, UIInventory_Implants.uc:341-348).
//  Two paths: the ResearchCompleted listener (X2EventListener_jepReusePCS) and a retrofit here
//  for saves where the tech was already done.
//---------------------------------------------------------------------------------------
class X2DownloadableContentInfo_jepReusePCS extends X2DownloadableContentInfo config(jepReusePCS);

var config name RequiredTech;

static event OnLoadedSavedGame()
{
}

static event InstallNewCampaign(XComGameState StartState)
{
}

static event OnLoadedSavedGameToStrategy()
{
	EnableIfReady("load");
}

static function EnableIfReady(string Why)
{
	local XComGameState_HeadquartersXCom XComHQ;
	local XComGameState NewGameState;

	XComHQ = XComGameState_HeadquartersXCom(`XCOMHISTORY.GetSingleGameStateObjectForClass(class'XComGameState_HeadquartersXCom', true));
	if (XComHQ == none)
		return;
	if (XComHQ.bReusePCS)
	{
		`log("bReusePCS already on (" $ Why $ ")", , 'jepReusePCS');
		return;
	}
	if (default.RequiredTech != '' && !XComHQ.IsTechResearched(default.RequiredTech))
	{
		`log("waiting for" @ default.RequiredTech @ "(" $ Why $ ")", , 'jepReusePCS');
		return;
	}

	NewGameState = class'XComGameStateContext_ChangeContainer'.static.CreateChangeState("jepReusePCS: enable reusable PCS");
	XComHQ = XComGameState_HeadquartersXCom(NewGameState.ModifyStateObject(class'XComGameState_HeadquartersXCom', XComHQ.ObjectID));
	XComHQ.bReusePCS = true;
	if (`XCOMGAME != none && `XCOMGAME.GameRuleset != none)
		`XCOMGAME.GameRuleset.SubmitGameState(NewGameState);
	else
		`XCOMHISTORY.AddGameStateToHistory(NewGameState);
	`log("bReusePCS set (" $ Why $ ")", , 'jepReusePCS');
}
