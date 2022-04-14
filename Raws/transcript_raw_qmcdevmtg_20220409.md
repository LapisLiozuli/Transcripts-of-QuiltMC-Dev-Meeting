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

26:34
