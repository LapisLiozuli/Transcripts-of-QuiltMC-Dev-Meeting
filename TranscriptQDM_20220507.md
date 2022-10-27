[07/05/2022: I Am the Perfect Stand-In](https://anchor.fm/quiltmc-dev-meetings/episodes/07052022-I-Am-the-Perfect-Stand-In-e1irmi4)  
In this episode, the teams discuss Build Tools, Decompilers, Mappings, QSL, and Quilted Fabric API, as well as Dev Meetings v3, sponsorships, and a brand-new community space.  
[https://quiltmc.org](https://quiltmc.org/)  
[QuiltMC on GitHub](https://github.com/QuiltMC)  
[Quilt Community Discord](https://discord.quiltmc.org/)  
[Quilt Toolchain Discord](https://discord.quiltmc.org/toolchain)  
[Quilt Forum](https://forum.quiltmc.org/)  
[Quilt Openings](https://quiltmc.org/openings)  
[RFC 54: Quilt Kotlin Team](https://github.com/QuiltMC/rfcs/pull/54)  
[Craig](https://craig.chat/)  
[Whose Line is it Anyway? (Gdude’s reference)](https://en.wikipedia.org/wiki/Whose_Line_Is_It_Anyway%3F_(American_TV_series))  
[Quilt Loom on GitHub](https://github.com/QuiltMC/quilt-loom)  
[Quilt Loom PR 11: Metadata priority](https://github.com/QuiltMC/quilt-loom/pull/11)  
[Cozy Discord Bot on GitHub](https://github.com/QuiltMC/cozy-discord)  
[Quiltflower on GitHub](https://github.com/QuiltMC/quiltflower)  
[Quiltflower 1.8.1](https://github.com/QuiltMC/quiltflower/releases/tag/1.8.1)  
[Quiltflower on r/java (Reddit)](https://www.reddit.com/r/java/comments/ue8u59/new_open_source_java_decompiler/)  
[Good First Quiltflower issues](https://github.com/QuiltMC/quiltflower/labels/good%20first%20issue)  
[Quilt Loader on GitHub](https://github.com/QuiltMC/quilt-loader)  
[Quilt Loader PR 73: Config System](https://github.com/QuiltMC/quilt-loader/pull/73)  
[Quilt Mappings on GitHub](https://github.com/QuiltMC/quilt-mappings)  
[https://github.com/quilt-standard-libraries](https://github.com/quilt-standard-libraries)  
[QSL PR 109: Fix issues with the recipe API](https://github.com/QuiltMC/quilt-standard-libraries/pull/109)  
[QSL PR 110: Rename Command Library](https://github.com/QuiltMC/quilt-standard-libraries/pull/110)  
[QSL PR 94: Initial Port of Fabric Biome API](https://github.com/QuiltMC/quilt-standard-libraries/pull/94)  
[QSL PR 81: Screen API](https://github.com/QuiltMC/quilt-standard-libraries/pull/81)  
[Quilted Fabric API on GitHub](https://github.com/QuiltMC/quilted-fabric-api)  
[Quilted Fabric API PR 10: BetterNether/End Comatibility](https://github.com/QuiltMC/quilted-fabric-api/pull/10)  
[QuiltMC on Mastadon](https://tech.lgbt/web/@quiltmc)  
[Cheater’s HackMD](https://hackmd.io/@CheaterCodes/SyEtwjQUc)  
[Hashed Mojmap on GitHub](https://github.com/quiltmc/hashed-mojmap)  
[Quilt on OpenCollective](https://opencollective.com/quiltmc)

=========================

**Gdude**: Hello and welcome to the QuiltMC Developer Meetings Podcast. The podcast that... isn’t really a podcast. If you’re new here, this is just a collection of recordings of each public Quilt Project Developer Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed from a Mumble server and recorded live by a fleet of Discord bots. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to [https://quiltmc.org](https://quiltmc.org).

=========================

SPEAKERS:

- **AlexIIL**
- **CheaterCodes**
- **Emmaffle**
- **Finn**
- **Gdude**
- **SuperCoder79**

ATTENDEES:

- **Blodhgarm**
- **darkerbit**
- **Deftu**
- **flogic**
- **Lapis Liozuli**
- **Octal**
- **Patbox**
- **Southpaw**

MENTIONS:

- **glitch**
- **Haven King**
- **NoComment**

=========================

**Gdude**: Now it's that time where I ping everyone. Hello everyone, welcome to yet another Dev Meeting.

**Emmaffle**: Yay~

**Gdude**: Yay. I'm excited, why aren't you excited, hehe. Usually we wait a few minutes just to allow people to show up, so we'll be starting in about 5 minutes. As you may have expected, or maybe haven't expected, we do have some good news today. But I may forget to tell it, so you know, tough luck if that hppns, hehe.

**CheaterCodes**: Are we just supposed to become a speaker the entire time? Just for when we talk, or...?

**Gdude**: The easiest thing to do, because becoming a speaker is like multiple button clicks, I would recommend becoming a speaker and then muting yourself until you're talking.

**CheaterCodes**: I think it's just one, but sure.

**Gdude**: Is it? Oh yeah, there's a thing at the bottom, isn't there? Whatever, it doesn't matter too much. As long as y'all are here. RFC 54? Which one is that? Is that the Kotlin one? Yeah, I have to admit, I haven't had a single moment to look at that yet.
(Transcriber's Note: [RFC 54: Quilt Kotlin Team by Oliver-makes-code · Pull Request #54 · QuiltMC/rfcs · GitHub](https://github.com/QuiltMC/rfcs/pull/54))

**Emmaffle**: But other people can!

**Gdude**: Yeah, absolutely. I hear it's a pretty busy one. It's good to be doing this on Discord again. I know that not everyone's a fan of it, but it does make our lives quite a bit easier. We're also testing a new Craig, so that'll be interesting. I'm not sure what it adds over the old one but I guess we'll find out.

**Emmaffle**: C'mon, why is `#meeting-chat` so dead?

**Gdude**: They're not dead, they're just waiting for us to start, hehe. While we're waiting for them to get here, so hey. 'Crank', what? Craig! 

**Emmaffle**: It's because of your accent.

**Gdude**: You can see that Craig is at the top of the user list on the right, at the top of the Online section. 

**Blodhgarm** — Today at 12:04 AM
I would be chatting if I wasn't loading a trailer with wood

**Gdude**: Understandable **Blodhgarm**. We need like an elevator music bot just while we're waiting for the first 5 minutes. Someone PR that to Cozy please, I'm only half joking, hehe.

**Emmaffle**: Instant DMCA

**Gdude**: Well it's been 5 minutes so we might as well get started folks. So as always, welcome to the meeting. I'm your host, **Gdude**. This is the show where the questions are made up and the points are- Wait a minute, that's the wrong show. As always, use `/ask` if you want to ask a question. We'll get to the questions towards the end of the meeting. Please don't send a shitpost. We tend to get too many of those. We'll launch right into it, I think.

**Emmaffle**: Now **Southpaw** is mad at you because he'll have to make another beep sound.

**Gdude**: Oh, well, right. Well, you know what, it's fine, hehe. They know how to do it now, hehe. Let's start off with Build Tools as always. **CheaterCodes**, are you there?

**CheaterCodes**: If I find the button, yes. So I'm the stand-in for **Glitch** today as **Glitch** is unfortunately unavailable. But looking at the Quilt Loom history, there's 2 relevant things that happened. Number 1 is, we got a PR merged by ~~**melog**~~, I guess, adding metadata priorities. Which from what I understand is to be able to select, or to choose whether fabric.mod.json or quilt.mod.json should be used if a mod has both of them. I'm sure people who have been desperately waiting for that feature know exactly what it's about. I'm unfortunately not exactly sure. What I can tell you though is that **Glitch** tonight - that is, 15 hours ago - merged upstream. Or, updated it to upstream. So any changes you see upstream should also be available in the latest version of Quilt Loom.

I think one more thing that I can ment, hopefully without building pressure, is that some of our volunteers have added Hashed Mojmap to Loom. So if that goes through, then hopefully we can soon switch to Hashed Mojmap, which would be neat. We'll see how that goes.

**Gdude**: That would be great. There's an interesting PR open somewhere, oh that's Loader, isn't it? We'll get there. Alright, thanks **CheaterCodes**. 

Next up, Community Tools Team, I guess that's me. Not a huge pile going on. Obviously we've been geting a lot of support request on the community server in the support channel. I set up Cozy to do some basic log parsing, so it currently detects a few different potential problems: Outdated QSL, outdated Loader, and mods using Fabric internals. So that's still not quite there. It's already helped quite a few people, which I'm happy with, despite it being as incredibly simple as it is. But if anyone has any ideas for anything else I could add to it, that would be great. But so far, it's at least been somewhat useful. 

Community Tooling doesn't really have anything much else to talk about. We're working on a couple of things that we aren't really ready to talk about yet. But they're small things really, so...

OK. So next up is Decompilers. **SuperCoder79** would you like to take that?

**SuperCoder79**: Hello. Yes, there's been some interesting development going on with QuiltFlower. We've released QuiltFlower 1.8.0 which fixes like 2 dozen bugs and adds quite a few features. We also decided that this would be a good time to go more public with QuiltFlower so there was a Reddit post we made which garnered quite a lot of reception. So we're working on another update right now to fix generic bugs. And if anyone would like to help out, or if they're interested in Decompilers, there's a few issues on the issue board for QuiltFlower ([Issues · QuiltMC/quiltflower · GitHub](https://github.com/QuiltMC/quiltflower/issues)) that are marked as 'good first issue'. Might be a fun place to start with. And I think that's it.

**Gdude**: Thanks for that **SuperCoder79**, I'll just link that in the channel for anyone who doesn't know where it is, here we go. Alright, next up is Loader, and I believe **CheaterCodes** is standing in again for that one.

**CheaterCodes**: I am the perfect stand-in, sorry, I forgot to click the button, whoops. So, I already forgot, there was just one thing I wanted to ment. Well, first off there's a lot of things that were fixed during the last week in Loader. Or bugfixes that were discovered thanks to people using it thanks to our Beta. But that's nice. 

At this point, first off, thank you to everyone who's reporting those bugs, reporting all those issues. And second of course, thank you to all the people who fixed those issues. Let me just quickly check the Quilt loader repository if there's an important thing I missed. No. So yeah, thanks for that. 

Thr's also quite another big thing that's happening with Quilt Loader that I think would make quite a lot of people happy and probably also some people upset. A new PR is open. It's [PR #73](https://github.com/QuiltMC/quilt-loader/pull/73). Nobody knew it was happening until it happened, except **Haven King** who made the PR. **Haven King** opened a PR to add a config system to Quilt loader itself. I've already made quite a thorough review and it looks pretty cool. So this will obviously be quite a big deal to have. Not just a first-party config system in Quilt, but also have it part of Loader. Which means that other tools - like CHASM for example in future - will also have access to the same config system. 

Now I know there's always a big debate about what config file to use, but now **Haven King** first added JSON5 because it was the easiest to add, and then added TOML, which is now the default. But it can also parse JSON5. And everyone has the option to add their own config parsers. If you think your config file parser is just superior to all the other options, feel free to make a parser yourself. Yeah, if anyone's interested in how that would possibly look in the API, or if you have some input you want to add, go look at the PR. 

**Haven King** is really on top of fixing things, which is amazing. So hopefully we could have this in an FPC soon, and then also merged, then everyone has a standard config library, which would hopefully make the whole system a bit less spilt up. 

**Gdude**: Sounds great to me. It's really an exciting PR to see finally open after the, well, months of discussion, hehe.

**CheaterCodes**: Yeah, I guess **Haven King** just decided it's enough.

**Gdude**: Yeah, I think so. 

**CheaterCodes**: Which is the right move for sure.

**Gdude**: I agree. Alright, thank you for that **CheaterCodes**, was that everything?

**CheaterCodes**: I think that was everything.

**Gdude**: Alright, fabulous, thanks for that. Alright, moving on, Mappings Team. **Emmaffle** would you like to talk about that?

**Emmaffle**: Yeah. So there's been exactly one interesting thing that has been added to the 1.18.2 mappings that changed one of the structure names to a much more accurate name. But other than that, we haven't really been doing much other than matching between pgss. So QM is still being released for snapshots. and other than that, the only thing we really have to say is that we're always looking for Mappings Triage members. Even if we're not doing that much right now, we're still looking for more Mappings Triage. So send a message in `#mappings-general` if you are at all interested.

**Gdude**: Thanks very much for that, **Emmaffle**. For QSL, **LambdAurora** would you like to talk about that?

**LambdAurora**: There's not a lot of stuff that has happened mainly in QSL. But points are, the Recipe API got fixes because in the original PR there was some stuff that has been forgotten, and was not considered initially. Which caused the recipes that were registered through the API to not work properly with the recipe book, and to also not be properly stored in the client ~~bt~~. 

Then, Common Library got renamed to Management Library. This has almost no consequences for most other people. The only consequence is [that] if you are a developer and use the manual Maven artifacts, then you would just need to change one thing, and only one thing. The rename was done so we can also patch other stuff like Permissions API without worrying too much about the scope. Otherwise, the merged PR also is the transitive access wideners for Block Constructors which got merged. This basically means: so when you have QSL in your development environment, a lot of the previously protected constructors and blocks are now public. 

And the only notable things are... the resource pack providers PR still neds to be merged. But, lately, no core members, we have time to merge it. But it will be merged soon. Then there is the BiomeModifications API that is now ready for review. There was an issue but now it's fixed. And the Screen API- Or if you want to be really precise, the ScreenEvents API is in the final comment period, so soon it'll be merged unless there is really a big issue with it. That's kind of it for today.

**Gdude**: Thanks very much for that **LambdAurora**. OK, for Quilted FAPI, **Emmaffle**, do you have anything to talk about there?

**Emmaffle**: Yep. We have a few releases for QFAPI, most notable of which would be Beta 13, the latest one, that gets around an issue with Windows Defender finding us as a virus, and also reduces the file size by almost half a megabyte. Other than that, there is a PR open for better compatible with BetterEnd and BetterNether that could use a couple reviews. But other than that, not very much has happened there either.

I just sent the PR in the `#meeting-chat`.

**Gdude**: For Community Team, you may have noticed that **NoComment** has been promoted to full moderator after just over 2 weeks in the trainee position. It's been great working with them. We think they're going to be great working in the position, and we hope y'all like them as well.

We're also on Mastodon now, assuming that's how you pronounce it. We're on lgbt.tech-

**Emmaffle**: Other way around, tech.lgbt.

**Gdude**: Even better, tech.lgbt. See, I can remember things. So if anyone's using Mastodon, you can find us there. I'l actually make a link, there we go. Yeah, we decided to set up there just as an alternative for people that want to get the sort of thing that we post but don't use Twitter or can't use Twitter, or just in case if Twitter dies in a fire after Musk bought it, or has bought it by now I guess. If you contact us there, you'll probably be talking to me, but yeah, we do use it, we keep it up to date. 

Alright, before we get to the questions, there's a few things to talk about here. First of all, as one of **Octal**'s members mentioned, there's a PR open for a Kotlin team. This is an RFC which defines basically a team for managing Kotlin-specific projects and a definition for some types of projects that maybe will come under that team. It's been a fairly busy PR, I think, or relatively at least. But yeah, if anyone's interested in that, it's still a draft, but it would great to get some further input on it. 

Additionally we're planning on moving our meetings to... We've been talking interally about how our developer meetings  going forward should be structured and how things should work. (You can airbrush them out, it's fine, hehe. I'm kidding, you don't have to do that. What was I saying? Oh yes.) 

We're planning on moving the dev meetings around. So we've been discussing internally a little bit on how our meetings should look going forward. We're planning on move these meetings - in the format that we have now - to the community server. They're going to work the same way, pretty much. 

But that's not going to be the only thing we're doing. We're also planning on setting up individual meetings for specific project teams. For example I think yesterday, I think it was, yesterday the CHASM team had it here on the Toolchain Server. Those meetings will happen here on this server. **CheaterCodes** would you like to quickly point at what happened in that meeting?

**CheaterCodes**: Yes, and I even found the button. So as **Gdude** said, the public dev meetings are quite fun and quite enjoyable.  However, we can't really talk to each other about stuff that's happening. So the origin plan of the dev meetings was to get developers to get together so they could decide on a direction for the project. But since the direction is pretty solid right now, that has gone away, and there's not really an opportunity to talk with fellow developers unless we just randomly meet up in chat. Which is of course possible. 

So while the develop meeting will become even more of a community-oriented public develop meeting, we're considering having test meetings now. While not everyone fully agrees with this, we made a test with the CHASM Team. So today we met, we talked for just over 1 hour about the current state of CHASM, what neds to be done and the future. And it's last to just assign tasks, that's not really the point of it. 

It's just so we can get the information out to each other, because right now I'm just a single person who really knows what's happening with CHASM so that's not great. So now we have at least 3, maybe 4 people who know what's happening with CHASM which is a good start. And if this becomes more of a success, we might also start to advertise them a bit more. So while they're technically public right now, we haven't really announced anywhere that it's happening. But in the future we might do that, so that people can join in and listen and get a more in-depth idea of what actually hppns. 

The idea of that would of course then be if anyone is interested in contributing to CHASM, that's a good place for them to just hop in and listen to what's happening and maybe get some kind of understanding of what's going on. Just to show this to you, this is also public. It's also pinned in the `#chasm-general` chat. 

I'll make a HackMD ([Chasm Meetings - HackMD](https://hackmd.io/@CheaterCodes/SyEtwjQUc "https://hackmd.io/@CheaterCodes/SyEtwjQUc")) where we can just take notes as we talk and this will be good for future reference. While it's not proper documentation, it's at least some documentation. It should also help other teams in geting an understanding of what's going on. Specifically the Outreach Team is tasked with the difficult challenge of geting information from developers.

**Gdude**: That'll make sense to me.

**CheaterCodes**: It's nice because I ~~thought this would be too much to ramble~~. So yeah, if anyone is interested in what's happening with CHASM, the next meeting is scheduled. It's probably going to be on May 16th, 5 PM UTC. It might move an hour backwards or forward depending on how the actual team people are available. But if you're interested in hearing a bit about what's going on with CHASM more in detail, about the technical challenges and more than just a quick status update like we usually do here, feel free to join us in the toolchain Discord and just in our development channel.

**Gdude**: Yeah. If anyone's interested in CHASM, obviously go to the meetings. The other teams are likely to schedule their own meetings soon as well. I guess we'll probably post those up in `#toolchain-news` somewhere, we'll figure it out anyway. But if that hppns, there'll be more information available on that. Now of course, we have one other big piece of news. Should I tell them **CheaterCodes**? I don't know they're ready for it.

**CheaterCodes**: Ahh, you know, I don't know if *we* are ready for it. 

**Emmaffle**: Maybe just hold it off until next week.

**CheaterCodes**: Yeah, maybe we should wait a bit.

**Gdude**: Enough, I'm not feeling mean today. You're going to know immediately what it is once I start talking about it. But pretty much since the start of the community server, or when it was made public at least, people have been asking about creating a forum as an alternative for Discord. And also for better places to talk about this in long-form, or just have things easier to discover or search for. It's been a long time in the making, we did a huge amount of research into it: Looking at different types of forums, what we neded for a forum, how moderation was going to work, and of course how it was going to be hosted. 

For that last point, someone pretty much everyone here is familiar with, the **Starchild** system offered to basically do all the hosting and setup work for a [forum](https://forum.quiltmc.org/) for us. An offer we've gladly accepted. So as of last week, we've had something to play with and set up. So I guess what I'm trying to say is, go ahead and sign up. It's ready. We hope you get as much fun out of using it as we had in seting it up. And I guess as much frustration the **Starchild** system had with geting it set up.
(Transcriber's Note: [Announcing the Quilt Forum | The Quilt Project](https://quiltmc.org/blog/2022/05/07/announcing-quilt-forum/))

**Emmaffle**: Yeah, that was really painful watching that.

**Gdude**: Yeah, discourse is not an easy thing to host on a cloud platform. But it's great, and of course there is the usual stuff: There you would expect to find the different categories, we have user announcements there, there's a meta section, you can post your projects there. Go wild, obviously. That will follow the same rules as everywhere else, which we will be updating eventually. But you should all be familiar with them by now, so just follow them there too and you should be fine.

Well then, let us move on to the questions. We've only got a few so far. If anyone has any questions, use `/ask` and we will go ahead and we will do our best to answer them. If you're geting a blank page, I will poke **Starchild** later. It should be OK though we know Cloudflare's being a bit weird at the moment. Let's take it from the top then, shall we? **AlexIIL**, would you like to take that first question?

**Deftu#0001** (432291917645086720)
Will Quilt support classpath loading of mods? For example, if I want to add a mod to the classpath without loading it conventionally (such as how the Essential mod works)

**AlexIIL**: Yes, Quilt Loader does scan the classpath for mods already, so yes, it just works basically.

**Gdude**: Excellent. I'm geting lost in a sea of replies.

**Emmaffle**: Is the next question mine?

**Gdude**: I'm not sure.

**Emmaffle**: I'm pretty sure it's mine.

**Gdude**: Well, then, go ahead, hehe.

**darkerbit#0143** (560515299388948500)
Which intermediaries does QM use right now?

**Emmaffle**: The answer to that is Hashed Mojmap. QM itself does use Hashed Mojmap, but we have a plugin - Quilt Mappings only - that actually changes that so that when you're compiling your mod, it compiles to Intermediary. Because that's what Quilt Loader uses right now. So hopefully soon enough we'll get some sort of compiling to Hashed Mojmap and also using Hashed Mojmap in Quilt Loader. But for now, Quilt Mappings itself uses Hashed Mojmap, but changes too.

**Gdude**: Thank you for that. I believe the next one is **LambdAurora**'s question.

**Deftu#0001** (432291917645086720)
Will Quilt have permissions in the way Android does? So a mod would require a certain permission to perform an action with files, etc

**LambdAurora**: One thing that I originally did again, hmmm. So there's 2 ways of perms, so there's server permissions, but that's not like Android. Server permissions is something that we will have, because it's very important. But for client stuff, like Android, that won't be a thing that we will do because basically it's not a sandbox environment. If you want that, we would need to sandbox everything which is not possible in the current state. And it just isn't realistic to do that.

**CheaterCodes**: I think just to clarify a little bit on this: It's also really hard to just do permissions like that in Java. There is currently a mechanism for that, there is a community manager, but it's deprecated and supposedly not being replaced. So I don't think it's possible really.

**LambdAurora**: Yeah, it's really difficult in Java. If you really wanted to do it, it would need something like- It would request each mod to be sandbox-ed basically, so it can't like access the file system while going through our system. And that's really difficult. I'm not really sure it's even worth it, because in the decades of modding, it's just a game of trust. It's been a decade like that. So I'm not sure if it's really worth spending a lot of time trying to change that. I think there's more important things to attend to for now.

**Gdude**: Thank you. I think next one is yours too.

**Deftu#0001** (432291917645086720)
Will Quilt have built-in telemetry? Such as ways to track it's own user counts, exclusive users, etc

**LambdAurora**: I think I'm pretty confident to say that we won't have anything like that. First of all, we have a lot of users who would be straight-up against it. And if you look at the clients in the modlist and the server, there was a lot of debacle. And again, it's not really worth it. Fabric doesn't do it, I don't know the state of Forge. The only stuff I know that collect statistics is some Bukkit plugins, and even that... There's a lot of people who don't appreciate it, so I might be confident to say that Quilt won't have built-in telemetry.

**Deftu** — Today at 12:35 AM
Forge does do it

**Gdude**: I have to agree with you, I just can't see it happening personally. I'm sure some 3rd-party might come up with something, but it's definitely not something we're interested in, as far as I've seen anyway.

**CheaterCodes**: Also, we already have plenty of statistics on Discord. I think **Gdude** is satisfied with that.

**Gdude**: Hehe, yeah, that's true. Yeah, I'm a bit of a statistics nerd and I'm fine with that. Now while you're working on claiming that, I'll take this one.

**Lapis Liozuli#2082** (150878072818761728)
If there will be separate dev meetings in future, are there any plans to scale up the recordings?

**Gdude**: Well, if there are going to be separate meetings, I think it's ultimately going to be down to the team running the meeting to decide how they want to do it. Now we do have Craig on both servers. I believe they should be able to use Craig if they wished to, so there's no reason that there can't be recordings. It's unlikely that **Southpaw** as our only editor would have time to edit these recordings, just because there's going to be more of them and you know, they take a lot of work. So it's hard to say specifically what's going to happen. I think it's going to be left down to individual teams. But of course if they need help we'll be happy to help them as well.

Ah **Finn**, you can take that one. Just click the stage button and off you'll go.

**Lapis Liozuli#2082** (150878072818761728)
Great to hear that BiomeModifications API is getting ready. Could I ask what was the main challenge in converting to 1.18?

**Finn**: Well, it was already converted, but we just thought of a problem that the End did not really exist because we just read a file wrong in the test mod. So we now know the test mod works and it's ready for release and we're just waiting on Github to be merged.

**Gdude**: Huh, that simple huh? Well, fair enough. OK, thank you. **LambdAurora**, I think you've got 2 more, hehe/

**flogic#0001** (168789991189774337)
Are there any plans for QSL modules for purely server side modding? Or is that out of scope of the project?

**LambdAurora**: Basically there will be the Permissions API which is purely server-side, that literally isn't useful in client. Except if you open the client in a single-player world, but that's kind of a very niche case. It's supported by the API. But basically for the server-side modding, there might be... I know that Patbox wants to write some stuff in the registry module to support server-side modded items and blocks. So it doesn't try to registry-sync server-side-only registry entries. 

I'm sure there will be other APIs, I can't tell right now what. But there will be others. It's not out of scope of the project. As long as it's not like really, really niche- As long as it helps to build mods in a more compatible way, it's welcome.

**Patbox** — Today at 12:39 AM
Virtual Networking Stages is planned by me

**Gdude**: Thanks for that. Maybe we'll go to the next one. But before we continue, we're running to the botm of our question list already, folks. We've still got another 20 minutes, so if you have more questions, hit up `/ask`, send them in. We'll get to them. Sorry, go ahead **LambdAurora**.

**Deftu#0001** (432291917645086720)
If issues were to occur or there was enough of an outcry for support with something, would an in-house fix be implemented? Like how Forge supports/supported(?) OptiFine

**LambdAurora**: That example would be quite simple to answer because definitely won't be an in-house fix. It's kind of not our job in that case. It's such an edge case, a complicated case that no, it's not our job. Aside from that example, it would really, really dependency on what neds the support. If the goal is to support like... an adjustment protocol like I don't know, for like maybe... I don't really have an example right now, but I can maybe think of Velocity being a bit different. 

But I think it's not really something you can do about it. It's really a difficult question actually. It will depend on what you have to support. If just to support one edge case, that is good for only do one thing, it most likely won't be support. Otherwise it's really a case-by-case thing, honestly. 

"I thought it would be easy to add support actually." No, it really depends. It's not something we can like globally implement.

**Gdude**: Alright, thank you for that. **Finn**, are you available to take that question?

**Lapis Liozuli#2082** (150878072818761728)
I think to clarify on the BiomeModifications question, I was curious how come it took so long to update it since 1.18 was first released. Like I think Fabric also struggled with it for a while.

**Finn**: Yes I am. The fact is at the moment, the Fabric API is ported over to Quilt. We will soon write our own or do heavy modifications to it. But at the moment it is just the Fabric API and I don't know why they took so long. You would have to ask there and why it took them so relatively long.

**Gdude**: Alright, thanks for that. Keep the questions coming folks, we still have a good 17 minutes.

**Deftu#0001** (432291917645086720)
Will QSL be fully thread-safe, or will extra effort have to be put in by the dev using it to ensure that they're using whatever it is they're using on the main thread?

**CheaterCodes**: I actually think I kind of want to talk about this. I think in general it's the developer's job. So people are like- No one's entirely sure in the internal chat, so don't take this as a definite answer, I'm not even on the QSL team. But the way I see it is, you're using 2 APIs when modding MC. One is MC itself, and the other is QSL. 

And MC is inherently not thread-safe. You have always to check yourself. There's very few situations or networking code, but they add some checks to make sure you're on the correct thread or whatever. But in general it's a developer's job. And I think it's dangerous to assume in MC that any API is thread-safe. If you're a developer who adds multi-threading to your mod, be aware that this is your own fault. 

I'd say just be very careful. Double-check the APIs. Again, QSL is not the only API where you would use it.

**LambdAurora**: I would add to this that it also dependencies on API because QSL is a set of APIs. It's not a unique one. 

Some APIs might contain quite safe features, but it's not guaranted. And if something is thread-safe, I think it would be said within the Javadocs. We can't really make a guarantee fo the whole of QSL.

**Gdude**: Alright, thanks for that, you two. We have currently reached the end of our list of questions, so if anyone has anything they want to ask from any team - not just the developers by the way - If you're curious about anything, please do go ahead and use `/ask`. We still have about 15 minutes.

**Emmaffle**: This is where the elevator music PR would come in. 

**Gdude**: Yeah, it would be quite handy, wouldnt it?

**Emmaffle**: Would that be **LambdAurora**'s one again?

**Gdude**: I think that would be **LambdAurora**'s, yeah.

**CheaterCodes**: It shows how popular QSL is.

**Gdude**: Hmm, what a great time to get a phone call.

**CheaterCodes**: You know I was thinking before, after you mentioned at the start where we like always wait 5 minutes where we were thinking of playing elevator music? Could be kind of cool to instead like- You can't screenshot in stage chnls, but it would be kind of cool to showcase some stuff at the start. We could like show some art, or like show new mods, just to bridge the time. That's hard of course without screen-sharing.

**Gdude**: It would be quite nice. But it's hard without screen-sharing, yeah.

**Blodhgarm#6853** (380859072729317377)
Stupid Quetion Here(Sorry): How easy is it to get a Fabric mod working with Quilt and how much time would such take?

**Emmaffle**: As somebody who's ported multiple of my mods from Fabric to Quilt, it's really not that much work. Most of the stuff has directly equivalent classes where used. If you don't want port your mod directly to Quilt, the Fabric version of your mod probably works fine. Like there's a pinned message in the `tech-support` channel over on the community server, and I think right now we have less than a dozen mods that work on Fabric but don't work on Quilt. So all in all, it's not that much work, and you don't even have to if you don't want to.

**Gdude**: Alright, thanks for that. I'll take this one.

**flogic#0001** (168789991189774337)
With the OpenCollective, is Quilt looking or open to sponsors from large servers / companies? 

**Gdude**: Usually we have an Administrator to answer this question, so don't take what I say as gospel. This is what I've collected from discussions interally. But we are working with a couple of groups. Like sponsorships are not something we're particularly against. We have one from 1Password which we use for storing our credentials and stuff in a way that's specific for each team. We got a sponsorship from the **Starchild** system, which you'll see on the website once they have a website for their own and stuff. They're hosting the forum. 

Pretty much everything else comes out of **Haven King**'s pocket and a small amount from mine as well. So like, we're not against it if there are like companies that want to help with that. Ideally we would prefer sponsorships that are like monetary just because controlling the infrastructure is important to us. 

But yeah, we're open to talk about it, as far as I've seen internally, so I don't see why not. If you want to bring it up to an administrator, I'm sure any of the 3 of them would talk to you about it. I'll take this next one as well then while you all are discussing that. Well, if you want to take it, then go ahead and take it.

**Deftu#0001** (432291917645086720)
Will there by additional APIs in QSL which will make creating multi-version mods easier? Such as what Architectury does with it's API

**LambdAurora**: It's slightly difficult to answer because there's a lot of uncertainty currently. The main thing is first of all, once we got CHASM and we start using uniq features from it, there's some likeliness that some APIs won't be as useful in that case. Because if other modloaders don't spot the same injection methods, issues will happen. 

The other thing is a lot of APIs are made with the Quilt philosophy, if you can call it that. It's a bit derived from the Fabric philosophy of last year, which is extremely different from the Forge philosophy. And basically what that means is that multi-version stuff is really difficult. 

The thing that happens is - at least for a multi-version alone - is we provide stable APIs, but not too stable. Because in snapshots, what can happen is we break some APIs if and only we need to make changes to make it either better because in the last iteration we missed some stuff. Or if for example Minecraft wipes it because it doesn't like, ~~it means their only use is to keep a broken API around~~, so it will really, really depend.

If Minecraft doesn't change much, and if the API doesn't need to evolve, then it'll have some stability guarantees. Otherwise for multi-loader stuff, it really depends. But a lot of APIs won't really be usable on other loaders. There might be some APIs that at one time might work on other loaders, but there's absolutely no guarantee on that. They're not in a state where we can answer more on this. It's something we will have to see with time.

**Gdude**: Alright, fabulous, thanks for that. I'll take the next one. Actually we're pretty close to the end, so I'm going to finish the AmA to make sure we have enough time to get through this question, but I think we will. Thanks **LambdAurora**, thanks for that. Oh, that didn't work at all. Why didn't it? 

I can't send the question to the channel, but **Deftu** asks, "Is it possible for Quilt to partner with larger mod developers/dev groups to benefit each other?"

**Gdude**: This is a bit of a broad question IMO. There's a couple of things to think about here. On the one hand we do work with some groups on the issues of moderation specifically. Like for example we work with Forge at Community Collaborate to work on events and moderation things. On the other hand, if you're talking about like PRs and things on Github, it's kind of difficult to say. We're in a position where we have an open enough system where we hope to avoid favouritism. 

It's understandable going to be difficult to balance that with the needs of larger developer groups .Obviously we want be as accommodating as long as we can. As long as that doesn't happen to the detriment of well, your regular user or contributor.

That doesn't mean we won't work with bigger developers of course, but we do want to prioritise everyone, not just specific groups in our decision-mking. I think that about covers the rough philosophy anyway.

**Southpaw** — Today at 12:56 AM
Everyone should get good treatment, not only big developers, is the point

**Gdude**: Alright thanks everyone. Thanks for your questions and thanks for coming. We'll be doing this again in 2 weeks on the community server instead of the toolchain server. We'll put an announcement out to that effect once we have everything set up. And in the meantime, thanks for coming. 

As always, I'm sure there'll be an after-party in the voice channels here. Or maybe even on [the community server if you're lucky. And uh yeah, thanks for coming. We hope to see you all again next time. If you have any fedback on the forum or anything else that has happened, just contact one of us. We'll be glad to hear about it. See ya everyone, we'll see ya in 2 weeks.

**Emmaffle**, **CheaterCodes**: See ya.
