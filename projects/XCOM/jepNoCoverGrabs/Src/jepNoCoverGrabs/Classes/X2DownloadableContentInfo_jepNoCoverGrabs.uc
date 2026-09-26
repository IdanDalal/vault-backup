//---------------------------------------------------------------------------------------
//  jepNoCoverGrabs, 2026-09-26, built by jep for Idi.
//  Viper-family tongue grabs can no longer target a unit in full cover (unless flanked).
//  Rule copied from the Viper King's own Bind (X2Ability_DLC_Day60ViperKing.uc:182-183):
//  X2Condition_Visibility, bRequireNotMatchCoverType, TargetCover = CT_Standing.
//  Grab list lives in Config/XComjepNoCoverGrabs.ini. Every other ability that carries an
//  X2Effect_GetOverHere is logged (tag jepNoCoverGrabs) so the list can be audited.
//---------------------------------------------------------------------------------------
class X2DownloadableContentInfo_jepNoCoverGrabs extends X2DownloadableContentInfo config(jepNoCoverGrabs);

var config array<name> GrabAbilities;

static event OnLoadedSavedGame()
{
}

static event InstallNewCampaign(XComGameState StartState)
{
}

static event OnPostTemplatesCreated()
{
	local X2AbilityTemplateManager Mgr;
	local array<X2DataTemplate> DataTemplates;
	local X2DataTemplate DataTemplate;
	local X2AbilityTemplate Template;
	local X2Condition_Visibility CoverCondition;
	local name AbilityName;
	local int i;

	Mgr = class'X2AbilityTemplateManager'.static.GetAbilityTemplateManager();

	foreach default.GrabAbilities(AbilityName)
	{
		DataTemplates.Length = 0;
		Mgr.FindDataTemplateAllDifficulties(AbilityName, DataTemplates);
		if (DataTemplates.Length == 0)
		{
			`log("not found:" @ AbilityName, , 'jepNoCoverGrabs');
			continue;
		}
		foreach DataTemplates(DataTemplate)
		{
			Template = X2AbilityTemplate(DataTemplate);
			if (Template == none)
				continue;

			CoverCondition = new class'X2Condition_Visibility';
			CoverCondition.bRequireGameplayVisible = true;
			CoverCondition.bRequireNotMatchCoverType = true;
			CoverCondition.TargetCover = CT_Standing;
			Template.AbilityTargetConditions.AddItem(CoverCondition);
		}
		`log("patched:" @ AbilityName @ "templates" @ DataTemplates.Length, , 'jepNoCoverGrabs');
	}

	foreach Mgr.IterateTemplates(DataTemplate, none)
	{
		Template = X2AbilityTemplate(DataTemplate);
		if (Template == none || default.GrabAbilities.Find(Template.DataName) != INDEX_NONE)
			continue;
		for (i = 0; i < Template.AbilityTargetEffects.Length; i++)
		{
			if (X2Effect_GetOverHere(Template.AbilityTargetEffects[i]) != none)
			{
				`log("unpatched GetOverHere-effect ability:" @ Template.DataName, , 'jepNoCoverGrabs');
				break;
			}
		}
	}
}
