Gdude: Hello and welcome to the QuiltMC Developers’ Meeting Podcast. The podcast that eh, isn’t really a podcast. If you’re new here, this is just a collection of recordings of each publicly recorded Developers’ Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed on a Mumble server and recorded live. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to QuiltMC.org.

Peter: Hey, it works. Finally. It only took a few minutes, but at least it gave everybody enough time to join. OK, well, welcome to our fortnightly Developers’ Meeting as Gdude likes to call it. Please a round of applause for Gdude in chat, who’s not here but still fixed our issues. Thank you.

Glitch: I can’t clap and hold the push-to-talk button thing.

Peter: So yeah, I’m going to be the stand-in tonight. I have help from other people, so if I mess up, I think people will let me know. But anyway, let’s get this thing started right away. Glitch, are you back yet?

Glitch: Yes.

Peter: So let’s start with Build Tools first, and Glitch will give us a quick update about it.

Glitch: Alright, for Build Tools, we’re working on fandangling Loom into understanding that files with quilt.mod.json files are actually mods and understanding how to read those. And once we have that done, either by getting that in upstream, or just forking Fabric Loom, we’ll be able to use Quilt Loader to make mods, essentially.

It’s not ideal, we’d rather not rely on Fabric Loom, because it’s big and complex and hard to change. We’d rather be using vanilla Gradle, but it’s just not there for the timeline we want to be able to make mods with Quilt Loader as soon as possible. Yes, and as Leo said, Loom is kind of a mess because it’s many years old and very, very big.

Peter: Alright, thank you for that. I'm going to intro a <mark>new ah</mark> this meeting. <mark>XXX </mark>asked, "For build tools, how ready are we for Quilt Beta?"

Glitch: Assuming what I mentioned gets merged or we just fork Loom, that should be good enough for Beta. Obviously we won't be able to use Hashed Mojmap, but it's something.

Peter: And we still got over a month's time, so most likely we're right on track. Next team for the list, Team QASL. I'm going to have the honour to talk about it myself. Um, there's two things that have been happening recently. One is the test of the Gradle plugin, which got a new revision at a new home on a new repository. And it's a lot cleaner now, it's actually less code. I think it works quite well, and the integration is as good as you can expect, as it should be expected to be.

Uh, it could be better, but <mark>again in a lot of text</mark> but they show up as the actual dependencies like actual Gradle Maven coordinates and Dependency View in IntelliJ for example. But honestly, that's low-priority and I'd rather have it working cleanly and having better maintainability.

Then the second thing <mark>that's been talked</mark>, the discussion again around <mark>QASL Line</mark>, because again two things here. First, I asked Crop to be so nice and try out a bit, and seems like Crop had a lot of fun with it. Um, except that he was complaining about a lot of missing functionalities so there's a PR that's adding a lot of missing operators to the current language implementation. However, I myself am currently looking at changing the language implementation over to use maybe Java CC instead of <mark>Antler</mark>. It's not a <mark>completely solved problem </mark>yet, but Java CC has some nice things that Antler doesn't, and *vice versa*, but mostly I like Java CC because it doesn’t have <mark>front-end pathing, so makes it easier to package in the cascade and plugins</mark>.

Those are the things that are happening right now, it’s moving. I’m about to lead myself into my own extension: How ready are we for Quilt Beta? Well, first off, QASL is not explicitly planned for Quilt Beta. There might be something, like I'm hoping and I'm planning access file implementation. And that’s pretty much it. I think it’s not realistic to have it ready for Quilt Beta, it’s too much work. Access files, maybe. Interface interactions as well, because that's quite simple. So are we ready for Quilt Beta? Yes, but also we don’t really have a project that's going to be in Beta just like the <mark>other focuses</mark>. Alright, I've talked myself dry, so let's move onto the next team: Community Tooling.

B: Ain’t got nothing to do.

Peter: Ain’t got nothing to do. Uh, it’s fine. It’s not really something that has anything that needs to be done for Quilt Beta. Decompilers are another thing. <mark>Just frequent grabs. Also, there’s no hard data</mark> on what it needs for Quilt Beta, it’s working great already. Same goes with Infrastructure, which we can skip today, Haven isn’t here. It’s working just fine right now. So finally, I’ll let somebody else talk. Glitch, can you give an update on the Loader?

Glitch: OK, hello again. So not much has happened in Loader for the last two weeks. The big thing that is something that I'm actually working on today. I want to get our installer for Quilt Loader running, which would mean that you'd actually be able to use Quilt Loader thru the Minecraft launcher. Um, we had something written by i5 mth ago, for which I’m going to have to learn the code structure.

Peter: *Typing sounds*

C: Peter, mute yourself.

Peter: Wait, I’m not muted.

C: No, you’re not.

Glitch: No, you just typed over my whole little speech there. Uh, to summarise, I’m re-learning i5’s Quilt Installer stuff and I’m changing it to work with how Quilt Loader has changed over t. And hopeful[ within the nxt few days you shld be able to use Qloader in the official MC launcher. And that shld be all.

Peter: Well, thank you. It will address first, it appr that for typing I’m using the wrong mike, but I’m not gonna change it now bcz it’s gg to mess up stuff. So Loader, the same qn: Are we rdy for Qbeta?

Glitch: Oh, sorry, I thought I was done. I wld say, sure once we have that installer run- agn, tt’s the major thing we nd to be able to use loader in pdtn, or else it’s not any gd. But for Loader itself, it’s run- fine, so I thk we’re gd.

Peter: TYVM. Next up, Team Mappings. Oro has sth to say abt tt, I thk.

Oro: Uh, yeah, so in the last 2 wk, 1.18.2 was rls_, and so we had to push for a bunch of mappings for that. And right now we hv a lot of PRs open, I can’t rmb how many exactly. But we’ve been merging PRs lk crazy. Uh, j give me 1 s. Yeah, we’re on Build 17 for 1.18.2. Tt means tt thr have been a lot of PRs merged for 1.18.2, which is great bcz a lot of mappings were being felt out, and tt Quilt Mappings is bcm- closer to tt 100% mark we’re looking for. Sth else tt j came up j ytd was tt Marktrix updated Enigma so tt syn classes and mthd and flds and stuff lk tt weren’t included in the % tt Enigma reports for how much of the mappings you’ve completed. So we have btr rep] of how close we are to cplt- all the mappings, which is v nice. Other than tt, I don’t thk thr’s rly much else to say about where Mappings is right now.

D: I’d lk to add sth. We have a lot more triage mmbr now, but we are still look- for more. So if you want to be a Mappings Triage mmbr, then go ahd to the #mappings-general chnl.

Oro: If you want to be in Mappings Triage, feel free to ping me as many t as you want. I will see tt and help you, hehe.

Peter: Yeah, TY for the updates. Yes, the pt of Triage, I thk it’s to have a v big team. So of course more ppl will help. Oro, so what abt Qbeta?

Oro: I thk, we’re definitely gd to go RN w Qmappings on Loom. The only- Thr’s a couple of PRs we’re work- on w tt, esp to add stuff like OnPick supt & more. Thk thr were a couple of issues tt we encountered tt were int to Loom and wldn’t be ez to fix. And so those wld have to be fixed b4 we wld be able to fully update. I can’t rmb exactly what it was, but thr was sth there. But we shld definitely be rdy by Beta, esp if we mk our own fork of Floom.

Peter: Fabric fork you mean ‘Floom’, right?

Oro: Loom.

Peter: Yeah, OK, j for clarify]. Yes, agn. Are we on track with the big proj? Talking abt great big proj, the last one, probably the biggest of them all- Aurora, do you want to talk to us about updates, the current state of QSL?

Aurora: Yes, so QSL got a lot of dev] recently, so we got duper requests, we got the rendering module. The requests, it seems rough but it’s there. We got API progress as current API progress, it progresses to make right to Qloader. Basically, for Qbeta, Quilt’s own lib will not work on Fabric any more, since about January. So this also means that any of the mods that were using QSL in Fabric will break. So they will have to be recompiled for proper Quilt supt. The QSL they use will be unsupt_.

And for Qbeta, we still don’t have a registry sink, so for now we think that we’ll use the Fabric one. We will work on a QSL version. Today I made progress to get us closer to our resource pack API in QSL. It only allows to use the new resource pack profiles. Resource pack profiles is the little item, you see in the resource bar in the selection screen. That’s that. But it’s already a nice step. We also made a condition of like the global pack directory a bit simpler, since it uses tt sys.

O/w, we do nd rvw on the QSAPS so tt we know we don’t mk a big mistake, and that eth actually works respective to the use cases. If someone looks for sth in QSL, we c look into the issues, since thr are issues abt what cld be done in QSL, so you can look into it. Maybe take one, maybe contact us too, to discuss a bit abt how to impl stuff extra that can be done thru Github Issues, or thru Discord. So I thk tt’s all I have to say.

Peter: TY Aurora. You alr mentioned Qbeta here, but maybe I can j ask agn v qk[, what’s missing?

Aurora: What’s missing RN, is QSL link to Qloader. Tt will hppn v soon. Currently thr’s some stuff to deal w, but tt shld be dealt w rather qk[. It’s not a specific req] but we still j thk it wld be rly nice. But until that is done, we can j use the Fabric one. Tt’s the two big things tt we needed for Qbeta. One of which doesn’t hav a hard req]. Basically, QSL is v close to being rdy for Beta.

Peter: Great to hear. Thank you all, though we have a limited amt of time, but we sth, I think we can make it, of course. So tt was all the test team. Right, Leo wanted sth.

Aurora: I totally didn’t see the poll. Which point Leo? So in reading chat, there is a link to a poll for the names for one of the modules, so you can look into it and vote.
Peter: It’s about Maven, yes? OK, If you’re interested in that, check out the poll. I see thr’s alr quite a few ppl voting. And it seems lk it might be an ez win for one of the options, but we’ll see how it turns out. OK, TY. So that was all the teams which leaves us with ??? teams. That is, the Comy Teams and Outreach Teams have terrible teams built all things together. So plz.

E: Right, so Outreach Team has had perhaps the most pdtv 2 wk in its hist, prob bcz we didn’t exist 2 wk ago. The pull request work got merged on March 1st w fn- mmbr. Southpaw is the lead of it. And during tt t, we hv done 3 main things. We revived the Twitter, we are work- on new blog posts, and we are work- on getting an official build forum. So tt’s all pretty exciting stuff, at least I wld say. We’re also look- for someone who c help manage the Github dev boards for lk todolists and stuff lk tt. So if you’re interested in help- w stuff like tt on the Outreach Team, plz send a msg to Motville. I don’t thk there’s rly tt much other stuff that’s been gg on w Comy Team. But we’ve been doing a lot w the forums, and I’m personally most exct_ for tt. Tho apparently the forum is j Comy Team in gnrl, not Outreach specifically, but same th.

Peter: Well, TY to the Comy Team. Yes, as Comy mentioned, Outreach is a sub-team of Comy now, which is dfrt to what it was OG[. I also got that a lil bit wrong. Comy has alw been really clogged, been very active. So yes, they nd more ppl. Plz help our Comy to be btr than ever before, even tho it’s alr been great.

E: Yes, and send msg to Modmail plz, if you’re interested in help-.

Peter: Alright, tt brings us to the end of the general dev mtg. So for the rest of our t, we’re gg to do the AmA, which has alr started. So feel free to use the /ask command in the mtg chat. Tt will put the qn in a queue, where we will look at them one-by-one, and your qn will be seen by the aprv_ mods and then ans_ by devs. And we usually don’t skip qn, so you will be heard, and you will be ans_. So, who goes first?

Glitch: I say we start from the top. The new questions.

Peter: That is a great idea. So maybe Aurora can take the first one? If you’re still here?

Glitch: If Aurora is not here, I can take it.

Peter: Go ahead, plz.

Glitch: Alr, so QSL is definitely not j a more callbacks thing.

Aurora: Wait wait wait wait wait wait wait, you nd to read out the qn.

Glitch: Sry, do you want to tk this since you’re here Aurora?

Aurora: I can.

Glitch: Yes plz.

Aurora: So, what is plans for QSL other than more callbacks? First of all, QSL is not j callbacks. For eg, the QSL Base module includes entrypoints, which is a bit more. But it also cntn the event infra, and a launch arg which cb used for auto-testing a server. What is does, is when a server is launched, it would only be work- for a set number of ticks. When it makes things loaded, it will shut down. So tt’s an eg. Thr’s other stuff lk registry sync. It’s not rly callbacks, but what it does is it will sync the registries of the client with the server during shutdown. For eg, if the client has more mods, if the mods are not loaded in the same order, in the event in the same registry with the same raw identifiers. And the raw identifiers is not a string identifier, it’s a number. If that doesn’t match, it will witness a lot of corruption on the client, bcz the client won’t rcg the proper items and blocks.

Other stuff lk blk xtd], it’s not j callbacks. It takes blk settings, which is a class used to set some basic settings and ppty of the blk. What it does, it xtd tt to be able to do more. Or you have the Quilt ItemGroups, which is kind of a port of the Fabric ones. That is a bit dfrt. What it does is, if a mod needs a new ItemGroup, it will be add_ proper[, there will be a punctuation sys. If you tk for eg, the case of Quilt Tags, you can have Tags tt are loaded entirely from the client. All Tags tt use the client resources as a fallback if the server doesn’t have the Tag. So thr’s a lil bit more than j callbacks.

Thr will be sth, I’m not entirely sure when it will be made, but was talk about flags being incl_ in QSL in some way, which is kinda an eqvt/replacement to Fabric Wanderer API. And tt thing is not j callbacks too. Flags come w a lot more features than Fabric Wanderer API. But to list out every new feature, tt wld be a bit hard, bcz we don’t know every new feature yet. But we will try to add stuff as nd_, so if someone rly nd use case for sth, we can look into it. And if it can really benefit the comy, it might be added. That’s it for now.

Peter: Thanks. I think that was an very xtd[ ans tt probably ans_ all qn tt were still linger- abt the public. Of course, plans can change. Next qn, I’ll just go and read it out so tt the spkr don’t forget. Qn by RTTB: Will Quilt have direct install] into MultiMC lk Fabric and Forge or wld it have to resort to live graphic install] and stuff?

Glitch: So, I’m not rly sure if MultiMC has express_ interest. I’ll say tt any launcher tt is interested in supt- Quilt Loader, we’ll help them w ath they nd to supt it. I know we have heard from, I blv, CurseForge, ATLauncher and MC tt they’re interested, but I haven’t heard ath MultiMC-wise yet. I hope tt ans the qn.

C: Heebee j said tt he’s gg to impl it in the mtg chat.

Peter: The next qn is, again from RTTB: Will QASM recreate the features that are from Fabric ASM, and other non-vanilla Fabric mods like mixin, bytecode editing tools?
Well first off, I’m curious, what are vanilla Fabric mods? Like what’s, IDK, vanilla tools? In gnrl, thr’s a bit of a misconception ard what QASM is. Many ppl view QASM as lk a mixin-replacement, but it is absolutely not what QASM is. QASM is an abstract layer on top of ASM, like an object on ASM. It’s just an abstraction to allow multiple ppl to use ASM at the same t w/o conflict-. Tt means tt QASM itself is not gg to supt mixin or ath lk tt, but they’re all [ gg to use QASM to impl sth.

So the ans to your qn is, QASM won’t do ath lk tt, but thr will be first- and third-parties who use QASM to enable tt sort of stuff. For eg, axis-slide rotations cannot be mntn_ by Quilt, kisinisquiting will not be mntn_ by Quilt, interface injections prob not gonna exist, bcz mixin w QASM works a lil dfrt[ than on Fabric. But if thr’s ath else, it’s fairly ez for a third-party to provide the tools w/o req- changes or dirty hacks into the toolchain, which is one of the reasons why doing ath on Loom is rly hard. Bcz you nd to hardcode every single stage and tform] inside of Loom. Whereas w QASM, you just state it. It’s like adding a new datapack, you can’t just add a new bombthat. Sth lk tt.

Peter: Alr, I thk the next qn is a bit of a gnrl one. It doesn’t j trgt_ one team, so I’ll j start and if aone else has to add sth to it. Southpaw asked, What promised features were missing from the tooling at the beta rls? So j for clarify], this is ask- abt features tt were promised to exist in Quilt, but migh be missing fr the beta rls. Promised in full rls but not present in beta. For eg, QASMixin - mixins on top of QASM, is not gg to be in the beta, thr’s no way. QASMixin gnrl, is not gg to cease to be in the beta, we’ll see about tt. Tools, is prob gg to be some form of fork of Loom.

Oro: Yes, build tools, we will be using a cplt[ dfrt proj for our build tooling betw beta rls and full rls, hopeful[. We’re using Floom RN, but we wld lk to use vanilla Gradle eventually.

Peter: It also means the default, we’re not sure whether the default decompiler will be set to QuiltFlower, or the hash probl won’t mk it into beta.

Glitch: Almost defeinitely not.

Peter: Yes, the final rls ???. Mappings, might still req the Quilt mappings on Loom rather than prvd- first-party direct supt. All those subtle small things are gg to be missing. But I think in terms of content as well, mappings, since some of the mappings are still in tooling. And pages are still not certain, also probl not gg to mk it into beta. prob want to have vers-indep mappings, also not gg to mk it into beta. So there’s a lot of- all those small things.

Glitch: To add on for loader, the Loader is promising loader plugins which are essentially ways to add more fn] to the loader. For eg being able to load Forge mods, Sponge plugins, etc. Tt prob will not be in a mth fr now. Alex isn’t here to confirm tt, but I’m pretty sure. And on the same token, we’ve talk_ abt auto dep downloading, which wld essentially mean for certain deps, like QSL, instead of jar-in-jarring them, Loader wld auto[ find the dep you nd and DL it fr a Maven. Which is definiely not thr yet, bcz Loader plugins have to exist for tt to hppn.

Peter: Ath else? I thk I’ll close out this one in particular by saying tt we’re waiting for full rls as gnrl lib tt might be add_ later.

Glitch: Gnrl[ we love it to be bigger and cover new things tt aren’t in FAPI and also eventually mk it so you can do alm eth FAPI does. It’s not the goal RN, but eventually, we would like essentially to req modders to not use FAPI in add] to QSL.

Peter: I hope Southpaw, it’s enough fuel for the blockart there. Feel free to ping us abt ath. You know whr we are, whr you can find us. Alr, Oro, you still here?

Oro: Yes, I can tk this qn.

Peter: Alr, the qn is, I won’t fool ard. IDK.

Oro: Alr, the qn. Will we ever be able to use Qmappings w/o the ugly-looking layered mappings things? In Loom, I’m going to say no. Techn[ thr’s a small chance you cld do it w/o the ugly-looking layered mappings thing, however I’m gg to kp it as layered mapings. One, tt’s the style tt Loom wants ppl to use. And two, I’m also add- other things like Parchment and Mojmap if ppl want those, so tt I’m not force- it, so tt it’s one way. Once we have our build tools version, it shld be fairly ez to add Qmappings w/o the layered mapings things, and w vanilla Gradle, I definitely know tt Glitch has put in a lot of work to mk the mappings sys v xtd[ and so Qmappings tgt w any add] we add will be v ez to use thr.

Peter: Alr, TY. Look, the qn’s coming, bcz RN we only have one more in our quue.

Glitch: I think this one is for me.

Peter: Go ahead.

Glitch: RTTB asks, Ath tt Quilt has done to mk it possible for Forge mods to be loaded? The ans is, you’re ask- for the wrong object. (Did I add an extra T? Oh well.) I also worked in the past on Patchwork, which was making Forge mods load on Fabric. Tt will be run- on Quilt, but tt will not be sth first-party w Quilt. We won’t ever supt load- other modloaders besides Fabric/Quilt officially.

Peter: Yes, now it’s here in, Fabric is sth tt exists as long as we kind of impl. Bcz it wld be q hard eventually to supt it. Most lkly it wld be an incredible burden to supt Forge. But for a start, for Forge it’s j not feasible. The design is too dfrt for us to supt.

Alr, any more qn? We got t. We’re run- dry here. O/w, in the meantime, while we give you a few more min to ans, I’ll do a gnrl call to chk out PRs to rvw. QSL has a separate chnl now for PRs tt nd rvw-. But mappings alw are PRs tt are great to fill up w them. And if you wld lk to contrib to any other proj, or even this proj as well, j pop into our toolchain Discord. You’re alr here, look into the corresp chnl, j leave a msg thr. If you’re brave, you can ping Cmos or a person you know. But it’s enuf to j drop a msg in thr and we’ll see it and then we can talk about how you can help w the proj.

Glitch: J to jump in- we’re not scary. We wld love ppl to come contrib. We have plenty to do. So you don’t nd to tk any kind of commit] to try and rvw a PR, or make some mappings, or write even an entirely new module for QSL. So if you’re interested, plz j hop on Discord and ask us abt it.

Peter: Alr, well, I thik there’s no new qn. I thk thr’s also no rmn- ans tt we have. Yep. So I guess it’s time to end this. Last min. Last second qn, I thik this one is for Glich again.

Glich: OK, Aqua asks, will Quilt’s mappings allow for layered mappigns as well? Uh, yes, vanilla Gradle will supt layered mappings. I spent a lot of work trying to figure out the best way to supt tt, so it is definitely a prio to me for tt to be work- well.

Peter: TY. Yes, sth I think tt’s kinda work- alr.

Glitch: V kinda. The whole packet needs to be rewritten for lk teh 4th time.

Peter: Yes, thr’s a lot of stuff about vanilla Gradle tt’s also not ideal for maps specifically and for remapping input mods, tt’s j how the sys is. So the futur of vanilla Gradle is still a lil bit uncertain RN. It’s a lot of work tto do a big proj lk tt. And also some of the tenets will be used by other proj. But we’ll have to see how it goes.

OK, so RTTTTT3 w another last-min qn, asking, What code from Fabric still exists on Quilt? I thk tt agn is still a bit of a proj qn. Look- at it real quick, RN it’s Loom tt’s prob gonna change, hope[[ gonna change with the full rls.

Glitch: Qloader is a fork of Floader.

Peter: Yes, it’s a fork with parts cplt[ swapped out, other parts basically cplt[ intact.
Aurora: For QSL, you can see which stuff is Fabric. Go into the header. For each file thr’s a nice big header. If it’s Fabric, it will cntn a line abt the OG ownership of Fabric for the code.

Peter: Does QSL use Fabric code specifically in FAPI in QSL ??? ?

Aurora: In FAPI-QSL compat, it’s a fork of FAPI, which re-impl some stuff using QSL instead. So yeah, of course it’s using Fabric code.

Peter: On mappings, it’s mostly tiny stuff which we talked abt last mtg, which we’re planning to hope[[ yeet at some point. Alr so, I’m gg to end this here now. So any last-min qn coming in will not be taken in now. I TY all for join- and listen- in and for the t to talk and for the comy team to be ard and mng stuff for us. And alw, or most of the t, I’m gg to invite you all to a quick after-party on the dev chnl on the toolchain Discord. We c j hang out a bit and chat a bit more, also about unrelated stuff as well. And I hope the new t is also sth gd for eone. So we’re gg to meet nxt week, same place, same t. TYVM.

Glitch: Bye eone.

Aurora: BB.

Peter: Why was I using the wrong mike? Now this is the correct mike.

Glitch: Sounds so much better.