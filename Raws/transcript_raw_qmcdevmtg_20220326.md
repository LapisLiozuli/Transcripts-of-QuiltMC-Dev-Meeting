nngdu: Hello, you all have j got pinged. Wlcm. It's t once agn for the next biweekly mtg. Let's do a qk check. Hey eone on Mumble, how's the sound?

A: Good.

nngdu: Good. (Good.) I forgot that it does tt, I'm sorry. Im, I'm not sorry, it's not my fault but yk. Anw, wlcm eone. We're gonna j wait a few mins for ppl to show up and then we'll get started, mb abt 4, 5 mins. BTW, nobody's found all the Easter eggs on the website. Ppl found one of them, but there's one of them they haven't found. Emails? It's not the best time for emails. See you ltr, KJJP.

"Are there more doors or wheels in the worlds?" Prob more wheels. Im, all you nd is a straight ans lk tt, and then it's lk, "Oh, who cares."

"I don't count your face as doors either." I see a few well-known faces in the stage here. Wlcm back.

We'll be starting in j a min. As alw, I'm gonna do this the same way we alw do it. Tt is, I will call on some mmbr of hte team to talk abt their team and they'll do so. Until we get to the bottom of the teams list, and then I'll talk about ttcomy stuff, and then we'll do qns. 

As a reminder for eone on Mumble, and myself as well, bcz I often 4get. When we do qns, we nd to read out the qn and the person tt asked it. But I'm sure tt's fine. As alw, if you wanna ask a qn, you can use the /ask cmd, and we'll get to them ltr on in the mtg. Don't ask abt doors and wheels though, pls. Shall we get started then? First on my list is CHASDON. nncheat, do you wanna talk abt tt?

nncheat: J as a gnrl upd8, thr's no chgs tt you c see on Github and the lk. But I hb re-writing part of the lang impl]. I was not happy how the first attempt turn_ out. Turns out it wasn't tt bad, bcz the second attempt was alm the same as the first one. But circular syntax tree is now an actual circular syntax tree, which is gd. And it's immutable so it's j a lil cleaner in gnrl. 

Currently try- to fix Gradle agn bcz for some rsn the tests are fail- and it's not tell- me why. But in gnrl, I hope this is a more stable impl] whr I'm happy to pass it on to other ppl to impv perf if necs to actl[ start work- w it, hope[[.

nngdu: Sounds gd, sounds lk you're hv- the same Gradle problems we all are.

nncheat: I tried to tk a break fr pgbuto, but Gradle haunts me.

nngdu: Grappek, wld you respond to the ping I j sent? Oops, looks lk he's bz. In tt case, nnalex, would you lk to talk abt Loader?

nnalex: Sure, so, in the last week, it turns out we had to rmv Quilt Loader entrypoints since it's not rly psbl to convert method ref] entrypoints betw irfcs, so istd entrypoints will be in QSL. Which was the plan og[[, but it means tt we won't have qlod-specific entrypoints, which shld reduce a bit of confusion. And tt's rly abt it for Qload.

nnaurora: But thr's also sth else you said, tt there's no entrypoints in qload. But isn't thr the pre-launcher entrypoint?

nnalex: Yes, yes, tt's a gd point. I should've said tt. So thr's a pre-launcher entrypoint which mods aren't rly meant to use, bcz, well, it's not rly meant to be used thr v much. But it does exist.

nngdu: Hehe, ok, fair. While we're on this subj, are you able to addr the qn tt's j in the chnl?

nnalex: "To the QSL Team, what entrypoints will be avbl at launch?"
If they're not in qload, I'm not the right person.

nngdu: Tt's a fair point. I 4got about tt.

nnaurora: Im I c ans it rn. So thr's the pre-launch one in qload, and then thr's 3 other entrypoints in QSL. Technically more, it's a bit confusing. So thr's the init one, which is launched b4 the regy freezing. It's ~~server~~-side. There's client-init, which is triggered in Minecraft client using a ~~slide~~. And thr's the last one for the dedi_ server. And then thr's a special sys tt allows some ~~errand~~ to bhv lk an entrypoint. Thr's tt too. It's a bit of a dffr[ sys, but it exists. Those are the dffr[ entrypoints tt are avbl.

nngdu: Alrt, thx for tt. For the ttmap, we have a new voice on the mtg landscape, I suppose. nnnocom, wld you lk to talk abt mapg?

nnnocom: Yes, hello. So mapg, bsc[ we're look- for rvws on most PRs. But specifically #5, the render- PR tt nnoro made. And other things, looking to rewrite ~~Mapture~~ and psbl[ integ it into the mapg build scripts, tho IDK exactly what's gg on thr. As for pgsnaps leading up to 1.19, updating them is gg q well. Builds are coming out in relatively gd t. I thk the one we did for 20w12a was lk 20 mins, I thk. Let me- Uh, IDK when it was released, but it was rsn[[ qk. But yeah, other than tt, tt's all I got.

nngdu: Alrt, thx for tt. nnaurora, wld you lk to talk abt qsl some more?

nnaurora: Yeah, sure. So thr was kinda a lot, esp bcz of the pgsnaps. So the first th was tt we had to fix some stuff in the regy events. Bcz the th is, we kinda haven't seen it when upd8-, bcz we didn't hv a test. But tt's a specific use-case. And tt specific use-case showed us we couldn't act with these blocks. Bcz the way it works is, contrary to the regy module, we have regy events which actually happen when a new event is add_ to the regy.

And we hv a v cool API for listen- for those reg], but also in a way that will trigger for every alr-add_ entries. So for mods lk Aurora's Decorations, it's rly cool bcz it allows v easily to anlz the regy in real-time, mb add new stuff dpd- on tt. The way it works is tt when we add tt new event listener, it'll go thru every entry alr add_. The issue is, if you reg sth based off tt, while it does the first iteration, it will crash. Bcz it'll try to add sth, to sth tt is being read. So tt is why we had to modify the API. So we had to actl[ chg tt, so we hv lk a special regy irfc tt allows us to delay all reg[s to after the iteration. So tt's one of the big API chgs we had to do. 

We also had to do some other chgs, mostly bcz of me. So I had the terrible idea to start sorting them out. The issue is, some APIs do not work bcz of 1.18.2. So we had to fix [them]. So it's kinda great bcz we see what we shld get in qsl to ease regy stuff w the new regy chgs. 

We also hv a new impl] of the BlockToItemMap, bcz the way it works in Fabric is, it starts listing at one pt. But it's way aft any mixins start doing tt. Which can cz issues in some mods if they add stuff w a mixin. So if reg] of stuff is done b4 the entrypoint, then it'll not work. The blocks will not be in tt map, which can cz a lot of issues. Tt's one of the ths, so we add_ a new th to the regy module which allows to fill tt map. And we chg_ the entrypoint so it's much earlier so it doesn't cz issues.

Aside fr regy stuff, we also had to to chg the API for cmd in 1.19, bcz Mojang broke stuff. Thr's a PR tt's open, so feel free to rvw. So for other stuff, we got 3 new ppl in qsl for world generation, so that'll be itrs-. I can't wait to see what they'll do for world gnr8]. That's exciting. O/w, thr's not a lot to say. Thr's a new PR tt cb look_ into if you want. We are still try- to migrate to qload. Thr's a PR open to ~~tune how long the time will be~~, but it'll be v soon. Once tt hppns, tt means tt QSL will not be run on Fabric anym. Ig tt's kinda it for now, I don't rly see what else thr is to say now, so yeah.

nngdu: Right, tt's great. Thx nnaurora. That was q a lot, don't worry. In tt case, I will cover the ttcomy stuff. ttout hb fairly bz. nnsouth wrote up a nice new blog post on the upcoming beta, which is a th eone shld read if they wanna learn a lil bit more abt it. We also moved the #openings chnl which was on the comy server to teh website. So if aone is wonder- what teams nd help, or yk, j hv openings, you c chk tt out here. I'm sure thr'll be a link in the podcast notes as well.

And we also set up a chnl in the comy server call_ #social-feed. nnsouth is start- to mk use of Twitter. If you're not folw- us thr and you're a Twitter person, pls do go ahead and do so. But tt chnl will also show ath we tweet, so you c keep an eye on it fr Discord as well.

Other than tt, non-ttout stuff, not a whole pile. I did mk a small chg to the comy server's gallery threads. They'll try and figure out a default name based on the text tt you put into your gallery post at the start. O/w, not too bz here atm.

Alrighty, tt abt covers all the teams for today. Did aone on Mumble have ath they wanted to talk about today? Alright, I'll say tt's a no. No prbm at all. Alrt, in tt case, we'll get to the qns. nnalex, you claimed a qn. Wld you lk to go ahead and tk tt?

nnalex: Sure, the qn by **RTTV** is, "Can we detect if *the* quilt loader entrypoint is being called on a client or server through a method param or something?"
The ans is, not thru a method param. Thr's a class MinecraftQuiltLoader, it's got getEnvironmentType(), which will give you the current env. So yeah, you can use tt istd of ath else.

nngdu: Tt crtn[ looks lk it'll mk life a lot easier. Alrt, nnaurora, yeah, you can tk tt one.

nnaurora: **Patbox** asks, "Do you plan releasing Beta for 1.18.2 or go straight for the snapshots?"

nnaurora: Bsc[ it'll be kinda both, bcz we hv to mntn for the pgsnaps, tt's for sure. Bcz as we fall bhd, tt'll be hell to upd8. But I thk gg for 1.18.2 is rly impt too, bcz it's kinda a stable rls. So currently all the PRs target tt vrsn. And once they're merged, they'll update to 1.19. I thk we will kp Beta for 1.18.2. But if it bcms too dfcl, it'll be a bit scary, but I thk it'll be fine. 

And it will be kinda impt, bcz it'll prove tt we're cpbl of mntn- it on a stable rls. And also mk sure tt we do upd8 to newer vrsns. After when we rls, we will hv to supt a stbl rls, and we will hv to upd8 to pgsnaps to mk sure tt they'll be avbl during the launch of the next new rls. So I thk we will j do it directly dir[ for Beta too~~. It might be simpler also for PR, bcz if a PR gets a stbl rls, it's much easier to rvw and integ than having two updates a week because of pgsnaps. So, yeah, ~~dffr[ ppl~~.

nngdu: TY nnaurora. We've got two unclaimed qns in the backlog here. While they're sort- tt out, feel free to use /ask to ask any more qns you might hv.

nncheat: I thk since no one rly knows the ans, might as well j tk it. Krisander asks, "Will other language support like Kotlin require a seperate compatibility mod like Fabric or will Quilt have this out-the-box in QSL/Loader?"

I'm actl[ not entirely sure abt the cplt history here, but it is a topic tt was at some pt hotly db8_. So, the ans is x4tun[[ not a simple Yes or No here. Hwvr, even if we don't end up put- it into qsl, thr's a gd chance tt if thr's a decent attempt at impl], it'll fall under auto-dep dl- means tt ppl will at least not hv to manually incl it. But yeah, it's not q clear-cut yet. Thr's opinions for either side, so we'll hv to see what turns up.

nngdu: Thx for tt, nncheat. nnalex, you can tk tt if you like.

nnalex: So RTTV asks, "Like *the* entrypoint, are there any 'FAPI features' that will be present on qload without installing qsl?"

So tknl[ Fabric loader cntns all of Fabric's enrypoints. Thr bsc[[ aren't any other FAPI fetr in Qlod bcz qload is just from Fabric loader, not the entirety of FAPI. So not rly.

nngdu: IIRC, the pt was more to prvd the fmwk to add fetr rather than j hv- them dir[ in loader, right?

nnalex: Yeah.

nngdu: We're out of qns, so if aone wants to ask, plz type /ask and get your qns in now. I'll give you a couple of mins.

nncheat: Looks lk we're doign a mtg speedrun this week.

nngdu: Imn, tt hppns 

nncheat: I'm no sure if it hb pt_ out yet, but this is the 2nd=to=last mtg b4 Beta.

nngdu: Oh yes, I never thought abt tt.

nncheat: Thr's a mtg in 2 weeks, and then there's less than 2 weeks until Beta

nngdu: Certainly is an exciting t, I hv to say. How are you all feel- about Beta?

nncheat: "Beta good." Yes, Potatoboy, ty for tt. I agree.

nnoro: I hv a couple final chgs I want to get in b4 Beta, and then, yeah.

nnaurora: It will be a lil bit stressful, bcz if sth goes wrong, it won't be good.

nncheat: If nth goes wrong, it's hardly a beta.

nnaurora: Yeah, but hope[[ nth goes wrong. I wld pref tt nth goes wrong.

nncheat: I'm still hoping tt I can hv CHASM access for Beta.

nngdu: I did get one qn in, b IDK if we hv an ans for it.

nncheat: We don't hv a why, but we hv a IDK, a when and who.

nngdu: I know when and who, but I'm j seeing if I c find a why. Well, IDK, it's just- Oh, I lk tt, let's use it.

nncheat: At this pt, let's j put it on stage.

nngdu: So, RTTV asks, "Why call it Quilt?"

It was j kinda a spur of the moment th in the initative srvr, I blv. I wasn't thr, nnhav came up w it and it j kinda stuck. And tt was lk, v early on, lk the start of Feb. Yes, 2nd of Feb last year. But I don't thk thr was any deep meaning bhd it, other than Fabric=eco stuff using fabric=related terms. 

Yeah, I lk tt take. Apophilim said, "Quilts are made of patches of Fabric and this is kinda the comy quilt whr eone gets a piece."

Someone in the chat said, "Hope Quilt is the Forge=killer." Dfnt[ not. Forge and Quilt and even Fabric will alw fulfill dffr[ corners of the modding sphere, I imgn. 

nnaurora: Yeah, on tt pt, I thk Forge is kinda unkillable. 

nngdu: Yeah, it's kinda too big to fail, isn't it?

nnaurora: Lk, it's the same as Optifine. It's j v hard or j impossible, bcz ulti[ thr are some ppl tt lk the philosophy, and they will go and they will die on the hill mk- sure tt it'll survive. So it's not killable. And even then, I don't thk the pt of Quilt= Eventually, If we c kinda reconciliate the rlsp betw Fabric modders that goes to Quilt and Forge, that would be kinda nice. I can't say much, bcz thr's not rly ath rn rn. But mk- sure tt eone stops beat- each other up over a loader, it wld actl[ be nice.

nngdu: Yeah, we do work with Forge on a few ths, and obv[ thr's no intention of kill- Forge here. But yeah, as I alw say, they fill dffr[ niches. Thr's no rsns for both to not exist.

nncheat: We actl[ do hv q decent connections w Forge, which is kinda nice.

nngdu: Yeah, we do. I can tk this one. RTTV: "What hardware does the quilt web servers run?"
I thk tt wld be a better qn for Github. We're using Github pages atm. If you're ask- abt the maven, nnhaven I blv has tt run- on AWS. So it's kinda dfcl to say what the spfc hardware is, when we're not dir[ run- on hardware. Altho, this is kinda fishing at this pt, isn't it RTTV? 

nncheat: J try- to help us out.

nngdu: Im, all our stuff is open-source, so if you're curious, you c alw hv a look at Github.

nnaurora: TropheusJay asked, "quilt getting more collab with forge before release than fabric ever did is impressive (edited)"
It's not tt surprising. Bcz= I can't rly go too much into dtl. ~~But actl[~~ Forge doesn't rly like, and tt's kinda why thr was not cooperation betw them. I won't go into more dtl, bcz tt's not hte pt.

They hv a history. So, tt's why. Well, I thk we're gonna close bcz we're j not get- qns. 

nncheat: ~~We were complain-~~ abt qns, and then now there's no qns. You can't decide.

nngdu: That's ok, I don't rly mind end- a lil bit earlier. This isn't q the speedrun we thought it was gonna be but tt's fine.

nncheat: Half of the og[[ t slot tt we plan_.

nngdu: Yeah, I thk it was, wasn't it?

nnaurora: And I was being worried tt my tknl in-depth of qsl ws too long.

nngdu: No, it's never too long.

nnaurora: I j hope tt I don't bore someone.

nngdu: It was fine. Don't worry abt it. Oh well, thx for coming eone. We're gonna wrap it up for now. See you in 2 weeks' t. As usual, there'll be an after=party in the #voice-chat chnl. That j tends to hppn at this pt. Mb thr won't be, but who knows. Either way, thx for coming eone, we'll catch up next time.

nnaurora: Bye bye~

nncheat: Bye.

nnoro: See ya.
