**Gdude**: Hello and welcome to the QuiltMC Developers� Meeting Podcast. The podcast that...isn�t really a podcast. If you�re new here, this is just a collection of recordings of each publicly recorded Developers� Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed from a Mumble server and recorded live, hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to over to [https://quiltmc.org](https://quiltmc.org)

**Emma**: Hey, it works!

**CheaterCodes**: Finally! It only took a few minutes, but at least it gave everyone enough time to join. OK, well, welcome everyone, to our fortnightly Developer Meeting, as Gdude likes to call it. Please, a round of apeopleause for Gdude in chat, who�s not here but still fixed our issues. Thank you.

**Glitch**: I can�t clap and hold the push-to-talk button, dang.

**CheaterCodes**: So yeah, I�m going to be the stand-in tonight. I have help from other people, so if I mess up, I think people will let me know. But anyway, let�s get this thing started right away. **Glitch**, are you back yet? Yes, **Glitch** is back. So let�s start with Build Tools first, and **Glitch** will give us a quick update on that.

**Glitch**: Alright, so, for Build Tools, we�re working on fandangling Loom into understanding that JAR files with quilt.mod.json files are actual mods and understanding how to read those. And once we have that done, either by getting that in upstream, or just forking Fabric Loom, we�ll be able to use Quilt Loader to make mods, essentially.

It�s not ideal, we�d rather not rely on Fabric Loom, because it�s big and complex and very hard to change. We�d rather be using VanillaGradle, but it�s just not there for the timeline we want to be able to make mods with Quilt Loader as soon as possible. Yes, and as Leo said, Loom is kind of a mess because it�s many, many years old and very, very big.

**CheaterCodes**: Alright, thank you for that. I'm going to intro a new part this meeting, and I'm going to ask Build Tooks: How ready are we for Quilt Beta?"

**Glitch**: Assuming what I mentioned gets merged or we just fork Loom, that should be good enough for Beta. Obviously we won't be able to use Hashed Mojmap, but it's something.

**CheaterCodes**: And we've still got over a month's time, and it sounds like we're right on track. 

Next team for the list, Team Chasm. I'm going to have the honour to talk about it myself. Um, there's two things that have been happening recently. One is the test of the Gradle plugin, which got a new revision at a new home on a new repository. It's a lot cleaner now, it's actually less code, I think it works quite well, and the integration is as good as you can expect, as it should be expected to be.

Uh, it could be better, by adding a lot of hacks, like making sure they show up as the actual dependencies like actual Gradle/Maven coordinates and Dependency View in IntelliJ for example. But honestly, that's low-priority and I'd rather have it working cleanly and having better maintainability.

Then the second thing that's been talked \[about\], the discussion again around Chasm-Lang, because again two things here. First, I asked **Kroppeb** to be so nice and try out a bit, and seems like **Kroppeb** had a lot of fun with it. Um, except that he was complaining about a lot of missing functionalitie,s so there's a PR that's adding a lot of missing operators to the current language implementation. However, I myself am currently looking at changing the language implementation over to use maybe Java CC instead of ANTLR. I'm not completely sold on that yet, but Java CC has some nice things that ANTLR doesn't, and *vice-versa*, but mostly I like Java CC because it doesn�t have runtime dependencies, so that makes it easier to package in the Chasm Gradle plugin.

Those are the things that are happening right now, it�s moving. Now, to lead myself into my own extension: How ready are we for Quilt Beta? Well, first off, Chasm is not explicitly planned for Quilt Beta. There might be something, like I'm hoping and I'm planning to have some sort of access widener implementation. And that�s pretty much it. Mixin is not realistic to have for Quilt Beta, it�s too much work. Access wideners, maybe, and also Interface interactions as well, because that's quite simple. So are we ready for Quilt Beta? Yes, but also we don�t really have a project that's going to be in Beta, ~~it'll be just fine~~ without Chasm. Alright, I've talked myself dry, so let's move onto the next team: Community Tooling.

**Emma**: Ain�t got nothin'.

**CheaterCodes**: Ain�t got nothing today. Uh, it�s fine. It�s not really something that has anything that needs to be done for Quilt Beta. Decompilers is on holiday,'s also well deserved, just \[at\] a very quick glance, there's no hard deadline on what it needs for Quilt Beta, it�s working great already. Same goes with Infrastructure, which we can skip today, **Haven** isn�t here. It�s working just fine right now. So finally, I�ll let somebody else talk. **Glitch**, can you give an update on the Loader?

**Glitch**: OK, hello again. So not much has happened in Loader for the last two weeks. The big thing that is something that I'm actually working on today. I want to get our installer for Quilt Loader running, which would mean that you'd actually be able to use Quilt Loader thru the Minecraft launcher. Um, we had something written by i5 month ago, for which I�m going to have to learn the code structure.

**CheaterCodes**: *Typing sounds*

**Emma**: **Cheater**, mute yourself!

**CheaterCodes**: Wait, I�m not muted?

**~~C~~:** No, you�re not!

**Glitch**: No, you just typed over my whole little speech there. Uh, to summarise, I�m re-learning i5�s Quilt Installer stuff and I�m changing it to work with how Quilt Loader has changed over time. And hopefully within the next few days you should be able to use Quilt Loader in the official MC launcher. And that should be all.

**CheaterCodes**: Well, thank you. It will address first, it appr that for typing I�m using the wrong mike, but I�m not gonna change it now because it�s going to mess up stuff. So Loader, the same question: Are we ready for Quilt Beta?

**Glitch**: Oh, sorry, I kinda thought I was done. I would say, sure once we have that installer running again, that�s the major thing: we need to be able to use Loader in production, or else it�s not any good. But for Loader itself, it�s running fine, so I think we�re good.

**CheaterCodes**: Thank you very much. Next up, Team Mappings. **Oro** has something to say about that, I think.

**Oro**: Uh, yeah, so in the last 2 week, 1.18.2 was released, and so we had to push for a bunch of mappings for that. And right now we have a lot of PRs open, I can�t remember how many exactly. But we�ve been merging PRs like crazy. Uh, just give me 1 second. Yeah, we�re on Build 17 for 1.18.2. That means that there have been a lot of PRs merged for 1.18.2, which is great because a lot of mappings were being felt out, and that Quilt Mappings is becoming closer to that 100% mark we�re looking for. 

Something else that just came up just yesterday was that **MartrixX** updated Enigma so that synthetic classes and methods and fields and stuff like that weren�t included in the percentages that Enigma reports for how much of the mappings you�ve completed. So we have better representation of how close we are to completing all the mappings, which is very nice. Other than that, I don�t think there�s really much else to say about where Mappings is right now.

**Emma**: I�d like to add something. We have a lot more triage members now, but we are still looking for more. So if you want to be a Mappings Triage member, then go ahead to the #mappings-general channel.

**Oro**: If you want to be in Mappings Triage, feel free to ping me as many time as you want. I will see that and help you, hehe.

**CheaterCodes**: Yeah, thank you for the updates. Yes, the point of Triage, I think it�s to have a very big team. So of course more people are welcome. **Oro**, so what about Quilt Beta?

**Oro**: I thk, we�re definitely good to go right now with Quilt Mappings on Loom. The only- There�s a couple of PRs we�re working on with that, especially to add stuff like ~~unpick~~ support & more. However, I think there were a couple of issues that we encountered that were inernal to Loom and wldn�t be easy to fix. And so those would have to be fixed before we would be able to fully update. I can�t remember exactly what it was, but there was something there. But we should definitely be ready by Beta, especially if we make our own fork of Fabric Loader.

**CheaterCodes**: By Fabric Loader you mean �Fabric Loom�, right?

**Oro**: Loom.

**CheaterCodes**: Yeah, OK, just for clarification. Great, so yes, so again, we are fully on track with the big projects. Talking about great big projects, the last one, probably the biggest of them all- **Aurora**, do you want to talk to us about updates to the current state of QSL?

**Aurora**: Yes, so QSL got a lot of development recently, so we got new pull requests, we got the rendering module pull request, it's in draft but it's there. We got a recipe reminder API Pull Request, a Screen API Pull Request, a Pull Request to migrate to Quilt Loader. Basically, for Quilt Beta, Quilt Standard libraries will not work on Fabric any more, since it was just temporary, this also means that any of the mods that \[are\] currently using QSL in Fabric will break. So they will have to be recompiled for proper Quilt support. The QSL they use will be unsupported.

And for Quilt Beta, we still don�t have a registry sync, so for now, for a registry sync, we'll use the Fabric one, though we will work on a QSL version. Today I made a Pull Request to get us closer to our Virtual Resource Pack API in QSL. It only allows to register the new resource pack profiles. A Resource pack Profile is the little item, you see in the resource pack the selection screen, so that�s that. But it�s already a nice step. It will also make [the] implementation of, like, a global datapack directory simpler, since it uses that system.

Otherwise, we do need reviews on the QSL PRs so that we know that we don�t make a big mistake, and that everything actually works respective to the use cases. If someone looks for something to do in QSL, we can look into the issues, since there are issues about what could be done in QSL, so you can look into it. Maybe pick one one, and maybe contact us too, to discuss a bit about how to implement stuff extra that can be done through Github Issues, or through Discord. I think that�s all I have to say.

**CheaterCodes**: thank you **Aurora**. You already mentioned Quilt Beta here, but maybe I can ask again, just for a very quick recap of what�s missing?

**Aurora**: What�s missing right now, is QSL ~~loading on~~ Quilt Loader. That will happen very soon. Currently, there�s some stuff to deal with, but that should be dealt with rather quickly. It�s not a specific requirement but registry sync would be really nice. But until that is done, we can just use the Fabric one. That�s the two big things that will be needed for Quilt Beta, one of which doesn�t have a hard requirement, but yeah. Basically, QSL is very close to being ready for Beta.

**CheaterCodes**: Great to hear. Thank you Lambda, and ~~we have a little bit more than a month of time, but in a week or something, I think we can make it. Of course, I'm not promising anything. 

So, that was all of the dev teams. Right, Leo wanted something.

**Aurora**: I totally didn�t see the poll, good point Leo? So in #meeting-chat, there is a link to a poll for the name for one of the modules, so you can look into it and vote.

**CheaterCodes**: It�s about naming, yes? OK. If you�re interested in that, check out the poll. I see there�s already quite a few people voting, and it seems like it might be an easy win for one of the options, but we�ll see how it turns out. OK, thank you. There, that's' with the dev teams,which leaves us with two more teams, that's there the Community Team and the Outreach Team, and Emma volunteered to do both of them, more or less together. So please.

**Emma**: Alright, so Outreach Team has had perhaps the most productive 2 weeks in its history, probably because we didn�t exist 2 week ago. The pull request work got merged on March 1st with a bunch of new members. **Southpaw** is the lead of it. And during that time, we have done 3 main things: We revived the Twitter, we are working on new blog posts, and we are working on getting an official Quilt forum setup. So that�s all pretty exciting stuff, at least I would say. 

We�re also looking for someone who can help manage the Github development boards for like to-do lists and stuff like that, so if you�re interested in helping with stuff like that on the Outreach Team, please send a message to ModMail. I don�t think there�s really that much other stuff that�s been going on with Community Team. But we�ve been doing a lot with the forums, and I�m personally most excited for that.  Oh, apparently the forum is just Community Team in general, not Outreach specifically, but same thing.

**CheaterCodes**: Well, thank you to the Community Team. Yes, the Community Team Mentioned— Oh yeah and Outreach is a sub-team of Community now, which is different to what it was originally, so I also got that a little bit wrong. \[But\] yeah, the Community Team is always doing great work, it's been very active, and yeah they need more people. Please help our Community to be better than ever before, even though it�s already been great.

*~Emma~** Yes, send messages to ModMail please, if you�re interested in helping.

**CheaterCodes**: Alright, that brings us to the end of the general dev meeting. So for the rest of our time, we�re going to do the AMA, which has already started. So feel free to use the `/ask` command in the meeting chat. That will put the questions in a queue, where we can look at them and work on them one-by-one, and your question will be seen and approved by moderators, and then answered by devs. And we usually don�t skip questions, so you will be heard, and you will be answered. So, who goes first?

**Oro**: I say we start from the top. The new questions.

**CheaterCodes**: That is a great idea. So maybe **Aurora** can take the first one? If you�re still here?

**Glitch**: If **Aurora** is not here, I can take it.

**CheaterCodes**: Go ahead, please.

**Glitch**: Alright, so QSL is definitely not just a more callbacks thing, um...

**Aurora**: Wait wait wait wait wait wait wait, you need to read out the question.

**Glitch**: Sorry, do you want to take this since you�re here **Aurora**?

**Aurora**: I can.

**Glitch**: Yes please, haha.

**Aurora**: So, what is plans for QSL other than more callbacks? First of all, QSL is not just callbacks. For example, the QSL Base module includes entrypoints, which is a bit more. But it also contain the event infrastructure, and a launch argument which can be used for auto-testing a server. What is does, is when a server is launched, it would only be working for a set number of ticks, then it will audit all the Mixins loaded, and it will shut down. So that�s an example.

There's other stuff like registry sync. It�s not really callbacks, but what it does is it will synchronise the registries of the client with the server, because in some cases, for example, if the client has more mods, if the mods are not loaded in the same order, it won't have the same registry with the same raw identifiers. And a raw identifiers is not a string identifier, it�s a number. If that doesn�t match, you will witness a lot of corruption on the client, because the client won�t recgonise the proper items and blocks.

Other stuff like block extensions, it�s not just callbacks. It takes block settings, which is a class used to set some basic settings and properties of the block. What it does, it extend that to be able to do more. Or you have the Quilt ItemGroups, which is kind of a port of the Fabric one, but it's a bit different. What it does is, if a mod registers a new ItemGroup, it will be added properly, there will be a pagination system. If you take for example, the case of Quilt Tags, you can have Tags that are loaded entirely from the client, or Tags that use the client resources as a fallback if the server doesn�t have the Tag. So, yeah there�s a whole bit more than just more callbacks.

There will also be... I�m not entirely sure how it will be made, but there was talk about FREX being included in QSL in some way, which is kind of an equivalent/replacement to the Fabric Renderer API, and that thing is not just callbacks at all. FREX come with a lot more features than the Fabric Renderer API. But to list out every new feature, that would be a bit hard, because, well, we don�t know every new feature yet. But we will try to add stuff when it's needed needed, so if someone really need use case for something, we can look into it, and if it's really benefitting the entire community, it might be added. That�s it for now.

**CheaterCodes**: Thank you. I think that was an very extensive answer probably answered all question that were still lingering about the topic. Of course, plans can change. Next question, I�ll just go and read it out so that the speakers don�t forget. Question by **RTTV**: Will Quilt have direct installation into MultiMC like Fabric and Forge, or would it have to resort to ViveCraft-like installation steps? **Glitch?**

**Glitch**: Slright, so, I�m not really sure if MultiMC has expressed interest. I will say that any launcher that is interested in supporting Quilt Loader, we will help them with anything they need to support it. I know we have heard from, I believe, CurseForge, ATLauncher and PolyMC that they�re interested, but I haven�t heard anything MultiMC-wise yet, so I hope that answer the question.

**Emma**: **KB** said that he�s going to implement it in the meeting chat.

**CheaterCodes**: The next question is, again from **RTTV**: Will Chasm recreate the features of Fabric ASM, and other non-vanilla Fabric mods like Mixin, bytecode editing tools?
Well first off, I�m curious, what are vanilla Fabric mods? Like what�s, I don�t know, vanilla tools? 

In general, there�s a bit of a misconception around what Chasm is. Many people view Chasm as like a Mixin replacement, but that is absolutely not what Chasm is. Chasm is an abstract layer on top of ASM, like an ~~object-level~~ ASM. It�s just an abstraction to allow multiple people to use ASM at the same time without conflicting. That means that Chasm itself is not going to support Mixin or anything like that, but they�re all going to use Chasm to implement something.

So the answer to that question is, Chasm won�t do anything like that, but there will be first and third-party Chasm frontends that enable that sort of stuff. For example, Access Widener is likely gonna be maintained by Quilt, Mixin is likely gonna be maintained by Quilt, interface injections are probably not gonna exist, because mixin with Chasm works a little differently than on Fabric. But if there�s anything else, it�s fairly easy for a third-party to provide the tools without requiring changes or dirty hacks into the toolchain, which is one of the big reasons why doing anything on Loom is really hard. Because you need to hardcode every single stage and transformation inside of Loom. Whereas with Chasm, you just state it. It�s like adding a datapack, you can just add a new frontend. Something like that.

Alright, I think the next question is a bit of a general one. It doesn�t just target one team, so I�ll just start and if anyone else has to add something to it. **Southpaw** asks, What promised features will be missing from the tooling at the beta release? So, just for clarifcation, this is asking about features that are promised to exist in Quilt, but might be missing from the beta release. Promised for the full release but not happening in beta. For example, Chasm Mixin - Mixins on top of Chasm, is not going to be in the beta, there�s just no way. Chasm in general not guaranteed to be in the beta, we�ll see about that. Build Tools, is probably going to be some form of fork of Loom.

**Glitch**: Yes, build tools, we will be using a completely different project for our build tooling between beta release and full release, hopefully. We�re using Fabric Loom right now, but we would like to use VanillaGradle eventually.

**CheaterCodes**: It also means the default, we�re not sure whether the default decompiler will be set to QuiltFlower, \[and\] Hashed probably won�t make it into Beta.

**Glitch**: Almost definitely not.

**CheaterCodes**: Yes, unless we find a really easy way to integrate it. Mappings, might still require the Quilt Mappings on Loom rather than being first-party direct support. All those sort of small things are going to be missing. But I think in terms of content as well, mappings, ~~said someone else on the mappings tooling~~. Unpick, also probably not going to make it into Beta. Probably want to have version-indepedent mappings, also not going to make it into Beta. So there�s a lot of- all those small things.

**Glitch**: To add on for Loader, the Loader is promising loader plugins which are essentially ways to add more functionality to the loader. For example being able to load Forge mods, Sponge plugins, etc. That probably will not be in in a month from now, Alex isn�t here to confirm that, but I�m pretty sure. And on the same token, we�ve talked about auto dependency downloading, which would essentially mean for certain dependencies, like QSL, instead of jar-in-jarring them, Loader would automatically find the dep you need and download it from a Maven. That is definiely not there yet, because Loader plugins have to exist for that to happen.

**CheaterCodes**: Anything else? I think on QSL there's nothing in particular waiting for full release, just general libraries that might be added later.

**Glitch**: Generally we love it to be bigger and cover new things that aren�t in Fabric API and also eventually make it so you can do almost everything Fabric API does. It�s not the goal right now, but eventually, we would like to not essentially require modders to use Fabric API in addition to QSL.

**CheaterCodes**: Alright, I hope **Southpaw**, that gives you enough fuel for the blog article, but otherwise just feel free to ping us. You know where we are, where you can find us. Alright, **Oro**, you still here?

**Oro**: Yes, I can take this question.

**CheaterCodes**: Alright, the question is, Emma...Emmawaffle..I don�t know what happened to the name now.

**Oro**: Alright, the question. Will we ever be able to use Quilt Mappings without the ugly-looking layered mappings thing? In Loom? I�m going to say no. Technically, there�s a small chance you could do it without the ugly-looking layered mappings thing, however I�m going to keep it as layered mappings, one \[because\] that�s the style that Loom wants people to use, and two, that allows adding other things, like Parchment and Mojmap if people want those, so that I�m not forcing it, so that it�s one way. Once we have our own build tools version, it should be fairly easy to add Quilt Mappings without the layered mappings thing, and with VanillaGradle, I definitely know that **Glitch** has put in a lot of work to make the mappings system very extendable and so Quilt Mappings together with whatever addition we add will be very easy to use there.

**CheaterCodes**: Alright, thank you. Well, keep the question�s coming, because right now we only have one more in our queue, so...

**Glitch**: I think this one is for me, haha.

**CheaterCodes**: Go ahead.

**Glitch**: **RTTTV** asks, Anything that Quilt has done to make it possible for Forge mods to be loaded? The answer is, you�re asking for the wrong object. (Did I add an extra T? Oh well.) I also worked in the past on Patchwork, which was making Forge mods load on Fabric. That will be running on Quilt, but that will not be something first-party with Quilt. We won�t ever support loading other modloaders besides Fabric/Quilt officially.

**CheaterCodes**: Yes, and ~~compatibility with~~, Fabric is something that's gonna exists as long as we kind of benefit from it, because it would be quite hard eventually to support it. Most likely it would be an incredible burden to support Forge. But for a start, it's definitely stuff we want, but for Forge it�s just not feasible, the design is too different to have first-party support.

Alright, any more questions, keep them coming, w're running dry here. Otherwise, in the meantime, while we give you a few more minutes to answer, I�ll do a general call to check out PRs to review. QSL has a separate channel now for PRs that need reviewing. Quilt mappings always has PRs that it would be great if you looked at them, and if you would like to contribute to any other project, or even those projects as well, just pop into our Toolchain Discord, you�re already here, look into the corresponding channel, just leave a message there. If you�re brave, you can ping the team or a specific person you know, but generally if you just drop a message in there, someone will see it after a bit, and then we can talk about how you can help with the project.

**Glitch**: Just to jump in- We�re not scary. We would love people to come contribute. We have plenty to do. So you don�t need to take any kind of commitment to try and review a PR, or make some mappings, or write even an entirely new module for QSL. So if you�re interested, please just hop on Discord and ask us about it.

**CheaterCodes**: Alright, well, I think there�s no new questions, and I think there�s also no remaining answers that we have. Yep. So I guess it�s time to end this.Ah, last minute, last second question! I think this one is for **Glitch** again.

**Glitch**: OK, **Octal** asks, will Quilt�s mappings allow for layered mappings as well? Uh, yes, VanillaGradle will support layered mappings. I spent a lot of work trying to figure out the best way to support that, so it is definitely a priority to me for that to be working well.

**CheaterCodes**: Thank you. Yes, I mean it's kind of working already, I think?.

**Glitch**: Very kind of. The whole backend needs \[to be\] rewritten for like the 4th time.

**CheaterCodes**: Yes, there�s a lot of stuff about VanillaGradle that�s also not ideal for Chasm specifically, and for remapping input mods, that�s just how the system is. So the future of VanillaGradle is still a little bit uncertain right now. It�s a lot of work to do a big project like that, that's also somewhat intended to be used by other projects. But we�ll have to see how it goes.

Alright, **RTTTTTV** with another last-min question, asking: What code from Fabric still exists on Quilt? I think that again is still a bit of a multi-project question. Looking at it real quick, right now it�s Loom, so that�s probably going to change, hopefully going to change with the full release.

**Glitch**: Quilt Loader is a fork of Fabric Loader.

**CheaterCodes**: Yes, it�s a fork with parts completely swapped out, other parts basically completely intact.

**Aurora**: For QSL, you can see which stuff is Fabric. Go into the header, for each file there�s a nice big header, and it�s from Fabric, it will contain a line about the original ownership of Fabric for the code.

**CheaterCodes**: Does QSL use Fabric code specifically in Fabric API in QSL, I'm assuming?

**Aurora**: In Fabric API-QSL compatibility, it�s a fork of Fabric API, which re-implements some stuff using QSL instead. So yeah, of course it's uses Fabric code.

**CheaterCodes**: On mappings, it�s mostly Tiny stuff which we talked about last meeting, which we�re planning to hopefully yeet at some point, and I think that's all the Fabric code that I can see. Alright so, I�m going to end this here now, so any last-minute questions coming in now will not be looked at any more. Uh, thank you all for joining and listening in and for the devs to talk and for the Community Team to be around and manage stuff for us. 

As always, or most of the time, I�m going to invite you all to a quick after-party on the Development channel on the toolchain Discord, where we can just hang out a bit and chat a bit more, about possibly unrelated stuff as well. And I hope the new time is also something that's good for everyone. But yeah, we're going to meet each-other again in two weeks, same day, same time. Thank you very much.

**Emma**: Bye everyone.

**Aurora**: Bye bye.

**CheaterCodes**: Oh damn, why is it using the wrong microphone? There we go, now it's back to the right microphone.

**Oro**: Sounds so much better.