nngdu: "**__Instructions for attendees__**\n\nIf you're here to listen to the meeting, chat in here and ask questions, welcome! We're making use of an AMA system to make everyone's lives easier, so please follow these instructions.\n\nFirstly, wait for the meeting to start and for one of us to open the session. You'll see a message posted in this channel by @AMA when we're ready to take questions - though do note that we'll be opening it before the developers will be answering them, to give you some time to collect your thoughts.\n\n**If you have a question:** Once the session has been opened, use `/ask` to submit a question. It'll be reviewed by the moderation team and, if approved, forwarded to the developers, who will be able to decide if and how they wish to answer it. \n\n**When the question is answered,** the @AMA bot will post an embed in here. If the question will be answered on the stage, the bot will say so as well. **If you're asking a question, make sure you're on the stage channel so you can get your answer!**\n\nWe currently have **no plans** to allow users to raise their hand to ask a question via voice. This may change in future, but we're keeping it simple for now.\n\n\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\n\n**Do not ping meeting participants with your questions,** they'll be ignored - but do be specific about who your question is for when you submit it!\n\nAdditionally, **don't spam the developers with questions** and, as always, **keep your questions appropriate and follow our rules and Code of Conduct.** We will take actions against users that send rule-breaking questions!\n\n\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\n\nWe're hoping for a smooth session, but bear in mind that most of us haven't run a stage like this before. Especially for the first couple of session, we'll still be getting used to the system - so be nice!"

nngdu: Uh, lemme look at my list here. Shall we start w CHASM?

nncheat: Oh! Yes, I was gonna do it a lil bit qk. 

nngdu: You go right ahd.

nncheat: OK, well, first of all, thx eone for coming. CHASM, I've been work- a lil bit on it. We hv a lot of stuff planned out, and for the last few weeks I hvb chopping away at it. I've not put too much priority on it bcz we still nd Quilt pgbuto, and pgbuto are more impt. But look- at it now, it's v well=thot out. Order- bcms super simple bcz we alr talked abt eth for lk hours or days. So I j wanted to say tt, mb don't xpk it for Beta rls or ath. But it's happen- for sure, and I can't wait for other stuff tb done so tt I'll hv t for it.

nngdu: Yeah, it's v much a slow=burn proj, but Ig we saw tt coming, right?

nncheat: Yeah, it's rly j a prio th. We rly nd pgbuto, and we nd the pghs, and we rly nd Mapg, and we rly nd eth else, then we c talk abt CHASM agn.

nngdu: Yeah, tt makes a lot of sense. OK, tt sounds good. nnkrop, wld you lk to talk about Decompilers for a bit?

nnkrop: Uh, yeah sure. So most impt news abt the Decompilers prob tt Quiltflower 1.6.0 hb rls_. On the Github I thk thr's a bigger changelog. It's q big, so I'm gonna go over it in a min by islf. But we are still work- on more impv] for the futr vrsns. Incl- switch xprs]s, which curr[ don't rly decompile well. But also generic impv]s. ~~Assets~~ are one of them, major decompiler issues, as well as ~~recompiler=based issues~~. Uh, we're also fix- gnrl ~~issues thr~~. We're also tryna to get ~~moments of deployment~~. Thr's still a lot of stuff we nd to do, but yeah.

nngdu: Well, gd. It's great to see a new rls coming out, esp w your work and eone else on the Decompilers Team. From what I've seen, it's a rly fantastic proj, honestly. And it's great to see the comy supt come out, like Gradle plugins for it. nnoro, wld you lk to talk abt what the ttinfra hb up to? I know it's not the t.

nnoro: Yeah, so I'm tknl[ not on the ttinfra, but I noticed tt a lot of the Quilt projs use the launcher metadata tt Mojang prvds. And they all parsed it in slightly dffr[ ways, and use it dffr[[. One th tt I did was I consolidated tt so tt it was in kinda one lib tt encompassed all the data tt cld be intro_. And tt way, when wtvr proj Quilt works on it the futr, istd of hv- to re=write all the parsing for the launcher metadata, we cld j use this lib. Tt wld make it a lot easier. J speed up dev], and j kinda test ths when we nd to. It's also public, so if aone h a proj tt also parses this launcher metadata, they can use it. So it was j kinda a way to tk a lot of common code and consolidate it.

nngdu: OK, tt sounds lk good prog for ~~Gravis~~, gd stuff. Yeah, if nnhav was here, I thk we cld chat a bit more abt Infra. But he's just not, so we'll see if he appears ltr. In the mntm, nnalex, wld you lk to chat abt qload?

nnalex: Sure. So, ths I had prev[ tt are rly impt is tt quilt.mod.json is done. I impv_ it. So ppl cld write mods tt use quilt.mod.json, so they'll appear as Quilt mods rather than as Fabric mods to qload. As for new ths, we've deprecated Fabric's metadata and added Quilt's, so most of the t mods will now be importing org.quiltmc.loader.api istd of Fabric when using Loader. Most usefully, we've add_ Quilt entrypoints, and these incl the ModContainer as an arg, which means you don't hv to use= Well, you don't hv to grab them from Qload and chk to see to mk sure tt your mod is null, bcz tt's a bit annoy-, but yeah...

nngdu: OK, sounds lk good prog so far, at least.

nnalex: Uh, I'm not q finished, thr's a bit more. Um, qload is now= qload only has static methods rather than having to use FabricLoader.getInstance(), you can now j use QuiltLoader.getMods() or any of the other methods there dir[, which makes it a lil bit ezr to use. Although we've moved MC=spfc methods to MC=qload, bcz we're work- twd  mv- away fr hv- MC as a core part of Loader. Bcz qload is meant tb use= Or psbl[ meant tb used by other games, we don't want to lk hard=code MC ewhr. So a few MC=spfc ths in the new MC=spfc parts.

The other th, teh second th is tt I've started work on Loader plugins. So these are gonna be v useful for load- mods for cplt[ dffr[ loaders. So foreg thr's curr[ a hacky Liteloader load- mods, and tt will hv tb re=written in sorta a more compat way, ig. A less hacky way, which wld be useful. Evtl[, this is the sorta th tt wld lead to lib= and mod=dl-, but tt hasn't started yet. Hope[[ lk auto mod=upd8- plugins. Not fr Quilt islf, but it shld be psbl to mk them. Tt's abt it for Qload, I thk.

nngdu: OK, sounds good. Alrt, Mapg looks lk we hv nnoro agn. What's gg on w Mapg?

nnoro: Uh, I thk thr's a couple qns tt j got ask_ abt qload.

nngdu: We c do those now, or we c do those at the end. I thk it's prob btr we do those at the end j to mk sure we're not gg over t.

nnoro: Alrt, mapg, let's see, yeah. It's going along well. We are curr[ try- to get= We're try- to get pghs to gnr8 auto[ when the pgsnaps come out, so tt's nice. nncheat will talk a lil bit more abt the technology of pghs. Yeah, Mapg, we've been upd8-, taking in PRs. Um, thr wasn't ath big for 1.18pre1, but we had a lot of mapg get add_ in right b4 21w44a. We hv a PRs, port- commits coming over from Yarn, we're gonna rvw those. Other than that, tech=wise, I finished a cplt= Well, not a cplt re=write, but lk a 70% re=write of the qmap build script. It used tb 1000 lines of Groovy, and I churned tt into 300 lines of Groovy and 1300 lines of Java code. But this makes it a lot more xpnd[ and ez to use, bcz the mapg were rly painful to work w.

**MartrixX** joined the ttmap, I thk smtm in the past two weeks, I don't rmb xk[ when. Yeah, last week. **MartrixX** hb work- on a bunch of other stuff, j kinda of ard mapg. He's done a bunch of work in Enigma. I thk he had some filament stuff tt fixed some issues with package infos. 

He also started a new proj called Draughtsman, and this proj strips all the code from methods and fields and stuff lk tt. Unless the fields are constants, or kinda lk "i = 3". And what tt will be used for is to re=writing how qmap gnr8s it src. Bcz curr[ it goes thru lk 3 dffr[ hoops of gnr8- actl Java src code istd of j run- a decompiler on some stuff tt's rly simple to decompile. And w the impv] in Quilt file and eth, we figr_ thr's an ezr and faster solution=

nngdu: Alrt, tt sounds lk q a lot of prog hb made thr.

nnoro: nncheat, do you wanna talk abt what pghs hb doing in the past couple of weeks.

nncheat: Pghs has seen a lot of dev] over the last few weeks. Luckily, or x4tun[, most of tt hb reverted. But we are abt to stabilise pghs, which is v impt. Bcz we've alw said, pghs has tb stbl. We can't hv pghs chg mid=vrsn or sth, it j doesn't work. But we hv a pghs tt seems tb stbl rn. I've opened an RFC and I pls ask eone to rvw it and pls tell us now if they see any issues. Bcz if tt RFC gets merged, and it's still not stbl, then we might run into trouble ltr. So once the RFC is merged, I'll stabilise pghs by putt- it under rls Maven. And tt shld then be cplt[ usable for devrs as well. So I'm j gonna mark the one qn as well, whr was it? Thr. So yeah, it's SoonTM. It is usable now, but once the RFC is thru, and once I test it once agn w the entire tlcn, see if thr's any issues, once it works, it's gonna go into the rls Maven, and then it's dfnt[ usable. Hope[[ this will happen w/i the next two weeks, until our next mtg.

nngdu: It's exciting stuff to hear, I hv to say.

nncheat: At least sth stbl is here now.

nngdu: OK, nnoro, wld you lk to talk on qsl?

nnoro: Yeah, I j v recently joined the ttqsl so I don't hv v much to say, but uh, qsl hb- Thr's a lot of PRs for qsl. If you feel lk rvw- them, plz go and rvw them, tt wld be great. If you want to write some code for qsl, open up a PR importing a Fabric module or sth lk tt, tt wld also be great. Rn qsl's at the pt whr it nds more dev] bcz thr is a lot of code tt nds tb written for it. And sbdy nds to write tt code. So rvw- tt helps us bcz we nd more eyes on code, and creating PRs also helps us bcz the ttqsl is not large enuf to improt eth from FAPI.

nngdu: Alrighty, I lost my list. Thr it is. Alrt, tt all sounds gd. It wld be great to get more eyes on ths.

nnoro: Yeah, **ADudeCalledLeo** also j said "review networking so nni5 merges it already please". Yes, plz do this.

nngdu: Uh, which PR is tt?

nnoro: I'll pull it up. It is [PR #34](https://github.com/QuiltMC/quilt-standard-libraries/pull/34)

nngdu: Thx **ADudeCalledLeo**. Prfk, prfk. So while we are on tt, if you care abt this part of the API, then plz get some rvws in, even if you're not part of the team. We rly cld use the input. Alrighty, I thk tt covers all of the dev teams, unless any of you has ath else to add? Nope, sounds good. 

I'll j chime in a lil bit on teh ttcomy as is trad. Not a whole ton of ths tt hvb hppn-. O/c we've gained a new staff mmbr, nnem, who you might know from the Modrinth moderation and ~~File~~ moderation teams. She j joined a couple days ago, she's doing great. Hope[[ you guys will get along w her as well. We've also been doing some work on Cozy, as usual. Spfc[ I went to clean up the sgst]s database. Turns out Cozy was submitt- sgst] to islf, smhw. Thk I fixed tt one. But it was pretty funny, I hv to say. 

And o/c, we hv the new stats irfc. If aone lks graphs as much as I do, you c head over to the #stats page and get a lil bit of info on what's gg on on both the servers. I'll link tt in the chnl now, [here it is](http://stats-quilt.gserv.me/public/dashboard/9b181b97-bd7f-4ab0-87ed-3239f9149932)

(nnem: "can also be accessed with `!stats` on either community or toolchain")

But agn, thr's not too much to talk abt on the comy side. A lot of ths hvb hppn- quietly, or they're collab=rel_ ths, so we don't tend to talk too heavily abt them. Altho it might be worth ment- tt we hv grown teh ~~comy callout efforts~~ q a bit. They were j a couple chnls on the comy server prev[, but we've split tt off into anor server, and thr's over twice the number of ppl thr now, which is nice. So ths are gg well comy=wise. Tho o/c we've still got a lot to do. I thk what I'm gonna do next is go thru all the open sgst] and mk sure they're all addr_ and put into hte issue tracker at the v least. But shld be thr soon, hope[[. 

Alrt, so since all the teams hv gone thru what they wanted to talk abt, we will open the floor for qns. Some of them hv alr been ans_. Gnrl[ I wld say we'll go top=down as they are. But if you hv any qns you want to submit, use the /ask cmd, the slash cmd. And we will go thru those shortly. You c put in wtvr qns you lk. Ppl won't necs[ ans them, we do vet them. But yeah, go ahd. J don't, yk, spam the hell out of it.

nncheat: ~~??????~~ Whoops, itrs-. Well, j post and ans it agn bcz it's the first qn in the list.

nngdu: Yeah, if you click the button agn, it will send it agn.

**IMS**: first question: when is it estimated that hashed mojmap will be useable for dev?"

nncheat: I will say= Yeah, I noticed= I wld say aft the RFC is merged. And tt means hope[[ in the next two weeks. nngdu, you take the next one?

nngdu: Yeah, I will tk tt one. I'm gonna read the qn out j for the sake of the recording. 
**sciwhiz12**: "Is there or will there be a canonical list of Quilt developers (particularly those who have qualified for and hold the Quilt Developer role in the Toolchain server)? In addition, will there be a same list for the whole Quilt team (Admin Board, Community Team, and the technical side) on the website?"
Yes, thr are plans for tt. Og[[ we were gonna put it thr on hte website. The website is largely mntn_ by **Fork** who is rly bz atm, and also disagrees w my web dsin style, so we'll see what hppns. But we dfnt[ do hv plans to hv an actl list up thr so eone knows who's rspb for eth. And kp- tt rltv[ up=to=date shouldn't be a huge prbm either, hope[[. But yes, we are plann- on tt.

nnoro: Right, I can also tk this one from Burger. I'll also read it out loud.
**burger**: "How does the mappings team feel about the potential effects quilt mappings could have on loader unity (vs using mojmap)? This doesn't apply to hashed or intermediary, only qm"
So, while loaders are moving twds using Mojmap, Fabric still uses Yarn, so asum- tt loaders are 100% moving to Mojmap is not correct. But I do know tt a lot of projs are csdr- moving to Mojmap to promote cross=loader unity. Such as= I know Canvas has, Iris I thk partially h, Caffeine is csdr- it. Yes, Blaze40 has. 

Now I know a lot of other projs hv started moving twds Mojmaps just for cross=loader unity, and I thk tt's sth tt qmap cld try to solve. We cld try to figr out how to use our mapg on ForgeGradle or sth lk tt. What qmap is, is tt while Mojmap is cplt, it often h rly bad names. Lk ResourceLocation or Myth for MapHelper, comparatively.

 And tt qmap aims to prvd accu, ustd[ names compared to Mojmap's names. Bcz when it comes down to it, Mojmap's names are thr for the devrs of Mojang, who c talk abt them amongst tslv. And they're not focused on creating, yk, a modding API, or good names. Whereas qmap has the focus of creating good names, and focus- on, "OK, what does this do, and why is this a good name?" Versus "OK, this name hb ard since like pre=Alpha, and we haven't touched it since then."

nncheat: I j want to add sth to this qn j for clarification as well. Bcz the qn asked how it afks the loader unity. And the ans is tt it doesn't apply to pghs to bgn w.

I j want to clarify this bcz loader does not care abt qmap. It's impt to note tt the actl mapg are only in the dev env. Once you pbsh your mod via jar it's in teh pghs anw. Or pgim for Fabric. Or I thk Sponge just does straight up Mojmap now. So ito loader unity, it's rly not abt qmap, it's abt using pghs. Which is an entirely dffr[ qn. Ito of using dev env, I'm not sure if Loom h the cpbl] yet, mb. 

But I thk tt dfnt[ sth we want to hv is to allow you to use pghs during dev]. If you choose, so if tt is what you want. Or you can use Yarn if you want. I don't thk we hv any real rsn to not allow it. J to clarify more abt this one.

nngdu: Alrt, thx for tt. Ig I'll take the next one then. Here we go. 

**Kroppeb** is asking when RFC #38 will be merged.
(**Kroppeb**: "RFC 38 has been in Final Comment with no comments for over a month. When can we expect it to be merged?")
Gnrl[ speak-, the admin team is in chrg of ulti[ merge- RFCs, so we do hv a rvw prcs. The admins hv all been xtrm[ bz, x4tun[. But we c crtn[ ping them on tt and mb see if they c take a look at it. But I thk it might be a lil longer than some ppl might be xpk-.

I'll tk this one from **yitzy**, no one's claimed tt one b4. OK **yitzy**, this is a good question.
**yitzy** is asking, "Is there any idea of having some community input on collaboration? There aren't many mod teams as open as quilt who might not be trusted to the same extent."
It's tricky, it's tricky. The prbm w being super=duper transparent abt collab is gnrl[= Well foreg, I've been target_ by ppl tt hvb unhappy w collab exist-. I got doxx'd a few weeks ago. And while we've dealt with it and it's fine, it's kinda impt tt we end up protecting the ppl tt are part of collab. Tho I thk on balance, abs transparency is not unlikely to happen. Tt said, if ath is gonna afk a user lk you on Quilt, I'm still gonna let you know abt it. But I don't thk we're gonna go supe in=depth onto what's hppn- in spfcs on collab. But yeah, it's a gd qn. It's a tricky blnc to make for us, x4tun[. But you gotta do what you gotta do, rly.

nncheat: Um, I thk I j wanna ans this qn, even tho I don't hv a proper ans for it. The qn by **StrikerRocker** is, "How will the official release of Quilt as a whole including QSL be determined?"
The prbm tt we hv rn is tt we hv a lot of ths we wanna do. We want to replace Loom. Loader needs some plugins. QSL, we're still unsure on how much of it is gonna be a wrapper ard FAPI and how much is gonna be new stuff. The ans to tt qn is rly we don't know what an official rls of Quilt wld require. So yeah, I thk for now tt's the ans to the qn unless someone else h a better ans to tt. Cool

nngdu: Alrt, sounds gd. 

nnalex: I'm just ans- the qn from **jamalam**: "I forgot, can Qload load mods with `fabric.mod.json` as well?"
Yes, this has alw been the case. This has alw been psbl. We're j gonna mv Fabric mod load- over to a plugin, rather than being dir[ in Quilt. But tt won't afk how ppl use it. You're still gonna alw be able to use Fabric mods on Qload.

nnoro: Alrt, I got 2. First one from nnem: "How will mapping changes from Yarn end up getting into qmap? Is there any sync system between Yarn and qmap, and if not, is it planned at all?"
(**Emmaffle**: "How many mapping changes from Yarn end up getting into QM? Is there any sync system between Yarn and QM, and if not, is it at all planned?")
No hardened sync sys. What we hv is tools tt c convert the git patch files betw pgim and pghs. And tt allows us to pull over= if thr are rly big or impt chgs we wanna pull over from Yarn, or tt we want flat=out, we c do tt. But most of the stuff h still been in=house dev]. 

And the rsn is tt rn Yarn has slightly more collaborators. But we're qk[ grow-, and I thk we'll soon be able to outpace Yarn with collaborators and new mapg. And that will be pretty gd. I've j been bz, so I haven't been able to make any PRs. But I know tt **MartrixX** hb making a bunch, and tt's been rly help[. And so ppl= So we're start- to get the ball roll-, but w any new proj it tks a while. So we're j kp- up w Yarn for a lil bit j bcz it helps a lil bit more w tt dev].

And then this next qn from **Blodhgarm**, sorry if I pronounced your name wrong: "Will qmap be usable with Forge? (Sorry if it is a stupid question)"
Tt I can't say. It c dfnt[ be used w ForgeLoom which wld then be able to compile to Forge. But then Idk if it wld then work in ForgeGradle. But tt wld be sth tt cld be explored.

nngdu: Sounds gd. Looks lk I've got one I c ans here. **sciwhiz12** is mostly asking abt substantial changes to RFCs and how tt shld work.
(**sciwhiz12**: "For substantial changes to existing RFCs, should they remain as amendments or be proposed as new RFCs? In the latter case, should the new RFC partially supersede the new RFC (adding new clauses or removing existing ones), or should the new RFC fully supersede the existing RFC (so the existing RFC has no more effect)?")
It's a tricky qn to a pt. It dpds honestly. So far honestly, we've kinda been avoiding using the amendment prcs for some ths. Lk w the ttcomy RFC, at least one of the ths we did was re=write several of the prcss thr. And at first I was gonna do an amendment prcs thr, but we had a chat and bsc[ it's much ezr to folw ths if you upd8 the og[ RFC. I don't thk thr's rly a prbm w tt, esp csdr- we do hv the commit history thr. Ig thr are prob ths whr you might want an amendment, but nth rly comes to mind atm. It's not so much tt a new RFC supersedes it. You're upd8 the og[ one. But you're still kp- the history thr in the commit history. So I thk tt works OK, at least so far. But if tt nds to chg, crtn[ it's sth we c look at.

nncheat: I'll tk the vrsn- one as well, bcz I thk it's an iteration of the last one. So the qn by **sciwhiz12** is, "What versioning scheme will or are Quilt's project use? 0=based versioning, or semantic versioning, or other? And is it or will it be different per project, depending on the will of its maintainers?"
I thk the last one is in gnrl most lkly. Hwvr, I do know tt most in Quilt said tt they don't rly lk 0=based vrsn-, so I thk for most stuff it's gonna be some sort of semantic vrsn-. Ik foreg pghs, I'm gonna switch it to 1.0 rls as soon as the RFC is merged. And then thr's some stuff w Qmap tt can't rly be Semver'd, so in gnrl MC=rel_ stuff tt dpds on the MC vrsn can't rly be Semver'd bcz MC doesn't hv numbers, so no promises on the exact format. But in gnrl, don't xpk 0=based vrsn- I thk.

So I'll also claim the next one, so let's kp gg with tt. **Fish** asks, "Will there be noticeable differences between Quilt and Fabric? Does Quilt have technology that would be impossible to port to Fabric?"
First, I wanna ans the second part. No, o/c not. Quilt was ported from Fabric. Quilt is a port of Fabric. Fabric cld j ezy get back eth if they wanted to. But at tt pt, Fabric bcms Quilt. 
But in gnrl, will there be noticeable differences between Quilt and Fabric? Yes, for sure. First off, the default stuff. So, using pghs and pgim istd of pgim. O/c Fabric cld switch over at some pt if they rly wanted to, but idth tt's super lkly. The other big dffr[ is Quiltflower, but I heard tt it might come over to Fabric soonTM, mb. I thk no promises. Then o/c, CHASM doesn't exist yet on Quilt. That might hppn on Fabric but tt one I thk is not as lkly bcz it wld reqr q a few chgs to Loom, which we're gonna make. But unless Fabric j literally takes our new pgbuto, they're not gonna get CHASM any time soon.
Um, what was the last one? I had one more. I 4got one, I had one more in my hand. Oh yes, loader plugins, exactly. Loader plugins are sth tt's gonna be dffr[. If you are wonder- what loader plugins *are*, tt's kinda a dffr[ qn. But one of the things tt's impt to us is to auto[ dl qsl if it's reqr_ so we don't hv users spamm- with "I istl_ Fabric but now it's tell- me tt Fabric is missing." 
So I thk those are a few dffr]s tt shld be noticeable. O/c they cld be ported but I don't xpk them to.

nngdu: Alrighty. nnaurora, are you OK to tk the next one? 

(**yitzy**: "Fabric is somewhat lacking in terms of events, especially world interaction ones, such as a lack of a block place event or screen handler events. Does QSL plan on addressing this, and if so, how far would these interaction events go?")
nnaurora: So, for qsl and events, the goal is to be a std lib, so it shld hv a lot of events to bring eth tgt. And so a block place event or screen handler events are, at least for me, v esnc[ for bring- mods tgt and for irxt-. So irxns of events are rly impt, so you shld xpk see- them in qsl. But when, tt cannot be said bcz it all dpd on what events we will get. But we do want those and we don't want to bikeshed abt them too much either bcz they're impt. I thk tt's it. Oh, I c tk the next qn. 

(**Hubry**: "Has a potential Datagen API been looked into? Having easy access to generating JSONs is very useful, but on Fabric it has been a pretty annoying process to set it up, compared to Forge's default inclusion")
So, datagen will be dfnt[ looked into. Bcz to make big mods wld be a pain to do w/o datagen, that's for sure. Even Mojang uses datagen, so we hv to use datagen. Idk yet how, mb we will try to use Mojang datagen sys, or mb we'll make our own. Curr[ tt's not set in stone. Thr's also plans for runtime datagen. But tt's not rly datagenning JSON. Tt's more lk mk- mod irxns ezr. Lk if you hv a mod tt adds a new wood type, you'd want stuff tb gnr8_ for tt wood type too in your mod. Lk if you add a new item, tt's also planned. But as I said, it's not rly= For now, the impl] is a no. So we'll see in futr. And I thk tt's it for now.

nngdu: Alrt, thx for tt nnaurora. I'll take **sciwhiz12**:'s one, I thk. So **sciwhiz12** is asking wheher the final votes for tknl dcds] will be made public.
(**sciwhiz12**: "Will the final tallies of votes for technical decision (for example, the proposed PR policy's conflict resolution through a team vote) be publicly released alongside the final decision, as part of policy? (I presume the names of those who voted for/against will not be included)")
It's a gd qn. This isn't one tt aone tt any of us c rly ans w/o someone from the Admin Board ard. Regard- RFCs, you'll see those on the RFC PR. Lk, the dscs] is thr, the rvws are thr. You c see what ppl thought of them. For other types of votes, it's hard to say. It's largely gg to dpd on whr they hppn. Foreg, so if sth hppns on Github, it's prob gonna be thru rxns. Mb it's not, a lot of this rly dpds on how the admins want to run tt. X4tun[ none of them are at the mtg this time. Mb they'll be at the next one, so you c ask it agn.

nncheat: I thk also to add onto this, idth it h rly happened yet. I thk thr was one poll so far tt was bsc[ a naming qn. But Idth thr's been any big ones yet, so...

Yeah, I'll ans the next one by **LOCAL** even tho it's a lil bit hard to ans. The qn was, "What major roadblocks remain to QML's public release?"
I'll preface this w some minimal viable product as nngdu calls it. And tt reqrs at least qload, which we did kinda reqrs loader plugins. So a lot of plugins nd to hppn. We nd pgbuto; we hv a vrsn of Loom tt might kinda be gd enuf for lk a Beta rls, but we might wanna switch over to pgvg or sth. So, I'd say rn we're mostly look- at get- some, not rls vrsn, but some beta vrsn of QML out, which is useable. Mb not eth is stbl. 

For the actl rls, it's j unclear what we want to hv for an actl rls. Do we want CHASM if we j do Beta now? Mb we j want CHASM for rls. Do we want a new pgbuto, lk a new integ] w Gradle or sth? It's j unlikely, x4tun[. But for a usable Beta rls, what we need is pgbuto tt are kinda work-, and qload tt is kinda work-. But yeah, I thk tt's it. Oh do we count the next one as well as part of the same qn?

(Transcriber's Note: A **[minimum viable product** (**MVP**)]([Minimum viable product - Wikipedia](https://en.wikipedia.org/wiki/Minimum_viable_product)) is a version of a product with just enough features to be usable by early customers who can then provide feedback for future [product development].

nngdu: Yeah I thk tt was part of the same qn, rly. **Fish** asked if thr's a roadmap and if thr's a rough ETA.
(**Fish**: "This question was probably answered earlier, any roadmap for Quilt?")
It's bsc[ exactly what was j talked abt. For an ETA, I don't blv we're committ- to ath. We were og[[ aim- tentatively for an alpha vrsn for MC 1.18. It's coming a bit sooner than we thot it wld. Tt said, who knows, we'll hv to see what hppns. But we're not committ- to any spfc rls t atm.

I can tk this one. nnaurora asks if thr's ath new on the idea of forums.
(nnaurora: "Anything new on forums? :pineapple:")
No, not rly. We did chat on what we'd use. It's prob gonna be discourse. But o/w we nd to wait on nnhav who is doing most of the infra work. While I cld stand up a forum on my own, on my own srvr, it's rly not ideal at all. We shld set it up on proper Quilt infra, and we nd nnhav for tt. Tt said, I thk he was not plann- on look- into it until we're close to rls? It's hard to say whether he thks we're close enuf at this pt or not. But agn, it's sth we'd hv to ask abt once the admins are here.

Hehe, nnaurora goes, "*Oh*." (*Long pause and brief remark by nncheat.*) I'll take this, I might as well. 
(**Fish**: "Does Quilt have a roadmap, where would it currently be at, and is there a rough estimated time of arrival for the mod loader?"
**Fish**: "To add on to my previous question, is there a publicly viewable roadmap, like Trello, which is a clear roadmap to where Quilt is potentially at right now?")
We don't hv any spfc codified roadmap up atm. It's not a bad idea, it's not a bad idea. Rn, I wld recommend look- at Github and j see- what's gg on thr. It's kinda dfcl to get a cplt roadmap written up at this early stage. 

(nnaurora: "There's this? <https://github.com/orgs/QuiltMC/projects/1>")
nngdu: Yeah, thr is tt proj, I don't thk it's public, I'm not sure. Agn, tt's sth we'll hv to ask the admins abt. Is it public, did they make it public? Finally. Um, lemme hv a qk look at that. Oh yeah, tt's right. Oh well, thr's your ans ig, hahahaha. But it hasn't upd8_ for a while. Yeah, it prob is a bit out=of=date. I thk we'll prob wanna talk to the admins on tt one. But I blv the other teams hv access to touch tt. So if they wanna upd8 it a bit, tt'll be great as well.

OK, I'll tk tt one. Alrt **arathain**. **arathain** is ask- abt Quilt merch.
(**arathain**: "I saw "quilt merch" be addressed once, I think it's reasonable to leave any of that for post-release; anyway, what's "the official stance" on it? What could it entail?")
The official stance is, we don't know. Realistically, we're try- to kp money out of the org as much as we can. Now, while we've talk_ abt this w the admins, largely it's a case of nnhav is pay- for eth tt mostly nds tb paid for. Thr's other ppl ctrb- a lil bit for domains and stuff. But rn we don't rly hv any plans to go further w tt. 

Aft Quilt's rls, we'll prob look into sth lk an Open Collective j to mk sure tt we c get all the infra paid for w/o drain- nnhav's beer money. But Idth we're gonna go super hard in on tt, since we rly don't want to start turn- this into a for=profit endeavour, at all. Oh, that's a gd qn in from **jamalam**, ty **jamalam**.
(**jamalam**: "Any updates on whether there'll be a way to support quilt financially (i.e. to help with infrastructure costs)")

nnsci asked if the Quilt Admin Board is locked to 3 board mmbrs.
(nnsci: "Is the Quilt Administrative Board locked to 3 board members? The Governance RFC provides that nominations are open when there are less than 3 members, yet does not give any indication to my understanding for the possibility of more than 3 members on the board.")
Fr recollection on the Initiative Server, which is bsc[ whr all the initial plann- hppn_, we wanted to hv at least 3 admins. I'm not 100% fmlr bhd the prcs of elect- a new admin, but I thk 3 was dcd_ as j a good number at the t. It might be worth re=visiting tt and j to clarify it. But idth tt thr's a big issue thr. 

Uh, Ig I c take on this?

nncheat: Alrt, I'll j tk this one, tk the first one. **Lith/Heli** is asking, "Any updates on using FREX inside qsl?"
I'm not sure if tt's ref- dir[ to the convo tt was had, but thr was a convo tt was had w **Grondag** talk- abt it. IDK ath else. I'll look if I qk[ c find it, it shouldn't be tt hard. And then I'll j link to it and then you c look at it.

nngdu: While you're look- for tt, **LOCAL** ment_ an odd number of admins is important.
Yes it is. We wanted to make sure tt things couldn't be too stacked by two people. But also, we nd them for tiebreakers. So if we had an even number of admins, tt wouldn't rly work v well. Oh, you found it?

nncheat: Yep.

nngdu: Alrt, Ig I'll try and addr **burger**'s qn. It's not an ez one for sure. **burger** asks, "It seems like many people working on Quilt are busy or can't focus on Quilt in full. From the outside, contributing to quilt or joining the team seems like a large commitment which may dissuade potential new members from joining. Any thoughts?"
I thk tt's a bit of a contradiction. Yes, a lot of ppl are bz and ~~hv focus~~. But we don't reqr tt of ppl, lk eone has a life tt they hv tb living outside of Quilt. And it's impt to us tt they're allowed to do tt. So while yes, ppl are gg tb bz, tt's j how it is. I thk tt it's still a fair concern. Ulti[ tho, being on a team is a rltv[ chill affair. We're not gg tb complain- if you're not give- as much t as we thk you cld or ath. It's rly j a case of gv- what you c. We're not gonna yell at you for it.

nncheat: Yeah, no one's complain- if you're join- a team and then not work- on it, heh. Honestly, if you j join the ttbuto, we're alr happy.

(nngdu and nnoro laugh.)

nncheat: If aone wants to work on Gradle, j say it. Even if it's j a single line in a build script, tt's cool. I thk tt one's for the ttcomy.

nngdu: Yeah, tt's dfnt[ for us. **yitzy** asked abt a showcase or starboard.
(**yitzy**: "Was there a plan for showcasing underused or just generally cool mods or a starboard?")
We do hv plans for a sorta a mod showcase. Aft Quilt rlss obv[ we wanna make use of the site more, and use the blog for more comy=rel_ ths. Nth super=dtl_ rn o/c, bcz it's pre=rls, but yes, we do hv plans. As for starboards, not rly. Thr are sgst] open abt a starboard. But I hv concerns abt how it might be used and how we might moderate it on top of eth else. Altho asum- we get more moderators, mb it'll hppn. It's hard to say for sure. But yes, we'll dfnt[ be doing some sorta a mod showcase th on the website, but then tt's sth we planned since lk the abs beginning. Tt's right, Emmy (nnem), you do hv experience w tt.

(nnem: "I mean I am the person who writes the mod showcase blogs for modrinth \uD83D\uDC40",)

nngdu: It looks lk tt we've come to the end of the qn queue, I blv. Yep, so if aone h any other qns to put in. We hv mb abt 10 mins left, at least on our predicted skdl. If not, then tt's cool too.

(**Fish**: "I asked a question earlier")

nngdu: Yeah, yeah, you did. Did you ask a qn abt prime numbers? It seem_ a bit off=topic, rly. Uh, if you rly nd an ans, no. Uh, this is a rly gd qn. So do I tk this one, or which one of you wld rather? Alrt, I'll tk it then. 
(nnsci: "What's the current bus factor for Quilt?")
Alrt, the bus factor for Quilt. It's actl[ rly a surprisingly gd qn. For those of you tt don't know what tt means, it's bsc[ the number of ppl tt wld nd tb hit by a bus to prvt the proj fr cont-. Rn, for most of Quilt, it's not tt low. It's crtn[ more than 1, which yk, you thk Fabric has lk a bus factor of 2? The whole pt of hv- distributed teams the way we do = at least tt's one of the rsns = is to mk sure tt's not rly a prbm. 

nnhav, we are work- on. When he's here next and when he is bz atm, we are gonna work on distro- credentials for the infra to j a couple of us who hv experience w tt. Not sure who exactly it's gonna be yet. But yet, we dfnt[ don't wanna to hv a super=low bus factor here. Haha, **burger**, I'm afraid tt nnhav is not a burger. But I'm not ptcr[ worried rn. I thk, agn, we rly nd to get a couple more ppl doing what nnhav is doing. But tt's not an issue, he j nds to be not bz and hand those credentials and we'll sort tt out pretty ezy.

We still hv t for a couple more qns if aone has any. Right, here's one, haha. **lenrik**, rly? "Is nnhav a cake?"
I c confirm that nnhav is indeed a Black Forest Gateau.

nncheat: OK, I thk I hv a qn I c ask in voice. "Oh man, this dev team seems rly nice and I hv so many of these qns to ask. C I ask them ltr as well?"

nngdu: Yeah, o/c, we're alw happy to tk qns. The AmA will be closed aft we're done with the mtg. But you're alw wlcm to ask any of the qns you might hv in the rlvt chnls. Or save them for nxt time.

nncheat: Yes, plz, hang ard. This is called the Tlcn Server, but not the Tlcn Dev] Server. Aone's free to hang ard and ask qns here. In fact, most lkly I will hang out in some other voice chat aft this mtg as well.

nngdu: Abs[, abs[.

I'll tk this one from **burger**, and I thk we're gonna finish up on this AmA after this one since we're runn- out of time. So **burger** asks, "who has the "nuclear codes" for everything? does one person have the ability to delete quilt?"
Well, it's a cplx qn. No one person, rly. For the comy stuff, mostly the Discord servers atm, **kashike** is the keyholder. He's thr bsc[ to prvt aone on the ttcomy or the Admin Team fr push- ahd w their own agenda. If you don't know him, Owl, he's a very well=known, v respected mmbr of the wider modding comy. He has no dir itrs in Quilt, tt's why he's in the position. 

As for the projs tslv, Github Perms suck, is all I c say. Tknl[ spk-, all of the admins hv access to mess up the repos. Thr's nth tt cb done abt tt, x4tun[. Tt's why you hv tb careful abt elect- admins, right? We do also enforce 2FAs, so I'm not worried abt them losing their accounts or ath lk tt.

nnalex: **ENDERZOMBI102** asked whether it wld be possible to hv more mods in a single jar, but not using jij sys.
(**ENDERZOMBI102**: "Will it be possible to have more mods in a single jar? not like multiple jijs, but most like "optional" or "child" mods, or is JIJ just better?")
This is sth tt ttload has sorta thot abt a lil bit b4. We haven't sorta looked into it yet, but this is sth tt sone wld hv to create lk either a proper RFC for, or j an issue and we'd nd to dscs it ltr. So bsc[, not yet, but it might hppn in futr.

nngdu: Alrt, I thk we're gonna call it an evening at this pt. Thx for coming ebdy, esp the ppl who ans_ qns and gnrl[ had a chat w us on here. And o/c the ppl who asked them, bcz we crtn[ nd them. We'll be doing this agn in 2 weeks, same time, same place. We're plann- on cont- this as long as we can, rly. Yes, evening, it is evening, trust me. I'll leave the #meeting=chat chnl open a lil bit more, in case ppl wanna catch up. And I'll also leave a record- posted in the #schedule chnl. If sone h t, we'll do a transcript. Abs[ cannot guarantee ath. We're rltv[ bz w what we're doing, but we'll see. So I thk tt abt covers eth for now. Thx for coming ebdy, we'll catch you in 2 weeks.



XXXXXXXXXXXXXX

**sciwhiz12**: "question to gdude, unrelated to Quilt but something which I noticed: how is it that @CrossLink is 'offline' yet still hoisted (on the right)\nis that a new feature of Discord bots or am I missing something"



**burger**: "how does making everything static work with multiple instances?"

nnalex: "It's not really possible to have multiple instances of loader in the same JVM, or at least not usefully - so we're not really loosing anything by doing it this way"

**yitzy**: "Was I right in seeing something about getting rid of the optional for mod containers?"

*sschr15**: "For that ModContainer being passed to the initializers as well as API methods, are annotations present / will they be present to identify nullability and other similar traits?",

nnalex: "@sschr15  I don't really understand sorry - if a mod has an initialiser, then it (by definition) must exist and so it's `ModContainer` cannot be null? Or do you have a different example when this is now a problem?\n\n*(For context: I'm referencing this change: https://github.com/QuiltMC/quilt-loader/commit/1d3a374acfcdb1ec71508efb0adb28feee406cd4)*",

nnalex: "I haven't touched kotlin before sorry - however I assume it would work the same way as other implemented interface methods work? (As in - you probably know more about this than me *anyway*, and what quilt-loader might need to do to make it work better with kotlin?)"



**burger**: "How does the ttmap feel about the potential effects qmap could have on loader unity (vs using Mojmap)? This doesn't apply to hashed or intermediary, only qm"











**Fish**: "is there going to be a (rough) transcription of this meeting for the questions?"




**burger**: "i think they mean if someone were to use technologies from quilt, are there some where the modder would be effectively barred from moving back to fabric"













nnsci: "~~What happens if Haven 'disappears'~~
