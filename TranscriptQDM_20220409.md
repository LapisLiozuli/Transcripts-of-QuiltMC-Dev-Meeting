[09/04/2022: My Welsh Isn't Great](https://anchor.fm/quiltmc-dev-meetings/episodes/09042022-My-Welsh-Isnt-Great-e1h6336)  
In this episode, the team discuss QSL, Mappings, Build Tools CHASM, and Loader, as well as Kotlin support for Quilt, and how to write issues that attract contributors.  
[https://quiltmc.org](https://quiltmc.org/)  
[QuiltMC on GitHub](https://github.com/QuiltMC)  
[Quilt Community Discord](https://discord.quiltmc.org/)  
[Quilt Toolchain Discord](https://discord.quiltmc.org/toolchain)  
[Quilt Openings](https://quiltmc.org/openings)  
[Quilt Standard Libraries on GitHub](https://github.com/QuiltMC/quilt-standard-libraries)  
[QSL PR #91: Dimension API](https://github.com/QuiltMC/quilt-standard-libraries/pull/91)  
[QSL PR #67: Server-side Argument Types](https://github.com/QuiltMC/quilt-standard-libraries/pull/68)  
[QSL PR #76: Migrate to Quilt Loader](https://github.com/QuiltMC/quilt-standard-libraries/pull/78)  
[Fabric API over QSL on GitHub](https://github.com/QuiltMC/fabric-api-qsl)  
[Quilt Mappings on GitHub](https://github.com/QuiltMC/quilt-mappings)  
[Hashed Mojmap Mappings Hasher on GitHub](https://github.com/QuiltMC/mappings-hasher)  
[Quilt Mappings Naming Conventions](https://github.com/QuiltMC/quilt-mappings/blob/22w15a/CONVENTIONS.md)  
[Quilt Mappings on Loom](https://github.com/QuiltMC/quilt-mappings-on-loom)  
[Quilt Loom on GitHub](https://github.com/QuiltMC/quilt-loom)  
[Chasm on GitHub](https://github.com/QuiltMC/chasm)  
[Chasm PR #42: Language Rework](https://github.com/QuiltMC/chasm/pull/42)  
[Chasm: Good First Issues](https://github.com/QuiltMC/chasm/labels/good%20first%20issue)  
[Chasm Issue #43: Instrinsic Functions](https://github.com/QuiltMC/chasm/issues/43)  
[Chasm Issue #45: Better Error Messages](https://github.com/QuiltMC/chasm/issues/45)  
[Chasm Issue #39: Language Specification](https://github.com/QuiltMC/chasm/issues/39)  
[Quilt’s (new and improved) Maven Repository](https://maven.quiltmc.org/)  
[Quilt Loader on GitHub](https://github.com/QuiltMC/quilt-loader)  
[Glitch’s Loader Issue](https://github.com/QuiltMC/quilt-loader/issues/59)

**Gdude**: Hello everyone that's just responding to the ping in an annoyed way. How're you doing, everyone. It's that time once again, and I'm actually doing something good for a change, look at me. Obviously, if you're sitting on Mumble, you'll want to be deafened on either one of them. Looking at the list, I'm like, "Hmmm, there's a few duplicates there." 

So, we're going to give like 5 minutes maybe, to let people show up. Feel free to chat away in the #meeting-chat channel just above the #stage channel. Certainty seing a few new faces this time. If you're new to the mtgs, welcome. Also, you're slightly late, but that's OK. Also, can someone confirm that I unlocked ~~Warp~~? The permissions look right, but nobody's chatting. Fabulous, thank you. What was that spooky voice I heard over the ether just there? Alright, nice, looks good to me.

As always, we open the AmA at the start and close it at the end. So if you want to ask any questions, you can use the /ama command on Discord, and they will queue up for us to answer later on. We also have a bit of an ordering difference later today, but I'll go into that in a little bit. Not a big deal, though. Here's the secret, **Glitch**: It's alphabetical. Well, mostly alphabetical. I mean, we do take a few liberties, but it's ok, we just re-define the alphabet instead. Hoisting, huh?

**CheaterCodes**: Oh yeah, "hoisting" is a great name. Exclamation mark CHASM is great. I guess triple or quadruple exclamation marks, just to be sure.

**Gdude**: *(sighs)* I love it when the Mumble bot reconnects on its own though.

**Glitch**: I thought you just put us on mute for a bit, to be honest.

**Gdude**: No, it just reconnected on its own, I think.

**CheaterCodes**: The only voice we lose in the recording is the one on Discord, not on Mumble. So just don't say anything important when it disconnects.

**Gdude**: I mean, y'all are the important people in this meeting. You like hoisting, **Yujin**? That is understandable, your name does start with a 'Y', I know. We'll be geting started in just a minute. I do wonder how many people like join when the event starts because they're interested, or join to complain about me pinging them? I mean, that's reasonable too, I'm all about that.

Alrt, I think we can get started. It's about five past, six past even. The order's a little bit different, we're going to be going through QSL and mappings first because **LambdAurora**'s got to leave later, but I'm sure y'all won't mind that. So let's get started, I guess. **LambdAurora**, would you like to get started with QSL?

**LambdAurora**: Yeah. So this is the last meeting before Beta, which means we won't talk on the same things because we have more of a focus on the Beta part. So for QSL, we are a bit concerned because we have to specify a versioning scheme for QSL. Before anyone says, "Yes, but there's Semver," it's not entirely about Semver. It's mostly about how we version the QSL as a rule of which version, or which module extra. How we version everything depending on the MC version, and a lot more.

So that's a lot of stuff that for example Semver doesn't really answer by itself. So we have to sit down and think about it. It's taking a long while, which is a bit concerning. Since while Beta isn't really that far away, but we do hope that we figure out something that is solid enough for Beta. Because the idea is that it's all set up so that we don't have to touch it too much, and so we don't have a big disaster. Because while we can break APIs in Beta, breaking the version scheme is much, much more dangerous and not really worth it. So yeah, that's something we need to get right.

Inrl[ there's been some discussion about Semver, because Semver was ~~fought~~ for libraries, mainly, and it's a bit different from mods. Mods are quite a weird case. There's also the case of content stuff which is another can of worms. So there's been talks about breaking Semver in Quilt Loader. No one's sure yet, so don't make assumption right now. But yeah, that's what all the versioning stuff was about.

Otherwise, for QSL, feature-wise, we had some PRs that had been merged. I think last time, If i remember correctly, we got a port of Fabric's Dimension API, which is mostly a helper to teleport entities between dimensions. Because apparently that's not easy without APIs. 

We got server-side argument types, which is really, really nice for common modules, because that means you can have an argument type that directly maps to an event without having it to be present on the client. Because for those who don't know, argument types are a bit weird, because they're not just interpreted on the server, but they're also interpreted on the client. You can't really synchronise that, like you cannot really send stuff that the client doesn't know. Because, well, first of all, you can't just transfer code. And there's also the case of a ~~linear~~ client that cannot even load it ~~all the way~~. So the goal of server-side argument types is to match an argument type to another existing type when sent to a client that doesn't have like mods that register that argument type. But if the mod is present, and Quilt Networking and Quilt Command APIs are present, then it will be actually sent.

There was a much smaller PR that ~~quit registry~~. But to be honest, I personally had issues with some stuff, because Aurora's Decorations does some weird stuff with registry. It initialises a bit too early for some of FAPI. So those have been ~~constructions~~ that have been applied to QSL. So like, there's a BlockItemMap, dictionary, whatever you want to call it, in MC, and that one allows us to know which Block maps to which Item. So when you control-click for example on a Block, it'll give you the right Item. And it has other uses. 

The thing is, that map, when it's created, it's not filled automatically. So basically in vanilla, the only moment when it's actually filled is when the Item's class - Which is a class for when every Item in the game is initialised, which is not great for modding. So what Quilt Registry does is it registers something totally after that is initialised. Some modded stuff just works. And just for like- Just to know what make it different from Fabric API is that we register that listener a bit earlier. So we catch more stuff. 

O/w, other stuff is we caught some issues in the Registry Monitor, which is an API to monitor registries, which is really, really cool. So you can do stuff on already existing entries in the registry, but also what is registered after. It's really useful, and there's a new bug that got in, in 1.18.2. Because now we cannot register stuff while iterating over the entries, so we had to modify that. It led to also new method in the context of trying to register something safely. 

Otherwise, feature-wise, I think that's all. QSL is- at least, it's ready feature-wise, there's not a lot of stuff to figure out. And we're well aware that we do not cover like every case that Fabric API covers, which is fine because well, it's still very early. So it's OK because people can still use Fabric API for stuff that we don't cover. So on that part, we're ready.

**Gdude**: Also there's something about geting QSL on Quilt Loader.

**LambdAurora**: Yeah, currently QSL is not depending on Quilt Loader. It will come soon. Actually the final comment period for the PR has ended. But we're waiting a little bit more because we want to be sure. Because there's some stuff that came after that we need to figure out. But otherwise that PR might be merged very soon. 

Also, **Glitch**, just to make sure, there's a little bit more stuff that wasn't covered in that PR. It's the fact that there's the ModContainer class that is used in the API so far. And the issue is that it's using the Fabric Loader one, and what's intended is for the Quilt Loader one to be used. So it also means that once we go on Quilt there will be an API breakage. So every mod that is currently using QSL, if you touch the register, like the resource pack, or resource loader, if you use the Quilt entrypoints, it'll break. Because there's a famous ModContainer class there. If anyone wasn't aware, now you're aware, but yeah.

The last thing is, QSL and Fabric API. ~~High priority~~ that gives Fabric API API ~~surface~~, while ensuring that it works with QSL. Because of some mods that have been production-testing with that. There was an incompatibility that was discovered with Continuity. It was fixed, so that's really good. There's some bug reports that are a bit obscure. So currently we don't know if it's really because of QSL stuff, or if it's because of jar-in-jar issues. So some stuff we'll have to be ~~contacted~~ with the QSL-FAPI ~~future currently~~ in the mods folder. But hopefully that'll help us to fix some maybe unseen bugs before Beta, so that'll be really, really nice. But at the same time, Beta is a time where there still can be bugs. But it's still better if there's not many bugs. 

O/w, I think that's all, aside from the usual reminder that we're still looking for people. Especially for Fabric API-QSL, because currently I'm the only one maintaining it. Which is a bit, how to say, exhausting. So if people are interested in maintaining that library, that would be really, really cool. Someone showed up, which is really nice, but otherwise if we can get more people to make sure that it's maintained and doesn't get left behind from upstream that'll be really, really cool. Otherwise I think I said all the things that needed to be said. Think we can go over to the next project.

**Gdude**: Thanks for that. Yes, just a reminder, **LambdAurora** just mentioned it, but to reiterate: QSL needs more people, especially QSL-FAPI Module Team, since it's just **LambdAurora** maintaining it and that's kind of stressful guys. So if anyone has any interest in that, please do let us know. Are you OK to go over mappings as well now?

**LambdAurora**: Yep. So I have to be honest, I do not really follow much mappings currently because I had a lot of stuff. But as usual, when a snapshot comes, we update. We do have caught some references where Mojang renamed stuff without actually having something that breaks the API. That's a little bit worrying, because initially when we brought up Hashed Mojmap, we kind of said that it should not really be happening. But so far it seems to be really, really rare occurrences, so it still should be fine. But what we noticed is the current Matcher that we have - that is, as a fun fact, written in Javascript - is not strong enough and really needs to be rewritten. First of all, in Java, and secondly, to cover many more cases.

The thing that ~~doesn't mesh~~ is that Hashed Mojmap is much, much faster to generate than Intermediary. We're usually able to update Quilt Mappings faster. So that's a really nice achievement. Otherwise, for anyone contributing to Quilt Mappings, there has been cases where Mojmap leaked in Quilt Mappings. Some people said like that, it doesn't sound like a big deal, since we don't have a cleanroom policy. But when it becomes a big deal is when it brings names that breaks the conventions that were set for Quilt Mappings. 

So for anyone contributing, be mindful of that. Double-check when you use a Mojmap name that it doesn't break a convention. So like, if you try to path serialise to JSON, in that case there's a convention in Quilt Mappings about serialisation methods that says ~~you don't have to be specific. Like it's serialised, it just to JSON~~. Any of those occurrences will be fixed, eventually. But for anyone that is willing, or is currently contributing to Quilt Mappings, it's just a reminder. 

O/w, about the Beta, Quilt Mappings has been in co-production already for a month. But there is some important stuff to consider. For example, and for Quilt Beta it'll be really relevant, we're currently using Quilt Mappings on Loom, because we do not have Build Tools yet. There are some issues with it. For example, there are really, really random methods that refuse to get mapped. I know there was talks about fixing it. I'm not really much informed about it. It's one thing to consider, and the other thing to consider is between ~~Mojmap names and constructors~~. Not entirely sure why, but for now it doesn't. So that's also one consideration. But otherwise, aside from those issues, it's definitely usable, at least and especially for Quilt Beta. Thanks to everyone that has used Quilt Mappings already because either it helps us to figure out bugs. It helps sometimes for the names. It shows that we're not doing that project for nothing. So, thank you at least. Otherwise, as long as QSL is updated, there's not really much more to say about all of this.

**Gdude**: Alright, thanks for that **LambdAurora**. You had a bit of a marathon there, good job. Alright, we will move straight on since we're already halfway through. **Glitch**, can you talk about Build Tools?

**Glitch**: Alright. Is this thing working? Alright, so Build Tools, we have our own fork of Loom now. I believe I brought that up last time. I've just been working on fixing the inevitable bugs I've introduced and making sure that everything is good to go for it to be used with QSL and Quilt Loader. And really, that's about it.

**Gdude**: Alright, thanks for that. **CheaterCodes**, would you like to talk about CHASM?

**CheaterCodes**: I would love to talk with CHASM. CHASM has had some busy 2 weeks. Or to be precise, some busy 4 days at the start of 2 weeks. Basically I've been re-writing the entirety of CHASM Line simply because I wasn't happy with the implementation. It was a bit messy in spots, it was basically my first attempt. I wasn't entirely sure what I was doing. So I basically scrapped it all, did it again, took what I learned and now it's better. 

It is again, 90% the same, so I guess it wasn't that bad in the first place. But the worst parts that I didn't like about the implementation are much cleaner now, so that's mostly related to expression-caching, function call-caching and dealing with occurrences and such. It also changed a bit in terms of of syntax. Small changes that people wanted, like bing able to omit the dollar sign for specifying a rule if it's ~~simply~~ for the terms, method, or whatever. And easier indexing, and very important, also now has the capability of providing intrinsic fns. So very simple operations like geting the length of an array, relevant for geting the number of instructions in a method, or specifically targeting the last instruction needed to know the length of an instruction array. So that works now. 

Hwvr, there's still a lot of stuff to do. The base functionality is pretty decent. I'm happy with where it is right now. There's some details we have to figure out regarding representation of function descriptors and parameters and ~~method types~~, because that's redundant if we represent them all, but it's annoying if we don't have them all. 

But actually, if anyone is interested in helping out with CHASM, there's a few very great simple issues open at the CHASM repository. If anyone feels like helping, the intrinsic functions one is really simple and probably like 10 lines of code for most of the functions on there. Error messages is a bit more of a language-parsing one if anyone is interested in helping with that. I had someone who was interested in writing up the language specifications, they started but never finished. That would also be highly appreciated because right now I'm mostly working alone in this, which is quick, because most of the groundwork has already been laid so it's not that bad. But I'd also appreciate more help.

I think as always, talking about Quilt Beta, CHASM is not ready for Quilt Beta. It was never planned to be ready for Quilt Beta. In fact, it's in much further progress than we even anticipated a year ago. I do have a chunky access file now, a prototype lying around now that kind of works. But nothing production-ready. We'll have to see how to integrate it into Quilt Loader and stuff. I think that's all.

**Gdude**: Fabulous, thanks for that **CheaterCodes**. **Haven King**, would you like to talk on Infrastructure for a moment?

**Haven King**: Sure, can everyone hear me alright? Great, so yeah, as people who've been around for a little bit know, I've been working on my own alternative system for hosting Maven repositories that doesn't rely on ~~Seriotypes~~, Nexus, or I - forget what the other one is that is popularly used - So that's really close to bing able to be used. I got repository mirroring down so we can host the files from central or from Fabric's Maven, or our own Maven. 

And then, I think the only things that are left are I need to rebuild or rewrite the portion that generate the static website so that you can browse all the artifacts that are in the repository. And that shouldn't be too bad. And I have add handling for snapshot repositories, which is also like 3 lines of code. So it should be really close to bing able to be used soon. It won't be pretty, but it'll be functional and it'll be a lot cheaper than what we're currently using.

**Gdude**: That's an absolutely big plus too considering you've been paying for it all, I have to say.

**Glitch**: **Haven King**'s really been carrying us here.

**Gdude**: Yes, it's true. Is that it for Infrastructure? Fabulous, thanks for that. **Glitch**, I think I have you down for Quilt Loader.

**Glitch**: Yeah, that's correct. So Quilt Loader is kind of the same deal. We're really working hard on making sure that everything is going to be as smooth an experience as possible. So as we're coming up with bugs, we're trying to squash them. We do have some new features coming down the pipeline. Work on loader plugins is I believe slowly coming in from **AlexIIL**. So it's a ways away, but it's coming down the line. We're geting ready for being able to support Hashed Mojmap properly. We're adding some extensions to the quilt.mod.json so we can figure out what Intermediary mappings a mod is using so that we can remap them. And since I don't believe I have another good chance to speak today, I'll just throw in that we will be having a proper Quilt example mod coming up within the next few days, hopefully. So keep an eye out for that.

**Gdude**: That's exciting stuff. That is prety exciting, I have to say, I'm looking forward to that as well. OK, I think that concludes all the big teams. Specific stuff, as always, hit up that /ask if you have some questions. We got a couple in already. There's a couple other things to cover before we move onto those though. 

First one, obviously: Hey, Beta soon. This is the last public develop meeting before the public Beta on the 20th, as **LambdAurora** has mentioned. So yeah, we're looking forward to that. We hope you're looking forward to that. But if you have any questions you need answered before that happens, this is the time to put them through. 

Additionally, the Events Team has been working on BlanketCon. Now, I assume most of you have heard of what that is at this point, but if you haven't, BlanketCon is essentially an in-game modded convention. So it'll have booths and events and panels and all that sort of thing. Sort of in the legacy of BetterThanMinecon if anyone here is aware of what that was. It's bing run by the Events Team in collaborate with the Modfest Team. So of course **LemmaEOF** is heading that up, as it does. 

I'm quite excited about it. There is a website, which I will link straightaway. Now, if you want to submit a panel, or event, or booth for this, you should do it really soon because we've got a crapton of submissions in and we're kind of running out of space. So if you were planning something, get that in as soon as you can. Otherwise, we hope to see you there. It's the start of May. Looking forward to it.

**Glitch**: "that's an excellent problem to have"

**Gdude**: Yes it is, it's a great problem to have. Alrighty, is there anything else anyone wanted to cover on Mumble? If not, we'll move into the questions.

**CheaterCodes**: Is there no news from teams outside of Events then?

**Gdude**: Not that I'm aware of, I've been quite busy. But I haven't seen much going on. The only things that I'm looking at right now since I've been that busy is, I think the Optifine community are looking to collaborate on moderation with us. Although, they're still discussing whether they'd like to do that. And the same thing with Blankworks, but we haven't heard back yet, so we'll see. Other than that, there hasn't been that much going on with the Community Team.

OK, I guess we'll move onto questions then, and that one is definitely yours, **CheaterCodes**.

**CheaterCodes**: That one is definitely mine. So first question is from **Byte** regarding CHASM. Actually, since **Byte** is not able to listen to the podcast-

**Gdude**: I'll try and type it.

(**Gdude**'s real-time notes: Yes and no, as always.  
Not directly, not first-party, don't think there's anything we really want from this, however, we would like to expand Mixin quite a bit.  
The Mixin frontend is quite comfortable to use for most people, they're used to it and we're like to keep that ing eg, we want to be able to target lambdas by callsite (rather than by name), should be easier and more intuitive

In terms of things that aren't Mixin/AQ - eg interface injection, which we get for free with CHASM - it's completely unnecessary, it's something that you might want but we already have it for free  
Also, **Kroppeb** has been doing some black magic regarding making some method calls automatically asynchronous; no idea what it's about but it sounds fun.  
The whole point of CHASM isn't that we provide every possible interface - it's more that anyone can add what they need to it.)

**CheaterCodes**: Maybe you can type it, thanks. So the question is, "Are there any concepts for CHASM frontends/transformers besides reimplementing Mixins/AW on CHASM?"
So, I think the answer to that is both yes and no, as always. First off, not directly. Like not as officially first-party support, I don't think there's anything we really want from this. However, we would like to expand Mixin quite a bit. So the Mixin frontend is quite comfortable to use for most people. They're used to it, and definitely would like to keep that. So for example, we want to be able to target lambdas, not by name, but by callsite which would be much more stable. And also, more intuitive.

But in terms of things that are not Mixin or access widener (AQ), we could for example talk about interface injection, which is essentially about making an interface visible on source code, like on your MC dependency. This is something we get for free with CHASM, so we don't even need to implement this.

**Gdude**: You cut out at "interface injection".

**CheaterCodes**: Right, so there is interface injection for example that we don't need, because we get it for free with CHASM. Because every mixin is probably going to be source-visible anyway. So it's completely unnecessary.

A quick question from **AlphaMode** just as a quick intermediate: "Isn't interface injection broken on runtime?"
No, it's just not meant to be working with runtime. It's exclusively meant for compile time. So yeah, that is something that for example is something you only need once, but we already have it for free. Then **Kroppeb** has been doing some black magic regarding making some method calls automatically asynchronous. I have no idea what it's about, but it sounds fun. The whole point of CHASM is not that we can provide many, many interfaces as a frontend, but that people can make their own frontends if the needd to without requiring hacks into it. I think that answers the question fairly extensive.

Thx **Gdude**, I hope you got all of that.

**Gdude**: Yep, more or less, thank you.

**CheaterCodes**: I think in the meantime we can answer the next question, because the answer is almost the same as last week. So I'm just going to take it. **Octal** asks, "Are there any plans for Kotlin on quilt? (I already know the answer to this, but others might not)"
It's been a discussion since the last meeting essentially again. I think the short answer to that is yes, there are plans. We just don't know exactly how they'll look yet. We want Kotlin as first-class support somewhere in Quilt. We're just not sure where. We're not sure if it's going to be in QSL, or if it's going to be a separate ~~lang~~ team, or like a separate Kotlin team. Just uncertain.

**Glitch**: It's pretty much just a matter that nobody has gone down and written down all of the advantages and disadvantages for both yet. Like I think that's pretty much where we are. Like somebody just needs to write a proposal and say why.

**Gdude**: Yeah, I guess ideally that would be kind of RFC territory, wouldn't it?

**CheaterCodes**: That is absolutely RFC territory.

**Gdude**: Yeah, so that would be a good way to start: Drafting up an RFC and see whether we get wider comments on that. It'll be great to have support. Obviously not biased at all as a Kotlin developer.

**CheaterCodes**: I think there's no one against support for Kotlin. It's just the question of how and where.

**Gdude**: Right, move on. Remember, get your questions in with /ask. We don't have that many in, so if you have anything, feel free. We still have like 15 minutes. Uh, my Welsh isn't great unfortunately, so I can't pronounce this name properly, but **grifferthrydwy** asks, "Is there anywhere to sign up to attend, but not showcase anything in BlanketCon?",
The answer is no, you don't need to. Just show up and join the server, install the modpack and you'll be there. No need to worry about that at all.

Alright, that is the bottom of my list of questions, if anyone has anything to ask, feel free with /ask. Within reason, that is.

**CheaterCodes**: Please come help out, we can always use more people. You don't need to be super professional, or 20 years' experience junior developer, something IDK.

**Gdude**: That would be one heck of a junior developer.

**CheaterCodes**: Again, especially for CHASM for example. We just need people who write like 10 lines of code, 20 times. Just- I really just can't be bothered because there's so much other stuff to do. I already had great help on CHASM the last time I tried to get people on it. But it was just- At Javadocs for example, you don't really need to know anything about Java to do that. So yeah. 

I'm sure there's plenty of similar cases. I know **Glitch** did something on Quilt Loader, think it's taken care of but... Mappings is also always something you can always review without knowing too much about the context. It's a great way to get started in Quilt.

**Glitch**: Uh, this is definitely more for the develops here than the community, but if you look at that issue that I opened on Quilt Loader, I feel like that's a very good eg on how to hand somebody work and get them to contribute.

**Gdude**: Do you have a link to that?

**Glitch**: Yeah, I can pull that up, give me one second: [https://github.com/QuiltMC/quiltingloader/issues/59](https://github.com/QuiltMC/quiltingloader/issues/59)
("This is a good first issue for anyone looking to dip in to contributing to Loader. If you are interested in getting this done, feel free to ask me questions at glitch#3274 on the Toolchain Discord....")

**CheaterCodes**: Also as a desperate call, if anyone's very comfortable with Build Tools, let us know.

**Glitch**: The trick is basically to implement the whole thing in your head, and then exactly what you need to do. And I know for this specific issue, it took me more time to write the issue than it would have for me to just implement it myself. But we had somebody do it, and did active contributing and that's what important really here.

**Gdude**: Yeah, because we're at the point where like some of the teams are fairly stretched out. So we really just need more people doing the same stuff in a lot of cases.

**Glitch**: Yes, exactly.

**CheaterCodes**: Yeah, it's really ~~about a~~ big issue there.

**Glitch**: And if you don't like go into that much detail, you definitely don't have to. But it helps to have things that are that easy just to get people who are nervous about it onboard.

**CheaterCodes**: Maybe we should have something where like, you copy from the #voice-chat and then explain it to them. Because it's probably faster than writing it out. I don't know, what if there's some fancy community magic we can do to get us closer to the community.

**Glitch**: This issue and all this is actually inspired by something that Rust does. They have mentors so they'll make issue that they'll assign a mentor to, then somebody takes this, and then they have one person that they contact. And then that have somebody that guides them through the whole process, helps them with responding to review comments, etc etc, and gets them through the whole way. And then, I'm pretty sure that they're pretty successful for that.

**CheaterCodes**: Yeah, that seems smart. Ok, yes, here's a fan favourite. **Will BL** asks, "will the chasm mixin front-end include anything like mixin-extras? (<https://github.com/LlamaLad7/MixinExtras>)"
Now, Mixin-Extras is a name that has been thrown around a lot. I haven't looked too closely at it to be honest. I'm pretty sure the answer is yes from what I've heard about it. Let me check. Yeah, so mod effect expression value, sure, that's something you can definitely have in CHASM. I think it's one of the most requested feature is like to modify conditions in if-statements or in loops or anything. Which I think is- For what I'm hearing in Mixin-Extras, definitely something we want. ~~Breadth-width~~ conditions sounds like something that we talked about. Non-conflicting overrides is what we called those, same idea. Or non-conflicting redirects even. Like you redirect some method call only if a certain condition happens, and you can do that without having a lot of mods conflicting.

So I think the answer is yes. I'll have to look in detail to see if there's anything that's not in the CHASM mindset, or we wouldn't want to implement this way. But in principle, yes, pretty sure. That's something you can expect in the main Mixin implementation on Quilt in future.

**Gdude**: Sound pretty fabulous to me. Any more questions to come in? We still got about 10 minutes. I have a question: **grifferthrydwy**, how do you pronounce your name?

**CheaterCodes**: Answered via text.

(**grifferthrydwy**: "griff earth ride why")

**Gdude**: So I'm not actually Welsh, it just looks Welsh. Griffer-thry-d-why? OK. That's not too bad. Griffer's the right way.
(****grifferthrydwy**: "add a discord bot that adds a number equal to the number of issues you've fixed to the end of your nickname. people like it when number go up")
The scordboard's is interesting, but I'm not too sure about doing that, just because I know that people like to game scoreboards. But like, if we thought it would work, it'd be pretty doable. I mean, we have the technology at this point.

**Glitch**: I think it'd be mostly the people writing issues for features that we'd be missing here. It'd be more about like, who gets to the "one issue you get a week first", than it is like, you know, who's contributing the most.

**Gdude**: Yeah, it could be interesting, it's just that I don't want to turn it into, you know, like an Agile burndown chart meeting.

**CheaterCodes**: Maybe you'd open issues for people to open issues.

**Gdude**: I mean, that's a thing that could happen.

**CheaterCodes**: I was honestly surprised when I asked for help on Javadocs and actually people were willing to do that because I hate doing that. So maybe, if there's someone who loves writing issues on Github, hit us up.

**Gdude**: I mean, we could always use someone to help with that, for sure. That's something I've been looking for anyway, so... Already, I think we're about out of questions, so let's call it there. Now, I know that there's still stuff to talk about. Were you guys planning on doing more voice in the other voice [channel], or were you going to do like a closed meeting for the extra Beta stuff?

**CheaterCodes**: Well, I think, as always, I invite the community to an after-party in #development-zero. However, it might be that a few of our develops will go into develop-mtgs and talk about stuff that they were talking about before the meeting started.

**Glitch**: I don't think anything we were talking about strictly has to be secret.

**CheaterCodes**: No, we can do it publicly, ~~but it's ultimately Discord. Discord has the public chats~~, so we'll see how it works out.

**Glitch**: I mean, version systems are controversial, but they're not like secret.

**CheaterCodes**: No no no, it's not secret, that's for sure. I mean, we can go into #dev-zero, and if it gets too loud for other reasons, then we can just move to #dev-one or whatever.

**Gdude**: Alright, sounds good. In that case, thanks for coming to the meeting everyone. The next meeting is probably actually going to be at BlanketCon rather than on Discord. Um, we'll make an event and post a bit more when we know a bit more.

**CheaterCodes**: That's two meetings. The next meeting is just after the Beta, then the one after is the one that's at BlanketCon.

**Gdude**: Oh, you're right. Yeah, that's the one after that. In that case, we'll see you all back here next week, with news from how you've been doing with the Beta ideally. Either way, thanks for coming everyone, and thanks for everyone coming on Mumble as well.



Byte: "Are there any concepts for CHASM frontends/transformers besides reimplementing Mixins/AW on CHASM?",

Octal: "Are there any plans for Kotlin on quilt? (I already know the answer to this, but others might not)",

grifferthrydwy: "is there anywhere to sign up to attend, but not showcase anything in blanketcon?",

Will BL: "will the chasm mixin front-end include anything like mixin-extras? (<https://github.com/LlamaLad7/MixinExtras>)", 
