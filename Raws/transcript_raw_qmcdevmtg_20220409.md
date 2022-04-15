nngdu: Hello eone tt's j respond- to the ping in an annoyed way. How're you doing, eone. It's tt t once agn, and I'm actl[ doing sth good for a chg, look at me. Obv[, if you're sit- on Mumble, you'll wanna be deafened on either one of them. Look- at the list, I'm lk, "Hmmm, thr's a few duplicates there." 

So, we're gonna gv lk 5 mins mb, to let ppl show up. Feel free to chat away in the #meeting-chat chnl j above the #stage chnl. Crtn[ see- a few new faces this t. If you're new to the mtgs, wlcm. Also, you're slightly late, but tt's OK. Also, c someone confirm tt I unlocked ~~Warp~~? The perms look right, but nobody's chatting. Fabulous, ty. What was tt spooky voice I heard over the ether j thr? Alrt, nice, looks good to me.

As alw, we open the AmA at the start and close it at the end. So if you wanna ask any qns, you can use the /ama cmd on Discord, and they will queue up for us to ans later on. We also hv a bit of an order- dffr] ltr today, but I'll go into tt in a lil bit. Not a big deal, tho. Here's the secret, nngli: It's alphabetical. Well, mostly alphabetical. Imn, we do tk a few liberties, but it's ok, we j re-define the alphabet istd. Hoisting, huh?

nncheat: Oh yeah, "Hoisting" is a great name. Exclamation mark CHASM is great. Ig triple or quadruple exclamation marks, j tb sure.

nngdu: Hai, I love it when the Mumble bot reconnects on its own tho.

nngli: I thought you j put us on mute for a bit, tbh.

nngdu: No, it j reconnected on its own, I thk.

nncheat: The only voice we lose in the recording is the one on Discord, not on Mumble. So j don't say ath impt when it disconnects.

nngdu: Imn, y'all are the impt ppl in this mtg. You lk Hoisting, Yujin? That is ustd[, your name does start with a 'Y', I know. We'll be get- started in j a min. I do wonder how many ppl lk join when the event starts bcz they're itrs_, or join to complain abt me ping- them? I mean, tt's rsn[ too, I'm all abt tt.

Alrt, I thk we c get started. It's about five past, six past even. The order's a lil bit dffr[, we're gonna be going thru qsl and mapg first bcz nnaurora's gotta leave later, but I'm sure y'all won't mind that. So let's get started, Ig. nnaurora, wld you lk to get started with qsl?

nnaurora: Yeah. So this is the last mtg b4 Beta, which means we won't talk on the same ths because we have more of a focus on the Beta part. So for qsl, we are a bit concerned bcz we hv to specify a versioning scheme for qsl. B4 aone says, "Yes, but there's Semver," it's not entirely abt Semver. It's mostly abt how we version the qsl as a rule of which version, or which module extra. How we vrsn eth dpd- on the MC vrsn, and a lot more.

So tt's a lot of stuff tt foreg Semver doesn't rly ans by islf. So we hv to sit down and thk abt it. It's taking a long while, which is a bit concern-. Since while Beta isn't rly tt far away, but we do hope tt we figure out sth tt is solid enuf for Beta. Bcz the idea is tt it's all set up so tt we don't hv to touch it too much, and so we don't hv a big disaster. Bcz while we can break APIs in Beta, break- the vrsn scheme is much, much more dangerous and not rly worth it. So yeah, tt's sth we nd to get right.

Inrl[ thr's been some dscs] abt Semver, bcz Semver was ~~fought~~ for libs, mainly, and it's a bit dffr[ from mods. Mods are q a weird case. Thr's also the case of content stuff which is another can of worms. So thr's been talks abt break- Semver in qload. No one's sure yet, so don't make asum] rn. But yeah, tt's what all the vrsn- stuff was abt.

O/w, for qsl, feature=wise, we had some PRs tt hb_ merged. I think last time, Iirc, we got a port of Fabric's Dimension API, which is mostly a helper to teleport entities betw dimensions. Bcz apparently tt's not ez w/o APIs. 

We got server-side arg types, which is rly, rly nice for common modules, bcz tt means you c hv an arg type tt dir[ maps to an event w/o hv- it tb present on the client. Bcz for those who don't know, arg types are a bit weird, bcz they're not j irpt_ on the server, but they're also irpt_ on the client. You can't rly sync tt, lk you cannot rly send stuff tt the client doesn't know. Bcz, well, first of all, you can't j tfr code. And thr's also the case of a ~~linear~~ client tt cannot even load it ~~all the way~~. So the goal of server-side arg types is to match an arg type to another exist- type when sent to a client tt doesn't hv lk mods tt reg tt arg type. But if the mod is present, and Quilt Ntwk- and Quilt Cmd APIs are present, then it will be actl[ sent.

Thr was much smaller PR that ~~quit regy~~. But tbh, I personally had issues with some stuff, bcz Aurora's Decorations does some weird stuff w regy. It initialises a bit too early for some of FAPI. So those have been ~~constructions~~ tt hvb applied to qsl. So lk, thr's a BlockItemMap, dictionary, wtvr you wanna call it, in MC, and tt one allows us to know which Block maps to which Item. So when you control=click foreg on a Block , it'll gv you the right Item. And it has other uses. 

The th is, tt map, when it's created, it's not fill_ auto[[. So bsc[ in vanilla, the only moment when it's actl[ fill_ is when the Item's class = Which is a class for when every Item in the game is initialised, which is not great for modding. So what Quilt Regy does is it reg sth totally aft tt is initialised. Some modded stuf j works. And j for lk= J to know what mk it dffr[ from fapi is tt we reg tt listener a bit earlier. So we catch more stuff. 

O/w, other stuff is we caught some issues in the Regy Monitor, which is an API to monitor regys, which is rly, rly cool. So you c do stuff on alr existing entries in the regy, but also what is reg_ after. It's rly useful, and thr's a new bug tt got in in 1.18.2. Bcz now we cannot reg stuff while iterating over the entries, so we had to modify tt. It led to also new method in the context of trying to reg sth safely. 

O/w, feature=wise, I thk tt's all. Qsl is, at least, it's rdy fetr=wise, thr's not a lot of stuff to figr out. And we're well aware tt we do not cover lk every case tt fapi covers, which is fine bcz well, it's still v early. So it's OK bcz ppl c still use fapi for stuff tt we don't cover. So on tt part, we're rdy.

nngdu: Also thr's sth abt get- qsl on qload.

nnaurora: Yeah, currently qsl is not dpd- on qload. It will come soon. Actl[ the final comment period for the PR has ended. But we're wait- a lil bit more bcz we want tb sure. Bcz thr's some stuff tt came aft tt we nd to figr out. But o/w tt PR might be merged v soon. 

Also, nngli, j to mk sure, thr's a lil bit more stuff tt wasn't covered in tt PR. It's the fact tt there's the ModContainer class tt is used in the API so far. And the issue is tt it's using the Fabric Loader one, and what's intended is for the qload one tb used. So it also means tt once we go on Quilt thr will be an API breakage. So every mod tt is currently using qsl, if you touch the reg, lk the resource pack, or resc loader, if you use the Quilt entrypoints, it'll break. Bcz thr's a famous ModContainer class thr. If aone wasn't aware, now you're aware, but yeah.

The last thing is, qsl and fapi. ~~High priority~~ tt gvs fapi API ~~surface~~, while ensuring tt it works w qsl. Bcz of some mods tt hvb pdtn=testing w tt. Thr was an incompatibility tt was discovered with Continuity. It was fixed, so tt's rly gd. Thr's some bug reports tt are a bit obscure. So currently we don't know if it's rly bcz of qsl stuff, or if it's bcz of jij issues. So some stuff we'll have tb ~~contacted~~ w the qsl=fapi ~~future currently~~ in the mods folder. But hope[[ tt'll help us to fix some mb unseen bugs b4 Beta, so tt'll be rly, rly nice. But at the same t, Beta is a t whr thr still cb bugs. But it's still better if thr's not many bugs. 

O/w, I think tt's all, aside fr the usual reminder tt we're still look- for ppl. Esp for fapi=qsl, bcz currently I'm the only one mntn- it. Which is a bit, how to say, exhausting. So if ppl are itrs_ in mntn- tt lib, tt wld be rly, rly cool. Someone showed up, which is rly nice, but o/w if we c get more ppl to mk sure tt it's mntn_ and doesn't get left bhd from upstream tt'll be rly, rly cool. O/w I thk I said all the ths tt nd_ tb said. Thk we can go over to the next proj.

nngdu: Thx for tt. Yes, j a reminder, nnaurora j mentioned it, but to reiterate: qsl nds more ppl, esp qsl=fapi Module Team, since it's j nnaurora mntn- it and tt's kinda stressful guys. So if aone has any itrs in tt, pls do let us know. Are you OK to go over mapg as well now?

nnaurora: Yep. So I hv tbh, I do not rly follow much mapg curr[ bcz I had a lot of stuff. But as usual, when a pgsnap comes, we upd8. We do have caught some refs where Mojang renamed stuff w/o actl[ hv- sth tt breaks the API. Tt's a lil bit worry-, bcz initially when we brought up pghs, we kinda said tt it shld not rly be happen-. But so far it seems tb rly, rly rare occurrences, so it still shld be fine. But what we noticed is the curr Matcher tt we have = tt is, as a fun fact, written in Javascript = is not strong enuf and rly nds tb rewritten. First of all, in Java, and secondly, to cover many more cases.

The th tt ~~doesn't mesh~~ is tt pghs is much, much faster to gnr8 than pgim. We're usually able to upd8 qmap faster. So tt's a rly nice achievement. O/w, for aone ctrb- to qmap, thr hb cases where Mojmap leaked in qmap. Some ppl said lk tt, it doesn't sound lk a big deal, since we don't hv a cleanroom policy. But when it bcms a big deal is when it brings names tt breaks the conventions tt were set for qmap. 

So for aone ctrb-, be mindful of tt. Double=check when you use a Mojmap name tt it doesn't break a convention. So lk, if you try to path serialise to JSON, in tt case thr's a conv in qmap abt serialisation methods tt says ~~you don't hv tb spfc. Lk it's serialised, it j to JSON~~. Any of those occurrences will be fixed, evtl[. But for aone tt is willing, or is curr[ ctrb- to qmap, it's j a reminder. 

O/w, abt the Beta, qmap hb in co=pdtn alr for a month. But thr is some impt stuff to csdr. Foreg, and for Quilt Beta it'll be rly relevant, we're curr[ using qmap on Loom, bcz we do not have pgbuto yet. Thr are some issues with it. Foreg, thr are rly, rly random methods tt refuse to get mapped. I know thr was talks abt fix- it. I'm not rly much informed abt it. It's one th to csdr, and the other th to csdr is betw ~~Mojmap names and constructors~~. Not entirely sure why, but for now it doesn't. So tt's also one csdr]. But o/w, aside from those issues, it's dfnt[ usable, at least and esp for qbeta. Thx to eone tt has used qmap alr bcz either it helps us to figr out bugs. It helps sometimes for the names. It shows tt we're not doing tt proj for nth. So, ty at least. O/w, as long as qsl is upd8_, thr's not rly much more to say abt all of this.

nngdu: Alrt, thx for tt nnaurora. You had a bit of a marathon thr, good job. Alrt, we will move straight on since we're alr halfway thru. nngli, can you talk about pgbuto?

nngli: Alrt. Is this th work-? Alrt, so pgbuto, we hv our own fork of Loom now. I blv I brought tt up last time. I've j been work- on fix- the inevitable bugs I've intro_ and making sure tt eth is good to go for it tb used with qsl and qload. And rly, tt's abt it.

nngdu: Alrt, thx for tt. nncheat, would you lk to talk abt CHASM?

nncheat: I wld love to talk w CHASM. CHASM has had some busy 2 weeks. Or tb precise, some bz 4 days at the start of 2 weeks. Bsc[ I've been re-writing the entirety of CHASM Line simply bcz I wasn't happy with the impl]. It was a bit messy in spots, it was bsc[ my first attempt. I wasn't entirely sure what I was doing. So I bsc[ scrapped it all, did it agn, took what I learned and now it's better. 

It is agn, 90% the same, so Ig it wasn't tt bad in the first place. But the worst parts tt I didn't like abt the impl] are much cleaner now, so tt's mostly related to expression=caching, function call=caching and deal- with occurrences and such. It also chg_ a bit ito of syntax. Small chgs tt ppl wanted, lk being able to omit the dollar sign for specifying a rule if it's ~~simply~~ for the terms, method, or wtvr. And easier index-, and v impt, also now has the cpbl] of providing intrinsic fns. So v simple operations lk get- the length of an array, rlvt for get- the number of istr]s in a method, or spfc[ target- the last istr] nd_ to know the length of an instruction array. So tt works now. 

Hwvr, thr's still a lot of stuff to do. The base fn[] is pretty decent. I'm happy w whr it is rn. Thr's some dtls we hv to figr out regard- rep] of fn descriptors and parameters and ~~method types~~, bcz tt's redundant if we rep them all, but it's annoy- if we don't hv them all. 

But actl[, if aone is itrs_ in help- out w CHASM, thr's a few v great simple issues open at the CHASM repo. If aone feels lk help-, the intrinsic fns one is rly simple and prob lk 10 lines of code for most of the fns on thr. Error messages is a bit more of a lang=parsing one if aone is itrs_ in help- w tt. I had someone who was itrs_ in writing up the lang specs, they started but never finished. Tt wld also be highly apc8_ bcz rn I'm mostly work- alone in this, which is qk, bcz most of the groundwork has alr been laid so it's not tt bad. But I'd also apc8 more help.

I thk as alw, talk- abt qbeta, CHASM is not rdy for qbeta. It was nvr planned tb rdy for qbeta. In fact, it's in much further prog than we even anticipated a year ago. I do have a chunky access file now, a prototype lying ard now tt kinda works. But nth pdtn=rdy. We'll hv to see how to integ it into qload and stuff. I thk tt's all.

nngdu: Fabulous, thx for tt nncheat. nnhav, wld you lk to talk on Infra for a moment?

nnhav: Sure, can eone hear me alrt? Great, so yeah, as ppl who've been ard for a lil bit know, I've been work- on my own altv sys for host- Maven repos tt doesn't rely on ~~Seriotypes~~, Nexus, or I = 4get what the other one is tt is popr[ used = So tt's rly close to being able tb used. I got repo mirroring down so we c host the files fr central or from Fabric's Maven, or our own Maven. 

And then, I thk the only ths tt are left are I nd to rebuild or rewrite the portion tt gnr8 the static website so tt you c browse all the artifacts tt are in the repo. And that shouldn't be too bad. And I have add handling for pgsnap repos, which is also lk 3 lines of code. So it shld be rly close to being able tb used soon. It won't be pretty, but it'll be fn[ and it'll be a lot cheaper than what we're curr[ using.

nngdu: Tt's an abs[ big plus too csdr- you've been pay- for it all, I hv to say.

nngli: nnhav's rly been carry- us here.

nngdu: Yes, it's true. Is tt it for Infra? Fabulous, thx for tt. nngli, I thk I hv you down for qload.

nngli: Yeah, that's correct. So qload is kinda the same deal. We're rly work- hard on making sure tt eth is gonna be as smooth an exp as psbl. So as we're coming up w bugs, we're try- to squash them. We do hv some new fetrs coming down the pipeline. Work on loader plugins is I blv slowly coming in from nnalex. So it's a ways away, but it's coming down the line. We're get- rdy for being able to support pghs properly. We're adding some extensions to the quilt.mod.json so we can figr out what pgim mapg a mod is using so tt we can remap them. And since I don't blv I hv anor good chance to speak today, I'll j throw in tt we will be having a proper Quilt eg mod coming up within the next few days, hopefully. So keep an eye out for tt.

nngdu: That's exciting stuff. That is prety exciting, I hv to say, I'm look- fwd to tt as well. OK, I thk tt concludes all the big teams. Spfc stuff, as alw, hit up that /ask if you hv some qns. We got a couple in alr. Thr's a couple other ths to cover b4 we move onto those tho. 

First one, obv[: Hey, Beta soon. This is the last public dev mtg b4 the public Beta on the 20th, as nnaurora has metn_. So yeah, we're look- fwd to tt. We hope you're look- fwd to tt. But if you hv any qns you nd ans_ b4 tt happens, this is the t to put them thru. 

Add[[, the Events Team has been work- on BlanketCon. Now, I asum most of you hv heard of what tt is at this pt, but if you haven't, BlanketCon is essentially an ingame modded conv. So it'll hv booths and events and panels and all tt sorta th. Sorta in the legacy of BetterThanMinecon if aone here is aware of what tt was. It's being run by the Events Team in collab w the Modfest Team. So of course **Lemma** is heading tt up, as it does. 

I'm q excited abt it. Thr is a website, which I will link straightaway. Now, if you wanna submit a panel, or event, or booth for this, you shld do it rly soon bcz we've got a crapton of submissions in and we're kinda run- out of space. So if you were plan- sth, get tt in as soon as you can. O/w, we hope to see you thr. It's the start of May. Looking fwd to it.

nngli: "that's an excellent problem to have"

nngdu: Yes it is, it's a great pblm to have. Alrighty, is thr ath else aone wanted to cover on Mumble? If not, we'll move into the qns.

nncheat: Is thr no news from teams outside of Events then?

nngdu: Not tt I'm aware of, I've been q bz. But I haven't seen much going on. The only ths tt I'm look- at rn since I've been tt bz is, I thk the Optifine comy are look- to collab on moderation with us. Altho, they're still dscs- whether they'd lk to do tt. And the same th w Blankworks, but we haven't heard back yet, so we'll see. Other than tt, thr hasn't been tt much going on w the Comy Team.

OK, Ig we'll move onto qns then, and tt one is dfnt[ yours, nncheat.

nncheat: Tt one is dfnt[ mine. So first qn is from **Byte** regard- CHASM. Actl[, since Byte is not able to listen to hte podcast=

nngdu: I'll try and type it.

(nngdu's real-time notes: Yes and no, as always.  
Not directly, not first-party, don't think there's anything we really want from this, however, we would like to expand Mixin quite a bit.  
The Mixin frontend is quite comfortable to use for most people, they're used to it and we're like to keep that - eg, we want to be able to target lambdas by callsite (rather than by name), should be easier and more intuitive\n\nIn terms of things that aren't Mixin/AQ - eg interface injection, which we get for free with CHASM - it's completely unnecessary, it's something that you might want but we already have it for free  
Also, **Kroppeb** has been doing some black magic regarding making some method calls automatically async; no idea what it's about but it sounds fun.  
The whole point of CHASM isn't that we provide every possible interface - it's more that anyone can add what they need to it.)

nncheat: Mb you c type it, thx. So the qn is, "Are there any concepts for CHASM frontends/transformers besides reimplementing Mixins/AW on CHASM?"
So, I thk the ans to tt is both yes and no, as alw. First off, not dir[. Lk not as officially first=party supt, I don't thk thr's ath we rly want from this. Hwvr, we wld lk to xpnd Mixin q a bit. So the Mixin frontend is q cmft[ to use for most ppl. They're used to it, and dfnt[ wld lk to kp tt. So foreg, we want tb able to target lambdas, not by name, but by callsite which would be much more stbl. And also, more intuitive.

But ito ths tt are not Mixin or access widener (AQ), we cld foreg talk abt irfc injk], which is essentially abt making an irfc vsbl on source code, lk on your MC dep. This is sth we get for free w CHASM, so we don't even nd to impl this.

nngdu: You cut out at irfc injk].

nncheat: Right, so thr is irfc injk] foreg tt we don't nd, bcz we get it for free w CHASM. Bcz every mixin is prob gonna be source=vsbl anw. So it's cplt[ xnecs.

A qk qn from **AlphaMode** j as a quick intermediate: "Isn't interface injection broken on runtime?"
No, it's j not meant tb work- w runtime. It's xcld[[ meant for compile time. So yeah, tt is sth tt foreg is sth you only nd once, but we alr hv it for free. Then **Kroppeb** hb doing some black magic regard- making some method calls auto[[ asynchronous. I hv no idea what it's abt, but it sounds fun. The whole pt of CHASM is not tt we c prvd many, many irfcs as a frontend, but tt ppl c make their own frontends if they nd to w/o reqr- hacks into it. I thk tt anss the qn fairly xtd[[.

Thx nngdu, I hope you got all of tt.

nngdu: Yep, more or less, ty.

nncheat: I thk in the meantime we c ans the next qn, bcz the ans is alm the same as last week. So I'm j gonna take it. **Octal** asks, "Are there any plans for Kotlin on quilt? (I already know the answer to this, but others might not)"
It's been a dscs] since the last mtg esnc[[ agn. I thk the short ans to tt is yes, thr are plans. We j don't know xk[ how they'll look yet. We want Kotlin as first=class supt swhr in Quilt. We're j not sure whr. We're not sure if it's gonna be in qsl, or if it's gonna be a separate ~~lang ~~team, or lk a separate Kotlin team. J uncertain.

nngli: It's pretty much j a matter tt nbdy has gone down and written down all of the advgs and xadvgs for both yet. Lk I thk that's pretty much whr we are. Lk sbdy j nds to write a proposal and say why.

nngdu: Yeah, ig ideally tt wld be kinda RFC territory, wouldn't it?

nncheat: Tt is abs[ RFC territory.

nngdu: Yeah, so tt wld be a gd way to start: Drafting up an RFC and see whether we get wider comments on tt. It'll be great to hv supt. Obv[ not biased at all as a Kotlin dev.

nncheat: I thk thr's no one against supt for Kotlin. It's j the qn of how and whr.

nngdu: Right, move on. Rmb, get your qns in with /ask. We don't hv tt many in, so if you hv ath, feel free. We still hv lk 15 mins. Uh, my Welsh isn't great x4tun[[, so I can't pronounce this name properly, but **grifferthrydwy** asks, "Is there anywhere to sign up to attend, but not showcase anything in blanketcon?",
The ans is no, you don't nd to. J show up and join the server, install the modpack and you'll be thr. No nd to worry abt tt at all.

Alrt, tt is the bottom of my list of qns, if aone h ath to ask, feel free w /ask. W/i rsn, tt is.

nncheat: Plz come help out, we c alw use more ppl. You don't nd tb super professional, or 20 years' exp junior dev, sth IDK.

nngdu: Tt wld be one heck of a junior dev.

nncheat: Agn, esp for CHASM foreg. We j nd ppl who write lk 10 lines of code, 20 times. J= I rly j can't be bothered bcz thr's so much other stuff to do. I alr had great help on CHASM the last time I tried to get ppl on it. But it was just= At Javadocs foreg, you don't rly nd to know ath abt Java to do tt. So yeah. 

I'm sure thr's plenty of smlr cases. I know nngli did sth on qload, thk it's taken care of but... Mapg is also alw sth you c alw rvw w/o know- too much abt the context. It's a great way to get started in Quilt.

nngli: Uh, this is dfnt[ more for the devs here than the comy, but if you look at tt issue tt I open_ on qload, I feel lk tt's a v gd eg on how to hand sbdy work and get them to ctrb.

nngdu: Do you hv a link to tt?

nngli: Yeah, I c pull tt up, give me one second: [https://github.com/QuiltMC/quilt-loader/issues/59](https://github.com/QuiltMC/quilt-loader/issues/59)
("This is a good first issue for anyone looking to dip in to contributing to Loader. If you are interested in getting this done, feel free to ask me questions at glitch#3274 on the Toolchain Discord....")

nncheat: Also as a desperate call, if aone's v cmft[ w pgbuto, let us know.

nngli: The trick is bsc[ to impl the whole th in your head, and then xk[ what you nd to do. And I know for this spfc issue, it took me more t to write the issue than it wld hv for me to j impl it mslf. But we had sbdy do it, and did active ctrb- and tt's what impt rly here.

nngdu: Yeah, bcz we're at the pt whr lk some of the teams are fairly stretched out. So we rly j nd more ppl doing the same stuff in a lot of cases.

nngli: Yes, xk[.

nncheat: Yeah, it's rly ~~about a~~ big issue thr.

nngli: And if you don't lk go into tt much dtl, you dfnt[ don't hv to. But it helps to hv ths tt are tt ez j to get ppl who are nervous abt it onboard.

nncheat: Mb we shld hv sth whr lk, you copy fr the #voice=chat and then xpln it to them. Bcz it's prob faster than writing it out. IDK, what if thr's some fancy comy magic we c do to get us closer to the comy.

nngli: This issue and all this is actl[ inspired by sth tt Rust does. They hv mentors so they'll mk issue tt they'll assign a mentor to, then sbdy takes this, and then they have one person tt they contact. And then that hv sbdy tt guides them thru the whole prcs, helps them w respond- to rvw comments, etc etc, and gets them thru the whole way. And then, I'm pretty sure tt they're pretty successful for tt.

nncheat: Yeah, tt seems smart. Ok, yes, here's a fan favourite. **Will BL** asks, "will the chasm mixin front-end include anything like mixin-extras? (<https://github.com/LlamaLad7/MixinExtras>)"
Now, Mixin Extras is a name tt hb thrown ard a lot. I haven't looked too closely at it tbh. I'm pretty sure the ans is yes fr what I've heard abt it. Lemme check. Yeah, so mod effect expression value, sure, tt's sth you c dfnt[ hv in CHASM. I thk it's one of hte most req_ fetr is lk to modify conds in if=statements or in loops or ath. Which I thk is= For what I'm hear- in Mixin Extras, dfnt[ sth we want. ~~Breadth=width~~ conds sounds lk sth tt we talked abt. Non=conflict- overrides is what we called those, same idea. Or non=conflict- redirects even. Lk you redirect some method call only if a crtn cond happens, and you c do tt w/o having a lot of mods conflicting.

So I thk the ans is yes. I'll hv to look in dtl to see if thr's ath tt's not in the CHASM mindset, or we wouldn't want to impl this way. But in principle, yes, pretty sure. Tt's sth you c xpk in the main Mixin impl] on Quilt in future.

nngdu: Sound pretty fabulous to me. Any more qns to come in? We still got abt 10 mins. I hv a qn: **grifferthrydwy**, how do you pronounce your name?

nncheat: Ans_ via text.

(**grifferthrydwy**: "griff earth ride why")

nngdu: So I'm not actl[ Welsh, it j looks Welsh. Griffer=thry=d=why? OK. Tt's not too bad. Griffer's the right way.
(****grifferthrydwy**: "add a discord bot that adds a number equal to the number of issues you've fixed to the end of your nickname. people like it when number go up")
The scordboard's is itrs-, but I'm not too sure abt doing tt, j bcz I know tt ppl lk to game scoreboards. But lk, if we thot it wld work, it'd be pretty doable. Imn, we hv the tech at this pt.

nngli: I thk it'd be mostly hte ppl writing issues for fetrs tt we'd be miss- here. It'd be more abt lk, who gets to the "one issue you get a week first", than it is lk, yk, who's ctrb- the most.

nngdu: Yeah, it cld be itrs-, it's j tt I don't want to turn it into, yk, lk an Agile burndown chart mtg.

nncheat: Mb you'd open issues for ppl to open issues.

nngdu: Imn, tt's a th tt cld happen.

nncheat: I was honestly surprised when I ask_ for help on Javadocs and actl[ ppl were willing to do tt bcz I hate doing tt. So mb, if thr's someone who loves writing issues on Github, hit us up.

nngdu: Imn, we cld alw use sone to help w tt, for sure. Tt's sth I've been look- for anw, so... Alr, I thk we're abt out of qns, so let's call it thr. Now, I know tt thr's still stuff to talk abt. Were you guys plan- on doing more voice in the other voice [chnl], or were you gonna do lk a closed mtg for the extra Beta stuff?

nncheat: Well, I thk, as alw, I invite the comy to an after=party in #development=zero. Hwvr, it might be tt a few of our devs will go into dev=mtgs and talk abt stuff tt they were talk- abt b4 the mtg started.

nngli: I don't thk ath we were talk- abt strictly has tb secret.

nncheat: No, we c do it publicly, ~~but it's ultimately Discord. Discord has the public chats~~, so we'll see how it works out.

nngli: Imn, vrsn syss are controversial, but they're not lk secret.

nncheat: No no no, it's not secret, tt's for sure. Imn, we can go into #dev=zero, and if it gets too loud for other rsns,, then we c j move to #dev=one or wtvr.

nngdu: Alrt, sounds good. In that case, thx for coming to the mtg eone. The next mtg is prob actl[ gonna be at BlanketCon rather than on Discord. Um, we'll mk an event and post a bit more when we know a bit more.

nncheat: Tt's two mtgs. The next mtg is j aft the Beta, then the one aft is the one tt's at BlanketCon.

nngdu: Oh, you're right. Yeah, tt's the one aft tt. In that case, we'll see you all back here next week, w news fr how you've been doing w the Beta ideally. Either way, thx for coming eone, and thx for eone coming on Mumble as well.
