//---------------------------------------------------------------------------------------
//  jepReusePCS: turn on reusable PCS the moment RequiredTech finishes (strategy layer).
//---------------------------------------------------------------------------------------
class X2EventListener_jepReusePCS extends X2EventListener;

static function array<X2DataTemplate> CreateTemplates()
{
	local array<X2DataTemplate> Templates;
	local X2EventListenerTemplate Template;

	`CREATE_X2TEMPLATE(class'X2EventListenerTemplate', Template, 'jepReusePCS_ResearchListener');
	Template.RegisterInStrategy = true;
	Template.AddEvent('ResearchCompleted', OnResearchCompleted);
	Templates.AddItem(Template);

	return Templates;
}

static function EventListenerReturn OnResearchCompleted(Object EventData, Object EventSource, XComGameState GameState, Name EventID, Object CallbackData)
{
	class'X2DownloadableContentInfo_jepReusePCS'.static.EnableIfReady("research");
	return ELR_NoInterrupt;
}
