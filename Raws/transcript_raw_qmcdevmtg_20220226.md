**Gdude**: Hello and welcome to the QuiltMC Developers’ Meeting Podcast. The podcast that isn’t really a podcast. If you’re new here, this is just a collection of recordings of each publicly recorded Developers’ Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed on a Mumble server and recorded live. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to QuiltMC.org.

**Gdude**: Well well well, it's me. I appreciate how qk[ ppl join when the event starts. It's j lk yeah, wait that's hppn- now, isn't it? Hehe. Oh hey eone, we're doing the same th we did last wk, or last fortnight. Last biweek. I will be here on Discord. Eone else is on the other end of Mumble where **~~staff~~** is rcrd- eth to mk sure , you know, we're able to put out the podcast later on. It's still a lil early out so we're gg to gv it a few min. Can sbdy on Mumble say sth? Hehe.

Haven King: Hey, hello eone.

**Gdude**: OK, excellent.

A: Hi eone.

**Gdude**: Oh no, 'fortnight'.

It's 'fortnight' w the trad spelling of 'night'. Not the trendy game style.

**Gdude**: Mm hmm. I thk my list is up to date. Excellent. I see your Mythbusters, Silas. Haha. OK, Emma. 

Haven King: That would be a pretty gd April Fools, Skyrising. Try and ~~mod a new religion~~. Haha.

**Gdude**: It wld be pretty gd, you hv to admit.

Haven King: Tt wld be v dfclt, but it wld be pretty funny.

**Gdude**: You know what, I'm not surprised smhw. Someone's gonna end up doing tt at some pt. Let's gv it a couple more min as we wait for ppl to get in here. Alrt, I thk we can prob get started. It's been abt 5 min. So yeah, wlcm to another public Quilt Dev Mtg. I'm gg to try tt agn ltr, don't worry. And we'll j get right into it, I guess. Earthcomputer, I guess you're rdy to talk abt CHASM?

Earthcomputer: Yeah, let me j find the notes.

**Gdude**: And while Earth does tt, if you want to ask any qn, you c use the slash cmd, /ask, and we'll get to them at the end of the mtg. Alrt Earth, whenever you're rdy.

Earthcomputer: Yeah, so Cheater has left me some notes on CHASM. He wasn't able to make it for the mtg. So what's been gg on? He's been dev- a CHASM-Gradle plugin to allow the co-pilot to see changes made by CHASM. For eg, lk added methods and etc. Quite stuff like access wideners will also be avbl for nicks, nicks and interfaces in the chat as necessary. Uh, not sure abt necessary, but thr you go.

Um, the plugin works TM, and I encourage- Cheater encourages, if you're interested in play- ard with CHASM, that he doesn't xpk the current vers to be super stable. You can find it on the CHASM repo, on a separate branch. He's work- on a another vers tt integ w Gradle and hopefully IDs tt will come to a repo near you soon. That's gd enuf I thk.

**Gdude**: Sounds gd to me. I'm sure thr's been a lot of prog on CHASM. Thr's been devlogs gg out on those as well, if aone's missed those, alw worth a read. Uh, OK, thx Earth. Next is me, right? Comy Tooling. Um yeah, most of what we've been doing w tooling is mostly the website. Mostly me, but I've had some help of course. For ppl who are interested in tt, thr was an announce] posted on the comy server abt it. I'm alw look- for fdbk, however I nd to update tt link since we changed how the prvw work_, but it's more of less up to date anyway. But yeah, if you are interested in seeing what the new site is gonna look lk and what's on it, tk a look at that announce] on Comy and gv me some fdbk bcz I cld rly use it.

Super, are you thr? Decompilers?

SuperCoder: Yeah, I'm here. Um, it's been kinda a quiet 2 wk. We've been work- imprv_ ptrn matching on both switch and if statements to mk the MC decompilation btr, hope[[. And tt's abt it.

**Gdude**: Tt's still impt work for that proj tho, gd stuff. Haven, do you have ath to talk regarding Infra?

Haven: Nth super sig, I've done a lil more work on my Maven app. But when I say a lil, lk rly small amt. I know I'm gonna fetch and process lk proxy repo, but tt's basic[ the only prog I've made.

**Gdude**: Alrty. Alex, wld you lk to talk abt Loader?

Alex: Sure, so Glitch's done a lot of work getting us up to date fr upstream, which is- it gets us a lot more closer to get- Qloader to run on newer vers of MC. We've also started publish- non-snapshot rls to Maven. It's still not fully rdy, but it's test[ at the moment. Thr are also two other q useful changes: The envt in a Qmodjson file now uses dedicated underscore server rather than j server, bcz we noticed tt was confuse- some ppl a bit. So tt j clarifies tt, to make sure so tt you don't j lk accident[ change your- set your own envt of your mod to Server, xpk- tt to work for the integ_ server when tt's not q how it works. 

We've also made it so tt mixins and by xtd] CHASM when we get it work-, mixins/CHASM can trgt MOjang-rel_ lib. DFUs (DataFixerUppers), brigaders, Java bridge and AuthLib, w mixins, which is q useful. Esp as they are pretty much made for MC, they are not gnrl lib. Tt's the other th, you can't trgt gnrl lib w mixins at the moment. I'm not sure if this is fn] nd, bcz most lib are pretty gnrl, but you can't do tt ATM.

Thr's also two issues with Qloader, or discussion I want more ppl to look at. And tt's whether we load mods from subfolders in the mod's folder. Tt's Qloader issue #38. Um, it's mostly for whether ppl want to org their mods in a btr way. Basic[ I'd q lk a settlement on tt b4 we rls Qloader properly so tt we don't hv to change tt in the future. And possibly, whether we lim some folders by MC vers. I'm less sure abt tt, but anw tt's issue #38 and #50 basically. I thk tt's abt it for Qloader, basically q a lot of prog.

**Gdude**: Tt's great, excellent work thr. I guess pushing to non-snapshots is why ppl were posting screenshots on ATLauncher show- 'Oh, here's how you use Quilt.'  But I don't think they've actly activated tt fn] on their launcher yet. But it's gd to see tt they pretty much alr hv supt. Alrt, thx Alex. Uh, Aurora, wld you lk to talk on QSL?

Aurora: Yeah, I j nd to thk lk what to say. We got new PRs ~~in the final player~~. So we hv only 3 modules in events. We got the Tags API, but it's straight for 1.18.2. We got the ~~PR pussy~~ merged. We also got a PR of QSL ~~done eating~~ into Qloader. We also got a lot of PR whr you ~~use tools yet~~. We also got Items in ~~API for the final period. Tt's also sth thr~~. Tt's kinda it now. Uh, also, we also got a PR for ~~Voice~~ API in the meantime. Yeah, tt's it.

**Gdude**: Alrt, thx for tt Aurora. As for the Comy Team, not too much news, as some of you hv seen fr the announcements on the comy server, I created an #openings chnl thr. Tt basic[ lists all the staff and other teams tt nd more mmbr. Thr's q a few th to look at in thr. We've got most, actly all the comy teams, exc for mngr. Build Tools, Mappings, then Triage and Worldgen, the QSL teams. Thr's a lot of stuff tobe done, and we cld alw use the help. So if you're interested, you can head over to the comy server, go to the #openings chnl, thr's a listing thr tt you can use. And we've also mentioned the new site here which is part of Comy Tooling. I thk tt's abt it for Comy. Can't thk of ath else, at least, not yet.

Alrt, is thr ath tt aone thr on Mumble wants to talk abt today?

Haven: I guess we hv an announcement of some kind? Do you want to handle it? Shld I or shld you aft the qn?

**Gdude**: I hv no idea what you're talk- abt Haven, I'm sry. But we c mv into the qn now if you'd pref.

Haven: Sure.

**Gdude**: Alrt, then let us tk a look. So as alw, I'm gg to read the qn out, and if I haven't talk_, I'll say my name. I asum the others will do tt as well. But I'll read the qn out and I'll read out who asked the qn. Alrt, haha, I guess we'll go thru these now. 

Silas asks, "When is the new site designed by His Eminence **Gdude** be made the public design of QMC?" PR's open ATM. I'll grab a link for you if sbdy doesn't beat me to it. Thr is one in thr, anw. If you go to the QMC.org referral on Github. I'm mng- too many th to get the link for you RN. Oh, thr you go, thx Emma. Once this goes thru, it'll be up once it's merged basically. I'm not sure what the criteria is bcz thr's not many ppl ard tt have the time and ability to rvw this kind of PR but we'll see how th go at least.

I can tk the nxt one as well. Silas is ask-, "For each mtg, is thr an agenda of items to ask being made internally?" Uh, no, I'm afraid not. The way we usually do it, since ppl are work- lk pretty much up to the time of mtg, is if I don't forget to set a reminder usually, we meet abt 15 min early internally, and then we j go thru all of the teams and see who has sth to talk abt. O/w we don't rly hv much of an agenda. I imagine some of the teams are kp- track of th on their own but o/w thr's no lk specific defined internal structure for th lk tt. It's not a bad idea, I'm just not sure how we cld do it.

Haven: Well, we were first doing the mtg internally b4 they went public. But if thr was lk a big issue, or a big convo we wanted to have, we wld hv it skdl_ b4hd. You know, say, "We'll be talk- abt it at this mtg." We still c do tt, but it j hasn't been sth tt has come up as often. Thr is also tt pause of mtg ard Dec bcz of hte hols and whatnot, so even tho thr were some big dcd] being made then, we j weren't ard to talk abt them. But we cld do tt agn, but it j hasn't come up agn.

**Gdude**: Tt's a fair pt. I'm losing track of th here. Well, Silas is ask- another qn, "When are we get- another new blog entry on the site?" Well, I thk ToffeeMax is actly work- on one. IDK if he's ard ATM, I thk he's busy. But this kinda ties into the Outreach Team. Lk we are plan- on build- a team. I thk it's pretty much done actly, we j nd to get the RFC merged, which wld handle stuff lk blogposts. ~~We should still put stuff thr.~~ Obv[ we want the site to be rebuilt by then as well since the current site doesn't hv pagination or ath j yet. But once tt's over, we can dcd it, then we get the Outreach Team, you shld start seeing more content then.

Alex: Ember asks, "Wld it be possible to have vers specific mod folders lk Forge?" So I briefly touched on this during what I was say-. So currently there's a discussion issue abt this. It's Qloader #50. So basically the ans is yes, it shld be possible, but IDK if this fn] shld be enabled by def. 

**Gdude**: I can hear Alex typing, so I'm asum- he got cut off.

Alex: Oh sorry, I thk tt's j me hold- down my push-to-talk key. So I thk tt's the qn ans_?

**Gdude**: Yeah, I thk so. Haven, do you want to tk teh next one?

Haven: Sure, as soon as I find the qn so I can see exactly what it was. Thr it is OK, so Silas asked, "So QMC has an ~~open colkv~~ page and it basically ans to the comy. And am I the admin thr bcz I'm on the admin board, or bcz I'm on the infra team?" And the ans is: Thr are plans to announce to the comy. I'm try- to kp it not private obv[, it's public and ppl can go thr. And it's evident bcz if you hv one contributor ppl can't contrib. But bcz we aren't launched yet, I didn't want to go ard ask- for money w/o a pdt tt ppl cld be using in xchg for their donations, you know, or in relation to it at least. So tt's why it's not public, or rather not publicised yet. 

As for why I'm the admin thr, it's bcz I'm on the admin board, and I shld get the other admins setup thr as well. Rly tho, as a mmbr of the Infra Team, I nd to submit expenses. If aone else had Quilt-rel expenses, they cld be add_ as mmbr so tt they cld submit those as well. But as far as I know nobody else has. I thk **Gdude** has some hosting expenses he cld potl[ put there as well. But tt's kind of the state of Open Collective ATM is tt nobody else has any expenses to put thr yet.

**Gdude**: Thx for tt Haven. Aurora, wld you lk to take tt one?

Aurora: Yep. "Are thr any plans to ~~add Forge-style initialisations~~ stages to Quilt? It wld potl[ mk a lot of API stuff much more opti_ by allow- two dynamically generated constants ~~extra~~." So I had pull up Forge docu bcz I used Forge a long time ago, so I don't rmb exactly all the specifics. But, how to say tt, but one of hte reasons they hv to use stages and stuff is bcz the energy thread modloading, it's not rly nd_ in our case since we got multi-thread modloading. And so lk, registry stuff, we don't use a ~~deferred~~ registry. The goal is to use the ~~many-armed~~ sys, so for tt thr's an entrypoint to be able for us to do stuff. 

But currently thr's four initialisation stages. You cld say stages, but it's not rly stages. So we have four entrypoints. We hv the pre-launching point, which is b4 MC is even loaded. Tt's for rly, rly, for stuff tt is rly b4. Then we have the main entrypoint, which is run on every site. Currently, it's in QSL, and it runs b4 the registries get locked. Then we have the client entrypoint, which when the MC client instance is created, it's not rly well-defined whr ~~CUTS OUT~~ or when it runs thr's alw the MC client instance running. And thr's the dedi MC server entrypoint. It's kinda not used, since it's kinda rare to use it. It makes stuff tt is strictly lim_ to dedi servers. Each ones, I thk, b4 or after the path loading, I thk b4. So if you want to add a path mod tt has an API, the way it works is tt tt mod defines its own entrypoint. Bcz we do not hv a well-dfn_ mod loading order, so we can't rly xpk a mod to be loaded b4 you also ~~begin the verse~~. 

So yeah, the way we do it is, it's the thing in Fabric land, the API mod dfn its own entrypoint for tt kinda stuff. So ModMenu dfn its own entrypoint for config providers. I thk maybe Trinkets dfn its own entrypoint for Trinkets stuff. Tt's the way we do it. Yeah, and mods are kinda in this waitlist in the wait file load order tt's not rly specified in this ~~CUTS OUT~~. The way I'm working on is dfn_ in the mod manifest. And then, thr's method and loader which allows you to get all the entrypoints by their keys. You can iterate and call tt into pt manually. And tt's what API mods do. They hv their own entrypoints w their own interfaces, then they call their own entrypoints tslv. So it's counted tt their target mod is loaded. Not sure we design needs, tt the design might not need an entrypoint, so it's kinda btr to use entrypoints. Bcz if the mod isn't present, then the entrypoint won't be called. So it's rly useful. I thk it ans tt. We don't rly have any staging stages. At least, it's not dfn_, but entrypoints kinda replace tt by virtue of entirely replacing it.

**Gdude**: Thx Aurora, tt was a v dtl_ ans. Tywus is asking, "Whether we've considered a sys wherein a repo cntn the official listing of Quilt staffers in a human-readable and computer-readable format? Basically for automation and for display on the site." Uh yeah, tt's in our plans. We don't rly know how we wanna do it j yet, and also actly writing tt sys has a lower prio than get- stuff lk the site rdy. But it's sth we definitely want to do, we j don't have an idea of how we want to do it j yet. If you have suggestions tho, you know, we'll tk them of course.

Alex: DEXD asked, "Whether Quilt will have supt for all the vers of MC unlike Fabric?" So v few of the proj will supt all the vers of MC. Only Loader might hv supt, and tt's in the sense tt we're kp- Loader on Java 8 so tt this is a possibility, but we're not actively put- in any work to actly loader Qloader on all the vers of MC. It's j potl[ sth tt Qloader cld do in the future. But proj lk QSL will definitely not supt all the vers of MC. So any mods for all the vers of MC tt were built on Qloader tt were made in the future wld have to do all the work tslv. They wld efkv[ only hv mixins/CHASM basically.

**Gdude**: Yeah, thx for ans- tt. Yeah, I mean I can't rly see Quilt officially supt- all the vers anw. The amt of extra work tt tt tk on its own is lk a lot. And I imagine the same th will hppn as what hppn_ w Fabric, asum- we hv enuf users for it to be a popr idea. You know, w comy proj. But I j can't see it as being a prio for us.

Um, I'm look- at the qn queue and thr's no qn left guys. Does aone hv ath else they want to ask? If you got sth you wanna ask, use the /ask cmd. We still hv plenty of t, so don't be too shy.

Aurora: Also I j wanted to mention, bcz I'm big dum-dum, I forgot tt the final commendarion for ItemSettings API ended today. So the ItemSettings API got merged in QSL.

**Gdude**: Sth hppn_ to the bot thr. So hey, Mumble, c you hear me? OK, gd, gd stuff. OK, tt's a gd num of qn. Thr we go. Yeah, Aurora, you c go ahd and tk tt one.

Aurora: So, where c I find the API submission gdln, I guess? So for QSL thr's a contrib- file tt dictates the PR process, the conventions and more. So tt's one of the entrypoints to see how we do stuff. The other gd th is to look ard in the existing APIs to see how it's done. Then the other stuff tt is not truly written, at least, I don't rmb, oh, it is, it is written. It is first to discuss the fitter, by opening an issue on Github or on Discord too, then we c look into it. Then we mk sure tt thr is no PR tt is made directly. If a PR up for discussion was made, the big risk is tt you either make an API tt is not nd_ for QSL, or it's an API tt's not fit for use. So it's alw best to discuss APIs before make- a PR. So an issue on Github or a discussion on Discord is really nice. But tt's for QSL.

For APIs in Loader, it's a bit dfrt, but I thk it's kinda the same. But contrib- gdln are not the same. But thr might be one Qloader but I'm not sure. Globally it's kinda the same. It's discuss the API, then we can look into if a PR can be made ~~as strong~~. We do not this hesitat to discuss this kind of qn.

**Gdude**: Thx for tt. Well, you know what, I asked for qn and we sure got qn. Chris asked, "Will Hashed exist for old vers of Mojmap in the future?" Rly no reason why it wldn't. Tt's kinda the idea, right? 

Silas is asking, "Who's currently in ctrl of hte QMC acct?" Well, I thk RN i5 is the one w the logins as he set it up OG[. We're wait- for him to not be too busy w uni so tt he c tfr all the logins into our 1Password. Aft tt it will be in ctrl of the Outreach Team and whoever they dcd to put it in thr, or whoever we dcd I guess, since I'll be in thr as well. In add] I have access to it via Tweet Deck, but it's kinda lim_ since I can't mod the profile or ath lk tt. So if you see abdy lk retweeting or tweeting on thr, it's prob me RN, but we'll see abt it later on once the Outreach Team is in place.

Favrito is asking where help is nd_ ATM. I mentioned it earlier, but agn, the #opening chnl on the comy server lists the teams tt nd ppl. You c also hv a look at the various issues on any proj tt you're interested in. I cld also use a bit of help on the Comy Toolings Team but I'm not rly too worried RN. It's chugging along j fine. And yes, sign up for Build Tools of course, that's in thr, it's in the list. So yeah, not much thr to say for tt one, I thk. Haven, I thk tt one's yours.

Haven: Yep, waiting for it to pop up in chat. If it's gg to. Or if it's- IDK.

**Gdude**: Click the stage button. Ah, thr we go. OK.

Haven: So Lembic asks, "If thr is a comy wish to create such a backport, wld thr be a chance tt it wld be considered official aft careful analysis?" This is a tough qn, bcz the bit abt careful analysis mk it seem lk tt you're looking for lk, if thr's a rly gd reason, cld we make it official? And I thk the ans is gonna be, prob not, bcz of the dfrt nd tt a backport wld hv, right? 

You see for a std workflow, we hv QSL and Mappings tt nd to be updated on a rolling update basis. When you're look- at a backport like for older vers, any API updates are gonna be stagnant, you're not gg to hv to worry abt pruning them. You know, MC updates or ath lk tt. So rly it's j an entirely dfrt body of work tt's being done. So the reason I wldn't mk it official is bcz it's totally segmented as far as what nd to hppn and the std core of devs is prob not gg to be v interested in work- on a backport lk tt. 

So tt's prob the main reason I wld be v hesitant to mk such a backport, even if it gains a v large amt of traction, official.

**Gdude**: Thx for tt, Haven. Yeah, Aurora, you cld tk tt one if you lk.

Aurora: OK, ~~~~do you all hv any idea how many days thr are left to~~? Or is it too far away RN? It rly dpd on the proj. For QSL it's usable. We still nd to test a lot to see if it's stable, but it's usable. Cmpr_ to FAPI thr's not as many features, but it's usable. For Qmappings, it's definitely usable, tho thr might be issues w the mob stuff. But tt boils down to ppl actly mapping stuff. But it's well usable RN. Compiler is alr used in a lot of proj. For Loader, I'm not entirely aware whr it is, but seems to be rly close to be able to test it. So tt's great. Build Tools, well, tt's another story, bcz thr's ppl work- on vanilla Gradle, but IDK whr tt is currently. As spoke earlier in the mtg, CHASM has made prog_, but IDK if it's gg tb usable in lk QSL and stuff rly soon, so kinda no for me. So it rly dpd on the proj for now. But we are slowly coming to sth useful globally.

**Gdude**: Thx Aurora. We're at the end of the queue agn. Are thr any more qn tb ask_?  Slab says, No. But for transparency, the devs don't actly see the qns until someone from our Comy Team aprv them, so they're not necs[ guaranteed tb ans_. Use the /ask slash cmd if you want to ask a qn.

Haven: Alrt, so the Nukelore asks, "Lkly it's been asked b4, as well as ans_ in an issue, but is thr any sort ModMenu or lib in Quilt itself? I asum not but you nvr know." Thr hasn't been an official dcd] or ath on this. Currently, a lot of us- The plan tt's being talk_ abt the most is to have ModMenu like more automatable. Tt will operate sort of similarly to how we're planning for FREX (freaks) to operate, whr it will be mntn_ by a outside party, but avbl as an auto DL in a similar way to how QSL will be. It is also possible that yeah FREX equals F.R.E.X., Xander - Grondax's tool. At least tt's how I pronounce it, I'm not sure how other ppl are pronouncing it. But basically, a aprv_ or indoors lib by Quilt tt cb used and incl_ similarly to QSL module, even if it's not actively mntn_ by Quilt developers. However, that is tentative planning and it can definitely change. We cld end up having our own ModMenu for wtvr, but tt's how I see the sitn RN.

**Gdude**: Thx Haven. I see a lot of ppl talk- about how you pronounced FREX (freks) there. But YK how it is.

Haven: Apparently my pronunciation of FREX (freaks) is dfrt from eone else's, heh heh.

**Gdude**: Silas was ask- whr the ~~SeshPod~~ disappeared to. It's still thr, we're not rly using it RN. We used to, but then Discord Events bcm a th, and we kinda j use those now. It's still useful for polls, but we don't rly do tt many of those on this server, so it's j kinda sitting thr until we nd it. Also, I was current but now I'm not bcz I needed to cut down on those a bit. So I'm not sure whether it's still suitable for those, but it prob is. We'll hv a look at it when we run the next poll, I imagine.

I was abt to say we hv no more qn but another one's j come thru. AManCalledSteve who is currently here, "Are there any upcoming dates we shld rmb?" Um, that's a gd qn.  Haven, what do you thk?

Haven: Yeah, YK, we have one date in particular tt's coming up. It cld be impt, some ppl might care abt it. 

**Gdude**: Yeah, maybe, I guess a few ppl might. Hehe.

Haven: So we hv, internally, betw talk- to the devr and eone, tentatively dcd_ tt April 20 mks sense as a initial beta rls for us to work twd here at Quilt. Thr have been a lot of good prog from Loader, thr have been a lot of good prog from QSL, so we're rly rly optimistic abt being able to get eth work- by then. YK we're not talk- abt- lk dep DLing won't be rdy, plugins prob won't be rdy. But it is a beta rls date tt will be usable for mod devt and testing is the goal.

**Gdude**: We can't guarantee any specific level of done-ness for some of the extra proj, but we're pretty happy tt tt's gonna be a rough date for the beta at least. Sorry, I thk I cut into you a lil bit thr, Haven.

Haven: Ah no, it's OK. I was j saying, I'm rly happy. As ppl have pointed out in chat, it'll be marking abt a year since we launched publicly these comy spaces. So it'll be rly fun to hv sth tt's out in the hands of devrs tt mb aren't involved in Quilt dev] specifically but are itrs in following the proj. So that's YK, look- fwd to seeing what eone does and when eone gets involved.

**Gdude**: Will this be on the tmln? I mean, the tmln is gg back and not fwd. But yeah, we can put it on thr. For those tt don't know, the tmln is on the new website as well. So yeah, tt's some news tt some of you might hv been itrs_ in. I'll write tt up smwr as well at some pt. It'll be on the Comy Server aft the mtg. I thk I'll j write it out bcz I thk not eone is gg to hear it here. Or mb I'll j mk them listen to the podcast, hmm.

We have a few qn to go thru here, so we'll kp gg. But if you hv any qn abt the rls, of course, feel free to put those thru as well.

Silas is ask- if the moderator team is diverse enuf in time zones to guar tt thr's alw someone ard. Tt's a gd qn. I blv we chk_, I can't rmb what the ans was at the time, but we do have pretty gd coverage to have at least one person ard. Also, for the times tt I'm awake, I'm pretty much alw avbl, or nearly alw avbl. And for the times tt I'm not, if it does hppn tt there's no moderators or managers ard, the admins sort of have emgy access to act as moderators as well in the worst-case scenario. But I'm not esp worried abt it. We haven't had any problems w it so far. Although I still wld of course lk to expand the moderation team esp considering the server is gg to grow aft tt beta rls. We're gg to nd more ppl at tt pt, so YK don't waste t if you're planning to sign up or apply. Go right ahd, please.

Haven: Cool. So this next qn fr the Nukelore is, "What's the plan with the whole dep DL? Lk will it be limited to QSL? Or all lib and APIs that have been confirmed to not be a danger to the end-user?" So dep DLing, eth we're gg to say abt it is v much in flux. Thr's no RFC yet, so nth is finalised, or even rly had extensive discussion abt it until we have an RFC. So take eth we say with a grain of... salt, yeah, in that it's v much still being dev_ even as an idea.

So the way tt I planned for dep DLing to kinda work, at least in the early stages of Quilt, is QSL only. In quotes really, it'll be restricted to the Quilt Maven repo only, so realistically ath tt we've hosted on thr, whether tt's QSL or eventually, FREX (freaks) right, or some obscure lk JSON lib for some reason. If you wanted to dpd on tt, bcz it's on our Maven repo, you'll be able to, even in the early stages of dep DL-. 

My idea is tt we'll roll out the ability to hv deps DLed from other repo as we dev the DL- infra and mk sure tt we c ensure the security of tt, right, bcz tt is a concern. Tt being said, thr will be blacklisted sites. Lk, Maven Central doesn't like having end-users DL software from them, so we wld not allow ppl to specify dep fr Maven Central. If you wanted to DL sth that was avbl thr, you wld have to set up your own Maven repo. But lk, proxies are j so tt we're not hitting Central w a bunch of traffic. But in short, the end goal is tt you shld be able to use dep DL- for any libs or APIs: QSL, stuff like Cloth Config, ModMenu, what hv you. YK, your tiny little homebrewed lib tt you j want to be able to use auto dep DL- for all of your other projs tt might use it, even if you're the only one using it, you shld be able to do it in the end. Tt's the goal. Alex, do you wanna talk a lil bit abt what you had in mind?

Alex: Uh, yes, so, it's still v much in flux. I rly don't have much to add to tt w/o being misleading.

**Gdude**: Fair enuf. What abt Chris's qn? Am I right in my assumption w tt?

Haven: Chris's qn? IG I'll j state this. "On building the dep DL- in qn, will verified devr also be a possibility? If so, how will it be done?" I thk this is an itrsing qn and it kinda speaks back what we were talking about with FREX (freaks or freks or however you wanna say it) and Grondag being basically what we wld consider a verified devr. 

And the ans is, other verified devr are a possibility, right. If Grondag can do it, surely others can. I thk the qn is, it's rly based on need. We don't wanna have verified devr left right and centre, right. We want to have ppl who are adding to the QSL experience. In the case of FREX, it's a rendering lib and we nd a rendering lib, so we'll bring Grondag in. Later down the road, it's possible tt there'll be verified devr j for hosting ths on our Maven repo. 

I know tt some ppl who were ard v early prob heard abt the registry being thrown ard a bit as being lk a Maven repo being avbl for aone to upload to. Tt's sth I'd still lk to do at some point. It doesn't play into this dep DL- paradigm directly, bcz it wld not be as thoroughly vetted as what we we're gonna say verified devr are. But it wld be an easy way for ppl to not hv to host their own stuff. Tt's a lot of dfrt sys in play as to what a verified devr rly is and what they mean, and none of tt's rly been figured out in a v concrete way. Does tt kind of ans your qn, Chris? I'm lost in chat, so if you want clarification on sth, feel free to ask. But if not, I'll asum we're gd and we c move on to the next qn, which IG I'll also take.

**Gdude**: It's definitely one of yours.

Haven: Yeah. So the qn is what hppn when/if the Maven fails? Well, the Maven fails. So RN the Maven is hosted using a SonioType Nexus. It's hosted on one individual server, which could theoretically fail. But if you've been ard, and if you've been ard for this mtg and for past mtgs, and you've heard me talk- abt my own Maven application sys tt I'm work- on which will not be bound to instances, like VM (virtual machine) or anything at all. It'll kinda be in the aether of AWS's (US telco provider) infra. So tt YK, if the Maven fails, in that case then we hv bigger problems than- YK, a gd amt of the Internet is gg down as well. Bcz tt wld reqr AWS itself to fail. Or for me to f*** up, which can hppn. Hope[[ won't, once we are in a pdtn-rdy phase. but it's possible.

But if we're talk- abt long-term, like archival, lk ten years' down the road from now, what hppn if the Maven fails? That's a great qn as well, and not sth I tt I'm able to ans super well, bcz it's hard to predict where we'll be ten years from now, but hope[[ I'll be able to kp the Maven running for a while. A big goal of my own Maven sys is tt it'll be much more cost-efkv, down to the pt to that if nobody is req- files, it'll cost me a couple of dollars per month, as opposed to currently sixty, so that I can keep it on for a long long period of time. Great. Hope[[ that ans your qn well enuf, Fabrito. Let's see what else we have here.

**Gdude**: I thk Alex has sth to add on to tt one.

Haven: Yeah, sure, go for it.

Alex: Yes, so, part of tt qn cld be: What hppn if it can't connect to the Maven while doing dep DL-? So what wld hppn then, if lk auto dep DL- cannot work, it j well, fails to DL and will prompt you to go DL it yourself, efkv[. So if dep DL- doesn't work, or the Maven doesn't work, you shld be able to go to a site like CurseForge to get the actual JAR, or possibly in the future, if there are archival sites for this sort of th. So basically, thr shld alw be a way for you to get the libs you actly nd, even if the Maven doesn't work in future.

Haven: Tt's a good callout, which does prompt me to explain a lil bit more on how I envisioned dep DL- working. I don't thk you wld declare... YK it's gonna be kinda similar to how ~~Maven~~ works, where you don't say you need this artifact from this repo. You cld, maybe tt's sth we'll look into, but rly it's gonna be you declare what your deps are and separately declare what repos you want to look in. And so we'll look for all the dep and all the repo until we find them and if we don't find them we'll j gv you the std error like Fabric does, lk 'Hey, you don't have this mod. You nd to install it." Right? Tt's kinda how I see tt wkfl gg.

**Gdude**: Thx for tt, you two. Uh, looks lk I've got a qn here. Silas asks, "What time zone is the most active for Quilt?" Uh, Silas, have you seen this? Haha, bcz tt shld definitely ans your qn. For those who haven't seen it, what I j linked is the stats dashboard for both Discord servers. It mostly looks aft itself, but I kp an eye on it. And honestly it's quite itrsing to j look it over and see what's hppn-. Aside from msg acty and usg acty on both servers, it also includes the suggestions. So if aone wants lk an easy way to browse thru all the suggestions, thr are as well. 

To ans your qn, the comy server is most actv ard 7 pm my time, which is GMT/UTC. And the dev] server/toolchain is most actv ard 4 pm UTC. Oh, and the massive influx of leaves aren't rly leaves. That started hppn- bcz we started kick- ppl who didn't pass mmbr screening within a few days. So tt's what those are. It's not actly ppl lk staying ard and then leaving. It's us kick- ppl tt nvr get thru mmbr screening.

Nobody's offered to take tt qn, haha. Will I take it?

Haven: What qn is it? Oh, bus factor one? Yeah, bus factor for Infra, currently one, because tt's me. Comy Team and Mng], tt's, I mean, a lot of ppl wld hv- It wld hv tb a rly big bus, in a lot of dfrt time zones too. Comy Team and Mng], we're not at a huge risk. As integral and peaceful as **Gdude** is, he's not eone and we have a great supt- comy set up as well. So I thk we wld be able to survive even if **Gdude** sadly didn't. The Development Team, I thk there are a couple of ppl, lk if Alex were to leave, unfortunately, Loader wld nd... at this pt, it's gd enuf, tt we wld be able to get ths working, and Glitch has done well, so I don't thk we're at a huge risk in the dev] space either.

I thk the weakest link is Infra, which is me, which YK, it's hard to shore tt one up. It's hard to find someone who knows the AWS side of ths and is willing to work on it for free. But thr is an initiative, or at least tt is thr shld be, thr will be at some pt, an initiative to get the access keys out thr, so tt if sth does hppn, someone can kp the lights running even if they're not entirely sure what eth is doing. Tt is sth tt shld be done at some pt and only hasn't bcz of restrictions on my own time.

**Gdude**: As Saf mentioned, now tt the 1Password is setup, bcz there is an Infra vault on thr now, so if you did want to you cld j put them in thr, I thk only the admins have access to it.

Haven: OK, I shld do tt.

**Gdude**: I'll j quickly tk this one, bcz it's been ans_ a few times. "Is the Maven a mod downloader?"" No, it's specifically, it's where we're placing Quilt components and libs to be DL_. It's not for mods. For mods, you use CurseForge for that.

Haven: Right, this one is: "When will Haven be taking an apprentice for the Quilt Infra?" I mean, if sbdy rly wants to learn infra, and wants to learn AWS and stuff, I cld pt you in the direction of some learning materials. Thr's a lot gg on thr. And then eventually, once you have a solid enuf footing in AWS in gnrl, I'll be happy to gv a lil bit of- I mean, rly if aone wants to know how ath tt we're dealing w works, I'll be happy to describe it and gv you an idea of what the architecture looks lk and how ths are interacting. It j prob won't be useful or v ez to ustd unless you hv a reasonable AWS backing. Or at least, YK, IT or whatnot.

**Gdude**: Actly, on that Haven, all tt stuff is v itrsing to me as well, it's j a case of t. But it wld be gd to get more ppl on tt. It's j a v involved set of technology to get to know abt. 

OK, I blv we've gone thru eth. As you've j realised, I j closed the AmA. We're a couple of min over, abt four min over. Usually we finish at abt 5'o clock my time. Is thr ath tt aone on Mumble wants to say?

Haven: IG I c follow up the infra qn real qk. If you are rly itrs_, feel free to DM me. Or ping me in the #infra chnl, either one.

**Gdude**: Excellent. Alrt, I thk tt concludes this mtg. It's been great to have eone here. Thx for coming, thx for eone on Mumble side for coming as well. As annc_, we're aiming for the 20th for Beta. Not j bcz it's the funny number, but bcz it's the same date last year tt Quilt bcm public. So we're looking fwd to tt, and of course well be back agn in two weeks, as alw. Az will work on their own t and get the podcast up when they're able to. So yeah, thx for coming and see you.
