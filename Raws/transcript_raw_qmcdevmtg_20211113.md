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

**Marktrix** joined the ttmap, I thk smtm in the past two weeks, I don't rmb xk[ when. Yeah, last week. **Marktrix** hb work- on a bunch of other stuff, j kinda of ard mapg. He's done a bunch of work in Enigma. I thk he had some filament stuff tt fixed some issues with package infos. 

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

IMS: first question: when is it estimated that hashed mojmap will be useable for dev?"

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

**sciwhiz12**: "question to gdude, unrelated to Quilt but something which I noticed: how is it that @CrossLink is 'offline' yet still hoisted (on the right)\nis that a new feature of Discord bots or am I missing something"

**yitzy**: "Was I right in seeing something about getting rid of the optional for mod containers?"

**burger**: "how does making everything static work with multiple instances?"

nnalex: "It's not really possible to have multiple instances of loader in the same JVM, or at least not usefully - so we're not really loosing anything by doing it this way"

**IMS**: "first question: when is it estimated that hashed mojmap will be useable for dev?"

**sschr15**: "For that ModContainer being passed to the initializers as well as API methods, are annotations present / will they be present to identify nullability and other similar traits?",

nnalex: "@sschr15  I don't really understand sorry - if a mod has an initialiser, then it (by definition) must exist and so it's `ModContainer` cannot be null? Or do you have a different example when this is now a problem?\n\n*(For context: I'm referencing this change: https://github.com/QuiltMC/quilt-loader/commit/1d3a374acfcdb1ec71508efb0adb28feee406cd4)*",

nnalex: "I haven't touched kotlin before sorry - however I assume it would work the same way as other implemented interface methods work? (As in - you probably know more about this than me *anyway*, and what quilt-loader might need to do to make it work better with kotlin?)"









IMS: "first question: when is it estimated that hashed mojmap will be useable for dev?", 

nnsci: "Is there or will there be a canonical list of Quilt developers (particularly those who have qualified for and hold the Quilt Developer role in the Toolchain server)? In addition, will there be a same list for the whole Quilt team (Admin Board, Community Team, and the technical side) on the website?", 

burger: "How does the mappings team feel about the potential effects quilt mappings could have on loader unity (vs using mojmap)? This doesn't apply to hashed or intermediary, only qm",

nnkrop: "RFC 38 has been in Final Comment with no comments for over a month. When can we expect it to be merged?"

**yitzy**: "Is there any idea of having some community input on collaboration? There aren't many mod teams as open as quilt who might not be trusted to the same extent

**StrikerRocker**: "how will the official release of quilt as a whole including qsl be determined?"

**jamalam**: "I forgot, can quilt loader load mods with `fabric.mod.json` as well?"

nnem: "How many mapping changes from Yarn end up getting into QM? Is there any sync system between Yarn and QM, and if not, is it at all planned?"

**Blodhgarm**: "Will quilted mapping be usable with forge? (Sorry if it is a stupid question)"

nnsci: "For substantial changes to existing RFCs, should they remain as amendments or be proposed as new RFCs? In the latter case, should the new RFC partially supersede the new RFC (adding new clauses or removing existing ones), or should the new RFC fully supersede the existing RFC (so the existing RFC has no more effect)?"

**Fish**: "is there going to be a (rough) transcription of this meeting for the questions?"

nnsci: "What versioning scheme will or are Quilt's project use? 0-based versioning, or semantic versioning, or other? And is it or will it be different per project, depending on the will of its maintainers?"

**Fish**: "Will there be noticeable differences between Quilt and Fabric? Does Quilt have technology that would be impossible to port to Fabric?"
**burger**: "i think they mean if someone were to use technologies from quilt, are there some where the modder would be effectively barred from moving back to fabric"

**yitzy**: "Fabric is somewhat lacking in terms of events, especially world interaction ones, such as a lack of a block place event or screen handler events. Does QSL plan on addressing this, and if so, how far would these interaction events go?"

Hubry: "Has a potential datagen api been looked into? Having easy access to generating json is very useful, but on Fabric it has been a pretty annoying process to set it up, compared to Forge's default inclusion"

**Fish**: "this question was probably answered earlier, any roadmap for Quilt?"

nnsci: "Will the final tallies of votes for technical decision (for example, the proposed PR policy's conflict resolution through a team vote) be publicly released alongside the final decision, as part of policy? (I presume the names of those who voted for/against will not be included)"

**LOCAL**: "What major roadblocks remain to QML's public release?"

**Fish**: "Does Quilt have a roadmap, where would it currently be at, and is there a rough estimated time of arrival for the mod loader?"

nnaurora: "Anything new on forums? :pineapple:"

**Fish**: "To add on to my previous question, is there a publicly viewable roadmap, like Trello, which is a clear roadmap to where Quilt is potentially at right now?"

**arathain**: "I saw \"quilt merch\" be addressed once, I think it's reasonable to leave any of that for post-release; anyway, what's \"the official stance\" on it? What could it entail?"

**jamalam**: "any updates on whether there'll be a way to support quilt financially (i.e. to help with infrastructure costs)"

nnsci: "Is the Quilt Administrative Board locked to 3 board members? The Governance RFC provides that nominations are open when there are less than 3 members, yet does not give any indication to my understanding for the possibility of more than 3 members on the board."

nnsci: "~~What happens if Haven 'disappears'~~

**Lith/Heli**: "any updates on using FREX ins qsl?"

**burger**: "It seems like many people working on quilt are busy or can't focus on Quilt in full. From the outside, contributing to quilt or joining the team seems like a large commitment which may dissuade potential new members from joining. Any thoughts?"

**yitzy**: "Was there a plan for showcasing underused or just generally cool mods or a starboard?"

nnsci: "What's the current bus factor for Quilt?"

**ENDERZOMBI102**: "will it be possible to have more mods in a single jar? not like multiple jar-in-jars, but most like \"optional\" or \"child\" mods, or is JIJ just better?"

lenrik: Is haven a cake?

burger: "who has the \"nuclear codes\" for everything? does one person have the ability to delete quilt?"
