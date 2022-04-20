[Meeting: 13th Nov 2021](https://anchor.fm/quiltmc-dev-meetings/episodes/Meeting-13th-Nov-2021-e1au4rn)  
Our first public developer meeting - uploaded for your convenience! In all Quilt developer meetings, we start by asking all the development teams what they've been up to. After that, the community team talks a little about what's been going on, and then we accept questions!  
If you'd like to listen to our meetings live, or you have questions to submit, please feel free to join us - every two weeks, [on Discord](https://discord.quiltmc.org/).

=========================

**Gdude**: Hello and welcome to the QuiltMC Developer Meetings Podcast. The podcast that... isn’t really a podcast. If you’re new here, this is just a collection of recordings of each public Quilt Project Developer Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed from a Mumble server and recorded live by a fleet of Discord bots. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to [https://quiltmc.org](https://quiltmc.org).

=========================

ATTENDEES:
<<<<<<< HEAD

=======
>>>>>>> c4ec2460a190145883867aa3e49ded7b9c17bd29
- **Emmaffle**
- **ADudeCalledLeo**
- **Blodhgarm**
- **Fork**
- **LOCAL**
- **Gdude**
- **sciwhiz12**
- **OroArmor**
- **lenrik**
- **ENDERZOMBI102**
- **MVP**
- **burger**
- **Kroppeb**
- **arathain**
- **StrikerRocker**
- **jamalam**
- **AlexIIL**
- **CheaterCodes**
- **yitzy**
- **Lith/Heli**
- **Hubry**
- **IMS**
- **MartrixX**
- **Grondag**
- **Fish**
- **i509VCB**
- **LambdAurora**
- **Haven King**

=========================

<<<<<<< HEAD
**Gdude**: "**Instructions for attendees** If you're here to listen to the meeting, chat in here and ask questions, welcome! We're making use of an AMA system to make everyone's lives easier, so please follow these instructions. Firstly, wait for the meeting to start and for one of us to open the session. You'll see a message posted in this channel by @AMA when we're ready to take questions ing though do note that we'll be opening it before the developers will be answering them, to give you some time to collect your thoughts.  
**If you have a question:** Once the session has been opened, use `/ask` to submit a question. It'll be reviewed by the moderation team and, if approved, forwarded to the developers, who will be able to decide if and how they wish to answer it.  
**When the question is answered,** the @AMA bot will post an embed in here. If the question will be answered on the stage, the bot will say so as well. **If you're asking a question, make sure you're on the stage channel so you can get your answer!**. 
We currently have **no plans** to allow users to raise their hand to ask a question via voice. This may change in future, but we're keeping it simple for now. **Do not ping meeting participants with your questions,** they'll be ignored but do be specific about who your question is for when you submit it!  
Additionally, **don't spam the developers with questions** and, as always, **keep your questions appropriate and follow our rules and Code of Conduct.** We will take actions against users that send rule-breaking questions!  
=======
**Gdude**: "**Instructions for attendees**
If you're here to listen to the meeting, chat in here and ask questions, welcome! We're making use of an AMA system to make everyone's lives easier, so please follow these instructions.
Firstly, wait for the meeting to start and for one of us to open the session. You'll see a message posted in this channel by @AMA when we're ready to take questions ing though do note that we'll be opening it before the developers will be answering them, to give you some time to collect your thoughts.
**If you have a question:** Once the session has been opened, use `/ask` to submit a question. It'll be reviewed by the moderation team and, if approved, forwarded to the developers, who will be able to decide if and how they wish to answer it. 
**When the question is answered,** the @AMA bot will post an embed in here. If the question will be answered on the stage, the bot will say so as well. **If you're asking a question, make sure you're on the stage channel so you can get your answer!**
We currently have **no plans** to allow users to raise their hand to ask a question via voice. This may change in future, but we're keeping it simple for now.
**Do not ping meeting participants with your questions,** they'll be ignored but do be specific about who your question is for when you submit it!
Additionally, **don't spam the developers with questions** and, as always, **keep your questions appropriate and follow our rules and Code of Conduct.** We will take actions against users that send rule-breaking questions!
>>>>>>> c4ec2460a190145883867aa3e49ded7b9c17bd29
We're hoping for a smooth session, but bear in mind that most of us haven't run a stage like this before. Especially for the first couple of session, we'll still be getting used to the system- so be nice!"

=========================

**Gdude**: Alright, we can get started. Uh, let me look at my list here. Can we start with CHASM?

**CheaterCodes**: Oh!! Yes, I was going to do it a little bit quick.

**Gdude**: You go right ahead.

**CheaterCodes**: OK, well, first of all, thanks everyone for coming. CHASM, I've been working a little bit on it. We have a lot of stuff planned out, and for the last few weeks I have been chopping away at it. I've not put too much priority on it because we still need Quilt Build Tools, and Build Tools are more important. But looking at it now, it's very well-thought out. Ordering becomes super simple because we already talked about everything for like hours or days. So I just wanted to say that, maybe don't expect it for Beta release or anything. But it's happening for sure, and I can't wait for other stuff to be done so that I'll have time for it.

**Gdude**: Yeah, it's very much a slow-burn project, but I guess we saw that coming, right?

**CheaterCodes**: Yeah, it's really just a priority thing. We really need Build Tools, and we need the Hashed Mojmap, and we really need Mappings, and we really need everything else, then we can talk about CHASM again.

**Gdude**: Yeah, that makes a lot of sense. OK, that sounds good. **Kroppeb**, would you like to talk about Decompilers for a bit?

**Kroppeb**: Uh, yeah sure. So most important news about the Decompilers probably that Quiltflower 1.6.0 has been released. On the Github I think there's a bigger changelog. It's quite big, so I'm going to go over it in a minute by itself. But we are still working on more improvement for the future versions. Including switch expressions which currently don't really decompile well. But also generic improvements. ~~Assets~~ are one of them, major decompiler issues, as well as ~~recompiler-based issues~~. Uh, we're also fixing general ~~issues there~~. We're also trying to to get ~~moments of deployment~~. There's still a lot of stuff we need to do, but yeah.

**Gdude**: Well, good. It's great to see a new release coming out, especially with your work and everyone else on the Decompilers Team. From what I've seen, it's a really fantastic project, honestly. And it's great to see the community support come out, like Gradle plugins for it. **OroArmor**, would you like to talk about what the Infrastructure Team has been up to? I know it's not the time.

**OroArmor**: Yeah, so I'm technically not on the Infrastructure Team, but I noticed that a lot of the Quilt projects use the launcher metadata that Mojang provides. And they all parsed it in slightly different ways, and use it differently. One thing that I did was I consolidated that so that it was in kind of one library that encompassed all the data that could be introduced. And that way, when whatever project Quilt works on it the future, instead of having to re-write all the parsing for the launcher metadata, we could just use this library. That would make it a lot easier. Just speed up development, and just kind of test things when we need to. It's also public, so if anyone has a project that also parses this launcher metadata, they can use it. So it was just kind of a way to take a lot of common code and consolidate it.

**Gdude**: OK, that sounds like good progress for ~~Gravis~~, good stuff. Yeah, if **Haven King** was here, I think we could chat a bit more about Infrastructure. But he's just not, so we'll see if he appears later. In the meantime, **AlexIIL**, would you like to chat about Quilt Loader?

**AlexIIL**: Sure. So, things I had previously that are really important is that `quilt.mod.json` is done. I improved it. So people could write mods that use `quilt.mod.json`, so they'll appear as Quilt mods rather than as Fabric mods to Quilt Loader. As for new things, we've deprecated Fabric's metadata and added Quilt's, so most of the time mods will now be importing `org.quiltmc.loader.api` instead of Fabric when using Loader. Most usefully, we've added Quilt entrypoints, and these include the ModContainer as an argument, which means you don't have to use- Well, you don't have to grab them from Quilt loader and check to see to make sure that your mod is null, because that's a bit annoying, but yeah...

**Gdude**: OK, sounds like good progress so far, at least.

**AlexIIL**: Uh, I'm not quite finished, there's a bit more. Um, Quilt Loader is now- Quilt Loader only has static methods rather than having to use `FabricLoader.getInstance()`, you can now just use `QuiltLoader.getMods()` or any of the other methods there directly, which makes it a little bit easier to use. Although we've moved Minecraft-specific methods to Minecraft Quilt Loader, because we're working towards moving away from having Minecraft as a core part of Loader. Because Quilt Loader is meant to be use- Or possibly meant to be used by other games, we don't want to like hard-code Minecraft everywhere. So a few Minecraft-specific things in the new Minecraft-specific parts.

The other thing, the second thing is that I've started work on Loader plugins. So these are going to be very useful for loading mods for completely different loaders. So for example there's currently a hacky Liteloader loading mods, and that will have to be re-written in sort of a more compatible way, I guess. A less hacky way, which would be useful. Eventually, this is the sort of thing that would lead to library- and mod-downloading, but that hasn't started yet. Hopefully like automatic mod-updating plugins. Not from Quilt itself, but it should be possible to make them. That's about it for Quilt loader, I think.

**Gdude**: OK, sounds good. Alright, Mappings looks like we have **OroArmor** again. What's going on with Mappings?

**OroArmor**: Uh, I think there's a couple questions that just got asked about Quilt Loader.

**Gdude**: We can do those now, or we can do those at the end. I think it's probably better we do those at the end just to make sure we're not going over time.

**OroArmor**: Alright, mappings, let's see, yeah. It's going along well. We are currently trying to get- We're trying to get Hashed Mojmap to generate automatically when the snapshots come out, so that's nice. **CheaterCodes** will talk a little bit more about the technology of Hashed Mojmap. Yeah, Mappings, we've been updating, taking in PRs. Um, there wasn't anything big for 1.18pre1, but we had a lot of mappings get added in right before 21w44a. We have a PRs, porting commits coming over from Yarn, we're going to review those. Other than that, technology-wise, I finished a complete- Well, not a complete re-write, but like a 70% re-write of the Quilt Mappings build script. It used to be 1000 lines of Groovy, and I churned that into 300 lines of Groovy and 1300 lines of Java code. But this makes it a lot more expandable and easy to use, because the mappings were really painful to work with.

**MartrixX** joined the Mappings Team, I think sometime in the past two weeks, I don't remember exactly when. Yeah, last week. **MartrixX** has been working on a bunch of other stuff, just kind of of around mappings. He's done a bunch of work in Enigma. I think he had some filament stuff that fixed some issues with package infos.

He also started a new project called Draughtsman, and this project strips all the code from methods and fields and stuff like that. Unless the fields are constants, or kind of like "i - 3". And what that will be used for is to re-writing how Quilt Mappings generates it source. Because currently it goes through like 3 different hoops of generating actual Java source code instead of just running a decompiler on some stuff that's really simple to decompile. And with the improvement in Quilt file and everything, we figured there's an easier and faster solution-

**Gdude**: Alright, that sounds like quite a lot of progress has been made there.

**OroArmor**: **CheaterCodes**, do you want to talk about what Hashed Mojmap has been doing in the past couple of weeks.

**CheaterCodes**: Hashed Mojmap has seen a lot of development over the last few weeks. Luckily, or unfortunate, most of that has been reverted. But we are about to stabilise Hashed Mojmap, which is very important. Because we've always said, Hashed Mojmap has to be stable. We can't have Hashed Mojmap change mid-version or something, it just doesn't work. But we have a Hashed Mojmap that seems to be stable right now. I've opened an RFC and I please ask everyone to review it and please tell us now if they see any issues. Because if that RFC gets merged, and it's still not stable, then we might run into trouble later. So once the RFC is merged, I'll stabilise Hashed Mojmap by putting it under release Maven. And that should then be completely usable for developers as well. So I'm just going to mark the one question as well, where was it? There. So yeah, it's soonTM. It is usable now, but once the RFC is through, and once I test it once again with the entire toolchain, see if there's any issues, once it works, it's going to go into the release Maven, and then it's definitely usable. Hopefully this will happen within the next two weeks, until our next meeting.

**Gdude**: It's exciting stuff to hear, I have to say.

**CheaterCodes**: At least something stable is here now.

**Gdude**: OK, **OroArmor**, would you like to talk on QSL?

**OroArmor**: Yeah, I just very recently joined the QSL Team so I don't have very much to say, but uh, QSL has beening There's a lot of PRs for QSL. If you feel like reviewing them, please go and review them, that would be great. If you want to write some code for QSL, open up a PR importing a Fabric module or something like that, that would also be great. Right now QSL's at the point where it neds more development because there is a lot of code that neds to be written for it. And somebody neds to write that code. So reviewing that helps us because we need more eyes on code, and creating PRs also helps us because the QSL Team is not large enough to import everything from FAPI.

**Gdude**: Alrighty, I lost my list. There it is. Alright, that all sounds good. It would be great to get more eyes on things.

**OroArmor**: Yeah, **ADudeCalledLeo** also just said "review networking so **i509VCB** merges it already please". Yes, please do this.

**Gdude**: Uh, which PR is that?

**OroArmor**: I'll pull it up. It is [PR #34](https://github.com/QuiltMC/quiltingstandardinglibraries/pull/34)

**Gdude**: Thanks **ADudeCalledLeo**. Perfect, perfect. So while we are on that, if you care about this part of the API, then please get some reviews in, even if you're not part of the team. We really could use the input. Alrighty, I think that covers all of the develop teams, unless any of you has anything else to add? Nope, sounds good.

I'll just chime in a little bit on the Community Team as is tradition. Not a whole ton of things that have been happening. Of course we've gained a new staff member, **Emmaffle**, who you might know from the Modrinth moderation and ~~File~~ moderation teams. She just joined a couple days ago, she's doing great. Hopefully you guys will get along with her as well. We've also been doing some work on Cozy, as usual. Specifically I went to clean up the suggestions database. Turns out Cozy was submitting suggestions to itself, somehow. Think I fixed that one. But it was pretty funny, I have to say.

And of course, we have the new statistics interface. If anyone likes graphs as much as I do, you can head over to the `#stats` page and get a little bit of information on what's going on on both the servers. I'll link that in the channel now, [here it is](http://statsingquilt.gserv.me/public/dashboard/9b181b97ingbd7fing4ab0ing87eding3239f9149932)

(**Emmaffle**: "can also be accessed with `!stats` on either community or toolchain")

But again, there's not too much to talk about on the community side. A lot of things have been happening quietly, or they're collaborate-related things, so we don't tend to talk too heavily about them. Although it might be worth menting that we have grown the ~~community callout efforts~~ quite a bit. They were just a couple channels on the community server previously, but we've split that off into another server, and there's over twice the number of people there now, which is nice. So things are going well community-wise. Though of course we've still got a lot to do. I think what I'm going to do next is go through all the open suggestion and make sure they're all addressed and put into the issue tracker at the very least. But should be there soon, hopefully.

Alright, so since all the teams have gone through what they wanted to talk about, we will open the floor for questions. Some of them have already been answered. Generally I would say we'll go top-down as they are. But if you have any questions you want to submit, use the `/ask` command, the slash command. And we will go through those shortly. You can put in whatever questions you like. People won't necessarily answer them, we do vet them. But yeah, go ahead. Just don't, you know, spam the hell out of it.

**CheaterCodes**: ~~??????~~ Whoops, interesting. Well, just post and answer it again because it's the first question in the list.

**Gdude**: Yeah, if you click the button again, it will send it again.

(**IMS**: First question: When is it estimated that Hashed Mojmap will be useable for developers?")

**CheaterCodes**: I will say- Yeah, I noticed- I would say after the RFC is merged. And that means hopefully in the next two weeks. **Gdude**, you take the next one?

**Gdude**: Yeah, I will take that one. I'm going to read the question out just for the sake of the recording. **sciwhiz12**: "Is there or will there be a canonical list of Quilt developers (particularly those who have qualified for and hold the Quilt Developer role in the Toolchain server)? In addition, will there be a same list for the whole Quilt team (Admin Board, Community Team, and the technical side) on the website?"

Yes, there are plans for that. Originally we were going to put it there on the website. The website is largely maintained by **Fork** who is really busy at the moment, and also disagrees with my web design style, so we'll see what hppns. But we definitely do have plans to have an actual list up there so everyone knows who's responsible for everything. And keeping that relatively up-to-date shouldn't be a huge problem either, hopefully. But yes, we are planning on that.

**OroArmor**: Right, I can also take this one from **burger**. I'll also read it out loud. **burger** asks, "How does the Mappings Team feel about the potential effects Quilt Mappings could have on loader unity (vs using Mojmap)? This doesn't apply to Hashed or Intermediary, only Quilt Mappings"

So, while loaders are moving towards using Mojmap, Fabric still uses Yarn, so assuming that loaders are 100% moving to Mojmap is not correct. But I do know that a lot of projects are considering moving to Mojmap to promote cross-loader unity. Such as- I know Canvas has, Iris I think partially has, Caffeine is considering it. Yes, Blaze40 has.

Now I know a lot of other projects have started moving towards Mojmap just for cross-loader unity, and I think that's something that Quilt Mappings could try to solve. We could try to figure out how to use our mappings on ForgeGradle or something like that. What Quilt Mappings is, is that while Mojmap is complete, it often has really bad names. Like `ResourceLocation` or `Myth` for `MapHelper`, comparatively.

And that Quilt Mappings aims to provide accurate, understandable names compared to Mojmap's names. Because when it comes down to it, Mojmap's names are there for the developers of Mojang, who can talk about them amongst themselves. And they're not focused on creating, you know, a modding API, or good names. Whereas Quilt Mappings has the focus of creating good names, and focusing on, "OK, what does this do, and why is this a good name?" Versus "OK, this name has been around since like pre-Alpha, and we haven't touched it since then."

**CheaterCodes**: I just want to add something to this question just for clarification as well. Because the question asked how it affects the loader unity. And the answer is that it doesn't apply to Hashed Mojmap to begin with.

I just want to clarify this because loader does not care about Quilt Mappings. It's important to note that the actual mappings are only in the develop environment. Once you publish your mod via JAR it's in the Hashed Mojmap anyway. Or Intermediary for Fabric. Or I think Sponge just does straight up Mojmap now. So in terms of loader unity, it's really not about Quilt Mappings, it's about using Hashed Mojmap. Which is an entirely different question. In terms of using [a] development environment, I'm not sure if Loom has the capability yet, maybe.

But I think that definitely something we want to have is to allow you to use Hashed Mojmap during development. If you choose, so if that is what you want. Or you can use Yarn if you want. I don't think we have any real reason to not allow it. Just to clarify more about this one.

**Gdude**: Alright, thanks for that. I guess I'll take the next one then. Here we go.

**Kroppeb** is asking when RFC #38 will be merged.
(**Kroppeb**: "RFC 38 has been in Final Comment with no comments for over a month. When can we expect it to be merged?")

Generally speaking, the Admin Team is in charge of ultimately merging RFCs, so we do have a review process. The admins have all been extremely busy, unfortunately. But we can certainly ping them on that and maybe see if they can take a look at it. But I think it might be a little longer than some people might be expecting.

I'll take this one from **yitzy**, no one's claimed that one before. OK **yitzy**, this is a good question. **yitzy** is asking, "Is there any idea of having some community input on collaboration? There aren't many mod teams as open as quilt who might not be trusted to the same extent."

It's tricky, it's tricky. The problem with being super-duper transparent about collaborate is generally- Well for example, I've been targeted by people that have been unhappy with collaborate existing. I got doxx'd a few weeks ago. And while we've dealt with it and it's fine, it's kind of important that we end up protecting the people that are part of collab. Though I think on balance, absolute transparency is not unlikely to happen. That said, if anything is going to affect a user like you on Quilt, I'm still going to let you know about it. But I don't think we're going to go supe in-depth onto what's happening in specifics on collab. But yeah, it's a good question. It's a tricky balance to make for us, unfortunate. But you got to do what you got to do, really.

**CheaterCodes**: Um, I think I just want to answer this question, even though I don't have a proper answer for it. The question by **StrikerRocker** is, "How will the official release of Quilt as a whole including QSL be determined?"

The problem that we have right now is that we have a lot of things we want to do. We want to replace Loom. Loader neds some plugins. QSL, we're still unsure on how much of it is going to be a wrapper around FAPI and how much is going to be new stuff. The answer to that question is really we don't know what an official release of Quilt would require. So yeah, I think for now that's the answer to the question unless someone else has a better answer to that. Cool

**Gdude**: Alright, sounds good.

**AlexIIL**: I'm just answering the question from **jamalam**: "I forgot, can Quilt loader load mods with `fabric.mod.json` as well?"

Yes, this has always been the case. This has always been possible. We're just going to move Fabric mod loading over to a plugin, rather than being directly in Quilt. But that won't affect how people use it. You're still going to always be able to use Fabric mods on Quilt Loader.

**OroArmor**: Alright, I got 2. First one from **Emmaffle**: "How many mapping changes from Yarn end up getting into Quilt Mappings? Is there any synchronise system between Yarn and Quilt Mappings, and if not, is it at all planned?"

No hard synchronise system. What we have is tools that can convert the git patch files between Intermediary and Hashed Mojmap. And that allows us to pull over- if there are really big or important changes we want to pull over from Yarn, or that we want flat-out, we can do that. But most of the stuff has still been in-house development.

And the reason is that right now Yarn has slightly more collaborators. But we're quickly growing, and I think we'll soon be able to outpace Yarn with collaborators and new mappings. And that will be pretty good. I've just been busy, so I haven't been able to make any PRs. But I know that **MartrixX** has been making a bunch, and that's been really helpful. And so people- So we're starting to get the ball rolling, but with any new project it takes a while. So we're just keeping up with Yarn for a little bit just because it helps a little bit more with that development.

And then this next question from **Blodhgarm**, sorry if I pronounced your name wrong: "Will Quilt Mappings be usable with Forge? (Sorry if it is a stupid question)"

That I can't say. It can definitely be used with ForgeLoom which would then be able to compile to Forge. But then I don't know if it would then work in ForgeGradle. But that would be something that could be explored.

**Gdude**: Sounds good. Looks like I've got one I can answer here. **sciwhiz12** is mostly asking about substantial changes to RFCs and how that should work.

(**sciwhiz12**: "For substantial changes to existing RFCs, should they remain as amendments or be proposed as new RFCs? In the latter case, should the new RFC partially supersede the new RFC (adding new clauses or removing existing ones), or should the new RFC fully supersede the existing RFC (so the existing RFC has no more effect)?")

It's a tricky question to a point. It depends honestly. So far honestly, we've kind of been avoiding using the amendment process for some things. Like with the Community Team RFC, at least one of the things we did was re-write several of the processs there. And at first I was going to do an amendment process there, but we had a chat and basically it's much easier to follow things if you update the original RFC. I don't think there's really a problem with that, especially considering we do have the commit history there. I guess there are probably things where you might want an amendment, but nothing really comes to mind at the moment. It's not so much that a new RFC supersedes it. You're update the original one. But you're still keeping the history there in the commit history. So I think that works OK, at least so far. But if that neds to change, certainly it's something we can look at.

**CheaterCodes**: I'll take the versioning one as well, because I think it's an iteration of the last one. So the question by **sciwhiz12** is, "What versioning scheme will or are Quilt's project use? 0-based versioning, or semantic versioning, or other? And is it or will it be different per project, depending on the will of its maintainers?"

I think the last one is in general most likely. However, I do know that most in Quilt said that they don't really like 0-based versioning, so I think for most stuff it's going to be some sort of semantic versioning (T/N: semver). Like for example Hashed Mojmap, I'm going to switch it to 1.0 release as soon as the RFC is merged. And then there's some stuff with Quilt Mappings that can't really be semver'd, so in general Minecraft-related stuff that depends on the Minecraft version can't really be semver'd because Minecraft doesn't have numbers, so no promises on the exact format. But in general, don't expect 0-based versioning I think.

So I'll also claim the next one, so let's keep going with that. **Fish** asks, "Will there be noticeable differences between Quilt and Fabric? Does Quilt have technology that would be impossible to port to Fabric?"

First, I want to answer the second part. No, of course not. Quilt was ported from Fabric. Quilt is a port of Fabric. Fabric could just easily get back everything if they wanted to. But at that point, Fabric becomes Quilt. 
But in general, will there be noticeable differences between Quilt and Fabric? Yes, for sure. First off, the default stuff. So, using Hashed Mojmap and Intermediary instead of Intermediary. Of course Fabric could switch over at some point if they really wanted to, but I don't think that's super likely. The other big different is Quiltflower, but I heard that it might come over to Fabric soonTM, maybe. I think no promises. Then of course, CHASM doesn't exist yet on Quilt. That might happen on Fabric but that one I think is not as likely because it would require quite a few changes to Loom, which we're going to make. But unless Fabric just literally takes our new Build Tools, they're not going to get CHASM any time soon.

Um, what was the last one? I had one more. I forgot one, I had one more in my head. Oh yes, loader plugins, exactly. Loader plugins are something that's going to be different. If you are wondering what loader plugins *are*, that's kind of a different question. But one of the things that's important to us is to automatically download QSL if it's required so we don't have users spamming with "I installed Fabric but now it's telling me that Fabric is missing."

So I think those are a few differences that should be noticeable. Of course they could be ported but I don't expect them to.

**Gdude**: Alrighty. **LambdAurora**, are you OK to take the next one?

(**yitzy**: "Fabric is somewhat lacking in terms of events, especially world interaction ones, such as a lack of a block place event or screen handler events. Does QSL plan on addressing this, and if so, how far would these interaction events go?")

**LambdAurora**: So, for QSL and events, the goal is to be a standard library, so it should have a lot of events to bring everything together. And so a block place event or screen handler events are, at least for me, very essential for bringing mods together and for interacting. So interactions of events are really important, so you should expect seing them in QSL. But when, that cannot be said because it all depend on what events we will get. But we do want those and we don't want to bikeshed about them too much either because they're important. I think that's it. Oh, I can take the next question.

(**Hubry**: "Has a potential Datagen API been looked into? Having easy access to generating JSONs is very useful, but on Fabric it has been a pretty annoying process to set it up, compared to Forge's default inclusion")

So, datagen will be definitely looked into. Because to make big mods would be a pain to do without datagen, that's for sure. Even Mojang uses datagen, so we have to use datagen. I don't know yet how, maybe we will try to use Mojang datagen system, or maybe we'll make our own. Currently that's not set in stone. There's also plans for runtime datagen. But that's not really datagen-ing JSON. That's more like making mod interactions easier. Like if you have a mod that adds a new wood type, you'd want stuff to be generated for that wood type too in your mod. Like if you add a new item, that's also planned. But as I said, it's not really- For now, the implementation is a no. So we'll see in future. And I think that's it for now.

**Gdude**: Alright, thanks for that **LambdAurora**. I'll take **sciwhiz12**'s one, I think. So **sciwhiz12** is asking wheher the final votes for technical decisions will be made public.

(**sciwhiz12**: "Will the final tallies of votes for technical decision (for example, the proposed PR policy's conflict resolution through a team vote) be publicly released alongside the final decision, as part of policy? (I presume the names of those who voted for/against will not be included)")

It's a good question. This isn't one that anyone that any of us can really answer without someone from the Admin Board around. Regarding RFCs, you'll see those on the RFC PR. Like, the discussion is there, the reviews are there. You can see what people thought of them. For other types of votes, it's hard to say. It's largely going to depend on where they happen. For example, so if something happens on Github, it's probably going to be through reactions. Maybe it's not, a lot of this really depends on how the admins want to run that. Unfortunate none of them are at the meeting this time. Maybe they'll be at the next one, so you can ask it again.

**CheaterCodes**: I think also to add onto this, I don't think it has really happened yet. I think there was one poll so far that was basically a naming question. But I don't think there's been any big ones yet, so...

Yeah, I'll answer the next one by **LOCAL** even though it's a little bit hard to answer. The question was, "What major roadblocks remain to QML's public release?"
I'll preface this with some minimal (sic) viable product as **Gdude** calls it. And that requires at least Quilt Loader, which we did kind of requires loader plugins. So a lot of plugins need to happen. We need Build Tools; we have a version of Loom that might kind of be good enough for like a Beta release, but we might want to switch over to VanillaGradle or something. So, I'd say right now we're mostly looking at geting some, not release version, but some beta version of QML out, which is useable. Maybe not everything is stable.

For the actual release, it's just unclear what we want to have for an actual release. Do we want CHASM if we just do Beta now? Maybe we just want CHASM for release. Do we want a new Build Tools, like a new integration with Gradle or something? It's just unlikely, unfortunate. But for a usable Beta release, what we need is Build Tools that are kind of working, and Quilt Loader that is kind of working. But yeah, I think that's it. Oh do we count the next one as well as part of the same question?

(T/N: A **[minimum viable product** (**MVP**)]([Minimum viable product ing Wikipedia](https://en.wikipedia.org/wiki/Minimumedviabledproduct)) is a version of a product with just enough features to be usable by early customers who can then provide fedback for future product development.)

**Gdude**: Yeah I think that was part of the same question, really. **Fish** asked if there's a roadmap and if there's a rough ETA.

(**Fish**: "This question was probably answered earlier, any roadmap for Quilt?")

It's basically exactly what was just talked about. For an ETA, I don't believe we're committing to anything. We were originally aiming tentatively for an alpha version for MC 1.18. It's coming a bit sooner than we thought it would. That said, who knows, we'll have to see what hppns. But we're not committing to any specific release time at the moment.

I can take this one. **LambdAurora** asks if there's anything new on the idea of forums.

(**LambdAurora**: "Anything new on forums? :pineapple:")

No, not really. We did chat on what we'd use. It's probably going to be Discourse. But otherwise we need to wait on **Haven King** who is doing most of the infrastructure work. While I could stand up a forum on my own, on my own server, it's really not ideal at all. We should set it up on proper Quilt infrastructure, and we need **Haven King** for that. That said, I think he was not planning on looking into it until we're close to release? It's hard to say whether he thinks we're close enough at this point or not. But again, it's something we'd have to ask about once the administrators are here.

Hehe, **LambdAurora** goes, "*Oh*." (*Long pause and brief remark by **CheaterCodes**.*) I'll take this, I might as well.

(**Fish**: "Does Quilt have a roadmap, where would it currently be at, and is there a rough estimated time of arrival for the mod loader?"

**Fish**: "To add on to my previous question, is there a publicly viewable roadmap, like Trello, which is a clear roadmap to where Quilt is potentially at right now?")

We don't have any specific codified roadmap up at the moment. It's not a bad idea, it's not a bad idea. Right now, I would recommend looking at Github and just seing what's going on there. It's kind of difficult to get a complete roadmap written up at this early stage.

(**LambdAurora**: "There's this? [Launch Roadmap · GitHub](https://github.com/orgs/QuiltMC/projects/1)")

**Gdude**: Yeah, there is that project, I don't think it's public, I'm not sure. Again, that's something we'll have to ask the administrators about. Is it public, did they make it public? Finally. Um, let me have a quick look at that. Oh yeah, that's right. Oh well, there's your answer I guess, hahahaha. But it hasn't updated for a while. Yeah, it probably is a bit out-of-date. I think we'll probably want to talk to the administrators on that one. But I believe the other teams have access to touch that. So if they want to update it a bit, that'll be great as well.

OK, I'll take that one. Alright **arathain**. **arathain** is asking about Quilt merch.

(**arathain**: "I saw "Quilt merch" be addressed once, I think it's reasonable to leave any of that for post-release; anyway, what's "the official stance" on it? What could it entail?")

The official stance is, we don't know. Realistically, we're trying to keep money out of the org as much as we can. Now, while we've talked about this with the admins, largely it's a case of **Haven King** is paying for everything that mostly neds to be paid for. There's other people contributing a little bit for domains and stuff. But right now we don't really have any plans to go further with that.

After Quilt's release, we'll probably look into something like an Open Collective just to make sure that we can get all the infrastructure paid for without draining **Haven King**'s beer money. But I don't think we're going to go super hard in on that, since we really don't want to start turning this into a for-profit endeavour, at all. Oh, that's a good question in from **jamalam**, thank you **jamalam**.

(**jamalam**: "Any updates on whether there'll be a way to support Quilt financially (i.e. to help with infrastructure costs)")

**sciwhiz12** asked if the Quilt Administrator Board is locked to 3 board members.

(**sciwhiz12**: "Is the Quilt Administrative Board locked to 3 board members? The Governance RFC provides that nominations are open when there are less than 3 members, yet does not give any indication to my understanding for the possibility of more than 3 members on the board.")

From recollection on the Initiative Server, which is basically where all the initial planning happened, we wanted to have at least 3 admins. I'm not 100% familiar behind the process of electing a new administrator, but I think 3 was decided as just a good number at the time. It might be worth re-visiting that and just to clarify it. But I don't think that there's a big issue there.

Uh, I guess I can take on this?

**CheaterCodes**: Alright, I'll just take this one, take the first one. **Lith/Heli** is asking, "Any updates on using FREX inside QSL?"

I'm not sure if that's referencing directly to the conversation that was had, but there was a conversation that was had with **Grondag** talking about it. IDK anything else. I'll look if I quickly can find it, it shouldn't be that hard. And then I'll just link to it and then you can look at it.

**Gdude**: While you're looking for that, **LOCAL** mented an odd number of administrators is important.
Yes it is. We wanted to make sure that things couldn't be too stacked by two people. But also, we need them for tiebreakers. So if we had an even number of admins, that wouldn't really work very well. Oh, you found it?

**CheaterCodes**: Yep.

**Gdude**: Alright, I guess I'll try and address **burger**'s question. It's not an easy one for sure. **burger** asks, "It seems like many people working on Quilt are busy or can't focus on Quilt in full. From the outside, contributing to quilt or joining the team seems like a large commitment which may dissuade potential new members from joining. Any thoughts?"
I think that's a bit of a contradiction. Yes, a lot of people are busy and ~~hv focus~~. But we don't require that of people, like everyone has a life that they have to be living outside of Quilt. And it's important to us that they're allowed to do that. So while yes, people are going to be busy, that's just how it is. I think that it's still a fair concern. Ultimately though, being on a team is a relatively chill affair. We're not going to be complaining if you're not giving as much time as we think you could or anything. It's really just a case of giving what you can. We're not going to yell at you for it.

**CheaterCodes**: Yeah, no one's complaining if you're joining a team and then not working on it, heh. Honestly, if you just join the Build Tools Teams, we're already happy.

(**Gdude** and **OroArmor** laugh.)

**CheaterCodes**: If anyone wants to work on Gradle, just say it. Even if it's just a single line in a build script, that's cool. I think that one's for the Community Team.

**Gdude**: Yeah, that's definitely for us. **yitzy** asked about a showcase or starboard.

(**yitzy**: "Was there a plan for showcasing underused or just generally cool mods or a starboard?")

We do have plans for a sort of a mod showcase. After Quilt releases obviously we want to make use of the site more, and use the blog for more community-reled things. Nothing super-detailed right now of course, because it's pre-release, but yes, we do have plans. As for starboards, not really. There are suggestion open about a starboard. But I have concerns about how it might be used and how we might moderate it on top of everything else. Although assuming we get more moderators, maybe it'll happen. It's hard to say for sure. But yes, we'll definitely be doing some sort of a mod showcase thing on the website, but then that's something we planned since like the absolute beginning. That's right, Emmy (**Emmaffle**), you do have experience with that.

(**Emmaffle**: "I mean I am the person who writes the mod showcase blogs for modrinth \uD83D\uDC40",)

**Gdude**: It looks like that we've come to the end of the question queue, I believe. Yep, so if anyone has any other questions to put in. We have maybe about 10 minutes left, at least on our predicted schedule. If not, then that's cool too.

(**Fish**: "I asked a question earlier")

**Gdude**: Yeah, yeah, you did. Did you ask a question about prime numbers? It seemed a bit off-topic, really. Uh, if you really need an answer, no. Uh, this is a really good question. So do I take this one, or which one of you would rather? Alright, I'll take it then.

(**sciwhiz12**: "What's the current bus factor for Quilt?")

Alright, the bus factor for Quilt. It's actually really a surprisingly good question. For those of you that don't know what that means, it's basically the number of people that would need to be hit by a bus to prevent the project from continuing. Right now, for most of Quilt, it's not that low. It's certainty more than 1, which you know, you think Fabric has like a bus factor of 2? The whole point of having distributed teams the way we do - at least that's one of the reasons - is to make sure that's not really a problem.

**Haven King**, we are working on. When he's here next and when he is busy at the moment, we are going to work on distributing credentials for the infrastructure to just a couple of us who have experience with that. Not sure who exactly it's going to be yet. But yet, we definitely don't want to to have a super-low bus factor here. Haha, **burger**, I'm afraid that **Haven King** is not a burger. But I'm not particularly worried right now. I think, again, we really need to get a couple more people doing what **Haven King** is doing. But that's not an issue, he just neds to be not busy and hand those credentials and we'll sort that out pretty easily.

We still have time for a couple more questions if anyone has any. Right, here's one, haha. **lenrik**, really? "Is **Haven King** a cake?" I can confirm that **Haven King** is inded a Black Forest Gateau.

**CheaterCodes**: OK, I think I have a question I can ask in voice. "Oh man, this dev team seems really nice and I have so many of these questions to ask. Can I ask them later as well?"

**Gdude**: Yeah, of course, we're always happy to take questions. The AmA will be closed after we're done with the meeting. But you're always welcome to ask any of the questions you might have in the relevant channels. Or save them for next time.

**CheaterCodes**: Yes, please, hang around. This is called the Toolchain Server, but not the Toolchain Development Server. Anyone's free to hang around and ask questions here. In fact, most likely I will hang out in some other voice chat after this meeting as well.

**Gdude**: Absolutely, absolutely.

I'll take this one from **burger**, and I think we're going to finish up on this AmA after this one since we're running out of time. So **burger** asks, "who has the "nuclear codes" for everything? does one person have the ability to delete quilt?"

Well, it's a complex question. No one person, really. For the community stuff, mostly the Discord servers at the moment, **kashike** is the keyholder. He's there basically to prevent anyone on the Community Team or the Admin Team from pushing ahead with their own agenda. If you don't know him, Owl, he's a very well-known, very respected member of the wider modding community. He has no direct interest in Quilt, that's why he's in the position.

As for the projects themselves, Github Permissions suck, is all I can say. Technically speaking, all of the administrators have access to mess up the repositories. There's nothing that can be done about that, unfortunate. That's why you have to be careful about electing admins, right? We do also enforce 2FAs, so I'm not worried about them losing their accounts or anything like that.

**AlexIIL**: **ENDERZOMBI102** asked whether it would be possible to have more mods in a single JAR, but not using Jar-in-Jar system.

(**ENDERZOMBI102**: "Will it be possible to have more mods in a single jar? not like multiple jijs, but most like "optional" or "child" mods, or is JIJ just better?")

This is something that Loader Team has sort of thought about a little bit before. We haven't sort of looked into it yet, but this is something that someone would have to create like either a proper RFC for, or just an issue and we'd need to discuss it later. So basically, not yet, but it might happen in future.

**Gdude**: Alright, I think we're going to call it an evening at this point. Thanks for coming everybody, especially the people who answered questions and generally had a chat with us on here. And of course the people who asked them, because we certainty need them. We'll be doing this again in 2 weeks, same time, same place. We're planning on continuing this as long as we can, really. Yes, evening, it is evening, trust me. I'll leave the `#meeting-chat` channel open a little bit more, in case people want to catch up. And I'll also leave a recording posted in the `#schedule` channel. If someone has time, we'll do a transcript. Absolutely cannot guarantee anything. We're relatively busy with what we're doing, but we'll see. So I think that about covers everything for now. Thanks for coming everybody, we'll catch you in 2 weeks.
