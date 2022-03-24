nngdu: So, this is gonna be a smwt dffr[ mtg. We'll wait a j a lil bit for more ppl to show up, but they shld get some pings. Hey Ara. So, the 4mt of this mtg hasn't chg_. However, you won't see the spkrs on Discord. They'll be talk- via the Cozy Mumble bot tt we hv set up, tt is curr[ not set as a spkr so we can'thear them rn. In a couple mins we will chg tt, and we'll see who shows up. 

Also j tb clear, you c type in the #meeting=chat chnl, right? Yep, OK, gd. Hey Livia, hey Merchrome. Wlcm wlcm. For the sake of not mk- this look so empty, I stay| in the stage, but I'm gonna be mute- and deafen- mslf and talk- via Mumble. Thr mb a small bit of latency but I don't imgn it'll be too bad. This is the first t we've done this. We did test it, but yk how it goes. I'm gonna set tt up right abt now. Alrt, tt appr tb work-. We'll j gv it a couple more mins. But yeah, hey eone from the other side of breach. Hey Trollzer, hey Pinkosick. Yeah, it's weird isn't it? Don't worry, it usually takes people a few mins.

nnoro: Mb we shld mk a mtg role, and then ping tt for attenders of this mtg.

nngdu: If you RSVP=_ to it, you wld hv gotten a ping when I started the event. We will tell you who we are, don't worry kb1000. You will not be lost, hope[[.

I'm lost.

I'm muted.

I'm disappointed in the number of groans I got abt tt. We usually do it for abt an hr, Parzi. I haven't seen it run over q a long t, so we shld be fine. Altho we'll see. Hey Kropp.

Kropp: Nbdy's talk-?

nngdu: We haven't started. We're abt to tho. Since you're here, do you hv ath abt CHASM?

Kropp: No.

nngdu: Tt's alrt. Well, we m as well get started then. Hello eone. Hope[[ you know my dumbass voice by now. It's nngdu. This is the first mtg we've had since Xmas, since b4 Xmas even. Obv[ it's tkn some t for ppl to get back in the swing of ths, tt's fine. I thk we've metn_ this b4, but we tend to skip over teams tt don't hv too much to say. We'll be doing tt today, thr's a couple teams tt thr's not rly much to talk abt, and thr's a couple teams whr ppl j aren't here atm. "Try agn in two weeks." But we shld be good.

So we hv nbdy here from ttbuto, and CHASM hasn't been too bz, so ig we're starting with ttcotl, which is bsc[ my team. ttcotl is mostly Cozy rn. Thr hb some work. A lot of what I've been doing hb infra =level kinda stuff, so istd of drct[ work- on fetrs, I've been 1o[ rewriting parts of Cozy. Tt's hppn- 1o[ to break up the code a bit into modules, which has the advtg of allow- other ppl to mk use of fetrs of Cozy in their own bots if they want to. Asum- they're using the same fetrs as us, which thr's a lot of bots using tt ard here , so I figured why not.

nngli hb doing work on the Github integ] stuff. It's slow work bcz thr's no API wrapper tt does eth. It turns out tt Github's APIs are q xcsis[. Thr are ths you c only do via Rest in the Github API and ths you c only do via GraphQL. So nngli is having to combine both of those tgt. It's a pain. It is a pain. But it's get- thr.

Obv[ thr is a lot of Cozy stuff to do. I am work- on modules atm, but I thk I will prob be tk- a break fr tt soon. Esp bcz Discord h gvn us a few more toys to play with, moderation=wise, tt nd tb set up. Can't rly gv you much info on tt rn, but we'll get there. I thk tt's all abt it for ttcotl atm. It looks like ttinfra is next. nnhav, wld you lk to intro yslf?

nnhav: Yeah, hey eone, this is nnhav. Infra's gonna be pretty short, j some minor th. Ig nnsouth didn't thk it was minor, but I've set up Open Collective, which is a way for us to  bsc[ publish fnc[ stuff, so this is only v minorly rel_ to Infra, bcz Infra is the only area whr Quilt curr[ h expenses. So I don't thk we're gonna be ask- for donations until we hv a stable pdt. But in theory, we can ask for donations and publish the expenses.

nngdu: Yeah, it's q an exciting th in some ways, bcz as some of you m know, nnhav hb pretty much pay- for eth out of his own pocket. It wld be nice for tt not tb the case. Open Collective will hope[[ gv us a way to fix tt prbm while being transparent abt whr the money is gg and how it's used. So hope[[ tt turns out well. I imgn we still hv to look at tt a lil bit more since i haven't seen it yet, but we'll get thr. Who's next, Mpngs? nnoro, would you lk to hv a chat?

nnoro: Yes, not much h hppn_ in the past month and a half=ish. I looked at the diffs. Thr's only been a couple minor PRs merged. The biggest th is tt we're now in anor wave of pgsnaps, so we're work on map- those, and yeah, tt's abt it.

nngdu: Alrighty, prog conts as alw. Uh, QSL, nnaurora, wld you lk to hv a chat?

nnaurora: Yeah, so, I j nd to mv up... So curr[ we are= I thk since last t we launched ~~3~~ modules. Also, we hv now the cmd modules. We hv a new fetr for baked events. Now they c be used as entrypoints, and thr's ~~curr[ a fly method to un-reg~~ a bunch of listeners for a bunch of errors. We also hv the Item Group API which is now merged. And curr[ we hv two PRs in ~~final com period~~ which is the Tooltip API and the Network- API. O/w we hv a lot of PRs wait- for rvws. I thk tt's kinda it.

nngdu: Gd stuff, sounds lk crtn[ a fair bit of prog. Gd work get- tt stuff mrg_ as well, nice work. Ig I c talk abt Comy a lil bit. For those of you tt haven't been folw- the annc]s, we dcd_ to finally replace the #showcase=dscs] chnl. So the #gallery chnl will auto[ hv threads set up. You guys hv used threads at this pt, we use them ewhr on Comy. The mapg hb upd8_ agn, they now supt Qmap now thx to upd8 to LInkie by Shedaniel, and also a ton of work by Chris, who is actl[ named sschr, but hey we'll j use tt name, he doesn't mind. 

Thr's also been some work on govc, thr is a govc PR atm. I'm not sure if we mrg_ tt. No, I don't blv we hv. Tt's RFC #47. If aone is itrs_ how Quilt is run, then dfnt[ go chk tt PR out. 100%, it's an impt one. Thr is anor one as well, the ttout which is curr[ in drafts. ttout is, well, it's bsc[ dsin_ tb a team tt tks care of ths lk social media a/cs, the website, tt sorta th. Tt will still nd irfcs. But if aone's itrs_ in tt, go tk a look. Obv[ we'll nd ppl on tt team ltr as well. I thk tt more or less covers it. It hasn't been super bz since Xmas since eone's been get- back into the swing of ths. If aone has any qns, go ahd and hit up tt /ask cmd, I see thr's a couple in thr. Does aone else hv ath to bring up b4 we move into tt? Alrt, Ig not. 

OK, Parzi. Parzi's asking if thr's any news rel- to the Cozy ban=sharing or showcase sharing?
Not yet. Rgrd- ban=sharing, thr was sth we were plan- to do, sorta inrl[, and then bring out into the wider comy. But when I got to chat- w the Geezer ppl abt it, they were at a proj tt they'd started for it. So the plan was to use their proj, bsc[. Now the person who was mntn- tt h ended up quit- for their own personal rsn, j in gnrl fr prgm-. So atm nth is hppn- on thr, bcz I don't hv enuf t to do tt and eth else. As for showcase sharing, nth yet. I don't csdr it a high prio since we haven't got Quilt set up yet. But we'll get thr. Thr's j more impt ths to do atm.

nnhav, do you wanna take tt one?

~~What was the question exactly? Parzi asked something like "What are the current infrastructure costs for Quilt?"~~
nnhav: Yeah, do I click the stage button? Or you click the stage button? Cool. So Maven's costs curr[ are the Maven srvr, which is a lil bit oversized, prob a lil bit bigger than it nds tb for the sake of safety. Tt being said, I'm do- work to replace the Maven srvr evtl[. But work on tt is slow-going bcz I'm do- a lot of ths at once, juggling a lot of balls thr. So short ans, mostly the Maven srvr, but thr's other small ths tt add up as well. Rn it's abt 70 dollars per month, Parzi.

nngdu: About 70? Yeah. I thk part of tt was email, wasn't it, bcz we nd_ tt for the=

nnhav: Yeah, emails, about 12 dollars. TBH I cld prob cut out 8 of it, bcz rly the only one who needs an a/c is TheSheikh.

nngdu: Yeah. Olivia's got a qn. I thk this is sorta a bit of a grp qn, b I c try and tk a stab at it. Olivia is asking, "What is the RFC sys? I don't rly ustd how it works, why it's thr and what are the pros and cons?"
Well, RFC is short for 'Request for Comment', and the idea bhd RFC is tt major orgn[ or prof chgs get docu_ on Github. They allow ppl to go thr and comment xrgrd[ of whether they're part of the staff teams or not. Thr they c, say, prvd advice, and j gnrl[ see how dcd] are made. Now, not eth's up there, ttcomy esp. We our prcss thr, but a lot of our other ths lk moderation stuff isn't thr bcz it nds to mv faster than the RFC prcs allows for. I can't q rmb the xk rsns we went w it. Do you rmb them, nnhav?

nnhav: Yeah, we nd_ a space to hold and lock our official docus. Right, so tt was gg tb a big th. Whether tt is = lk you metn_ = policy chgs, tknl specs, they're all on a central repo, as well as a way for us to hv a formal prcs for dcd- on them. So whether it's dcd- how QSL modules shld be specified or mrg_, dcd- how we shld hire new staff mmbrs. All those ths hv tb codified swhr, and this is a great way for us to hv a formal way of dcd- what we shld do and kp- track of it, right. Tt was the gist.

nngdu: Tt's right, I rmb most of tt actl[. As for the pros and cons, well, obv cons is tt it tks a while to get ths pushed thru. But I thk thr are a lot of advtgs to it as well, esp hv- those dscs] avbl in the public eye, whr eone c see and contrib to them. I thk tt's rly impt, esp gvn whr we came fr. Tpnt]'s been sth we've rly been thk- abt, pretty much since the start of the proj, and I thk this helps a lot w it, honestly. I thk this one's for you, nnhav.

(~~Something to do with sharing the Open Collective for Quilt~~)

nnhav: Yeah, in theory it's set up. I don't thk I'm gg to share it for a bit. Agn, I cld, but agn, I don't feel lk we shld ask for money until we hv sth to show for our efforts. If ppl inss, Ig I can share tt b I want to do a lil bit more work inrl[ b4 doing so.

nngdu: Tt's fair, tt's fair. I wonder, do yk if they have an API? Did you notice ath lk tt?

nnhav: I have no idea.

nngdu: Might be sth to integ into one of the wlcm chnls ltr on. Tt might be itrs-. We're at the end of the queue alr, tt was qk guys. DAE hv any qns they want ans_? If so, hit up tt /ask cmd, I'll gv you a few mins. Yeah, it hb the shortest mtg in a long t. I had a feeling it wld be, bcz ppl are still recovering from the holiday season. Ppl ask, "Where is Quilt?" But nbdy asks, "How is Quilt?" Tt's a classic meme, Parzi.

nnhav: Tt's a much harder qn to ans.

nngdu: Does aone want to tk the next incoming qn?

nnhav: Bsc[, bcz tt's what Fabric's was. I don't thk we did ath more than tt, we bsc[ j cloned their repo.

nngdu: Tt mks sense.

nnoro: I c tk nncheat 's. "Do you hv an ETA for an ETA for Quilt?"
Yes. Well, not q. We hv an ETA for the ETA for the ETA. And tt is alw 2 weeks from wnvr you're listen- to this.

nngdu: Yeah, it's kinda hard to have an estimate, isn't it? Main th hold- us back is, as alw, Build Tools. It's j rly hard to get Gradle experts to help. If you know any, send them our way, plz. But once we hv pgbuto done= I thk nncheat metn_ on Comy, tt if we wanted to, a few weeks' of crunch on the other projs wld prob get those to rls once we hv pgbuto. Obv[ I don't thk we rly want to do tt, but it rly shows how far bhd pgbuto is cmpr_ to eth else. It's j x4tun[ tt it's tt way atm. Yep, agreed, Gradle rly is j an eldritch demon, says Ara. 

I lk this qn. Parzi asks, "Are thr any plans gg fwd to do TED talks whr modders come in and talk abt gnrl fetr dsin, or spfc impl] of itrs- / noteworthy fetrs?"
In short, yes. We hv ths plan_ w the Events Team. We actl[ j started plan- sth rcnt[, b it's gg tb a while b4 we get to the pt whr we c actl[ talk abt it. B yeah, events, they're crtn[ a th we wanna be do-. Talks were dfnt[ sth I had in mind when we were forming the ttev at least. IDK if any of them are listen- atm. But yeah, we're gonna figure out a few ths lk tt planned. No doubt abt tt. I thk this one is for nnoro.

nnoro: Wdym by "Renamed Quilt's Intermediary Mapg when?" Wdym, lk renaming pghs? Or pghs is a good name?

nngdu: pghs is a gd name. It's not a fun name, but it's kinda the pt, isn't it.

nnoro: See here's the th, Fabric kinda mess_ ths up by call- it pgim, bcz pgim is literally what tt style of mapg is. So we hv to go w pghs. I don't wanna call eth pgim bcz tt gets confused w Fabric pgim. So we kinda hv this weird issue.

nngdu: We h some dscs]s abt mapg b4, abt what to call it. Uh, I can't rmb xk[ what names we came up w, but I thk we end_ up dcd- at tt moment tt we wanted to kp the names descriptive. I can't rmb 100% why we did tt, b I thk it turned out tb a gd choice in the end. Yeah, pghs, tt's accu, that is what it is.

nnoro: I mean, it is pbsh_ under Hashed namespace tho, so...

nngdu: Does aone want to tk this one? Don't thk we hv ath on Blurry. Or do we hv aone fr Blurry here?

nnhav: Thr isn't rly any upd8 in tt area. It's the bsc TLDR.

nngdu: We hv talk_ a lil bit abt it inrl[, b then agn it's still early. Thr is some ths to thk abt tt as well, rgrd- platforms like CurseForge. We're not rly sure whr tt's gonna go yet. They hv req_ a spec docu fr us, b we're j not at the pt whr we're rdy to prvd tt yet. So, we'll see. We're not sure yet. We're still thk- it's gonna hppn tho. So it's a case of get- to tt pt.

"~~No 4gv] ~~for pgbuto." I mean, sth to thk abt more than ath, when you thk abt sth lk CHASM which used tb call_ ASMR= I'm not sure whr the CHASM name came from aside from a cvnt acronym. But it sure beats what Forge hb do- w their proj names. Um, c any of us ans tt one?

nnhav: Bsc[, the plan is for it tb a 'privileged' lib. Thr's not a name, or a formal strc for tt or ath. But it's gonna hv a lot of the same bnfts tt QSL does in tt it cb auto=resolved, or auto=dl_. So the bsc idea is tt it'll be auto=resolved or auto=dl_ lk QSL Module is, so it cb used in devt env for mods by dfal w/o hv- to set deps, or use `includes` or ath right off the bat. B also=

nngdu: Uh, I thk nnhav's j crashed. He suddenly left the Mumble srvr. RIP. 

nnoro: Does aone thk they can grab what he was abt to say?

nngdu: I'm afraid not. Oh no! Windows Updates! Oh, OK. Sad, sad. OK, well.

Parzi asks, "Pointless qn, b why does the MC Update RSS bot smtms tk so long?"
The dirty secret is, bcz it's not an RSS bot. It's actl[ poll- the launcher patch notes. So thr's two rsns tt it's slow. The first rsn is tt Mojang j doesn't pbsh them smtms, or they take ages to pbsh them. Lk it took them a week to pbsh the second=to=most=recent pgsnap. The second th is, Mojang = and Microsoft in gnrl = hv a ~~fren cache~~ set up. And it doesn't expire for, I thk they hv it set to an hour or sth. So dpd- on how their srvrs are feel-, it c tk up to an hour aft they pbsh it for the bot to pick up on it. And even then you'll find tt if you're ard when the bot picks up on it and posts the embed, if you click twd the patch notes on the side, you m still not see them bcz their cache hasn't upd8_ in your region yet. It's a pain in the ass, honestly. 

I've been thk- of a way to mk it more rely[, but ulti[ we want the patch notes on Discord, and thr isn't rly a btr way of get- them. So, I'm not rly sure. But hey, if you hv any ideas, I'll hear them. Yeah, tt's what I used to do. I used ot write them manually, Ara. But it's been a while since I've had the t. Atm8- what I c is crtn[ whr we wanna be w tt. Parzi says, "Pay lobbyists to stand otsd their windows and take pics of their editors." Yeah, mb. Skyrising, doing some cache=busting. I'm also doing some cache=busting. It doesn't help.

~~A~~: Yeah, abt tt, ~~gets launcher meta within a second of pbsh-, b nodule content~~ tks 1 hour, so...

nngdu: Yeah. Meta, you c get, but launcher cntt won't, it j won't. It's rly annoy-, actl[. The ths tt we put up w for Mojang, right? Lk, it wouldn't be so bad if we wanted to use the upd8 notif. We cld j chk meta. B we want the patch notes, and tt's actl[= On the Comy Srvr, tt's lk= If I j open Insights here for a second, actl]... Uh, whr am I? Server Insights... If I go to the #annc] chnl on Insights, I c see the most rcnt post in #comy=news made it to 27 srvrs. And the most rcnt post in #minecraft=news made 63 srvrs. So, ppl want the patch notes, clearly. Uh, tt's lk 6 more srvrs than December too. Er, so thr are 2 srvrs w over 10,000 users folw- us. That's kinda scary.

Uh, tt's what cache=bust- usually ivlvs, nnkb. Usually you j add a query parameter w the curr t in it. Um, tt doesn't work. It mks sense tt it wouldn't, but still annoy-. I apc8 tt qn. Uh, btw nnearth, did you end up get- back?

nnearth: Yes, I did.

nngdu: Oh nice. Well, wlcm back.

nnearth: Hello. Well, I cld mk some of the mtgs.

nngdu: Congrats, you did it. Eh, why not? We might as well. "How are you guys today? How's 2022 treat- you guys?" From Olivia.
Uh, personally or proj=wise? Personally, it's fine. It's anor year, yk. Hope[[ less Covid, prob not. How abt the others in here? Aone wanna chk in?

nnoro: Pretty good, yeah. Went to some family event.

nngdu: Tt's gd to hear. Uh, proj=wise, we're still get- back into the swing of ths, as I've said. No major worries. It wld be nice to get pgbuto done. Well, fn[. 

I see Leo say- on Mumble, "NFTs haven't died yet, so this year still sucks." I mean, fair. Yeah, thr's an awful lot of NFT stuff gg on. Thr's actl[= I saw some tweets posted earlier to Comy, whr svrl of the major Discord bots by Botlab have started ad- crypto=bots. Those play=to=run bots. Tt cld only go bad.

nnoro: Isn't that a scam?

nngdu: Not ncsy[? It's peggy, which is ~~out~~ for a long time.

"Is cereal soup?" says Arathain.

nnoro: Yes.

~~(One half of a convo happening here)~~

nngdu: No, I thk it's more of a salad, and milk is the dressing. "Salad is j unmixed soup." I mean, ig. Oh, the ~~culebroom~~. I had heard of tt, I j never saw it. "Salads in a breadbowl are quiche." Yk what, we can't be frens, I'm sorry. Thk goodness for starch. Yeah, it's great, isn't it?

Uh, OK. Are thr any more qns? Any more on=topic qns, hope[[? Ath you wanna yell at me abt on the ttcomy? I see Favrito j got here. Hi Favri= Yeah, I'm gonna try tt agn. Hi Favrito. "What's curr[ block- the Quilt launch?"
pgbuto. pgbuto, pgbuto, pgbuto. Um, we say tt a lot bcz we nd Gradle ppl. If we had Gradle ppl, we'd be a lot further ahd, I thk. Um, it's j how it is. At this pt, mb we shld j cobble sth tgt and get sth fn[, w/o the bells and whistles, b=

nnearth: Yeah, at least I hv the feeling tt if we get at least sth fn[, then new ppl c prog w the other projs and help to atrk more contributors, bcz we hv actl[ stuff to do= more stuff to do on the other projs. Then we can see it used in practice. Then mb any of abt 1 in 500 of those ppl might want to work on sth w Gradle.

nngdu: Yeah, prcs[. "I wish I cld offer my skills, b my Gradle skills are pretty bad."
Yeah, Gradle's the only realistic tool, I thk. It's the one most ppl are used to. Mostly the other altvs are... strange. Or j too domain=spfc, rly.

nnoro: Or xtrm[ proprietary.

nngdu: Or xtrm[ proprietary, yeah. Or j rly old. Rly, it [Gradle] j ends up being the best option. A lot of people hv sgst_ Braquira, but it's way too dmn=spfc, and kinda niche. I thk, anw. Lk, sure, OK, you build mods with Braquira (Transcriptor's Note: I couldn't find anything about this), b thk abt how tt lims you when it comes to gnrl devt. ~~Bundle sth else~~. Lk if you hv an executable mod foreg, yk OK, they cld add it, b what else is gonna be missing, yk? It doesn't supt Kotlin or other langs yet either. Mb it'll be sth to look at, but we're j gonna hv to stick w Gradle for the t being. Sorry, that's my dog.

nnearth: Thr's also a MC=spfc build sys tt's being built by sone, I can't rmb what it's call_. Apologies, b agn, tt's a lil bit too= most of us thk tt's a lil bit too new to jump onboard with.

nngdu: Are you thk- of Braquira?

nnearth: It might be the same th.

nngdu: I thk it is. The altv is Basil, but not rly many ppl ustd it. Basil is not MC=spfc, but it's v new and strange and kinda lim-.

nnaurora: I'm not sure tt it's rly new, bcz I had heard abt it years ago. B it's= In my exp, it wasn't right w lk IntelliJ.

nngdu: Uh, yeah, tt makes sense.

nnaurora: And for stuff, lk in the case of deps, at least, by dfal it doesn't supt Maven and stuff. So it's rly manual, it's not practical.

nngdu: And thr goes nnkb, our Basil evangelist, saying it's prob not a gd choice. I've a Gravel ustd- from a user perspective. I've tried to write plugins and fail_ miserably, so tt tells you abt all you nd to know abt tt. You are the ~~one percent~~, Parzi. J wait- for sone to sgst makefiles. Bcz you know it's gonna hppn.

nnoro: For those in the podcast, who can't see the chat, the chat j exploded w 'NO's in resp to nngdu 's sgst]. Thr's at least one, "I'd quit modding." Yep. Alrt, well, we're skdl_ for abt 10 more mins if aone h anym qns.

nnsouth does not like ~~Glinting~~, poor nnsouth. Hey, you're lucky. I almost moved to Spotless, and tt's even worse. Well, nnearth...

nnearth: I'm not gonna ans ath right this min.

nngdu: I j find it funny tt you metn_ tt yslf earlier as well.

nnearth: Yeah, we metn_ literally tt inrl[. Oh, hang on, is that= We haven't even=

nngdu: I'm not gonna click it bcz we nd nnhav to ans tt rly. So we got your qn, Parzi. We can't ans it rn. Yeah, we c save it for next week. We'll j leave it in thr, we can go back to it. Yeah, but it's a difficult one. A dfcl one. Tknl[ it's up to nnhav or well, the ttadmin, but we'll nd to see what hppns w Open Collective first, I thk. Yeah, I like Ko-Fi, b IDK, Open Collective will dfnt[ suit us btr if we end up using it. But, uh congratulations Parzi, you've spawned a whole inrl convo, w/o even rlz- it. Congrats. 

I apc8 the off=topic qns, Olivia, but if we hv on=topic ones, I wanna do those first bcz we don't hv much t left. OK, Ig we will then. Well, Alizay lks sushi, apar[. I'm a burger kinda person mslf. I used to lk pizza, but I don't eat it anym bcz I'm lactose=intolerant now. nnhav says, "Lim- me to one favourite meal is simply impossible." That's what Olivia asked, I forgot to say. It's not so bad. I mean, you get used to it when you hv no choice. Lactose intolerance is j one of those ths, yk. And thr's a lot of gd vegan altvs and those are all lactose=free bcz obv[.

nnoro: Yeah, being lactose=intolerant isn't gonna be lk the worst, since thr's a lot of options. I'm gluten=free so I know what it's lk to not be able to hv a lot of stuff. B I feel lk being both lactose=intolerant and gluten=free wld be abs[ horrible.

nngdu: It wld be pretty bad, honestly. It wld. Yk bkfs cereals? It turns out a lot of them hv powder_ milk in them, for some rsn. And when you look at lk gluten=free cereals foreg, which do exist, most of them also hv milk powder in them to bulk them out. So tt way, you'd be eat- a lot of your stuff yourself, I thk. Or j eat- vegetables all day, which, fine, Ig. 5 mins, if thr's any last-min qns.

nnearth: Soy as well. Thr's other soy ths as well. Soy lechitin, soy proteins. It's j ewhr.

nngdu: Oh, here's a qn. I thk I c ans this one. nnsouth asks, "Did we ever figure out whether the Quilt Client was ever gg to send a list of install_ mods to the Quilt srvr?"
I don't thk we finalised it entirely. B the plan was bsc[ tt we were gonna use plugin chnls. If you hv QSL istl_, or a mod using QSL = therefore we istl QSL for you = when you connect to a srvr tt also has QSL istl_, then the client wld tell the server what mods it has istl_. J the mod IDs. Now, this is an itrs- medium in my opinion, bcz you end up w a sitn whr this only hppns when the client and the srvr hv QSL istl_. So if the srvr doesn't hv QSL = unless it's Hypixel = it's prob not listen- for the mods in the first place. So we j nvr send them. Tt's abt the long and short of it. QSL isn't gg action the list. It's j gg to rcv it, and other mods will be able to get at it if they want to.

nnaurora: Well, if the chnl is reg_, aone, any srvr ~~cld reg, thr's no rsn for it~~. So it cld get the modlist. Even Spigot cld get the modlist.

nngdu: Yeah, of course the srvr cld reg the chnl. But the pt was more tt if the chnl's not reg_, we don't even try and send it. So it's rly up to the srvr.

nnaurora: I mean, tt's literally dfal MC bhvr.

nngdu: Yeah, of course. Ah, hello nnhav.

nnhav: Hi, I have returned.

nngdu: You hv return_, wlcm back.

nnhav: Seems lk we're pretty much wrap- up here.

nngdu: Yeah, more or less. More or less. Thr's one more qn we c do, if no one wants to tk tt.

nnhav: Oh, the Config API one? Sure, I c talk abt tt a lil bit. Ig I'll reiterate. Hi, this is nnhav. I have return_ from my Windows Update kerfuffle. The qn is, "On a scale of Cloth Config to Omega Config, how dtl_ and cplx will the Config API be?"
Tt's a qn tt has a couple dffr[ anss, partially bcz thr's no real consensus yet, and partially bcz of my plans tt I hv = tt bsc[ exist in only my head and tt I haven't formalised ahwr = for it to be more of an open backend w a fairly rsn[ dfal frontend for ppl lk devs to use. But lk w a lot of xpnd]s. 

Foreg, don't intend on the dfal way of making configs being smlr to Cloth Config / AutoConfig. I don't want it tb annotation=based. I don't lk annotation=based ths, so if I mk a dfal frontend it won't be annotation=based. Tt being said, the backend shld be open enuf tt sone cld come in and write a frontend for dvlp- configs tt cld be annotation=based and still mk use of all of the fetrs such as: Lk I was say-, I plan on hv- config sync-, and config screens tt cb built atm8[. Integ] w wtvr ModMenu=type th we end up hv-. So I can't xk[ say on a scale of Cloth Config to Omega Config, how dtl_ it'll be, b those are my gnrl plans rn. If tt helps ans tt qn.

nngdu: Alrt, thx for tt nnhav. So we hv hit the hour-mark. We usually end at abt this t, b is thr aone on the Mumble here who wants to get ath out b4 we do? Nope, doesn't look like it. I hv to say, I didn't xpk this mtg tb mostly qns, b tt's how it goes.

nnhav: Yeah, it's alrt.

nngdu: Xk[. Alrt, well, Ig we'll wrap it up then. Thx eone for coming. As alw, we'll be back in 2 weeks with the next mtg. And we'll get this cut down and put into a podcast. Hope[[ at some pt today if we hv t. Hope[[ we will. I thk we will, b we'll see how we go. Anw, thx for coming.


















