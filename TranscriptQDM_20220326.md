[26/03/2022: Why Called Quilt?](https://anchor.fm/quiltmc-dev-meetings/episodes/26032022-Why-Called-Quilt-e1gchd5)  
In this episode, the team discuss progress made on Chasm, Loader, Mappings, and QSL, as well as recent developments in the Community Team. They also take questions from the community, and we find out how Quilt got its name.  
[https://quiltmc.org](https://quiltmc.org)  
[QuiltMC on GitHub](https://github.com/QuiltMC)  
[Quilt Community Discord](https://discord.quiltmc.org)  
[Quilt Toolchain Discord](https://discord.quiltmc.org/toolchain)  
[Doors and Wheels](https://twitter.com/newyorknixon/status/1500000428985286657)  
[Chasm on GitHub](https://github.com/quiltmc/chasm)  
[Chasm PR #42: Language Rewrite](https://github.com/QuiltMC/chasm/pull/42)  
[Quilt Loader on GitHub](https://github.com/quiltmc/quilt-loader)  
[Quilt Mappings on GitHub](https://github.com/quiltmc/quilt-mappings)  
[Quilt Mappings PRs](https://quiltmc.org/quilt-mappings/pulls/)  
[Quilt Mappings PR #5: Start work on refactoring rendering names](https://github.com/quiltmc/quilt-mappings/pulls/5)  
[Quilt Standard Libraries on GitHub](https://github.com/quiltmc.org/quilt-standard-libraries)  
[QSL PR #90: Fix Command API registration method](https://github.com/QuiltMC/quilt-standard-libraries/pull/88)  
[QSL PR #78: Migrate to Quilt Loader](https://github.com/QuiltMC/quilt-standard-libraries/pull/78)  
[Quilt Enters Beta (Quilt Blog)](https://quiltmc.org/blog/2022/03/22/quilt-enters-beta/)  
[Quilt Openings (Quilt Website)](https://quiltmc.org/openings)  
[@Quilt_MC on Twitter](https://twitter.com/quilt_mc)  
[How it all began](https://imgur.com/a/fGfr3sd)

**Gdude**: Hello, you all have just got pinged. Welcome. It's time once again for the next biweekly meeting. Let's do a quick check. Hey everyone on Mumble, how's the sound?

A: Good.

**Gdude**: Good. (Good.) I forgot that it does that, I'm sorry. I mean, I'm not sorry, it's not my fault but you know. Anyway, welcome everyone. We're going to just wait a few minutes for people to show up and then we'll get started, maybe about 4, 5 minutes. By the way, nobody's found all the Easter eggs on the website. People found one of them, but there's one of them they haven't found. Emails? It's not the best time for emails. See you later, **KJJP**.

"Are there more doors or wheels in the worlds?"  
Probably more wheels. I mean, all you need is a straight answer like that, and then it's like, "Oh, who cares."

"I don't count your face as doors either." I see a few well-known faces in the stage here. Welcome back.

We'll be starting in just a minute. As always, I'm going to do this the same way we always do it. That is, I will call on some member of the team to talk about their team and they'll do so. Until we get to the bottom of the teams list, and then I'll talk about Community Team stuff, and then we'll do questions. 

As a reminder for everyone on Mumble, and myself as well, because I often forget. When we do questions, we ned to read out the question and the person that asked it. But I'm sure that's fine. As always, if you want to ask a question, you can use the /ask command, and we'll get to them later on in the meeting. Don't ask about doors and wheels though, please. Shall we get started then? First on my list is CHASMDON. **CheaterCodes**, do you want to talk about that?

**CheaterCodes**: Just as a general update, there's no changes that you can see on Github and the like. But I has been re-writing part of the language implementation. I was not happy how the first attempt turned out. Turns out it wasn't that bad, because the second attempt was almost the same as the first one. But circular syntax tree is now an actual circular syntax tree, which is good. And it's immutable so it's just a little cleaner in general. 

Currently trying to fix Gradle again because for some reason the tests are failing and it's not telling me why. But in general, I hope this is a more stable implementation where I'm happy to pass it on to other people to improve performance if necessary to actually start working with it, hopefully.

**Gdude**: Sounds good. Sounds like you're having the same Gradle problems we all are.

**CheaterCodes**: I tried to take a break from Build Tools, but Gradle haunts me.

**Gdude**: **Grappek**, would you respond to the ping I just sent? Oops, looks like he's busy. In that case, **AlexIIL**, would you like to talk about Loader?

**AlexIIL**: Sure, so, in the last week, it turns out we had to remove Quilt Loader entrypoints since it's not really possible to convert method reference entrypoints between interfaces, so instead entrypoints will be in QSL. Which was the plan originally, but it means that we won't have Quilt Loader-specific entrypoints, which should reduce a bit of confusion. And that's really about it for Quilt Loader.

**LambdAurora**: But there's also something else you said, that there's no entrypoints in Quilt Loader. But isn't there the pre-launcher entrypoint?

**AlexIIL**: Yes, yes, that's a good point. I should've said that. So there's a pre-launcher entrypoint which mods aren't really meant to use, because, well, it's not really meant to be used there very much. But it does exist.

**Gdude**: Hehe, ok, fair. While we're on this subject, are you able to address the question that's just in the channel?

**AlexIIL**: "To the QSL Team, what entrypoints will be available at launch?"
If they're not in Quilt Loader, I'm not the right person.

**Gdude**: That's a fair point. I forgot about that.

**LambdAurora**: I mean, I can answer it right now. So there's the pre-launch one in Quilt Loader, and then there's 3 other entrypoints in QSL. Technically more, it's a bit confusing. So there's the initial one, which is launched before the registry freezing. It's ~~server~~-side. There's client-init, which is triggered in Minecraft client using a ~~slide~~. And there's the last one for the dedicated server. And then there's a special system that allows some event to behave like an entrypoint. There's that too. It's a bit of a different system, but it exists. Those are the different entrypoints that are available.

**Gdude**: Alright, thanks for that. For the Mappings Team, we have a new voice on the meeting landscape, I suppose. **NoComment**, would you like to talk about mappings?

**NoComment**: Yes, hello. So mappings, basically we're looking for reviews on most PRs. But specifically #5, the rendering PR that **OroArmor** made. And other things, looking to rewrite ~~Mapture~~ and possibly integrate it into the mappings build scripts, though IDK exactly what's going on there. As for snapshots leading up to 1.19, updating them is going quite well. Builds are coming out in relatively good time. I think the one we did for 20w12a was like 20 minutes, I think. Let me- Uh, I don't know when it was released, but it was reasonably quick. But yeah, other than that, that's all I got.

**Gdude**: Alright, thanks for that. **LambdAurora**, would you like to talk about QSL some more?

**LambdAurora**: Yeah, sure. So there was kind of a lot, especially because of the snapshots. So the first thing was that we had to fix some stuff in the registry events. Because the thing is, we kind of haven't seen it when updating, because we didn't have a test. But that's a specific use-case. And that specific use-case showed us we couldn't act with these blocks. Because the way it works is, contrary to the registry module, we have registry events which actually happen when a new event is added to the registry.

And we have a very cool API for listening for those registration, but also in a way that will trigger for every already-added entries. So for mods like Aurora's Decorations, it's really cool because it allows very easily to analyze the registry in real-time, maybe add new stuff depending on that. The way it works is that when we add that new event listener, it'll go through every entry already added. The issue is, if you register something based off that, while it does the first iteration, it will crash. Because it'll try to add something, to something that is being read. So that is why we had to modify the API. So we had to actually change that, so we have like a special registry interface that allows us to delay all registrations to after the iteration. So that's one of the big API changes we had to do. 

We also had to do some other changes, mostly because of me. So I had the terrible idea to start sorting them out. The issue is, some APIs do not work because of 1.18.2. So we had to fix [them]. So it's kind of great because we see what we should get in QSL to ease registry stuff with the new registry changes. 

We also have a new implementation of the BlockToItemMap, because the way it works in Fabric is, it starts listing at one point. But it's way after any mixins start doing that. Which can cause issues in some mods if they add stuff with a mixin. So if registration of stuff is done before the entrypoint, then it'll not work. The blocks will not be in that map, which can cause a lot of issues. That's one of the things, so we added a new thing to the registry module which allows to fill that map. And we changed the entrypoint so it's much earlier so it doesn't cause issues.

Aside from registry stuff, we also had to to change the API for command in 1.19, because Mojang broke stuff. There's a PR that's open, so feel free to review. So for other stuff, we got 3 new people in QSL for world generation, so that'll be interesting. I can't wait to see what they'll do for world generation. That's exciting. Otherwise, there's not a lot to say. There's a new PR that can be looked into if you want. We are still trying to migrate to Quilt Loader. There's a PR open to ~~tune how long the time will be~~, but it'll be very soon. Once that hppns, that means that QSL will not be run on Fabric anymore. I guess that's kind of it for now, I don't really see what else there is to say now, so yeah.

**Gdude**: Right, that's great. Thanks **LambdAurora**. That was quite a lot, don't worry. In that case, I will cover the Community Team stuff. Outreach Team has been fairly busy. **Southpaw** wrote up a nice new blog post on the upcoming beta, which is a thing everyone should read if they want to learn a little bit more about it. We also moved the #openings channel which was on the community server to the website. So if anyone is wondering what teams need help, or you know, just have openings, you can check that out here. I'm sure there'll be a link in the podcast notes as well.

And we also set up a channel in the community server called #social-feed. **Southpaw** is starting to make use of Twitter. If you're not following us there and you're a Twitter person, please do go ahead and do so. But that channel will also show anything we tweet, so you can keep an eye on it from Discord as well.

Other than that, non-Outreach Team stuff, not a whole pile. I did make a small change to the community server's gallery threads. They'll try and figure out a default name based on the text that you put into your gallery post at the start. Otherwise, not too busy here at the moment.

Alrighty, that about covers all the teams for today. Did anyone on Mumble have anything they wanted to talk about today? Alright, I'll say that's a no. No problem at all. Alright, in that case, we'll get to the questions. **AlexIIL**, you claimed a question. Would you like to go ahead and take that?

**AlexIIL**: Sure, the question by **RTTV** is, "Can we detect if *the* quilt loader entrypoint is bing called on a client or server through a method parameter or something?"
The answer is, not through a method parameter. There's a class MinecraftQuiltLoader, it's got getEnvironmentType(), which will give you the current environment. So yeah, you can use that instead of anything else.

**Gdude**: That certainty looks like it'll make life a lot easier. Alright, **LambdAurora**, yeah, you can take that one.

**LambdAurora**: **Patbox** asks, "Do you plan releasing Beta for 1.18.2 or go straight for the snapshots?"  
Basically it'll be kind of both, because we have to maintain for the snapshots, that's for sure. Because as we fall behind, that'll be hell to update. But I think going for 1.18.2 is really important too, because it's kind of a stable release. So currently all the PRs target that version. And once they're merged, they'll update to 1.19. I think we will keep Beta for 1.18.2. But if it becomes too difficult, it'll be a bit scary, but I think it'll be fine. 

And it will be kind of important, because it'll prove that we're capable of maintaining it on a stable release. And also make sure that we do update to newer versions. After when we release, we will have to support a stable release, and we will have to update to snapshots to make sure that they'll be available during the launch of the next new release. So I think we will just do it directly directly for Beta too. It might be simpler also for PR, because if a PR gets a stable release, it's much easier to review and integrate than having two updates a week because of snapshots. So, yeah, ~~different people~~.

**Gdude**: Thank you, **LambdAurora**. We've got two unclaimed questions in the backlog here. While they're sorting that out, feel free to use /ask to ask any more questions you might have.

**CheaterCodes**: I think since no one really knows the answer, might as well just take it. **Krisander** asks, "Will other language support like Kotlin require a seperate compatibility mod like Fabric or will Quilt have this outingthingbox in QSL/Loader?"

I'm actually not entirely sure about the complete history here, but it is a topic that was at some point hotly debated. So, the answer is unfortunately not a simple Yes or No here. However, even if we don't end up puting it into QSL, there's a good chance that if there's a decent attempt at implementation, it'll fall under dependency auto-downloading. Which means that people will at least not have to manually include it. But yeah, it's not quite clear-cut yet. There's opinions for either side, so we'll have to see what turns up.

**Gdude**: Thanks for that, **CheaterCodes**. **AlexIIL**, you can take that if you like.

**AlexIIL**: So **RTTV** asks, "Like *the* entrypoint, are there any 'FAPI features' that will be present on Quilt Loader without installing QSL?"

So technically Fabric loader contains all of Fabric's enrypoints. There basically aren't any other FAPI feature in Quilt Loader because Quilt Loader is just from Fabric Loader, not the entirety of FAPI. So not really.

**Gdude**: If I remember correctly, the point was more to provide the framework to add features rather than just having them directly in Loader, right?

**AlexIIL**: Yeah.

**Gdude**: We're out of questions, so if anyone wants to ask, please type /ask and get your questions in now. I'll give you a couple of minutes.

**CheaterCodes**: Looks like we're doing a meeting speedrun this week.

**Gdude**: I mean, that happens.

**CheaterCodes**: I'm not sure if it has been pointed out yet, but this is the 2nd-to-last meeting before Beta.

**Gdude**: Oh yes, I never thought about that.

**CheaterCodes**: There's a meeting in 2 weeks, and then there's less than 2 weeks until Beta.

**Gdude**: Certainly is an exciting time, I have to say. How are you all feeling about Beta?

**CheaterCodes**: "Beta good." Yes, **Potatoboy**, thank you for that. I agree.

**OroArmor**: I have a couple final changes I want to get in before Beta, and then, yeah.

**LambdAurora**: It will be a little bit stressful, because if something goes wrong, it won't be good.

**CheaterCodes**: If nothing goes wrong, it's hardly a beta.

**LambdAurora**: Yeah, but hopefully nothing goes wrong. I would prefer that nothing goes wrong.

**CheaterCodes**: I'm still hoping that I can have CHASM access for Beta.

**Gdude**: I did get one question in, but I don't know if we have an answer for it.

**CheaterCodes**: We don't have a why, but we have a IDK, a when and who.

**Gdude**: I know when and who, but I'm just seeing if I can find a why. Well, I don't know, it's just- Oh, I like that, let's use it.

**CheaterCodes**: At this point, let's just put it on stage.

**Gdude**: So, **RTTV** asks, "Why call it Quilt?"

It was just kind of a spur of the moment thing in the initative server, I believe. I wasn't there, **Haven King** came up with it and it just kind of stuck. And that was like, very early on, like the start of Feb. Yes, 2nd of Feb last year. But I don't think there was any deep meaning behind it, other than Fabric-ecosystem stuff using fabric-related terms. 

Yeah, I like that take. **Apophilim** said, "Quilts are made of patches of Fabric and this is kind of the community quilt where everyone gets a piece."

Someone in the chat said, "Hope Quilt is the Forge-killer." Definitely not. Forge and Quilt and even Fabric will always fulfill different corners of the modding sphere, I imagine. 

**LambdAurora**: Yeah, on that point, I think Forge is kind of unkillable. 

**Gdude**: Yeah, it's kind of too big to fail, isn't it?

**LambdAurora**: Like, it's the same as Optifine. It's just very hard or just impossible, because ultimately there are some people that like the philosophy, and they will go and they will die on the hill making sure that it'll survive. So it's not killable. And even then, I don't think the point of Quilt- Eventually, If we can kind of reconciliate the relationship between Fabric modders that goes to Quilt and Forge, that would be kind of nice. I can't say much, because there's not really anything right now right now. But making sure that everyone stops beating each other up over a loader, it would actually be nice.

**Gdude**: Yeah, we do work with Forge on a few things, and obviously there's no intention of killing Forge here. But yeah, as I always say, they fill different niches. There's no reasons for both to not exist.

**CheaterCodes**: We actually do have quite decent connections with Forge, which is kind of nice.

**Gdude**: Yeah, we do. I can take this one. RTTV: "What hardware does the quilt web servers run?"
I think that would be a better question for Github. We're using Github pages at the moment. If you're asking about the maven, **Haven King** I believe has that running on AWS. So it's kind of difficult to say what the specific hardware is, when we're not directly running on hardware. Although, this is kind of fishing at this point, isn't it **RTTV**? 

**CheaterCodes**: Just trying to help us out.

**Gdude**: I mean, all our stuff is open-source, so if you're curious, you can always have a look at Github.

**LambdAurora**: **TropheusJay** asked, "quilt getting more collaborate with forge before release than fabric ever did is impressive (edited)"
It's not that surprising. Because- I can't really go too much into detail. ~~But actually~~ Forge doesn't really like, and that's kind of why there was not cooperation between them. I won't go into more detail, because that's not hte point.

They have a history. So, that's why. Well, I think we're going to close because we're just not geting questions. 

**CheaterCodes**: ~~We were complaining~~ about questions, and then now there's no questions. You can't decide.

**Gdude**: That's ok, I don't really mind ending a little bit earlier. This isn't quite the speedrun we thought it was going to be but that's fine.

**CheaterCodes**: Half of the original time slot that we planned.

**Gdude**: Yeah, I think it was, wasn't it?

**LambdAurora**: And I was being worried that my technical in-depth of QSL was too long.

**Gdude**: No, it's never too long.

**LambdAurora**: I just hope that I don't bore someone.

**Gdude**: It was fine. Don't worry about it. Oh well, thanks for coming everyone. We're going to wrap it up for now. See you in 2 weeks' time. As usual, there'll be an after-party in the #voice-chat channel. That just tends to happen at this point. Maybe there won't be, but who knows. Either way, thanks for coming everyone, we'll catch up next time.

**LambdAurora**: Bye bye~

**CheaterCodes**: Bye.

**OroArmor**: See ya.



RTTV: "can we detect if *the* quilt loader entrypoint is being called on a client or server through a method param or something?", 

Patbox: "Do you plan releasing beta for 1.18.2 or go straight for snapshots", 

isXander: "Will other language support like Kotlin require a seperate compatibility mod like Fabric or will Quilt have this out-the-box in QSL/Loader", 

RTTV: "like *the* entrypoint, are there any \"fapi features\" that will be present on quilt loader without installing qsl?", 

RTTV: "why called quilt", 

RTTV: "what hardware does the quilt web servers run?", 

Byte: "Are there any concepts for CHASM frontends/transformers besides reimplementing Mixins/AW on CHASM?", 

Octal: "Are there any plans for Kotlin on quilt? (I already know the answer to this, but others might not)", 

grifferthrydwy: "is there anywhere to sign up to attend, but not showcase anything in blanketcon?", 
