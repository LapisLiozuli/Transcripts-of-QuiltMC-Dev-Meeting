nngdu: Since bcm- a speaker reqr click- mtpl buttons, I would rcmd bcm- a speaker and then muting yslf.

nngdu: RFC 54? I must admit, I haven't had a single moment to look at that yet.

It's gd tb doing this on Discord agn, even tho not eone's a fan of it. But it does mk our life a bit ezr. We're test- the new Craig, I'm not sure what it adds over the old one but Ig we'll find out.

[RFC 54: Quilt Kotlin Team by Oliver-makes-code · Pull Request #54 · QuiltMC/rfcs · GitHub](https://github.com/QuiltMC/rfcs/pull/54 "https://github.com/QuiltMC/rfcs/pull/54")



nngdu: 'Crank'? Oh you mean Craig. You c see that Craig is the top user on the right, at the top of the Online section.

nncheat: Must be bcz of your accent.

Blodhgarm — Today at 12:04 AM
I would be chatting if I wasn't loading a trailer with wood

nngdu: Ustd[ blodhgarm. We nd an elevator music bot for the first 5 mins. I'm only halfway joking.

nnem: Instant DMCA

nngdu: Well it's been 5 mins so we might as well get started folks. Wait a min, it's teh wrong show. As usual, /ask if you hv qns to ask and we'll ans those at the end of the mtg.

nnem: ??

nngdu: Well it's fine, Ig they'll hv to do it now. Let's start of w the tools as alw. nncheat, are you thr?

nncheat: If I find the button then yes. I'm stand- in for nngli today as nngli is x4tun[[ unavbl. But look- at the git there's 2 ths tt hppn_ by menoprot, ig. First is add- data prerogative to choose whether quilt.mod.json or fabric.mod.json wld be used if both are present. I'm not sure what tt is mslf, but I'm sure tt those who hvb wait- for this will know what it is. And nngli has merged the upstream.

One more th tt I'll ment_ w/o build- pressure, then some volunteers hvb add- pghs to Loom. So we'll see how tt goes.

nngdu: Tt'll be great. Thr's an itrs- PR swhr, wonder whr it is. We'll get thr. Now it's ttcotl, tt's me. We're get- a lot of req on the comy server. Cozy set up, outdated qsl, outdated loader, and mods using Fabric inrls. It's still not q thr. It's alr help_ q a few ppl, which is supz- given how simple it is. Please let me know if thr are any other fetrs, but it's been work- great so far.

Next up is Decompilers. nnsup would you lk to tk tt?

nnsup: Yes, thr's been some itrs- dev] gg on w QuiltFlower. 1.8.0 which fixes 2 dozen bugs and adds q a few fetrs. We also decided to go a bit more public w QuiltFlower so thr was a Reddit post we made tt rcv_ q a lot of reception. Now we're look- at fix- a few more bugs. Thr's a few more issues on the issues board for QuiltFlower.... And I thk tt's it.

[Issues · QuiltMC/quiltflower · GitHub](https://github.com/QuiltMC/quiltflower/issues "https://github.com/QuiltMC/quiltflower/issues")

nngdu: Thx for tt nnsup, I'll just link tt in the chnl for aone who doesn't know whr tt is. Next up is Loader, and I blv nncheat is stand- in agn for tt one.

nncheat: I am the prfk stand=in, I forgot to click the button. I4got what I wanted to say, but 1st th is tt thr were a lot of ths fixed for Loader thx to Beta. First off, thx to all of those who reported those bugs. And next, thx to all those ppl who fixed the issues. J qk[ chk the Qload repo to see if thr's ath I missed. Nth. 

Thr's also q a big th w Qload tt wld make q a lot of ppl happy and maybe some ppl upset. Nbdy knew what wld happen, but nnhav made a PR to add a config sys to Qload. So this will be q a big deal bcz not j first=party will be able to mk chgs to qload, but now CHASM can also mk chgs.

nnhav add JSON5 which was much ezr to add, and now it uses TOML. But it c still use JSON5, and aone can add other parser options tt they thk are far superior, then they're wlcm to go ahd... nnhav is rly on top of fix- ths, and tt's rly amazing... Then eone will hv a std config lib which will mk eone standardised.

nngdu: It's gd to see a config PR aft mths of dscs].

nncheat: ???

nngdu: Ty nncheat, was tt eth?

nncheat: I thk tt was eth.

nngdu: Next up, ttmap. nnem wld you lk to talk abt tt?

nnem: Yes, thr's been exactly one itrs- th tt happened inth 1.18.2 mapg which chg_ a structure mapg to a much more accu name. But other than tt thr's not been too much. We're alw look- for Mapg Triage mmbr, even tho we're not doing tt much rn but send a msg in the #mappings=chat if you're at all itrs_.

nngdu: Ty nnem. For qsl, nnaurora wld you lk to talk abt tt?

nnaurora: So, thr's not a lot of stuff tt has hppn_ for qsl. But pts are, the Recipe API got fixes bcz in the og[ PR thr was some stuff tt hb 4goten, and the recipes tt were reg_ thru the API did not work properly in the recipe book, and were not properly stored in the client. Common lib got renamed to Menagerie lib. This has alm no consequences for most other ppl. The only consequence is tt you are a dev and use the manual Maven artifacts, then you j nd to chg one th, and only one th. The rename was done so tt we cld update other stuff ??? w/o worry- too much abt teh scope. O/w, the merged PR is also the transitive access wideners for Block Restrictions tt got merged. This bsc[ means tt for qsl a lot in dev], a lot of bsc[ protected ctors and blocks. Other groupings like the Resource Packs... But lately no commenters hv had t to merged.

And then there ist he Biome Modifications API tt is rdy tb merged, thr were some issues but it's rdy tb fixed. And the ScreenHandler API is in the final comment period, and soon it'll be merged. And thr is rly a big issue w it. Tt's kinda it for today.

nngdu: Thx for tt nnaurora. For Quilted FAPI, nnem, do you hv ath to talk abt thr?

nnem: We hv a few ths to talk about for QFAPI, first of which is... and also rdcs the file size by alm half a megabyte. Other than tt, thr is a PR open for BetterEnd and BetterNether tt cld use a couple reviews. But other than tt, nth much h hppn_ thr either.

I j sent the PR in the #meeting=chat.

nngdu: For ttcomy, you may have noticed that nnnocom hb promoted to full moderator. Plus we're on Mastodon now. We're at ..., see I c rmb ths. So if aone's using Mastodon, you c find us thr. We j set it up thr as an altv for ppl who don't want to use it, or can't use it, or if Twitter dies in a fire after Musk bought it, or has bought it. We do use it and keep it up to date. Ath tt we put on Twitter also ends up thr.

B4 we get to the qns, thr's a few ths to talk about here. First th, as one of Octal's team mmbr req_, thr's an RFC for a Kotlin team. ... some kinds of projs tt m come under tt team. It's been a pretty bz PR, or rltv[ bz at least. Add[[ we're plan- on move- our mtgs to... We've been talk- inrl[ abt how our dev mtg should go. We're plan- on move- the dev mtg ard, so we're look- at how to mv fwd. ... Mv them tot he comty server. But tt's not gg tb the only th we're do-. We're also look- at set- up indiv mtg for indiv teams. So like CHASM... nncheat wld you lk to qk[ pt at what hppn_ in tt mtg?

nncheat: As nngdu said, the public dev mtgs are fun, but devs can't rly talk to each other much. ... but as the direction is pretty solid rn, thr's not been much. So ... So while the dev mtg will bcm even more public, we'll be hv- test mtgs now. Not eone agrees w this, but we tried this with CHASM Team... we c get the info out to each other, so ... so we hv at least 3, 4 ppl who know what's gg on w CHASM and tt's a gd start. And if this bcms a success, we might xtd this further. While it's tknl[ public, we havne't rly publicised it. So if aone is itrs_ in CHASM and wants to ctrb, it's agd place for them to hop in and listen to what's gg on. So you c j take notes as we talk. While it's not proper docu, at least it's some docu. At least it'll help other teams to get an idea of what's gg on. The ttout was tasked w the dfcl task of get- info from devs.

[Chasm Meetings - HackMD](https://hackmd.io/@CheaterCodes/SyEtwjQUc "https://hackmd.io/@CheaterCodes/SyEtwjQUc")

nngdu: Tt sounds nice to me.

nncheat: ??? Yes, so if aone is itrs_ in what's hppn- w CHASM, the next mtg is skdl_. The planned date is 16 May, XX UTC. So if you're itrs_ in what's hppn- w CHASM in dtl, feel freee to join us in the tlcn Discord and the dev chnl.

nngdu: So if aone's itrs_ in CHASM, pls go thr. The other teams are setting up their own mtgs, but once ths hppn we'll post more on tt. We hv one other big piece of news. Shld I tell them nncheat? Idth they're rdy for it.

nncheat: Idth we're rdy for it. 

nngdu: Mb leave it for next week. PRetty much since teh Discord comy started, ppl hvb ask- for forums for btr discussion and qns. We've done a lot of work on this, such as setup, moderation, as for the last qn, pretty much eone is fmlr w this, but hte Starchild sys offered to set up the hosting and do the forum for us. An offer we've gladly acpt_. So as of the last week, we've been play- ard and set- it up. So what I"m trying to say is, go ahead and play ard w it.

[https://forum.quiltmc.org/](https://forum.quiltmc.org/ "https://forum.quiltmc.org/")

[Announcing the Quilt Forum | The Quilt Project](https://quiltmc.org/blog/2022/05/07/announcing-quilt-forum/ "https://quiltmc.org/blog/2022/05/07/announcing-quilt-forum/")

nngdu: Discord th is not ez to host on a cloud platform. But it's gerat, it's work- rly well. Thr's news and annc] thr, you c post your projs thr. Go wild. And it'll folw the same rules as ewhr else, but you shld be fmlr w them, so folw them and it'll be fine.

Deftu#0001 (432291917645086720)
Will Quilt support classpath loading of mods? For example, if I want to add a mod to the classpath without loading it conventionally (such as how the Essential mod works)

nnax: Yes, qload does scan the classpath for mods, so yes, it j works.

darkerbit#0143 (560515299388948500)
Which intermediaries does QM use right now?

QM uses pghs but chgs to pgim.

nngdu: Ty for tt. I blv the next one is nnaurora's qn.

Deftu#0001 (432291917645086720)

Will Quilt have permissions in the way Android does? So a mod would require a certain permission to perform an action with files, etc

nnaurora: One th tt I og[[ did agn. So thr's 2 kinds of perms, so thr's server perms, but tt's not lk Android. Server perms is sth tt we'll hv, it's v impt for server moderation. But client perms... it's not a sandbox env. If we do tt, we'd hv to sandbox eth which isn't feasible.

nncheat: I thk j to clarify a bit on tt, it's also rly hard to do ths lk tt in Java. Thr's sth for tt, but it's deprecated and currentlty not being replaced.

nnaurora: Yeah, it's rly difficult in Java. If you wanted to do sth, it reqrs ea mod tb sandbox=ed so tt it c use the file sys while access- our file sys. I'm not rly sure if it's worth it, bcz in the ?? of mod-, it's based on trust. It's just the game is lk tt. But I thk thr's more impt ths to add into now.

Deftu#0001 (432291917645086720)

Will Quilt have built-in telemetry? Such as ways to track it's own user counts, exclusive users, etc

nnaurora: I thk I'm pretty confident to say tt we won't hv ath lk tt. First off, we hv a lot of users who wld be against it. If you look at the modloaders, thr was a lot of debacle tt j was not rly use it. Fabric doesn't use it, Idk the state of Forge. The only th I know tt colk stats is Bukkit plugins, and thr's a lot of ppl who don't apc8 it, so I'm confident to say tt Quilt won't hv built=in telemetry.

Deftu — Today at 12:35 AM
Forge does do it

nngdu: I hv to agree w tt. I'm sure some 3rd=party might come up w sth, but we won't.

nncheat: Also, nngdu set up the stats on Discord.

Lapis Liozuli#2082 (150878072818761728)
If thr will be separate dev meetings in future, are there any plans to scale up the recordings?

nngdu: Now we do hv Craig on both servers, so they shld be able to use Craig if they wanted to. I doubt tt nnsouth as our only editor wld be able to edit these recordings, so I thk it's gg tb left down to indiv teams. But if they nd help we'll be happy to help them as well.

Lapis Liozuli#2082 (150878072818761728)
Great to hear that BiomeModifications API is getting ready. Could I ask what was the main challenge in converting to 1.18?

Well, it was alr converted, but we h a prbm whr the End didn't rly exist. Now we know the test mod exists and we're j wait- on Beta tb merged.

flogic#0001 (168789991189774337)
Are there any plans for QSL modules for purely server side modding? Or is that out of scope of the project?

nnaurora: Thr are some perm API on the side, which isn't useful for the client. The exception is in a single=player world. But for the server=side mod-. Ik tt Patbox wants to write some stuff in the regy module to supt server=side modded items and blocks. So it doesn't try to regy sync server=side reg entries. I'm sure there will be other Server=side APIs, I can't rmb what. But it's not outside the scope of the proj.

Patbox — Today at 12:39 AM
Virtual Networking Stages is planned by me



Deftu#0001 (432291917645086720)
If issues were to occur or there was enough of an outcry for support with something, would an in-house fix be implemented? Like how Forge supports/supported(?) OptiFine

nnaurora: It's j not critical for lk, hv to thk, I don't rly hv an eg rn but I c mb thk of velocity being a bit dffr[, but it's not rly sth tt you c do abt it. It's rly a dfcl qn actl[. It dpd on what you hv to supt actl[. J to supt one edge case, j to do one th, it most lkly won't be supt. O/w if it's sth tt... It's rly case by case.

Lapis Liozuli#2082 (150878072818761728)
I think to clarify on the BiomeModifications question, I was curious how come it took so long to update it since 1.18 was first released. Like I think Fabric also struggled with it for a while.

Deftu#0001 (432291917645086720)
Will QSL be fully thread-safe, or will extra effort have to be put in by the developer using it to ensure that they're using whatever it is they're using on the main thread?

nncheat: I thk in gnrl it's the dev's job. So ppl are lk= No one's entirely sure in the inrl chat, not even in the qsl team, but the way I see it is, you're using 2 APIs when mod- MC. First is MC, next is qsl. And MC is not safe. You c add checks, but I thk it's dngr[ to asum tt MC is fully thread=safe. J double=check the APIs. And again, QSL is not the only API whr you wld use it.

nnaurora: qsl is a set of APIs, it's not a uniq one. Some APIs might contain safe fetrs, but it's not a guarantee. It wld say within the Javadocs. We can't mk a guarantee fo the whole of qsl.

nnem: Ig the elevator music PR is coming in. Wld tt be nnaurora's one agn?

nncheat: It shows how popr qsl is.

nngdu: Hmm, what a great t for a phone call.

nncheat: Yk I was thk- at teh start whr we were thk- of play- elevator music, but it wld be kinda cool to showcase some stuff. So lk show some art, showcase some mods, j to pass the t.

Blodhgarm#6853 (380859072729317377)
Stupid Quetion Here(Sorry): How easy is it to get a Fabric mod working with Quilt and how much time would such take?

nnem: As sbdy who's ported mtpl of my mods fr Fabric to Quilt, it's rly not much work. Most of hte stuff h roughly eqvt stuff. If you don't want ot port it, j using it directly is mostly fine. Thr's a pinned msg on the comy server, and rn we have less than a dozen mods tt work on Fabric but don't work on Quilt. ... if you don't want to .

flogic#0001 (168789991189774337)
With the OpenCollective, is Quilt looking or open to sponsors from large servers / companies? 

nngdu: Usually we hv an Admin to ans this qn, soo... We are work- w a couple of grps. We hv one from 1Password which we use for storing our credentials. We hv one from the Starchild sys, they're the one host- the sys. Pretty much eth comes out of nnhav's pocket and a small amt from mine as well. We wld prefer sponsorships tt are monetary bcz ctrl- the infra is impt to us. If you wanna bring it up to an admin, I'm sure any of hte 3 wld talk to you abt it.

Deftu#0001 (432291917645086720)
Will there by additional APIs in QSL which will make creating multi-version mods easier? Such as what Architectury does with it's API

nnaurora: It's slightly dfcl to ans bcz thr's a lot of uncertainty curr[. The main th is first of all, once we got CHASM and we start use- uniq fetrs from it, thr's a psbl] tt some APIs won't be tt useful in tt case. Bcz is not all trhe modloaders don't spot the same injk]s, issues will hppn. And the other th is tt a lot of APIs are made w the Quilt philosophy. It ... v dffr[ from the Forge philosophy. And what tt means is tt multi=loader or multi=vrsn stuff is v dfcl. For the loader, we prvd stable APIs, but not too stable. So what hppns is tt for each version, we break ths if and only if it'll mk ths bttr, bcz in the last iteration we missed some stuff. ... So it will rly dpd. If MC doesn't chg much, and if the API doesn't nd to evolve, then it'll hv some stability guarantees. O/w for multi=loader stuff, it rly dpd. But other APIs won't be usable on other loaders. Thr might be some, but thr's abs[ no guarantees on tt. They're not rly in a state whr we can ans more on this. It's sth we'll hv to see w time.

nngdu: Fab, thx for tt. Actl[ we're get- pretty close to the end, so I'm gg to finish the AmA to mk sure we hv t.

Deftu:

nngdu: This is a bit of a broad qn IMO. On the one hand we do work w some groups on the issue of moderation specifically. Lk we work with Forge moderation team. On the other hand ... Github... We hope to avd favouritism. It's ustd[ gg tb dfcl to blnc tt w the nd for a larger dev group. As long as it doesn't hppn to hte detriment of the ... 

Southpaw — Today at 12:56 AM
Everyone should get good treatment, not only big developers, is the point

We are still gg to work w big devs, but eone shld get equal treatment ideally.

Alrt, thx eone for coming.

And if you hv any fdbk on the forum or for ath else tt has hppn_, feel free to let us know.

nnem, nncheat: See ya.
