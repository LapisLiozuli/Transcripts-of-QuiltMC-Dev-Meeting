[Meeting: 12/03/2022](https://anchor.fm/quiltmc-dev-meetings/episodes/Meeting-12032022-e1fp4mo)  
In this episode, the team discuss progress made on Build Tools. CHASM, Loader, and QSL, and their readiness for the beta. They also discuss the Community and Outreach teams, and take questions from the community.  
[https://quiltmc.org](https://quiltmc.org)  
[QuiltMC on GitHub](https://github.com/QuiltMC)  
[Quilt Community Discord](https://discord.quiltmc.org)  
[Quilt Toolchain Discord](https://discord.quiltmc.org/toolchain)  
[Fabric Loom](https://github.com/FabricMC/fabric-loom)  
[Quilt Loom Fork](https://github.com/QuiltMC/quilt-loom)  
[CHASM on GitHub](https://github.com/QuiltMC/chasm)  
[CHASM Gradle Plugin on GitHub](https://github.com/QuiltMC/chasm-gradle-plugin)  
[CHASM Operators PR](https://github.com/QuiltMC/chasm/pull/41)  
[Quiltflower Decompiler on GitHub](https://github.com/QuiltMC/quiltflower)  
[Quilt Loader on GitHub](https://github.com/QuiltMC/quilt-loader)  
[The installer is working! (Twitter)](https://twitter.com/quilt_mc/status/1502939380205428740)  
[Quilt Mappings on GitHub](https://github.com/QuiltMC/quilt-mappings)  
[Quilt Mappings PRs](https://github.com/QuiltMC/quilt-mappings/pulls)  
[Quilt’s Enigma fork](https://github.com/QuiltMC/enigma)  
[Quilt Standard Libraries on GitHub](https://github.com/QuiltMC/quilt-standard-libraries)  
[QSL PR #83: Add Rendering Module](https://github.com/QuiltMC/quilt-standard-libraries/pull/83)  
[QSL PR #82: Recipe Reminder API](https://github.com/QuiltMC/quilt-standard-libraries/pull/82)  
[QSL PR #81: Screen API](https://github.com/QuiltMC/quilt-standard-libraries/pull/81)  
[QSL PR 78: Migrate to Quilt Loader](https://github.com/QuiltMC/quilt-standard-libraries/pull/78)  
[QSL PR 87: Add a way to register new resource pack providers](https://github.com/QuiltMC/quilt-standard-libraries/pull/87)  
[QSL Issues](https://github.com/QuiltMC/quilt-standard-libraries/issues)  
[QSL Poll on Class Naming (Toolchain Discord)](https://discord.com/channels/833872081585700874/951957775280373800/952247417116430366)  
[Outreach Team RFC](https://github.com/QuiltMC/rfcs/blob/master/structure/0048-outreach-team.md)  
[Outreach Team PR](https://github.com/QuiltMC/rfcs/pulls/48)  
[Quilt Twitter](https://anchor.fm/twitter.com/quilt_mc)  
[FREX on GitHub](https://github.com/vram-guild/frex)  
[MultiMC](https://anchor.fm/multimc.org)

=========================

**Gdude**: Hello and welcome to the QuiltMC Developer Meetings Podcast. The podcast that... isn’t really a podcast. If you’re new here, this is just a collection of recordings of each public Quilt Project Developer Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed from a Mumble server and recorded live by a fleet of Discord bots. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to [https://quiltmc.org](https://quiltmc.org).

=========================

ATTENDEES
- **Emmaffle**
- **Gdude**
- **OroArmor**
- **Kroppeb**
- **Leo**
- **CheaterCodes**
- **Haven**
- **Octal**
- **Glitch**
- **MartrixX**
- **kb1000**
- **Southpaw**
- **i509VCB**
- **LambdAurora**
- **RTTV**

=========================

**Emmaffle**: Hey, it works.

**CheaterCodes**: Finally. That only took a few minutes, but at least it gave everybody enough time to join. OK, well, welcome to our fortnightly Developer Meeting as **Gdude** likes to call it. Please a round of applause for **Gdude** in chat, who’s not here but still fixed our issues. Thank you.

**Glitch**: I can’t clap and hold the push-to-talk button thing.

**CheaterCodes**: So yeah, I’m going to be the stand-in tonight. I have help from other people, so if I mess stuff up, I think people will let me know. But anyway, let’s get this thing started right away. **Glitch**, are you back yet? Yes, **Glitch** is back. So let’s start with Build Tools first, and **Glitch** will give us a quick update about it.

**Glitch**: Alright, for Build Tools, we’re working on fandangling Loom into understanding that JAR files with quilt.mod.json files are actually mods and understanding how to read those. And once we have that done, either by getting that in upstream, or just forking Fabric Loom, we’ll be able to use Quilt Loader to make mods, essentially.

It’s not ideal, we’d rather not rely on Fabric Loom, because it’s big and complex and hard to change. We’d rather be using VanillaGradle, but it’s just not there for the timeline we want to be able to make mods with Quilt Loader as soon as possible. Yes, and as **Leo** said, Loom is kind of a mess because it’s many years old and very, very big.

**CheaterCodes**: Alright, thank you for that. I'm going to introduce a new section this meeting. I'm gonna ask Build Tools: How ready are we for Quilt Beta?

**Glitch**: Assuming what I mentioned gets merged or we just fork Loom, that should be good enough for Beta. Obviously we won't be able to use Hashed Mojmap, but it's something.

**CheaterCodes**: And we've still got over a month's time, and it sounds like we're right on track.

Next team for the list, Team CHASM. I'm going to have the honour to talk about it myself. Um, there's two things that have been happening recently. One is the test of the CHASM Gradle plugin, which got a new revision at a new home on a new repository. It's a lot cleaner now, it's actually less code, I think it works quite well, and the integration is as good as you can expect, as it should be expected to be.

Uh, it could be better, by adding a lot of hacks, like making sure they show up as the actual dependencies like actual Gradle/Maven coordinates and Dependency View in IntelliJ for example. But honestly, that's low-priority and I'd rather have it working cleanly and having better maintainability.

Then the second thing that's been talked *about*, the discussion again around CHASM-Lang, because again two things here. First, I asked **Kroppeb** to be so nice and try it out a bit, and seems like **Kroppeb** had a lot of fun with it. Um, except that he was complaining about a lot of missing functionalities, so there's a PR that's adding a lot of missing operators to the current language implementation. However, I myself am currently looking at changing the language implementation over to use maybe Java CC instead of ANTLR. I'm not completely sold on that yet, but Java CC has some nice things that ANTLR doesn't, and *vice-versa*, but mostly I like Java CC because it doesn’t have runtime dependencies, so that makes it easier to package in the Chasm Gradle plugin.

Those are the things that are happening right now, it’s moving. Now, to lead myself into my own extension: How ready are we for Quilt Beta? Well, first off, CHASM is not explicitly planned for Quilt Beta. There might be something, like I'm hoping and I'm planning to have some sort of access widener implementation. And that’s pretty much it. Mixin is not realistic to have for Quilt Beta, it’s too much work. Access wideners, maybe, and also interface injections as well, because that's quite simple. So are we ready for Quilt Beta? Yes, but also we don’t really have a project that's going to be in Beta. It'll be just fine without CHASM. Alright, I've talked myself dry, so let's move onto the next team: Community Tooling.

**Emmaffle**: Ain’t got nothin'.

**CheaterCodes**: Ain’t got nothing today. Uh, it’s fine. It’s not really something that has anything that needs to be done for Quilt Beta. Decompilers is on holiday, also well deserved, just [at] a very quick glance, there's no hard deadline on what it needs for Quilt Beta, it’s working great already. Same goes with Infrastructure, which we can skip today, **Haven** isn’t here. It’s working just fine right now. So finally, I’ll let somebody else talk. **Glitch**, can you give an update on the Loader?

**Glitch**: OK, hello again. So not much has happened in Loader for the last two weeks. The big thing that is something that I'm actually working on today. I want to get our installer for Quilt Loader running, which would mean that you'd actually be able to use Quilt Loader through the Minecraft launcher. Um, we had something written by i5 months ago, for which I’m going to have to learn the code structure.

**CheaterCodes**: *Clicking and typing sounds*

**Emmaffle**: **CheaterCodes**, mute yourself.

**CheaterCodes**: Wait, I’m not muted.

**Emmaffle** No, you’re not.

**Glitch**: No, you just typed over my whole little speech there. Uh, to summarise, I’m re-learning **i509VCB**’s Quilt Installer stuff and I’m changing it to work with how Quilt Loader has changed over time. And hopefully within the next few days you should be able to use Quilt Loader in the official Minecraft launcher. And that should be all.

**CheaterCodes**: Well, thank you. I appologize for typing, it appears that I’m using the wrong microphone, but I’m not gonna change it now because it’s going to mess up stuff. So Loader, the same question: How ready are we for a Quilt Beta?

**Glitch**: Oh, sorry, I thought I was done. I would say, sure once we have that installer running again, that’s the major thing we need to be able to use loader in production, or else it’s not any good. But for Loader itself, it’s running fine, so I think we’re good.

**CheaterCodes**: Thank you very much. Next up, Team Mappings. **OroArmor** has something to say about that, I think.

**OroArmor**: Uh, yeah, so in the last 2 weeks, 1.18.2 was released, and so we had to push for a bunch of mappings for that. And right now we have a lot of PRs open, I can’t remember how many exactly. But we’ve been merging PRs like crazy. Uh, just give me 1 second. Yeah, we’re on Build 17 for 1.18.2. That means that there have been a lot of PRs merged for 1.18.2, which is great because a lot of mappings were being filled out, and that Quilt Mappings is becoming closer to that 100% mark we’re looking for.

Something else that just came up just yesterday was that **MartrixX** updated Enigma so that synthetic classes and methods and fields and stuff like that weren’t included in the percentages that Enigma reports for how much of the mappings you’ve completed. So we have better representation of how close we are to completing all the mappings, which is very nice. Other than that, I don’t think there’s really much else to say about where Quilt Mappings is right now.

**Emmaffle**: I’d like to add something. We have a lot more triage members now, but we are still looking for more. So if you want to be a Mappings Triage member, then go ahead to the #mappings-general channel.

**OroArmor**: If you want to be in Mappings Triage, feel free to ping me as many time as you want. I will see that and help you, hehe.

**CheaterCodes**: That's great to hear, thank you for the updates. Yes, the point of Triage is, I think, to have a very big team. So of course more people are welcome. **OroArmor**, so what about Quilt Beta?

**OroArmor**: I think, we’re definitely good to go right now with Quilt Mappings on Loom. The only- There’s a couple of PRs we’re working on with that, especially to add stuff like unpick support & more. However I think there were a couple of issues that we encountered that were internal to Loom and wouldn’t be easy to fix. And so those would have to be fixed before we would be able to fully update. I can’t remember exactly what it was, but there was something there. But we should definitely be ready by Beta, especially if we make our own fork of Fabric Loader.

**CheaterCodes**: By Fabric Loader you mean ‘Fabric Loom’, right?

**OroArmor**: Loom.

**CheaterCodes**: Yeah, OK, just for clarification. Great to hear, so we are again fully on track with the big projects. Talking about great big projects, the last one, probably the biggest of them all- **LambdAurora**, do you want to talk to us about updates, the current state of QSL?

**LambdAurora**: Yes, so QSL got a lot of development recently, so we got new PRs, we got the Rendering Module PRs, it's in draft but it’s there. We got a Recipe Remainder API PR, a Screen API PR and a PR to migrate to Quilt Loader. Basically, for Quilt Beta, QSL will not work on Fabric any more, since it was just temporary. This also means that any of the mods that were using QSL in Fabric will break. So they will have to be recompiled for proper Quilt support. The QSL they use will be unsupported.

And for Quilt Beta, we don’t have Registry Sync yet, so for now we think that we’ll use the Fabric one. We will work on a QSL version. Today I made a PR to get us closer to our Virtual Resource Pack API in QSL. For now it only allows to register new resource pack profiles. A Resource pack Profile is the little item, you see in the resource pack the selection screen, so that’s that. But it’s already a nice step. It will also make [the] implementation of, like, a global datapack directory simpler, since it uses that system.

Otherwise, we do need review on QSL PRs so that we know we don’t make a big mistake, and that everything actually works respective to the use cases. If someone looks for something to do in QSL, you can look into the issues, since there are issues about what could be done in QSL, so you can look into it. Maybe pick one, maybe contact us too, to discuss a bit about how to implement stuff extra that can be done through GitHub Issues, or through Discord. So I think that’s all I have to say.

**CheaterCodes**: Thank you **LambdAurora**. You already mentioned Quilt Beta here, but maybe I can just ask again for a very quick recap of what’s missing?

**LambdAurora**: What’s missing right now, is QSL link to Quilt Loader. That will happen very soon. Currently there’s some stuff to deal with, but that should be dealt with rather quickly. It’s not a specific requirement but Registry Sync would be really nice. But until that is done, we can just use the Fabric one. That’s the two big things that would be needed for Quilt Beta. One of which doesn’t have a hard requirement. Basically, QSL is very close to being ready for Beta.

**CheaterCodes**: Great to hear. I think we have a little more than a month of time, a month and a week or something. I think we can make it, of course I'm not promising it. So that was all the dev teams. Right, **Leo** wanted something.

**LambdAurora**: I totally didn’t see the poll. Which point **Leo**? So in #meeting-chat, there is a link to a poll for the names for one of the modules, so you can look into it and vote.

**CheaterCodes**: It’s about naming, yes? OK, If you’re interested in that, check out the poll. I see there’s already quite a few people voting. And it seems like it might be an easy win for one of the options, but we’ll see how it turns out. OK, thank you. So that's it with the dev teams which leaves us with two more teams. That is, the Community Teams and the Outreach Team and **Emmaffle** volunteered to do both of them, more or less together. So please.

**Emmaffle**: Right, so Outreach Team has had perhaps the most productive 2 weeks in its history, probably because we didn’t exist 2 weeks ago. The PR work got merged on March 1st with a bunch of new members. **Southpaw** is the lead of it. And during that time, we have done 3 main things. We revived the Twitter, we are working on new blog posts, and we are working on getting an official Quilt forum set up. So that’s all pretty exciting stuff, at least I would say.

We’re also looking for someone who can help manage the GitHub development boards for like todo-lists and stuff like tt. So if you’re interested in helping with stuff like that on the Outreach Team, please send a message to **ModMail**. I don’t think there’s really that much other stuff that’s been going on with Community Team. But we’ve been doing a lot with the forums, and I’m personally most excited for that. Though apparently the forum is just Community Team in general, not Outreach specifically, but same thing.

**CheaterCodes**: Well, thank you to the Community Team. Yes, as Community mentioned, Outreach is a sub-team of Community now, which is different to what it was originally. I also got that a little bit wrong. Yeah, Community Team is always doing great work, being very active. And yeah, they need more people. Please help our Community to be better than ever before, even though it’s already been great.

**Emmaffle** Yes, and send message to Modmail please, if you’re interested in helping.

**CheaterCodes**: Alright, that brings us to the end of the general dev meeting. So for the rest of our time, we’re going to do the AmA, which has already started. So feel free to use the /ask command in the meeting chat. That will put the questions in a queue, where we will look at them one-by-one, and your question will be seen, first it will be approved by moderators and then answered by devs. And we usually don’t skip question, so you will be heard, and you will be answered. So, who goes first?

**Oro**: I say we start from the top. The new questions.

**CheaterCodes**: That is a great idea. So maybe **LambdAurora** can take the first one? If you’re still here?

**Glitch**: If **LambdAurora** is not here, I can take it.

**CheaterCodes**: Go ahead, please.

(**RTTV**: What is planned for QSL other than more callbacks?)

**Glitch**: Alright, so QSL is definitely not just a more callbacks thing.

**LambdAurora**: Wait wait wait wait wait wait wait, you need to read out the question.

**Glitch**: Sorry, do you want to take this since you’re here **LambdAurora**?

**LambdAurora**: I can.

**Glitch**: Yes please, haha.

**LambdAurora**: **RTTV** asks, "What is planned for QSL other than more callbacks?"
First of all, QSL is not just callbacks. For example, the QSL Base module includes entrypoints, which is a bit more. But it also contain the event infrastructure, and a launch argument which can be used for auto-testing a server. What is does, is when a server is launched, it would only be working for a set number of ticks. Then it will audit all Mixins loaded and then it will shut down. So that’s an example.

There's other stuff like Registry Sync. It’s not really callbacks, but what it does is it will synchronize the registries of the client and the server during shutdown. For example, if the client has more mods, or if the mods are not loaded in the same order, it won't have the same registry with the same raw identifiers. And the raw identifier is not a string identifier, it’s a number. If that doesn’t match, it will witness a lot of corruption on the client, because the client won’t recognise the proper items and blocks.

Other stuff like BlockExtension, it’s not just callbacks. It takes BlockSettings, which is a class used to set some basic settings and properties on a block. What it does, it extend that to be able to do more. Or you have the Quilt ItemGroups, which is kind of a port of the Fabric ones. That is a bit different. What it does is, if a mod registers a new ItemGroup, it will be added properly, there will be a pagination system. If you take for example, the case of Quilt Tags, you can have Tags that are loaded entirely for the client. Or Tags that use the client resources as a fallback if the server doesn’t have the Tag. So there’s a whole lot more than just callbacks.

There will be something, I’m not entirely sure when it will be made, but was talk about having FREX being included in QSL in some way, which is kind of an equivalent/replacement to the Fabric Renderer API. And that thing is not just callbacks too. FREX comes with a lot more features than Fabric Renderer API. But to list out every new feature, that would be a bit hard, because we don’t know every new feature yet. But we will try to add stuff as needed, so if someone has a really big use case for something, we can look into it. And if it can really benefit the community, it might be added. That’s it for now.

**CheaterCodes**: Thank you. I think that was an very extensive answer probably answered all questions that were still lingering about the topic. Of course, plans can change. Next question, I’ll just go and read it out so that the speakers don’t forget. Question by **RTTV**: "Will Quilt have direct installation into MultiMC like Fabric and Forge, or would it have to resort to ViveCraft-like installation steps?" **Glitch**?

**Glitch**: Alright, so, I’m not really sure if MultiMC has expressed interest. I will say that any launcher that is interested in supporting Quilt Loader, we will help them with anything they need to support it. I know we have heard from, I believe, CurseForge, ATLauncher and PolyMC that they’re interested, but I haven’t heard anything MultiMC-wise yet, so I hope that answer the question.

(**kb1000**: Sounds easy to adjust then, MultiMC's component-based architecture would make it possible to reuse the Fabric intermediary component.)

**Emmaffle**: **kb1000** said that he’s going to implement it in the meeting chat.

**CheaterCodes**: The next question is, again from **RTTV**: "Will CHASM recreate the feature set of Fabric-ASM and other non-vanilla Fabric mod (like Mixin) bytecode editing tools?"
Well first off, I’m curious, what are vanilla Fabric mods? Like what’s, I don’t know, vanilla tools?

In general, there’s a bit of a misconception around what CHASM is. Many people view CHASM as like a Mixin replacement, but that is absolutely not what CHASM is. CHASM is an abstract layer on top of ASM, like [Object Web ASM](https://asm.ow2.io/). It’s just an abstraction to allow multiple people to use ASM at the same time without conflicting. That means that CHASM itself is not going to support Mixin or anything like that, but they’re all going to use CHASM to implement something.

So the answer to that question is, CHASM won’t do anything like that, but there will be first and third-party CHASM frontends that enable that sort of stuff. For example, Access Widener is likely gonna be maintained by Quilt, Mixin is likely gonna be maintained by Quilt. Interface injections are probably not gonna exist, because Mixin with CHASM works a little differently than on Fabric. But if there’s anything else, it’s fairly easy for a third-party to provide the tools without requiring changes or dirty hacks into the toolchain, which is one of the big reasons why doing anything on Loom is really hard. Because you need to hardcode every single stage and transformation inside of Loom. Whereas with CHASM, you just state it. It’s like adding a datapack, you can just add a new frontend. Something like that.

Alright, I think the next question is a bit of a general one. It doesn’t just target one team, so I’ll just start and if anyone else has to add something to it. **Southpaw** asks, What promised features will be missing from the tooling at the beta release? So, just for clarifcation, this is asking about features that are promised to exist in Quilt, but might be missing from the beta release. Promised for the full release but not happening in beta. For example, CHASM Mixin - Mixins on top of CHASM, is not going to be in the beta, there’s just no way. CHASM in general not guaranteed to be in the beta, we’ll see about that. Build Tools, is probably going to be some form of fork of Loom.

**CheaterCodes**: Alright, I think the next question is a bit of a general one. It doesn’t just target one team, so I’ll just start and if anyone else has to add something to it. **Southpaw** asked: "What promised features will be missing from the tooling on the beta release?"

**CheaterCodes**: So just for clarification, this is asking about features that were promised to exist in Quilt, but might be missing from the beta release. Promised in full release but not present in beta. For example, CHASM-Mixin - Mixins on top of CHASM, is not going to be in the beta, there’s no way. CHASM in general is not guaranteed to be in the beta, we’ll see about that. Tools, is probably going to be some form of fork of Loom.

**Glitch**: Yes, build tools, we will be using a completely different project for our build tooling between beta release and full release, hopefully. We’re using Fabric Loom right now, but we would like to use VanillaGradle eventually.

**CheaterCodes**: It also means the default, we’re not sure whether the default decompiler will be set to QuiltFlower, Hashed(-Mojmap) probably won’t make it into Beta.

**Glitch**: Almost definitely not.

**CheaterCodes**: Yes, unless we find a really easy way to integrate it. Mappings, might still require the Quilt Mappings on Loom rather than being first-party direct support. All those sort of small things are going to be missing. But I think in terms of content as well, mappings, since some of the mappings are still in tooling. Unpick, also probably not going to make it into Beta. Probably want to have version-indepedent mappings, also not going to make it into Beta. So there’s a lot of- All those small things.

**Glitch**: To add on for Loader, the Loader is promising loader plugins which are essentially ways to add more functionality to the loader. For example being able to load Forge mods, Sponge plugins, etc. That probably will not be in in a month from now, Alex isn’t here to confirm that, but I’m pretty sure. And on the same token, we’ve talked about auto dependency downloading, which would essentially mean for certain dependencies, like QSL, instead of jar-in-jarring them, Loader would automatically find the dependency you need and download it from a Maven. That is definiely not there yet, because Loader plugins have to exist for that to happen.

**CheaterCodes**: Anything else? I think on QSL there's nothing in particular waiting for full release, just general libraries that might be added later.

**Glitch**: Generally we love it to be bigger and cover new things that aren’t in Fabric API and also eventually make it so you can do almost everything Fabric API does. It’s not the goal right now, but eventually, we would like to not essentially require modders to use Fabric API in addition to QSL.

**CheaterCodes**: Alright, I hope **Southpaw**, that gives you enough fuel for the blog article, but otherwise just feel free to ping us. You know where we are, where you can find us. Alright, **OroArmor**, you still here?

**OroArmor**: Yes, I can take this question.

**CheaterCodes**: Alright, the question is by, **Emmaffle** or Emma Waffle... I don’t know what happened to the name now.

**OroArmor**: Alright, the question by **Emmaffle** is, "Will we ever be able to use QM without using the ugly-looking layered mappings thing? :P"
In Loom, I’m going to say no. Technically there’s a small chance you could do it without the ugly-looking layered mappings thing, however I’m going to keep it as layered mappings. One, that’s the style that Loom wants people to use. And two, that allows adding other things like Parchment and Mojmap if people want those, so that I’m not forcing it, so that it’s one way. Once we have our Build Tools version, it should be fairly easy to add Quilt Mappings without the layered mappings things. And with VanillaGradle, I definitely know that **Glitch** has put in a lot of work to make the mappings system very extensible. And so Quilt Mappings together with whatever addition we add will be very easy to use there.

**CheaterCodes**: Alright, thank you. Keep the questions coming, because right now we only have one more in our queue.

**Glitch**: I think this one is for me, haha.

**CheaterCodes**: Go ahead.

**Glitch**: RTT~~T~~V (**RTTV**) asks: "Anything Quilt has done to make it possible for Forge mods to be loaded?"
The answer is, you’re asking the wrong project. (Did I add an extra T? Oh well.) I also worked in the past on Patchwork, which was making Forge mods load on Fabric. That will be running on Quilt, but that will not be something first-party with Quilt. We won’t ever support loading other modloaders besides Fabric/Quilt officially.

**CheaterCodes**: Yes, I'll add here, compatibility with Fabric is just something that gonna exist as long as we kind of benefit from it. Because it would be quite hard eventually to support it. Most likely it would be an incredible burden to support Forge. But for a start, it's definitely something we want. But for Forge it’s just not feasible. The design is too different for us to have first-party support.

Alright, any more questions? Keep 'em coming. We’re running dry here. Otherwise, in the meantime, while we give you a few more minutes to answer, I’ll do a general call to check out PRs to review. QSL has a separate channel now for PRs that need reviewing. Quilt Mappings always has open PRs that would be great if you looked at them. And if you would like to contribute to any other project, or even those projects as well, just hop into our toolchain Discord. You’re already here; look into the corresponding channel, just leave a message there. If you’re brave, you can ping a team or a specific person you know. But in general, if you just drop a message in there someone will see it and then we can talk about how you can help with the project.

**Glitch**: Just to jump in- We’re not scary. We would love people to come contribute. We have plenty to do. So you don’t need to take any kind of commitment to try and review a PR, or make some mappings, or write even an entirely new module for QSL. So if you’re interested, please just hop on Discord and ask us about it.

**CheaterCodes**: Alright, well, I think there’s no new questions, and I think there’s also no remaining answers that we have. Yep. So I guess it’s time to end this. Ah, last minute, last second question! I think this one is for **Glitch** again.

**Glitch**: OK, **Octal** asks, "Will Quilt's mapping system allow for layered mappings as well?"
Uh, yes, VanillaGradle will support layered mappings. I spent a lot of work trying to figure out the best way to support that, so it is definitely a priority to me for that to be working well.

**CheaterCodes**: Thank you. Yes, something I think that’s kind of working already.

**Glitch**: Very kind of. The whole backend needs to be rewritten for like the 4th time.

**CheaterCodes**: Yes, there’s a lot of stuff about VanillaGradle that’s also not ideal for CHASM specifically and for remapping input mods, there’s just not a system there. So the future of VanillaGradle is still a little bit uncertain right now. It’s a lot of work to do a big project like that, that's also somewhat intended to be used by other projects. But we’ll have to see how it goes.

OK, so **RTT~~TTTT~~V** (**RTTV**) with another last-minute question, asking: "What code from Fabric still exists on Quilt?"
I think that again is still a bit of a multi-project question. Looking at it real quick, right now it’s Loom that’s probably going to change, hopefully going to change with the full release.

**CheaterCodes**: On mappings, it’s mostly Tiny stuff which we talked about last meeting, which we’re planning to hopefully yeet at some point, and I think that's all the Fabric code that I can see. Alright so, I’m going to end this here now, so any last-minute questions coming in now will not be looked at any more. Uh, thank you all for joining and listening in and for the devs to talk and for the Community Team to be around and manage stuff for us.

As always, or most of the time, I’m going to invite you all to a quick after-party on the Development channel on the toolchain Discord, where we can just hang out a bit and chat a bit more, about possibly unrelated stuff as well. And I hope the new time is also something that's good for everyone. But yeah, we're going to meet each-other again in two weeks, same day, same time. Thank you very much.

**Emmaffle**: Bye everyone.

**Glitch**: Quilt Loader is a fork of Fabric Loader.

**CheaterCodes**: Yes, it’s a fork with parts completely swapped out, other parts basically completely intact.

**LambdAurora**: For QSL, you can see which stuff is Fabric. Go into the header, for each file there’s a license header. If it’s from Fabric, it will contain a line about the original ownership of Fabric for the code.

**CheaterCodes**: Does QSL use Fabric code specifically in Fabric API on QSL, I'm assuming?

**LambdAurora**: In Fabric API-QSL compatibility, it’s a fork of Fabric API, which re-implements some stuff using QSL instead. So yeah, of course it’s using Fabric code.

**CheaterCodes**: On mappings, it’s mostly Tiny stuff which we talked about last meeting, which we’re planning to hopefully yeet at some point, and I think that's all the Fabric code that I can see. Alright so, I’m going to end this here now, so any last-minute questions coming in now will not be looked at any more. Uh, thank you all for joining and listening in and for the devs to talk and for the Community Team to be around and manage stuff for us.

As always, or most of the time, I’m going to invite you all to a quick after-party on the Development channel on the toolchain Discord, where we can just hang out a bit and chat a bit more, about possibly unrelated stuff as well. And I hope the new time is also something that's good for everyone. But yeah, we're going to meet each-other again in two weeks, same day, same time. Thank you very much.

**Emmaffle**: Bye everyone.

**LambdAurora**: Bye bye.

**CheaterCodes**: Oh damn, why is it using the wrong microphone? There we go, now it's back to the right microphone.

**OroArmor**: Sounds so much better.
