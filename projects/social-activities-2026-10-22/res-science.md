---
type: research
created: 2026-10-22
author: jep
---

# Adult friendship science - evidence base for an activity recommender

Format per line: claim | source (author, year, venue, link) | measured | n / effect | replication | popular claim vs measured.
Status: complete 2026-10-22. "jep inference" marks reasoning beyond the sources.

## 1. Adult friendship formation

- **Hours to friendship** | Hall, J.A. (2018 online, 2019 print), "How many hours does it take to make a friend?", J. Social & Personal Relationships 36(4) | doi 10.1177/0265407518761225 | https://news.ku.edu/news/article/2018/03/06/study-reveals-number-hours-it-takes-make-friend
  - measured: Study 1 = online survey, n=355 adults who moved in last 6 months, retrospective self-estimate of hours with one new person + rated closeness stage; Study 2 = n=112 KU freshmen, two new acquaintances, follow-up at 4 and 7 weeks
  - result: ~40-60 h acquaintance → casual friend; ~80-100 h → friend; 200+ h → close friend (press rounding; Simply Psychology reports model estimates 94 / 164 / 219 h, https://www.simplypsychology.org/news/how-many-hours-does-it-take-to-make-a-friend/)
  - activity type mattered: hanging out, joking, playing video games predicted closeness; hours working together counted much less
  - replication: no independent replication found; hours are self-estimated recall (memory bias), cross-sectional + 7-week window, US college / movers only
  - popular vs measured: popular = "50 hours makes a friend" as a recipe; measured = association between recalled hours and closeness label; Hall himself said people can share years of hours and never become friends. Hours are necessary-ish, never sufficient. Confidence in exact numbers: low; in direction (lots of leisure-type hours needed): medium-high
- **Adams' three conditions** | Rebecca G. Adams (UNC Greensboro sociology), quoted in Alex Williams, "Friends of a Certain Age", New York Times, 13 Jul 2012 | https://legallysociable.com/2014/01/23/the-three-conditions-sociologists-say-are-crucial-for-friendship/ (reprint; NYT original paywalled)
  - claim: proximity + repeated, unplanned interactions + a setting that encourages people to let their guard down and confide
  - status: expert synthesis in a newspaper interview, not a single study; draws on 1950s sociology (Festinger et al. below) and Adams' own friendship research. No effect size exists for the triad as a unit
  - popular vs measured: widely quoted as "science says 3 conditions"; it is a heuristic distilled from the literature. Useful as a checklist; confidence medium
- **Propinquity, Westgate** | Festinger, Schachter & Back (1950), Social Pressures in Informal Groups (MIT, Westgate housing) | https://en.wikipedia.org/wiki/Propinquity
  - measured: friendship nominations among married MIT student residents, by physical distance and "functional distance" (paths residents are forced to walk, e.g., stairwells, mailboxes)
  - result: friendship "determined in large part by physical and functional distance"; residents at stairwell feet / mailboxes got more cross-floor friends
  - caveat: homogeneous 1950 sample (married veteran students, same life stage), observational. The specific percentages circulating online (e.g., "41% next door", "65% within five doors") could not be verified against the original tables
  - recommender use: **functional distance** = being on the path others must walk (the door, the bar, the queue, the sign-in table) beats raw physical closeness
- **Random seat assignment → friendship 1 year later** | Back, Schmukle & Egloff (2008), "Becoming friends by chance", Psychological Science 19:439-440 | doi 10.1111/j.1467-9280.2008.02106.x | https://www.sciencedaily.com/releases/2008/06/080602163842.htm
  - measured: n=54 German freshmen, seats randomly assigned at a one-off intro session; friendship intensity rated 1 year later
  - result: random neighbors (and same-row) rated higher friendship intensity a year later. Random assignment = causal for proximity at first meeting
  - caveat: small n, one cohort, then shared a degree program (so later repeated contact also present). Replication: consistent with later classroom seating studies (e.g., scimex 2023 coverage of assigned seating promoting dissimilar friendships, https://www.scimex.org/newsfeed/assigned-seating-in-class-could-create-unlikely-friendships), direct replication not found
- **Mere exposure, field version** | Moreland & Beach (1992), J. Experimental Social Psychology 28:255-276 | https://savemyexams.com/dp/psychology/ib/17/sl/revision-notes/human-relationships/formation-of-personal-relationships/three-key-studies-of-sociocultural-theories-of-attraction-
  - measured: 4 female confederates attended a lecture class 0/5/10/15 times, never interacted; ~130 students rated them at semester end
  - result: more attendance → higher liking, attractiveness, perceived similarity, without students remembering seeing them
  - recommender use: just showing up to the same room weekly raises liking before a word is spoken. Low cost for a socially anxious person
- **Mere exposure, meta-analyses** | Bornstein (1989), Psychological Bulletin 106(2):265-289, 208 experiments, overall r ~ 0.26 (secondhand figure, small-moderate) | Montoya, Horton, Vevea, Citkowicz & Lauber (2017), Psychological Bulletin 143(5):459-498, ~268 curve estimates from 81 articles | https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/A-re-examination-of-the-mere-exposure/991005635870307891
  - result 2017: inverted U, liking rises with exposures then declines (tedium/satiation). Exact peak number not verified
  - popular vs measured: popular = "familiarity breeds liking, always"; measured = mostly lab stimuli (faces, shapes, words), effect bounded, strongest for brief novel stimuli. Human field evidence = Moreland & Beach, Back 2008
- **Dunbar layers** | Dunbar & Sutcliffe (2012) and Sutcliffe et al. (2012), Br. J. Psychology; social-brain hypothesis | https://www.psy.ox.ac.uk/publications/516499
  - claim: personal networks layer at ~5 / 15 / 50 / 150 (ratio ~3), each layer kept by declining contact frequency; time is the binding constraint; adding a friend tends to displace one
  - evidence: replicated as a pattern in phone-call data, Christmas card lists, online games, Facebook/Twitter (Saramäki et al. 2014 PNAS showed per-person "social signatures" persist even as members turn over)
  - critique: Lindenfors, Wartel & Lind (2021) Biology Letters reanalysed primate brain data, 95% CI for group size too wide (roughly 2-520, recalled figure, not re-verified this session) to support a fixed 150 (https://kottke.org/21/06/the-circles-of-friendship coverage; paper itself not fetched). Layers as a time-budget pattern are better supported than the exact integer 150
  - recommender use: a new friend needs weekly-ish contact to enter the 15-layer; a monthly event can feed the 50/150 layers only


### What makes a setting "friend-generating" (synthesis of section 1)
- Same people, same place, recurring schedule (Back 2008, Moreland & Beach 1992, Dunbar layers)
- Contact is incidental, no invitation needed each time (Adams "unplanned"; Festinger functional distance)
- Leisure-type time with talk, jokes, play (Hall 2019: work hours count less)
- Enough hours: dozens of hours per person to reach casual friend (Hall; low confidence on numbers)
- A moment where disclosure is normal (Adams condition 3)

## 2. Nightclubs, dance, synchrony

- **Synchrony + exertion in dance → bonding** | Tarr, Launay, Cohen & Dunbar (2015), Biology Letters 11:20150767 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4650190/
  - measured: n=264 Brazilian high-school students (mean age 14.8), 60 groups of 3, 2x2 (same vs different moves; full-body vs seated), 10 min; pain threshold (BP cuff, endorphin proxy) + 7-point closeness to in-group and to absent classmates
  - result: synchrony and exertion each raised pain threshold (F=13.98, F=11.31) and in-group closeness (F=5.97, F=5.86, p~0.015); no interaction; **no effect on closeness to people outside the dancing group**
  - limits: teens, one culture, proxy measure only, F stats without standardized effect sizes; bonding was toward the 2 people you danced with
- **Silent disco: synchrony with strangers** | Tarr, Launay & Dunbar (2016), Evolution and Human Behavior 37(5):343-349 | doi 10.1016/j.evolhumbehav.2016.02.004 | https://bura.brunel.ac.uk/handle/2438/12402
  - measured: strangers dancing in small groups with headphones playing the same vs offset music; pain threshold, closeness, weak-link coordination game
  - result (abstract-level): dancing in synchrony raised pain threshold and social closeness toward co-dancers. Full text not retrieved; sample and effect sizes unverified
- **Singing "ice-breaker effect"** | Pearce, Launay & Dunbar (2015), Royal Society Open Science 2:150221 | https://ora.ox.ac.uk/objects/uuid:e02457e7-5a9a-47d5-9bfb-65bf0f08b13f
  - measured: newly formed adult-education classes (singing vs crafts vs creative writing) followed 7 months, closeness at months 1, 3, 7
  - result: singers bonded faster at month 1; **non-singing classes caught up by month 3**. Long-run: any recurring group class bonded people to a similar degree
  - recommender use: synchronous activity is a speed boost; the weekly class format is what carries the long-run bond
- **Synchrony meta-analyses** | Rennung & Göritz (2016), Z. Psychologie, 60 experiments, medium effect of synchrony on prosocial attitudes and behavior, moderated by experimenter effects (https://pmc.ncbi.nlm.nih.gov/articles/PMC5137339/) | Mogan, Fischer & Bulbulia (2017), J. Exp. Social Psych. 72, strongest effect on prosocial behavior | critique: Atwood et al. (2022), expectancy effects may inflate the synchrony-prosociality link (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9987344/)
  - status: effect real in labs, size probably overestimated; replication = contested
- **Local pub vs city-centre bar** | Dunbar, Launay, Wlodarski et al. (2017), "Functional benefits of (modest) alcohol consumption", Adaptive Human Behavior and Physiology 3:118-133 (journal name from press, not verified on publisher page) | https://cherwell.org/2017/01/13/going-to-the-pub-is-good-for-you-say-oxford-researchers/
  - measured: 3 studies: observation of conversations in pubs, questionnaire of patrons, CAMRA national survey (n ~2,000 reported in press)
  - result: people with a "local" (pub where they know the landlord and other regulars personally) reported more close friends (~8 vs ~6, press figure) and higher life satisfaction; city-centre bar drinkers stood in bigger groups and took part less in conversation
  - limits: cross-sectional, funded by CAMRA, self-report, cannot separate cause (sociable people pick locals)
  - recommender use: the variable is **known-by-name regulars + small groups + conversation-possible**, independent of alcohol
- **Nightclub scoring against Adams/Hall (jep inference, medium confidence)**
  - proximity: high (crowded floor)
  - repeated contact: medium, same club weekly gives mere exposure to regulars, but crowd churns and nobody tracks who came
  - unplanned interaction: low-medium, high noise blocks speech; no shared task to start talk
  - confiding setting: low, shouting over music, alcohol, late hour, mating-market framing
  - hours that count: Hall's "hanging out, joking" hours require talk; dancing alone near strangers generates exposure hours, few talk hours
  - synchrony bonus: real, but the bonding studies measured closeness to the 2-4 people you moved in sync WITH; dancing solo to the same beat as a crowd is untested as a bonding route
  - sensory: autistic accounts split, some find loud rhythmic music regulating and talk pressure lower (DJ Mag, https://djmag.com/features/how-can-we-make-clubs-more-accessible-autistic-ravers); advocacy, no trial data
  - upgrade path: the same body skill (hip-hop dance) inside a weekly class or crew practice converts exposure into named, repeated, talk-capable contact (Pearce 2015 class format + Tarr synchrony with specific partners)

## 3. Autistic adults socializing

- **Double empathy problem** | Milton, D. (2012), "On the ontological status of autism: the 'double empathy problem'", Disability & Society 27(6):883-887 | https://doi.org/10.1080/09687599.2012.710008 | summary https://reframingautism.org.au/miltons-double-empathy-problem-a-summary-for-non-academics/
  - type: theoretical paper, no data. Claim = social breakdowns between autistic and non-autistic people are two-way mismatches, not one-sided deficits
  - popular vs measured: often cited as "proven"; it is a framework, tested by the studies below with mixed results
- **Diffusion chain 2020** | Crompton, Ropar, Evans-Williams, Flynn & Fletcher-Watson (2020), "Autistic peer-to-peer information transfer is highly effective", Autism 24(7):1704-1712 | https://www.research.ed.ac.uk/en/publications/autistic-peer-to-peer-information-transfer-is-highly-effective/
  - measured: n=72, chains of 8 retelling a story; autistic, non-autistic, mixed chains
  - result: autistic chains = non-autistic chains on retention; mixed chains lost detail faster; rapport lower in mixed chains
- **Registered replication 2025 (did NOT replicate the main effect)** | Crompton et al. (2025), "Information transfer within and between autistic and non-autistic people", Nature Human Behaviour 9(7):1488-1500 | doi 10.1038/s41562-025-02163-z | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12283400/
  - measured: n=311, same diffusion-chain design, multi-site, preregistered
  - result: no difference in information transfer between matched and mixed chains (autistic communication not deficient, and mixed-chain penalty not found); rapport highest in non-autistic chains; **disclosing diagnosis raised rapport**
  - status: the "autistic-autistic is better" headline from 2020 is weakened; the "autistic people communicate effectively" headline survives
- **Rapport by neurotype matching** | Crompton, Sharp, Axbey, Fletcher-Watson, Flynn & Ropar (2020), Frontiers in Psychology 11:586171 | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.586171/full
  - result: non-autistic pairs highest self-rated rapport; autistic pairs higher than mixed pairs. Small lab sample
- **Real-world dyads** | Morrison, DeBrabander, Jones, Faso, Ackerman & Sasson (2020), Autism 24(5):1067-1080 | https://pubmed.ncbi.nlm.nih.gov/31823656/
  - measured: autistic and non-autistic adults (secondary summary says 40 autistic participants; total n not verified), 10-min chats with an unfamiliar partner of same or other neurotype
  - result (secondary summary, check paper): autistic adults reported more closeness and disclosed more with autistic partners; outside raters rated autistic adults less favorably regardless of partner
- **First impressions** | Sasson et al. (2017), Scientific Reports 7:40700 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5286449/
  - measured: 3 studies, non-autistic observers rate thin slices (seconds) of autistic vs non-autistic people
  - result: less favorable impressions of autistic people within seconds, lower willingness to interact; **bias vanished when observers saw only transcript content** (style drives it, substance does not); Sasson & Morrison (2019), Autism in Adulthood: disclosure + autism knowledge improve impressions (https://journals.sagepub.com/doi/pdf/10.1089/aut.2019.0018)
  - recommender use: settings judged on output (a build, a match result, a dance routine, a critique) and repeated exposure give content a chance to beat first-impression style bias
- **Belonging with autistic peers (qualitative)** | Crompton, Hallett, Ropar, Flynn & Fletcher-Watson (2020), "'I never realised everybody felt as happy as I do when I am around autistic people'", Autism 24(6):1438-1448 | https://nottingham-repository.worktribe.com/output/5141432
  - n=12 (10 women, 21-51), interviews; themes: cross-neurotype understanding, minority status, belonging; authors recommend autistic-led social opportunities
  - meta-synthesis: Watts, Crompton et al. (2024), "A certain magic", 52 qualitative papers: experiences with autistic peers mostly positive, linked to better quality of life (https://durham-repository.worktribe.com/output/3200095)
  - limit: qualitative, self-selected, female-skewed; no outcome trials of autistic-led meetups found
- **Interest-based clubs** | Koegel, Kim, Koegel & Schwartzman (2013), J. Autism Dev. Disord. 43(9):2121-2134 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3672252
  - measured: multiple-baseline single-case design, ~3 high-school students; lunch clubs built on each student's preferred interest
  - result: engagement and initiations to typical peers rose; peers enjoyed it; generalized to similar activities
  - limit: teens, n tiny, no adult RCT of interest clubs found. Direction consistent across Koegel lab studies; confidence medium for "shared interest lowers the cost of initiating"
- **PEERS for Young Adults** | Gantman et al. (2012) pilot RCT, J. Autism Dev. Disord. (https://link.springer.com/doi/10.1007/s10803-011-1350-6); Laugeson et al. (2015) RCT, J. Autism Dev. Disord., doi 10.1007/s10803-015-2504-8
  - measured: 16-week caregiver-assisted group skills program (conversation, entering groups, get-togethers, dating), ages 18-24; 2015: n=22 (12 treatment, 10 waitlist)
  - result: improved social skills knowledge, social engagement frequency (get-togethers), social responsiveness; 2012 pilot = lower self-reported loneliness; gains mostly kept at 16-week follow-up
  - limits: tiny samples, waitlist control, unblinded caregivers, ages 18-24 only, requires a caregiver coach. Hebrew PEERS adaptation exists for adolescents (Rabin, Golan et al. 2018 Autism Research, n=41; 2021 n=82, https://cris.biu.ac.il/en/publications/an-israeli-rct-of-peers-r-intervention-effectiveness-and-the-pred/), no Israeli adult RCT found
  - popular vs measured: "PEERS teaches autistic adults to make friends"; measured = knowledge and get-together counts in short trials, friendship quality long-term untested
- **Loneliness in autistic adults** | Umagami, Remington, Lloyd-Evans, Davies & Crane (2022), Autism, systematic review of 34 studies | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9597154/
  - associated with lower loneliness: having relationships, social-skills programs, self-acceptance, time in online gaming; higher loneliness: anxiety, depression, lack of autism acceptance
  - meta-analysis (Grace et al., UWA, 39 studies): autistic samples lonelier than non-autistic, Hedges g = 0.89 (large); loneliness correlates with anxiety r=.29, depression r=.48 (https://research-repository.uwa.edu.au/en/publications/loneliness-in-autism-and-its-association-with-anxiety-and-depress/)
- **Setting features (qualitative + survey, medium-low confidence)**
  - preference for compact, stable networks and connection through shared activity and mutual interest (Li et al., secondary summary)
  - parallel play (side by side, same activity) preferred by some autistic adults (IPA study, n=22 UK adults, via PMC 8788910 citations)
  - Community participation survey: 70% felt they did not participate enough in social groups; 43% rated social groups important (https://cshp.rutgers.edu/publications/self-reported-community-participation-experiences-and-preferences-of-autistic-adults)
  - "one size does not fit all" for autistic adults 40-78 (co-produced interviews, n=33)
  - structure, predictable schedule, low sensory load: supported by autistic self-report and advocacy, no controlled trial isolating these features found

## 4. Social anxiety, exposure, loneliness interventions

- **Treatment of social anxiety disorder** | Mayo-Wilson et al. (2014), Lancet Psychiatry 1:368-376, Bayesian network meta-analysis, 101 trials, 41 treatments (NICE-funded) | doi 10.1016/S2215-0366(14)70329-3 | https://publichealth.jhu.edu/2014/talk-therapy-not-medication-best-for-social-anxiety-disorder-large-study-finds
  - result: individual CBT (cognitive behavioral therapy, the exposure + belief-testing family) beat no treatment and pill and psychological placebos; vs placebo only CBT and SSRIs/SNRIs stayed significant; CBT recommended first line. Exact g for individual CBT not retrieved
  - status: strong, replicated across meta-analyses; this measures clinical treatment, not leisure activities
- **Safety behaviours** (things done to feel safe that keep anxiety alive: rehearsing lines, avoiding eye contact, staying on the edge) | Taylor & Alden (2011), J. Abnormal Psychology 120(1):129-141, doi 10.1037/a0022127 | Plasencia, Alden & Taylor (2011, 2016) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6773421/
  - result: avoidance-type safety behaviours made conversation partners like the anxious person less and want less future contact; dropping them raised felt authenticity and the anxious person's own desire to interact again
  - recommender use: settings where the task gives a natural reason to be there (dancing in a class, playing a match, volunteering shift) reduce the need for safety behaviours; "just hanging around" settings invite them. jep inference, medium confidence
- **Kindness as exposure** | Trew & Alden (2015), "Kindness reduces avoidance goals in socially anxious individuals", Motivation and Emotion | https://psych.ubc.ca/news/kindness-may-help-socially-anxious-people-relax-says-new-research-by-dr-lynn-alden/
  - measured: n=115 socially anxious undergrads, randomized 4 weeks: acts of kindness vs plain social exposure vs diary control
  - result: kindness group showed the largest drop in desire to avoid social situations. Effect sizes not retrieved; single study, students
  - recommender use: helping roles (volunteering, helping at an event, teaching a skill) are a lower-threat entry for socially anxious people. Confidence low-medium (one RCT)
- **Loneliness interventions, classic** | Masi, Chen, Hawkley & Cacioppo (2011), Personality and Social Psychology Review 15(3):219-266 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3865701 | https://www.sciencedaily.com/releases/2010/09/100907171640.htm
  - 4 strategies: social skills training, social support, more opportunities for social contact, addressing maladaptive social cognition
  - result: randomized trials showed a small but significant average effect; non-randomized designs inflated effects; **among RCTs, interventions targeting maladaptive social cognition (expecting rejection, hypervigilance for threat) worked best**; merely adding contact opportunities did less
  - popular vs measured: popular = "join a group to cure loneliness"; measured = in RCTs, contact alone was weak; changing how the person reads social situations mattered more. Mostly older-adult samples
- **Loneliness interventions, recent** | Hickin, Käll, Shafran, Sutcliffe, Manzotti & Langan (2021), Clinical Psychology Review 88:102066, 28 RCTs meta-analysed | doi 10.1016/j.cpr.2021.102066 | https://discovery.ucl.ac.uk/id/eprint/10135088/
  - result: psychological interventions reduce loneliness, small-moderate pooled effect (g ~ 0.43, secondhand figure); CBT most common and effective; interventions mostly face-to-face, group-based, weekly; heterogeneity substantial
  - other reviews: 2022 older-adult RCT review = mostly small effects; 2024 review of reviews = small-to-moderate effects in meta-analyses, mixed in narrative syntheses; group-based delivery repeatedly appears among the better formats (https://www.mcmasteroptimalaging.org/full-article/23F3F01647686F413021B5BC5FEA6DC0)
- **Graded exposure in practice (jep synthesis, high confidence on principle)**: CBT for social anxiety works by repeated contact with feared situations without safety behaviours, stepped from easier to harder. A weekly activity ladder (show up → do the task → one exchange → one repeat contact → one invitation) maps onto this structure. For a clinical-level case, formal CBT has far stronger evidence than any leisure activity

## 5. Third places and weak ties

- **Third places** | Oldenburg, R. (1989), The Great Good Place (book) | https://en.wikipedia.org/wiki/Third_place
  - claim: informal public places beyond home (1st) and work (2nd): neutral ground, conversation as main activity, regulars, accessible, low profile, playful mood, "home away from home"
  - status: sociological description and argument, not a measured study. Empirical support comes indirectly (Dunbar 2017 "local" pubs; library/cafe studies). Confidence in the regulars + conversation features: medium
- **Strength of weak ties** | Granovetter, M. (1973), American Journal of Sociology 78(6):1360-1380 | https://www.jstor.org/stable/2776392 (abstract; sample details from the paper as commonly reported, not re-read this session)
  - measured: how professional/technical workers in a Boston suburb found jobs (n ~282 survey + 100 interviews): job info more often came via acquaintances than close friends
  - replication: large causal test, Rajkumar et al. (2022) Science, LinkedIn experiment on ~20 million users: moderately weak ties most useful for job mobility
  - popular vs measured: measured = **information flow** (jobs, news) through acquaintances; wellbeing and friendship are a different claim
- **Weak ties and wellbeing** | Sandstrom & Dunn (2014), PSPB 40(7):910-922 | doi 10.1177/0146167214529799 | https://repository.essex.ac.uk/15300/
  - measured: Study 1 students counted interactions with classmates on class days; Studies 2A/2B clicker counts of strong- and weak-tie interactions over days
  - result: days with more weak-tie interactions than usual → more happiness and belonging, within-person
  - status: correlational, students and community samples within the same paper; related later work by Sandstrom's lab (Sandstrom, Boothby & Cooney 2022, J. Exp. Social Psych., week-long "talk to strangers" intervention) targets fear of starting conversations, a separate claim, not verified here. Confidence medium
  - recommender use: a recurring venue gives weekly weak-tie "hellos" that lift mood even before any friendship forms; weak ties are also the pool friends come from
  - Rajkumar link: https://digitaleconomy.stanford.edu/publication/a-causal-test-of-the-strength-of-weak-ties (Science 377:1304-1310, inverted U: moderately weak ties best)

## 6. Men, friendship recession, side-by-side bonding

- **Friendship recession** | Survey Center on American Life (Cox, 2021), "The State of American Friendship: Change, Challenges, and Loss", American Perspectives Survey, May 2021 | https://www.americansurveycenter.org/research/the-state-of-american-friendship/
  - measured: n=2,019 US adults, Ipsos KnowledgePanel online, May 14-23 2021, MoE ±2.4; self-reported count of close friends (relatives excluded, "close" undefined); compared with a 1990 Gallup phone poll (n=1,226)
  - result: men with no close friends 3% (1990) → 15% (2021); men with 6+ close friends 55% → 27%; ~20% of single men reported zero close friends; women with zero = 10%
  - caveat: two different survey modes 31 years apart, single-item measure, US only; size of the drop uncertain. Israel data not found
  - popular vs measured: "men have no friends"; measured = self-reported counts, mode change confounds the trend
- **Side-by-side vs face-to-face** | Wright, P.H. (1982), "Men's friendships, women's friendships and the alleged inferiority of the latter", Sex Roles 8(1):1-20 | https://sk.sagepub.com/ency/edvol/embed/humanrelationships/chpt/friendships-sex-differences-similarities
  - claim: men's same-sex friendships tend to form "side by side" around shared activity; women's "face to face" around talk; **differences vanished in very strong, long-lasting friendships**
  - Caldwell & Peplau (1982), Sex Roles 8: no sex difference in number of friends or time with friends; men emphasized doing things together, women emotional sharing (https://peplau.psych.ucla.edu/wp-content/uploads/sites/141/2017/07/Caldwell-Peplau-82.pdf)
  - status: 1980s US student samples; Wright (1988) urged caution about overstating sex differences. Medium confidence that a shared activity lowers the entry cost for many men; low confidence it is a male-specific rule
  - "shoulder to shoulder" is a popular paraphrase (Men's Sheds slogan), not a phrase from these papers
- **Men's Sheds** (community workshops where men build and repair things side by side) | Milligan et al. (2016), Ageing & Society, scoping review (https://resolve.cambridge.org/core/journals/ageing-and-society/article/older-men-and-social-activity-a-scoping-review-of-mens-sheds-and-other-gendered-interventions/76C6C5DBD76D55AD2717BC4BB421AA4A) | Albrecht et al. (2022) mixed-methods systematic review, 52 studies (35 qualitative) (https://pmc.ncbi.nlm.nih.gov/articles/PMC8928410)
  - result: reported benefits to wellbeing, social isolation, self-rated health; studies small, cross-sectional or qualitative, quality criticized; no RCT; population mostly retired men 50+
  - recommender use: supports "task-centered, hands-on, regular workshop" as a format; evidence weak-moderate, age mismatch with a 37-year-old
- **Tabletop roleplaying for autistic adults** | Atherton, Hathaway, Visuri & Cross (2024), "A critical hit: Dungeons and Dragons as a buff for autistic people", Autism | https://www.plymouth.ac.uk/news/dungeons-and-dragons-can-help-autistic-people-gain-confidence-and-find-their-inner-hero
  - measured: small qualitative study (~8 autistic adults, multi-session campaign + interviews)
  - result: relief from social strain, fast kinship, group participation without masking pressure, character traits carried into daily confidence
  - limits: tiny n, no control; confidence low-medium. Fits the interest-based + structured + recurring pattern

## 7. Volunteering, sport, regular classes

- **Volunteering after widowhood** | Carr, Kail, Matz-Costa & Shavit (2018), J. Gerontology Series B 73(3):501-510 | doi 10.1093/geronb/gbx092 | https://ideas.repec.org/a/oup/geronb/v73y2018i3p501-510..html
  - measured: n=5,882 married adults 51+, Health and Retirement Study 2006-2014
  - result: widowed people who started volunteering 2+ h/week had loneliness similar to still-married volunteers; under 2 h/week no buffer
  - limits: observational, older adults
- **Volunteering dose ~100 h/year** | HRS 12-year follow-up (2023, J. Gerontological Social Work): 60+ volunteers with >100 h/year had lower risk of becoming lonely; <100 h/year no protective effect (https://hrs.isr.umich.edu/bibcite/reference/17128) | German Ageing Survey (Richardson et al. 2025): starting to volunteer → small loneliness drop, β = -0.07, p=0.04 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11726694/) | SHARE incl. Israel (2023): volunteering protective even controlling prior loneliness (https://link.springer.com/10.1007/s10433-023-00788-5)
  - status: consistent direction across 3 large panels, effects small, all observational, all 50+; no meta-analysis for adults under 50 found. **Dose threshold ~2 h/week appears twice**
- **Sport participation** | Eime, Young, Harvey, Charity & Payne (2013), Int. J. Behavioral Nutrition and Physical Activity 10:135, systematic review, 11 studies | https://pmc.ncbi.nlm.nih.gov/articles/PMC4028858
  - result: sport linked to better wellbeing, less distress and stress; **club-based / team sport associated with better outcomes than individual activity**, attributed to the social element
  - update: Eather, Wade, Pankowiak & Eime (2023), Systematic Reviews: team sport > individual sport in adults (https://pmc.ncbi.nlm.nih.gov/articles/PMC10286465/)
  - limits: mostly cross-sectional; healthier, social people self-select into teams
- **Regular classes** | Pearce, Launay & Dunbar (2015) (section 2): recurring adult-education classes (singing, crafts, creative writing) all raised closeness over 7 months; singing faster, others caught up by month 3 | Moreland & Beach (1992) + Back et al. (2008) (section 1): same room, same people, recurring
  - recommender use: a weekly class with a fixed roster delivers proximity + repetition + a shared task + Hall's hours (2 h/week x 26 weeks = 52 h, near the casual-friend threshold, if spent talking with the same people). Arithmetic is jep's, built on Hall's low-confidence numbers
- **Online gaming** | Umagami et al. (2022) review (section 3): time in online gaming associated with lower loneliness in autistic adults. Correlational. Hall (2019): playing video games together counted toward friendship hours

## Design rules for picking activities

1. **Recurring beats one-off: same people, same slot, weekly or more.** A one-time meetup feeds acquaintances only. Confidence high. Back 2008, Moreland & Beach 1992, Pearce 2015, Dunbar layers, Adams 2012
2. **Shared task first, talk second.** Pick settings with a built-in activity (play, build, rehearse, serve) so conversation starts from the task and safety behaviours have less room. Confidence medium-high. Wright 1982, Caldwell & Peplau 1982, Koegel 2013, Taylor & Alden 2011, Men's Sheds reviews
3. **Interest-matched rooms.** Choose groups organized around an existing interest (strategy games, film critique, AI, dance); interest lowers the cost of initiating and lets content beat first-impression style bias. Confidence medium. Koegel 2013, Sasson 2017, Atherton 2024
4. **Talk must be physically possible.** A room where speech is drowned out generates exposure hours, short of the "hanging out, joking" hours Hall found predict friendship. Keep the club for joy and synchrony; never count it as the friendship engine. Confidence medium. Hall 2019, Dunbar 2017 (local vs city-centre bars)
5. **Budget the hours.** Expect roughly 40-60 shared leisure hours with one person before casual friendship, 200+ for close friendship; pick activities that accumulate this within months (2-3 h/week). Confidence low on exact numbers, medium on order of magnitude. Hall 2019
6. **Be a regular someone can name.** Same night, same spot, introduce yourself to the organizer, get known by name: the "local" effect. A functional position (door, setup, scorekeeping) multiplies contacts. Confidence medium. Dunbar 2017, Festinger 1950, Oldenburg 1989
7. **Synchrony as a speed boost, inside a fixed group.** Moving or singing in sync with specific partners speeds early closeness; the bond attaches to the people you synced with, so a dance class or crew beats solo dancing in a crowd. Confidence medium (lab effect real, size likely inflated). Tarr 2015/2016, Pearce 2015, Rennung & Göritz 2016, Atwood 2022
8. **Include at least one autistic-majority or neurodivergent-friendly room.** Autistic adults report belonging and easier rapport with autistic peers; disclosure improves rapport in mixed rooms. Confidence medium-low (2025 replication weakened the transfer finding; belonging data qualitative). Crompton 2020a/b, Watts 2024, Crompton 2025, Morrison 2020
9. **Use a helping role as the anxiety on-ramp.** Volunteering or teaching gives a script and a reason to be there; kindness reduced social avoidance in an RCT; volunteering 2+ h/week tracks lower loneliness. Confidence medium (single RCT; volunteering data observational, 50+). Trew & Alden 2015, Carr 2018, HRS 2023
10. **Climb a graded ladder and drop safety behaviours.** Order activities from low to high social demand, step up once the current rung feels routine; exposure works when avoidance and rehearsed scripts are dropped. If anxiety is clinical, formal CBT outranks any hobby. Confidence high for the principle. Mayo-Wilson 2014, Taylor & Alden 2011, Hickin 2021
11. **Weak ties count from week one.** Every recurring room gives small "hello" contacts that lift mood and form the pool friends come from; measure progress by named weekly contacts first, friends later. Confidence medium. Sandstrom & Dunn 2014, Granovetter 1973, Rajkumar 2022
12. **Contact alone is the weakest lever; pair it with re-reading rejection.** In RCTs, adding contact opportunities helped less than correcting expectations of rejection; pair activities with a habit of logging what happened vs what was feared. Confidence medium. Masi 2011, Hickin 2021

Status: COMPLETE 2026-10-22
