[Meeting: 11th Dec 2021](https://anchor.fm/quiltmc-dev-meetings/episodes/Meeting-11th-Dec-2021-e1bjsbo)  
On this episode the team discuss the progress made on Build Tools, Loader, Decompilers, Chasm, QSL, Mappings, and Infrastructure. They also take questions from the community, and introduce a brand new Quilt team.  
If you'd like to listen to our meetings live, or you have questions to submit, please feel free to join us live - every two weeks, [on Discord](https://discord.quiltmc.org/).  
[quiltmc.org](http://quiltmc.org/)  
[Quilt Community Discord](https://discord.quiltmc.org/)  
[Quilt Toolchain Discord](https://discord.quiltmc.org/toolchain)  
Shownotes:  
Welcome  
Build Tools  
[VanillaGradle by SpongePowered](https://github.com/SpongePowered/VanillaGradle)  
[Earthcomputer's PR](https://github.com/SpongePowered/VanillaGradle/pull/47)  
Community Tools  
[Cozy Discord Bot source](https://github.com/QuiltMC/cozy-discord)  
Loader  
[Quilt Loader source](https://github.com/QuiltMC/quilt-loader)  
Decompilers  
[Quiltflower source](https://github.com/QuiltMC/quiltflower)  
[Quiltflower 1.7.0](https://github.com/QuiltMC/quiltflower/releases/tag/1.7.0)  
[LoomQuiltflower](https://github.com/Juuxel/LoomQuiltflower)  
[Quiltflower IntelliJ plugin](https://plugins.jetbrains.com/plugin/18032-quiltflower)  
Chasm  
[Chasm source](https://github.com/QuiltMC/chasm)  
QSL  
[QSL source](https://github.com/QuiltMC/quilt-standard-libraries)  
[Keybinding API Plans](https://github.com/QuiltMC/quilt-standard-libraries/issues/61)  
[Keybinding API V1 PR](https://github.com/QuiltMC/quilt-standard-libraries/pull/59)  
[Register Dictionary API PR](https://github.com/QuiltMC/quilt-standard-libraries/pull/29)  
Mappings  
[Hashed MojMap mappings hasher source](https://github.com/QuiltMC/mappings-hasher)  
[Quilt Mappings source](https://github.com/QuiltMC/quilt-mappings)  
Infrastructure  
Q&A  
[ASMR Processor Prototype](https://github.com/QuiltMC/asmr-processor-prototype)  
[Fernflower (Minecraft Forge mirror)](https://github.com/MinecraftForge/FernFlower)  
[Forgeflower by Forge](https://github.com/MinecraftForge/ForgeFlower)  
[Fabric API QSL](https://github.com/QuiltMC/fabric-api-qsl)  
[The Patchwork Project](https://github.com/PatchworkMC)  
[AuroraDecorations QSL commit](https://github.com/LambdAurora/AurorasDecorations/commit/22cbf1290e41ddc2d310c871b45f7d7b3d4423c6)  
Wrap-up

=========================

**Gdude**: Hello and welcome to the QuiltMC Developer Meetings Podcast. The podcast that... isn’t really a podcast. If you’re new here, this is just a collection of recordings of each public Quilt Project Developer Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed from a Mumble server and recorded live by a fleet of Discord bots. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to [https://quiltmc.org](https://quiltmc.org).

=========================

**CheaterCodes**: Alright. I think we can start, the time is now. Hello everyone and welcome to the last QDM of 2021. I'll say that right now because the next meeting would be [in] 2 weeks, that'll be the 25th of Dec. I seriously doubt if anyone is willing to come to a developers' meeting on the 25th of Dec, so that's going to be skipped. 

For this week I'm sorry that **Gdude** isn't available right now. So I have to fill in. I hope that I can do the meeting justice. So, we're just going to do the same thing we do every week. We go through each team, each team can do a little talk, a little update about what's happening. 

And we're going to start right at the top, with our first team, Build Tools Teams. There's actually nobody here that's officially part of Build Tools Teams, but I just want to talk a little bit about it because I've been working on Build Tools a little bit over the past week. Unfortunately, Gradle is still a pain as always. I know that on the VanillaGradle side there have been some changes, that are progress forward, but also unfortunately reverted some. The promising PR from **EarthComputer** might still happen in the future. I want to use this opportunity again: If anyone is interested in helping out with Build Tools, because we really need someone who knows how to deal with Gradle. OK, that's from Build Tools Teams.

Next team- Oh, we have a new team. **i509VCB**, do you want to introduce the new team?

**i509VCB**: OK, so, we actually have a new team now, and this is actually the Community Tools Team. So it's essentially going to be the team for the Cozy Discord bot and any of the other tools the Community Team's going to be using for enforcing the rules and ensuring the community is kept in shape. I think that the two people on it right now are **Gdude** and **AppleTheGolden**. Yeah, 'Community Tools', IDK why I said the wrong word. I think that's all I really have to say at the moment about the new team. If **Gdude** or **AppleTheGolden** were here, they could have provided more information, but well, they don't appear to be here at the moment.

**CheaterCodes**: Yeah, just as a quick reasoning. It's just become appoint that Cozy's geting quite big, and it would be good to have some contributions on our official repository for that. So if anyone wants to help with Cozy, or any sort of any other community tools we might need, feel free to drop into the current channels that exist already. The Community Tooling channels, check them out. Ask if you can help them in some way or interest. We would definitely appreciate any help. Alright, then, on a not so new team. **AlexIIL**, any news on Loader?

**AlexIIL**: So there's some news. Nothing particularly interested though. There's been some progress on the big Fabric upstream merge, but nothing- Well it's not done yet, really. I've also been working on implementing Loader plugins, still. But again, it's still progress, it's not really anything usable yet. That's about it, really.

**CheaterCodes**: I mean, there's going to be ~~holidays~~ soon, so maybe we can see more progress then? But really, you're in a team in a ~~generally good position and really cool numbers~~, so... Loader was doing a ton of progress recently, it's just... It doesn't look that way right now unfortunately right now because of [how] merge conflicts are not pushed on Github, obviously. 

Alright, next team: Decompilers. Unfortunately, our lead compiling goddess, **SuperCoder79**, is not here today. However, **EarthComputer** volunteers to be the voice.

**EarthComputer**: 'Volunteered', that's an interesting word to describe it.

**CheaterCodes**: Been volunteered.

**EarthComputer**: Anyway, QuiltFlower 1.7 was releaseed in the last fortnight, so that's there for everyone. It's available on a ~~linked QUO file,~~ and via IntelliJ as always. So progress on 1.8 is steady, but don't expect it anytime soon. Well like, obviously not this year. 1.7.1 will be releaseing soon to fix some debugs. That's most of it. I suppose we can leave the rest to questions.

**CheaterCodes**: Alright, thank you. Yeah, if you haven't noticed, unfortunately there's a few members missing today, so it's going to be a bit of a shorter meeting than you may be used to. But just like **CheaterCodes** also pointed out, please if you have any questions, just ask. You can use the /ask command in the #meeting-chat. We'll get to the questions at the end of the meeting. 

Right, I think that's my turn: CHASM. Team CHASM. Well, last week, I haven't done that much, but the week before, CHASM Line was born. The Github repository got moveed around a little. CHASM went to its own submodule, CHASM Line got a new submodule. And it honestly felt really fun to use. CHASM Processor is like, I won't call it complete, but most of the important representation is working. **EarthComputer** has last week been working on geting local variables properly represented. It's not merged yet, but I think it'll be merged soon, I hope.

**EarthComputer**: Not quite finished.

**CheaterCodes**: Not quite finished. The checkstyle is not happy yet as well. But we'll have local variable representation soon, and then I think we'll have complete representation of the class tree? And CHASM Line is working, so technically at that point, CHASM is fully functional, but there's still a ton of stuff to be fleshed out with the processing of the I/O performance and mostly with the language. But it's really cool already, there's some tests on- There's some testing repository for where I know how CHASM will look and work. You can look at the CHASM langtests. There's a Brainfuck implementation that's... You can just ignore that, that's for proving a point. And some little transformers that are kind of cool.

Alright. Let's see. In QSL.

**LambdAurora**: QSL Time~ We have multiple people to talk about it, so we'll start quickly. I think we have some PRs. The Keybinding API 1, which introduceed a lot of stuff like- It does some changes to the Keybinding GUI, like showing conflicting keys with a tooltip, exposing some APIs, and allowing to dynamically enable or disable some keybindings. There are more coming, but not in that PR. So that's definitely a thing to look out for. 

And for Resource Loader, there will be some work in the coming weeks, like- What I want to do is caching. I want to mod resource packs to build a directory tree which will be used for caching, which will allow the resource conditions to be implemented, because the issue with resource conditions is it will slow down Resource Loader. So to combat this, caching will need to be done, and that's something I want to implement. My goal is to see if it would slow down Resource Loader too. To test, I will use the All of Fabric modpack and that will be interesting. I hope it will make stuff faster. After that, I also want to implement a symbolic linking which will allow to re-direct a resource to another. It might be a bit niche, but it will be useful for some stuff and for like, APIs which migrate to a new version. It will be useful for like FAPI-QSL addition, so it's something to look out for to. And that is something that will also need a caching system to work nicely. 

And ~~cond[ resource~~ will allow us to- So the goal is to have a registry of predicates, and the goal is you can use those predicates to say, if these directories or resource files exist or not depending on the conditions you would list in a special file. I think that's all for Resource Loader. I know that **Leo** has some stuff to talk about registry dictionaries. They can't talk, so it'll be on the text channel. But I can read it out once he's typed it out.

(**ADudeCalledLeo**: "**Registry Dictionaries API** (originally known as Registry Entry Attributes API) is pretty much feature-complete (besides networking)! A recently implemented feature allows you to use tags as keys, meaning you can _give multiple entries the same value if all the entries are in a specific tag_. Currently tags aren't _completely_ tested, but they are implemented and _should_ work if I understand how tags work.")

**LambdAurora**: If you're asking what's the Registry Dictionaries API, it's basically the same as tags except we can also give values to each entry. So the use case can be like a biome dictionary which could be used to also give- Well, it can be used to determine which biomes the mod will spawn along with weights. To call the ~~interred~~ like that. The goal is to be able to view that in code and via datapacks. ~~I think with 32~~. Unless **i509VCB** has something to say, then that's all.

**i509VCB**: I believe we'll be fine, yep. If there's other questions, we can answer them closer to the end of the meeting.

**CheaterCodes**: I mean, that was a lot of news, so thank you for that. Yep, perfect. Well, thanks for the update. That was very extensive and really informative, thank you very much. 

So, we have two teams left. I'll quickly talk about the Mappings Team. First off, my ~~child Hashed~~ has now stabilised, so Hashed Mojmap is now found in the release Maven repository. This does mean for the time being that we switch back to manually triggering the action for updating Hashed Mojmap. It's still no big deal. Mappings Team is most of the time manual anyway. So they just run the actual first. Reason for this is that we don't really like the big delay that we get from Github Actions when running is automated. So we're looking to trigger them ~~per files~~ in the future by some bot that pulls the version manifest. 

On Quilt mappings itself, there's obviously been progress. Since I'm not really doing much for Quilt mappings myself, I'm not going to talk in detail about it. But you can check out the #devlog-mappings in the toolchain server, or just the #devlog on the community server. And you can see every time there's new mappings added, they put it into the devlog for the next release of snapshots. So obviously the big one was 1.18, which had a lot of differences from 1.17 of course. And then the recent 1.18.1 pre-releases didn't have too many mapping changes. But nothing too much happening there. But Quilt mappings isn't the point that while it's not complete, not 100% done, it's normal operation now. There's no big tooling changes that need to be done right now immediately that block PRs or anything. So great time to contribute and get your stuff in. Anything that you think is important to be in before Quilt release, now is the time to do it.

Last team, there's nothing to say really. Infrastructure Team is not present, but also hasn't done anything because there wasn't really anything to do. Infrastructure Team is of course mostly a supporting team. Managing our Maven, and I'm guessing the website, I'm not particularly caught up. But obviously they only really do stuff if there's some changes required, and recently there's been nothing, so there hasn't been anything happening on that team. Although I want to say it would be great again, if anyone has experience on AWS, or really wants to get some experience, we would be very happy to expand the Infrastructure Team.

OK, that was all the teams for the meeting updates section, and now we can move over to the questions section. I've already claimed a question, so go ahead and answer that one.

**EarthComputer**: Hello, so how do I even do that? Do I press 'Stage'?

**CheaterCodes**: Yes, press 'Stage' and then you talk about it.

**EarthComputer**: So, the question by **LambdAurora** is, "Could CHASM be used to determine any patches at compile time and maybe generate a GraalVM native image with all of the patches applied?"
So yeah, so one of the advantages of CHASM is that it can be applied at compile time and not just run time because of its pure nature. So the output is completely deted by obviously the Minecraft jar, the mod jar, then the transformers and any other settings. Possibly some other things we design in the future. So yeah, it'll be able to run at compile time. It can then be decompiled in Gradle and you'll be able to see the transformations in the source like you can with Forge patches already. And I don't see a reason why someone wouldn't be able to make a GraalVM native image. Although, I'm not particularly sure why you'd want that because it'll all be cache anyway. But I mean, if you want to, go ahead.

So yeah, so one of the advantages of CHASM is that it can be applied at compile time and not just run time because of its pure nature. So the output is completely deted by obviously the Minecraft jar, the mod jar, then the transformers and any other settings. Possibly some other things we design in the future. So yeah, it'll be able to run at compile time. It can then be decompiled in Gradle and you'll be able to see the transformations in the source like you can with Forge patches already. And I don't see a reason why someone wouldn't be able to make a GraalVM native image. Although, I'm not particularly sure why you'd want that because it'll all be cache anyway. But I mean, if you want to, go ahead.

**CheaterCodes**: It's a big motto of CHASM. "Yeah, you can do it, but maybe you shouldn't."

**EarthComputer**: Er haha, I wouldn't maybe encourage that because it's not quite the same as coremodding. Well, it is still coremodding, but it's not in the traditional sense because it is collision handling. It's not really possible to- Well, at least it's difficult to use it in a way that's not collision handling, and you can't blame mods and stuff.

**CheaterCodes**: Alright, thanks for that. Next up, our most super of coders has appeared.

**SuperCoder79**: Hello. Yes, so for the QuiltFlower 1.0 thing, I think at this point we've kind of reached the point where we've implemented all the modern Java features, so we're just going to fix bugs, improve like local variables, generics. And my eventual goal is to basically make it recompile, and after that, make it recompile into a perfect match of the binary. Which is a lofty goal. But I think with some effort, we could probably get there in a bit.

**CheaterCodes**: Alright, cool. Maybe for completion, because we forgot that before, maybe read out the questions if it's not- I mean, this wasn't really a question, so it's fine. But the next 2 questions, we could read them out as well. So, let's take this one by **Kitchura**, I think. "What advantages does a modder gain when using Quilt instead of Forge/Fabric library?"
Now we assume this is talking specifically about QSL. And **LambdAurora** is going to talk about this.

**LambdAurora**: So, at least for QSL, the biggest arguments for QSL over Forge and Fabric libraries is we have a big focus on the data part of MC. Because there's more and more things that get data-driven. So having good APIs taking advantage of that part is very important. And the other thing is, not everything should be only JSON only because it's often a big pain to deal with. We have a lot of content. So there's also a focus on making it available ~~incontenally~~. There's also advantage, at least compared to Forge, we want to be able to listen to registry and then act upon what's in the register. 

So you can, for example, register a new wood type. That could generate in other mods that add wooden content, which would be able to generate new stuff using the new wood type. That's why data is really important, because if you have a good data library, we can make this much easier. Because I've done it with Fabric but it's not easy. Not sure if it's something we can ask the API for. But by doing this project, it allowed me to think of new features that should be in the libraries to allow this [data-driven aspect] much easier. There are also some advantages for resource loaders, since I'm not really contributeing to the Fabric one now. There will be new features that will be kind of important. 

The other advantage is, is we want to kind of expand. Not just limit ourselves to ~~upstream notechunking~~. As much as ~~when we call~~. For example for the Keybinding API, my thoughts, because we are removing that limit that FAPI has, we can change some little stuff to make the experience better for the user too. Not just the mod developer. That will be advantages for both mod developers and users. Talking about this, it's not an excuse to modify vanilla behaviour, so that's no change. At the moment, I can't think of other stuff, but there might be other stuff, but currently I can't think of any. So I think that's it.

**CheaterCodes**: Perfect, thank you very much. Next question is by **Byte**. "I'm glad to see Quilt is approaching release. I was worried there would be a loss of momentum after a while. How old is Quilt in its current form?"
I think our administrators are perfectly capable of answering that. **i509VCB**?

**i509VCB**: OK, so give me a second to get my throat. OK, so Quilt in its current form was actually started in early February this year. We did have to go public I think in March, because we did run out of internal Github Action minutes. And well, I would definitely say it was worth going public when we did, because we were able to utilise the community more towards progressing Quilt at a faster rate.

**CheaterCodes**: Another quick and easy question that we're going to move ahead I think. **Banzobotic** asks, "Does CHASM completely replace the ASMR prototype?"
And **EarthComputer**, what's the answer?

**EarthComputer**: Yes.

**CheaterCodes**: Thank you.

**EarthComputer**: Haha, I can give a bit more detail. The ASMR prototype was meant for us to be able to like, figure out what the problems we're going to hit are. It was not designed to be long-term maintainable or anything. CHASM does steal the bits of the ASMR prototype that works, and that ~~reworks~~, and some of the bits that didn't. So, that's what the prototype is for. And yes, it's deprecated.

**CheaterCodes**: A simple question with a short answer. Next up, I think **SuperCoder79** can take this one by **Byte** again.

**SuperCoder79**: Yes, **Byte** asks, "Have you thought about upstreaming Quiltflower's changes to Fernflower? I'm not sure if JetBrains even maintains Fernflower anymore though, to be honest."
 I think eventually, once we reach a stage where we can call our work like more or less done, we may start mergeing our changes with FernFlower. But in the meantime, we've been contributeing back to ForgeFlower to help out our moding friends with stuff like optimisation, new features and stuff like that.

**CheaterCodes**: Yeah, I think there's been recently also upstream changes to FernFlower, weren't there? Or did I mis-understand that?

**SuperCoder79**: Yeah, I think one of ForgeFlower's PRs got accepted. But it was kind of a minor one.

**CheaterCodes**: Ah, OK. Alright, another question by **Byte**. "Is applying transformation at compile time something that only is in development, or can you also ship your mods as patches?" **EarthComputer**?

**EarthComputer**: Hold on, let me just find it. Yes, so most of the time for compile time, I mean, if you want to, you could ship your mods as patches. But given the only way to apply the patches will be through - I was about to say ASMR - CHASM anyway, there's not really much point. Again, because CHASM catches the output of the transformation. It's not even like it gives any benefit. So, you can, but you don't have to.

**CheaterCodes**: Yeah, again, the motto of CHASM. "You can, but you probably shouldn't."

**EarthComputer**: I- But- Why?! Like what it would look like, is probably it's just some- it would take a transformer and convert it to another transformer. And it would be less compatible with other people's transformers. So please, don't do that please. You would lose intelligent conflict handling. So a transformer can specify, "Oh, I want this block of code not to change for my transformer not to work." And that information is lost with patches. You got to think that patches are not complete description of transformation. They don't fully describe the intent. If you're adding a line of code, is the intent to add it after the previous line, or add it before the next line? So you got to bear that in mind.

**CheaterCodes**: So we have one more question by **Byte**. "So Mojang has made more and more stuff data-driven, so you're focusing on APIs for those things in QSL, and especially creating resources programmatically, because JSON files are a pain sometimes, right?"

**LambdAurora**: Yes! Yes, so we're focusing on those APIs, and creating resources programmatically is important. There will be data generation APIs. There will be runtime resource packing dictionary APIs, and for that one is something that I've been planning for a month, and I still haven't got around to making one. And there is also that controversial Recipe API that is still in my mind. But that one needs a lot of framework to be easy to use and compatible and doesn't remove features from other mods. The thing is, giant JSON files are great for datapack makers. But for development it's kind of a pain when you're not right. So not duplicating a lot of data is important too.

**CheaterCodes**: 'Kay, thank you very much. So there's been some last minute questions that we can still answer, and I think after those questions, we'll call the meeting a day. Let's do the second one, I think that one's easier, by **Fish**. "Can we still go from Quilt to Fabric fairly easily?"
I'll start with this one. If anyone wants to add something, let me know. First off, I know that the Fabric API compatibility with QSL is still important and still happening. So that should be fine, maybe QSL can later specify on that. I want to quickly say that mixins should be mostly supported, however there are some questions we'll have to figure out. For example, local variable bytecode indices is something that's not very stable, and not very good to use anyway. So we might have to deprecate those. There might be a compatibility layer there that's either slow or incomplete. We'll see about that but-

**EarthComputer**: Yeah, it's bad practice to use them anyway. I think the bigger one is the integer priorities in mixins. We want to deprecate them. They cause issues, in short.

**CheaterCodes**: Integer priorities are another thing we could potentially kind of implement as a patch to allow Fabric mixins or Sponge mixins to work. But it's definitely something we don't want in Quilt CHASM mixer. And there was one more- Oh yeah, and mixin plugins are still a no-go. There should be other ways to do those. You should not need mixin plugins anymore. And we can maybe support a subset of those, but probably not really. We'll see about that.

**LambdAurora**: And for that question, I also have to add, for QSL, there's the Fabric API-QSL thing, and you can use that to run stuff that needs QSL on Fabric for now. If not, ~~they for are~~ available on Fabric but it is kind of available. So switching, so that's something that can be used.

**CheaterCodes**: Hey! My ultrasound just went off because that's my thing. **Grondag** asks, "What is the replacement for Mixin Plugins if we need conditional mixins?"
Well, the replacement will be conditional mixins. Like actual conditional mixins rather than a mixin plugin. So, I don't know exactly how it looks, but in order to to maybe help with bits of mixin compatibility, probabaly just an annotation you make for the mixin, probably just another field that just says, "Execute if another thing's present." In CHASM there is ways to do conditional tranformations. So we just need to implement some [conditional tranformations] with mixin-consistent formats. So I think you just add in an annotation that is ignored by Sponge mixins. So your mixin plugin works there. And on Quilt, you just literally say, "If mod is loaded." Which is, I think, by far the most common use case for conditional mixins.

I think I can also answer this one because it's fairly easy. **TheBlackSquidward** asks, "Are there plans to have compatibility with Forge?"
No, not officially. It's just not feasible to have an official support for that. However, Patchwork, as far as I'm aware, is sitll planning to happen on Quilt in the future.

**i509VCB**: Just to clarify about Patchwork, even though **Glitch** isn't here, I believe he is going to be continuing work on Patchwork when Quilt is released. So, this isn't really an immediate priority for **Glitch** to try for Forge compatibility at the moment.

**CheaterCodes**: Yes, Forge compatibility is kind of hard because it's just very different designed compareed to Quilt and Fabric.

**Juuz** asks, "Will creating resources programmatically in QSL (at runtime - think dynamic mod compat or something) prefer creating actual resource data and deserialising it, or injecting it into the recipe etc. managers directly?"

**LambdAurora**: That depends on the resource. For texture generation, you will have to create something that will deserialise it. We'll need to store bytes within a virtual resource pack. Because doing it another way would be way too difficult. But stuff like recipes, for example like a Recipe API is to be able to modify recipes and add recipes. The goal is not have to use actual resource data and just inject repeatedly into the manager, because it's faster. It's way faster to do that than spending time we could otherwise on deserialising it, storing duplicate data in an virtual resource pack. Generateing stuff generally should be prefered. If it's not possible, it won't be done. But if it's possible, it will be prefered. And that's it

**CheaterCodes**: Cool. Another real quick one. **Fish** asks, "Planned features for the future of Quilt?"
I'll just say, we'll move this question to the next meeting. Currently we're haveing some discussions about that, but you know, next time.

Alright, I think this is answered now? Due to it being answered in the chat, I'll just read it out for completion. **Tropheus Jay** asked, "Will these meetings always be at the same time, because if they do, I won't be able to make it to any of them for months and I'm sure I'm not the only one in this situation."
And **Gdude**'s answered with, "It's the time that worked best for team members when we first started doing meetings. Since this is the last meeting of the year, we'll probably take some time to regroup and figure out of if there's a better time moving forward."
Of course, timezones make it a little hard to organise them, but yeah, we'll figure something out I'm sure. There are some people who don't like geting up this early, some countries that don't want to stay up this late.

Alright, we have one more question that's fairly a general one. So I'll just read it out and talk a bit, and if anyone has something else to add... **Fish** asks, "What's the biggest difference between Fabric and Quilt in terms of code? And would require the most re-structuring in a mod?"
Now I'll be talking about this from a CHASM perspective since that's my thing. Of course, CHASM doesn't exist in Fabric, so that's a big difference. Mixins will exist in Quilt, it'll just look a little bit different. As we mentioned before, there will be some re-strcing requested regarding mixins where you should not use integer priorities and you should not use integer indices for local variables and that sort of stuff. And you'll have to move your conditional mixins to an actual conditional mixin rather than doing the mixin plugins. Anyone wants to add something with regards...?

**i509VCB**: Regarding the re-structuring, I imagine we will probably write some sort of guide closer to release about what changes you'd probably want to make to your mod when porting over. But I imagine that's something for ltr.

**LambdAurora**: I have an actual example of one part of porting. In Aurora's Decorations, I decideed to use Block Extensions API of QSL, so I have a commit so you can see what parts have changed. But for Fabric API and QSL, for a while we will be able to use the QSL-Fabric compatibility system. But it won't stay like that.

**CheaterCodes**: Alright. We've also closed the AmA so thanks everyone for participating. There's still very much progress in Quilt, and it's very exciting and I hope we can keep it up in the future. Oh, I forgot the teams of Community. But I don't think anyone knew anybody from there. I'm sure they have something to add next time. Some exciting stuff after the holidays. Yeah, thank you everyone for showing up in the meeting. I think we can basically make it a tradition now and we'll go into an after-party in the #dev-chat. So if you want to hang out and talk a bit, feel free to come. But regarding the official meeting, thank you very much and have a very nice evening, or day, or morning, depending on where you live.

**EarthComputer**: See ya.
