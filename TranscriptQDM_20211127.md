[Meeting: 27th Nov 2021](https://anchor.fm/quiltmc-dev-meetings/episodes/Meeting-27th-Nov-2021-e1au58n)  
Another public developer meeting - uploaded for your convenience! In all Quilt developer meetings, we start by asking all the development teams what they've been up to. After that, the community team talks a little about what's been going on, and then we accept questions!  
If you'd like to listen to our meetings live, or you have questions to submit, please feel free to join us - every two weeks, [on Discord](https://discord.quiltmc.org/).

=========================

**Gdude**: If you’re new here, this is just a collection of recordings of each public Quilt Project Developer Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks and recorded live by a fleet of Discord bots. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to [https://quiltmc.org](https://quiltmc.org).

=========================

**Gdude**: Alright, let's get started, shall we? Uh, it's good to have everyone here again. I didn't ping everyone this time, which I'm sure people will be appreciative of, somewhat. Let's get started with... **CheaterCodes**, do you want to talk about CHASM a bit? What's going on?

**CheaterCodes**: Yes, I would like to talk about CHASM a little bit. Lots has been happening on CHASM during the last 2 weeks. Last time I talked a little bit about how I slowly kept working away on the new version of CHASM that's hopefully no longer ~~poor tide~~, and there's really a lot of progress. As people may or may not have seen, we successfully had our first actual ~~Bedrock~~ transformations on the new version, and it works very well. After fixing some initial performance bottlenecks, we're now easily doing millions of transformations per second, so performance shouldn't be a problem. Which was a little bit of a concern in the past because we had no information on that.

I have been working on the CHASM-Lang a little bit, which is not public yet. Not sure if it's going to be the final version, but need something for development. And yeah, all in all, good progress. Feel free to check it out. It's worked really well. Contributions have been great. I opened a bunch of issues on the first day for the public, and people are very eager to help join in and tackle some of the easier and more complex tasks, which is really great. We're trying to do this for some other projects now, so if you're interested in doing some little things that always help out, there's always, always a bunch of stuff that people don't want to do because it's just a bunch of work that are not really hard.

(**Gdude** chuckles.)

Like for example for CHASM, it was... What was the top one? Ah, it was just re-format a big class that has like a single method with hundreds of lines of code, [then] split up into multiple methods, and it made the code so much better. Anyone can do that, but I'm more worried about getting the rest going. So that worked really well, and we'll try to do that for other projects as well. So that's cool. Um, yeah. It's not like we're going to have a full release on Tuesday for 1.18, but we're getting progress done. Really good progress, which is really cool.

**Gdude**: Yeah, it's quite impressive work, actually, considering how much longer you guys thought it was going to take to get to this stage.

**CheaterCodes**: It felt like- It really was like, you know this thing where it's like 80% planning and then it's 20% execution? It's like, CHASM has been about 99% planned-out until now. Protoype was mainly there for just more planning, and it's just such a good picture in mind of where you want to be and the implementation is just hacking away at the keyboard and not thinking too much about it. So yeah.

**Gdude**: Do you think the original estimate of, was it like 2 years, was a bit over-the-top maybe?

**CheaterCodes**: I don't know when that estimate was, haha. Yeah, there's still a bunch of stuff to do. There's still a bunch of stuff to do, because for example we don't have the logs implemented yet. And we're not entirely sure how to represent local variables or method parameters. All that stuff still neds to be figured out. But yes, for the most common things, the injects, for the simplest inject, that would already be working. So yeah. Looking very cool. Very excited.

**Gdude**: Great, that's excellent, great work has been done there. Yeah, I'm excited too. **SuperCoder79**, would you like to have a quick chat about Decompilers?

**SuperCoder79**: Um, yes. First of all, I would like to say that the Quiltflower-IDEA plugin is now available for everyone to use on the store made by **EarthComputer**. It's really good, I would recommend it. We also have a snapshot repository if you haven't been looking at the devlog. It has bleeding-edge builds for everything that we've been working on, which includes improved try-with-resources, switch expressions, improved line mapping once again by **EarthComputer**, the formatter by **EarthComputer** again, some more miscellaneous fixes and some optimisation.

Thr's also a 1.6.1 release to fix a few of the most glaring bugs with 1.6.0. It might be good if you're looking to recompile the game or something, but it's not too important, I think. I would wait for 1.7.0, because then you'll get all the cool stuff. I think that's it.

**Gdude**: That sounds great. It's always really impressive to see all the work coming from that project, especially coming from your hands. It's kind of ridiculous honestly, kind of good stuff.

**SuperCoder79**: Thank you.

**Gdude**: I think everyone agrees there. Alright, **AlexIIL**, **EarthComputer**, I think one of you is to talk about Quilt Loader. Maybe **AlexIIL**?

**EarthComputer**: Nah, I'll talk about what I've done. I mean, I've been working on merging upstream because like we've been falling quite behind on upstream. Um, *pfft*, just reading what **CheaterCodes** said.

(**CheaterCodes**: "dunno, I feel like I always pick up the projects earth got burned out on :pineapple:")

Yeah, so I got about halfway through that, fixed all the merge conflicts, and then I become kind of busy with updating my own mods for 1.18 because I don't want them to fall behind either. So **Glitch** offered to take over the merging upstream and he was going to do it before college originally, but apparently has not. He's not managed to download it, but anyway that's being done. Likely won't be out for 1.18 straightaway at least. **AlexIIL**, do you want to talk about some of the stuff you've done as well, because I don't know anything about that.

**AlexIIL**: Sure. So I've been doing a bit of work on loader plugins. They're still in fairly early development at the moment, it's not really usable, but they're progressing. That's about it sadly.

**Gdude**: That's alright, progress is still progress after all. Uh, OK, **OroArmor**, would you like to talk about Quilt Mappings? Yes, I said "Progress is still progress" and now I'm blocked by **haykam**, who cares hehe.

**OroArmor**: Haha, yeah. Quilt Mappings has been going on really well. We've been getting lots of PRs in the past 2 weeks. I think there's 4 right now that are almost ready to be merged in before 1.18. I think there's one that I need to go and fix up, that's a huge re-factoring of rendering, but I just don't have time for that. But it probably should be done because rendering code's not very great but whatever.

Other stuff, the build script for Quilt Mappings since last week has been completely redone. I have PR that re-wrote all of it into Java instead of Groovy, and it's a lot better now. It's a lot easier for the Quilt Mappings Team to add new features to that build script. So one of the things that we did is we made it so that you could decompile the game in both Quilt file and CFR (T/N: Class File Reader, a decompiler). Previously it was just CFR, so that's nice. Another thing that we're working on right now is adding ways to check that mappings are spelled correctly, that `public static final` fields are all-caps and underscored, stuff like that. So at least the names, er, not the names but the actual words and stuff like that have consistency. So you don't just see a field and see it as a constant even though it's something that could change.

**Gdude**: OK, certainly sounds like good progress as well. The rendering names are something that people have had sort of a pain point for a long time with Yarn, hasn't it.

**OroArmor**: Yes, I can attest to this personally. I have worked on Blaze4D, which we chose to switch to Mojmap because of some of the poor names. Hopefully I can get our team to switch back but I'm not sure about it. This PR is also just the first phase where I go for 100% mapping coverage in the rendering and ~~usual~~ stuff.

Oh yeah, that's actually a big thing I forgot about. Because we have access to Mojmap, something we've decided to do is migrate the Blaze3D packages - that's Mojang's Rendering API - into their own package if they are part of that package in Mojmap. So a lot of the classes in Yarn that are in `net.minecraft.client.gl` are actually part of the Blaze3D stuff. And so this PR takes all the rendering ones for that and moves them into `com.mojang.blaze3d`. And that's to make sure that you know, what you're looking at is more representative of what Minecraft's code is. Because Blaze3D was eventually planned on being taken out. So if it does go down the future, having it kind of in its own package is helpful. So that's nice.

And I think yeah, there's another thing here. Quilt Mappings on Loom got an update a while ago. It now works a little bit better and hopefully doesn't have as many issues, though I still see people keep popping up with issues and I'm like, "Oh no, I don't like working with Loom." Because it's a very big mess.

**Gdude**: Well, that seems to be the inevitability of Gradle plugins at this point, doesn't it.

**CheaterCodes**: If Gradle like fixes my issue that I opened on their Github, maybe I'll go back to Build Tools.

**Gdude**: Alright, that sounds like a lot of great progress on Quilt Mappings. We'll come back to you a bit later of course since there's a few more things to talk about, but that can wait a little bit. Um OK, **LambdAurora**, would you like to talk about QSL a little bit?

**LambdAurora**: Yeah. So, QSL. Since last meeting, I think we merged the Tags API, which means now there's a way to get tags easily. And the difference with Fabric API is that it has tag types, which means you can have clients in the tags, you can have clients ~~for bug~~ tags, and you can save your tags as required or ~~severed~~ by the client. Which are kind of essential features when you think about it, so yeah. It's cool.

It's not yet usable with Fabric API because there isn't a- Because Fabric API Compatibility Library isn't done yet. But it's also being worked on because since Quilt loader won't be available for 1.18, we'll try to at least make QSL available on Fabric instead through the compatibility- through the Fabric API Compatibility Library. Which means it's a re-implementation of Fabric API, but some parts we use QSL instead of its own implementation. So it both ensures compatibility and it ~~tells us~~ to use QSL.

And now, there's still a lot of PRs open which kind of require a lot of reviews. The most urgent one currently is the event phases one because it introduces some re-factors. And once it's in, it will simplify a lot of things, and it will simplify the Fabric API Compatibility Library. So here are a list of the QSL PRs that need some attention. And it's ~~???~~, so hopefully we can get something for 1.18 quickly. And the main goal is to have event phases before Nov 13th so that we can do the Fabric API compatibility quickly. It should also be available shortly, and I think that I've said it all.

Oh yes, there was also some changes. There's a run config in Loom which is 'Run automatic test server'. But in normal envs, it won't run. It won't be automatic because it will never stop. But now with QSL Base, if you include the `quilt.auto_test` with a number of ticks, it will automatically stop the server after the given tick time. So now the task can actually be used outside of test mods. So hopefully that can be useful for some people. The other thing I would like to review just as fast as we can is the Game Test API, so we can have some game tests in QSL from the start, so we can ensure everything is tested correctly.

And another thing we could do is make a common repository of test structures to ensure that mods don't break something. We could give to modders so that they can test stuff easily without having to reiterate common tests. So yeah. I don't think I have more to say now, so yeah, that's it.

**Gdude**: That is a fantastic amount of stuff, I can't lie. You've been super busy, clearly. If anyone missed it, **LambdAurora** did post a nice big list of PRs that need attention. I've pinned it in the `#meeting-chat` channel. So if you're a developer, you're interested in QSL, please go have a look. Go help those PRs get some reviews, get some feedback. Always appreciated.

(**LambdAurora**: "List of interesting QSL PRs requesting attention: [Add event phases. by LambdAurora · Pull Request #53 · QuiltMC/quilt-standard-libraries · GitHub](https://github.com/QuiltMC/quilt-standard-libraries/pull/53) - Event phases [Urgent][Item Group API by OroArmor · Pull Request #40 · QuiltMC/quilt-standard-libraries · GitHub](https://github.com/QuiltMC/quilt-standard-libraries/pull/40) - Item Group API [Command module by williambl · Pull Request #33 · QuiltMC/quilt-standard-libraries · GitHub](https://github.com/QuiltMC/quilt-standard-libraries/pull/33) - Command API [Block Extensions API by Leo40Git · Pull Request #41 · QuiltMC/quilt-standard-libraries · GitHub](https://github.com/QuiltMC/quilt-standard-libraries/pull/41) - Block Extensions API [Loot Table API by ByMartrixx · Pull Request #54 · QuiltMC/quilt-standard-libraries · GitHub](https://github.com/QuiltMC/quilt-standard-libraries/pull/54) - Loot Table API [port] [Entity Events module by williambl · Pull Request #42 · QuiltMC/quilt-standard-libraries · GitHub](https://github.com/QuiltMC/quilt-standard-libraries/pull/42) - Entity Events [WIP]")

**Gdude**: Alright, I guess I'm next. As for the Community Team, not a whole ton of things have been happening. I'd say the big one that anyone would have noticed is the change to the mappings commands. Now there is still issues with these commands mostly because Hashed Mojmap isn't quite stable yet. Which means Linkie-Core is- Well, it's not entirely working with it. As Hashed Mojmap progresses, hopefully we'll work with **Shedaniel** to fix that. But in the meantime, we've update them to slash commands and a whole bunch of fixes have been put in mostly by **sschr15**, or who we often wrongfully refer to as Chris.

(**CheaterCodes**: "@gdude I think `#devlogs` are also your domain for this meeting?")

Done a crapton of PRs in the background that you guys haven't seen. Yeah, that's right **CheaterCodes**. As **CheaterCodes** ments, we've set up different `#devlog` channels for each of the different Quilt teams. So for their projects, you can subscribe to the individual channels if your communitys or projects have specific interests in any team's work. They're also forwarded to the `#devlogs` channel on the Community Server right on the top there under information.

We've also onboarded a few more staff members. **Akarys** and **Alizée** who are part of the same plural system have joined the trainee team on, I think it was the 18th. And they're doing well, they've been helping us out, very professional work. Of course **Emmaffle** has just graduated today. Congratulations, **Emmaffle**.

**Emmaffle**: Hello, thank you.

**Gdude**: So things are moving along. Personally I have RSI, so I haven't been able to do too much this week or last week, but I'm getting better and I'll get back on track with that again.. Of course most of what I have to do is Cozy-related.

We also had a discussion about the plurality tools we're using, specifically Tupperbox. Some issues were brought up with Tupperbox and the approach we were taking to it. When I'm doing a bit better, I'm going to replace that with PluralKit, which as you may know is an open bot. And I'll integrate that with Cozy a bit better, so that should be a bit nicer for our plural users.

And of course, we had Trans Day of Remembrance on the 20th. **LemmaEOF** put out a great announcement about that with a few words, if you haven't seen that, go and take a look at that. It's a super important day basically for our community. Uh, I think that about covers everything that I can remember. Can you think of anything else **Emmaffle**?

**Emmaffle**: I think you covered everything.

**Gdude**: Alright, cool. As others have mentioned, if you have any questions to ask any of the teams, including Community Team, you can use the `/ask` command in the `#meeting-chat` channel. We're not quite at the point where we're going to answer questions yet. I had a chat with **OroArmor** earlier about how Hashed Mojmap has been- how updates have happened, and I think he'd like to talk a little bit about that.

**OroArmor**: Yeah, so, while I am talking about how Hashed Mojmap auto-updates and everything like that, you guys can send us in some questions so that after we're done we can go right into that. So, Hashed Mojmap is- The way that Hashed Mojmap is able to so easily auto-update is because Mojang doesn't change the names that they use very often, so that means that between versions, names wil be very consistent, so that you could compile down to the Mojmap names and your mod will work across multiple versions. The only problem with compiling with Mojmap names is that... Crash of course would be in Mojmap, I think there were issues able potential re-distribution. Basically, no one wants to compile down just to Mojmap.

So what we decided to do is that we can take the names and run them through a hashing algorithm, and then that hashing algorithm is then what we use. So because we only take the names from each version, that means that Hashed Mojmap has no concept of update between versions, which is one of the issues in Intermediary, where you have to match between versions manually. Which means that yes, theoretically that Hashed Mojmap will have more mismatches and you may need to compile your mod multiple times. But it also means that Mojang most likely changed their function and it has to be updated anyway. **CheaterCodes**, you want to say something?

**CheaterCodes**: Yeah sure. I think I want to clean up a little bit on like a few more reasons why we don't want Mojmap in general as well as an underlying thing. One of the big reasons for me is, working in a development environment, if Quilt Mappings is not perfectly or 100% complete. Which it never is because there's always new stuff added by Mojang, [so] it could be very confusing if you suddenly run into Mojmap names when working with Quilt Mappings at any time. So that's one of the reasons why we don't want Mojmap.

The other reason we don't want Mojmap is because it's not perfectly stable. You might think it's perfectly stable because it's the official name. But one of the very common things that happens is that Mojang moves classes around in packages and that will always break all the mods that are built for that version. For Hashed Mojmap we don't have that trouble because we always omit the package so that can't happen to us. And you might think, "Oh well, that can't be that bad if just a few classes are moved around." But yeah, it also changes all the decryptions and everything, there's a bunch of stuff that can go wrong. So Hashed Mojmap is good for that. Also having unique names is great.

**OroArmor**: Yep. And since Hashed Mojmap is essential just generated purely from Mojmap names, and it doesn't rely on multiple versions, that means we can update the names almost as soon as a new version or a new snapshot comes out. So one of the things we currently have is a Github Action that is supposed to run every 10 minutes, but it's not as consistent as that. But as soon as a new Minecraft version comes out, that ~~hashed for Quilt~~ runs automatically which allows us to update Hashed Mojmap without even needing any human input.

Which is really big because that allows not just modders to start working- Though there would be issues with that because there would be no Quilt Mappings - but because it allows people to start playing on the new version with mods compiled on the previous version, instantly. I see that as really useful for a lot of the technical YouTubers who want to check out new features, and for people who use mods like Replay or Iris when the new snapshot comes out.

We also plan on having similar workflow for Quilt Mappings. That is less planned out right now, but it is something that we're thinking about. So something that could potentially happen in the near future is that the entire Quilt Mappings toolchain - so both Hashed Mojmap and Quilt Mappings - will be able to be auto-updated hopefully within 15 minutes of the snapshot coming out. Completely removing the human factor of availability from that, which is something that both Quilt Mappings has had - not quite issues with, but like we haven't been super fast sometimes. And I'm sure that's also happened with Fabric. I think there is a time that where it took like a day for new mappings to come out for a snapshot.

But by doing this automatic stuff we allow for you guys, the devs, to start working almost immediately with new snapshots, new versions. So we don't have to wait for, you know, someone to show up and do that. Which is big because I don't think there's any- There's no modding toolchain for Minecraft that does this yet. So by doing that, it gives Quilt quite an advantage over the other toolchains.

**CheaterCodes**: Yep. If I may also add something onto this, one side is the user side, I think it's nice. Another thing is also- To be fair, I think it's mostly bragging rights if you update within 1 minute over updating like an hour. But one reason that I like it so much more is because right now there's always this pressure on the Quilt mappings Team members. It's like, "Oh, there's a snapshot out. Can any one of you make it within like the next hour to update this?"

Sometimes that's fine, sometimes it's, you know, you happen to be on the PC anyway. Sometimes like, the last few days, where it gets really at noon for my time, or early in the morning for like American timezones, it's really just not good to have this pressure on the developers to force them to be available at that time. So we really want this to be fully automatic to the point where nobody has to worry about it. There's still always going to be some manual matching involved with Yarn, I mean Quilt mappings. But the requirement should not be to push out a manual mappings update the first day. But it's fine if it takes 2, 3 days for the first update to come out because the initial update is at least good enough for most people to work with. Which is really just, yeah, it should really relieve the pressure.

**OroArmor**: And also the actual release versions of MC, because they have RCs (release candidates) and pre-releases for them, we will reach higher and higher mappings coverage and there will be less and less of mappings dropped. So when a full release comes out, you won't be missing, you know, 10% of mappings versus like, "Oh, they just refactored how all of entities work. There goes a third of the entity mappings in the snapshot." So it's not something that if you work on releases will be a big issues, but in snapshots there will definitely be stuff that changes. And it won't be too hard for us to change it around, but it won't be immediate.

**CheaterCodes**: Yeah, I forgot one thing. But I think I forgot it, so whatever.

**Gdude**: It's OK. Well, I see questions coming in. Is there anything else you two want to cover on mappings? Alright, I'll take that as a No. OK, in that case let's move onto the questions. Let's just have one second here. **LambdAurora** has deafened, hang on a second. **OroArmor**, would you like to take that question relating to Hashed Mojmap?

**OroArmor**: Yeah, uh, let's see. Is that the latest one?

(**!alpha**: "How do you guys plan on handling conflicts on hashed? Hashing does not guarantee uniqueness.")

Yeah, so, there are a couple of conflicts that can happen. One of the conflicts is we have two classes with the same name. The way we deal with that is that- So for classes where we just have the raw class name. So if it's like `net.minecraft.client.MinecraftClient`. So we'll hash just the `MinecraftClient` part.

However if there's two classes that have the same name - there's a couple of instances of that. There's some with `Tag`, there's some with `BlockStatePredicate`, something like that. If we have those, we then hash the entire name, including the package. As for methods, if there are two different methods with the same name, but different signatures, we add the signature into the hash. I don't think there's anything for fields. **CheaterCodes**?

**CheaterCodes**: There's technically no fields. I think, if I may take over, you're absolutely correct with everything you say. I think you just missed the point of the question. Sorry. I'm pretty sure the question is actually about hash collisions. Um, because, when hashing of course, it could happen that two different inputs give the exact same output. Sorry to cut you off there. Actually **EarthComputer** did a real quick calculation back in the day on the first RFC. I was just trying to find it. Couldn't really find it quickly though.

**Gdude**: Oh, I vaguely remember that, yeah.

(T/N: I also faintly recalled this discussion and dug up this [link from a year ago.](https://discord.com/channels/833872081585700874/833876911868346368/841410345876062219))

**CheaterCodes**: Yeah, I found it, I found it. It's a really, really low probability. OK, I found it. OK, he said, "Using the estimate that there are 5,000 classes in MC-" which is about right, and we want a probability of 0.01, we get that many bits and then he said, "7.6 digits is appropriate." And then I actually used 8 digits now, base-26 digits, which is actually more than this. So he estimated that if [in] every snapshot, if all the mappings were changed, and there would be a snapshot every week, then we would expect the time until we have a name collision in 190 years.

So we decided that's a non-issue. It could theoretically happen, but we decided that for one snapshot we have a name collision. But even if we had a name collision, the chances of them being in the same class, the same method and actually being collisions is really, really low. So it should not be an issue.

**EarthComputer**: Yeah, and that's if every single mapping was changed every single snapshot. You got to remember that most of the mappings stay the same every snapshot.

**CheaterCodes**: I think the question above that is more **OroArmor**'s area, expertise.

**Gdude**: Would you like to take **burger**'s question, **OroArmor**?

**OroArmor**: **burger**'s question: "> Can hashed work as an intermediary without Quilt Mappings? I forgot but you probably already said."

I'm assuming your question is referencing to: Can other mappings be built on top of Hashed Mojmap? And the answer to that is yes, absolutely. One of the reasons I have also been re-factoring the Quilt Mappings build script is so that other people can go and write their own mappings using this build script. Because if you try to use- Like it took me forever to figure out how to use the build script because it was taken directly from Yarn, and it was very- I mean, when I got it, it was 1000 lines long, and there have been a couple of things added since then. And so by re-writing in Java, I'm opening it up to more people so that they can use it easier as well. And yes, please make your own custom mappings for Hashed Mojmap. You know, just by having more people looking at the code, maybe you'll pick up a very good name, and Quilt Mappings will decide to incorporate it because we just like it so much.

**CheaterCodes**: OK, yeah, I'll take the CHASM one for the time being. So the question by **!alpha** is "Why does CHASM need a custom language?"

OK, so, I'll make this one a little bit longer of an answer. The short answer to that is that it doesn't. It just doesn't need a custom language. The long answer starts with when we made the first prototype of CHASM. There was some debate on what file format we should use, because you somehow need to- The mod somehow neds to explain what kind of background stuff and transformation it wants to do. So the requirements for language were basically, "It should be Turing-complete." That's basically all the requirement we had originally.

So the first idea was, you know, if we need a Turing-complete language, why don't we just use JVM-bytecode. That's Turing-complete, it works perfectly fine most of the time. That should be good. So we experimented with that a bit. Then we talked about caching. We need to make sure that if our input doesn't change- Well one goal of CHASM is that we can hash it. So if you don't change, mods don't change your config files or whatever, you don't need to re-apply all the transformations. The idea is that hopefully it helps with startup time. So we wanted it to be cacheable. So that meant that whatever describes the transformations you want to perform needs to be the same every single time.

So OK, we need to make sure that people don't use System Random in their transformers. And bytecode meant that we had to manually check the bytecode and verify that it doesn't use anything we don't want it to use. And JVM-bytecode, you can literally import it whatever you want and there's hardly restrictions on it. So we had to make a bytecode analyzer that verifies that nothing fishy is going on in the transformer. And one of the decisions we made after that long discussion was that we should probably not use the JVM-bytecode-

(**EarthComputer**: "ah yes the fridge verifier")

**CheaterCodes**: We should probably not use the JVM-bytecode and instead just make- use some other language that on its own guarantees that it doesn't like import System Random, that we can easily guarantee it's functionally pure. So that basically was the decision to make a custom language. Now what kind of form the custom language is, is not exactly sure.

(**asie**: "When proposing asm-regex, I was torn between validating JVM bytecode and providing a custom bytecode myself"

**EarthComputer**: "wasn't the main reason because bytecode is annoying to generate? and because it requires us to make a stable API")

**CheaterCodes**: The other reason- Thanks, I almost forgot about that. The other reason I didn't like JVM-bytecode is because- Two other reasons, thanks, completely forgot. Using the JVM meant that we had to provide a Java-facing API for CHASM which had many issues. We had to verify that everything was called at the correct time, that it doesn't call functions it's not supposed to call. Really restrict the API.

And the other reason was that basically everyone who tried something in ASMR ended up writing the transformer in Java and compiling it to bytecode. Which was not the point of the transformation. The point was that some front-end would generate. But it turned out really the only convention way to generate a JVM-bytecode is providing it in Java. And essentially that would mean that everyone who makes a front-end, neds to make a Java compiler and that's really not what I wanted for the project.

Yeah, so there's multiple reasons we wanted a non-JVM language. I was looking at other language options, like there's a bunch of stuff, and at the end decided, "You know I just always wanted to write a language on my own. I'm just going to write one by myself for now because it's fun." And there's no promises that this is the one we're going to use at the end. **Kroppeb** also has one that looks interesting. It's completely different, so no promises there. We'll see what ends up being the actual language.

**Gdude**: There's a couple other questions here, but I don't know if we can answer them without the Admin Team.

**OroArmor**: **Madilene**, I'm sure that there could be some way to- Because of how Loom works with layered mappings which is a blessing - even though it's horrible - that you could create a fully-encompassing mappings set that does convert the two. I'm sure someone will make a plugin that also takes the hashed names and converts them to Intermediary so that you can see the- easier to visualise namespace. Hashed Mojmap is definitely not something for people to use. It's definitely a backend. But yes, there could potentially be ways to do that.

And if I'm going to be honest, I would much rather see Quilt Mappings reach 100% coverage rather than have to make something easier to read. IDK when we can reach the 100% coverage, but maybe by 1.20? Oh, that sounds weird to say.

**CheaterCodes**: Hehehe. And yeah, one more thing to add onto Hashed Mojmap. Because one of the concerns that people had was about readability of hashed names. I personally think it's a non-issue, but I'm not going to tell people it's not. Maybe it turns out to be, maybe it's just for them annoying. But people complained that they think that letters make it less readable, and they'd rather have more numbers like in Intermediary.

Just want to say that obviously you can apply another layer on top and then very easily you might want to rehash the hashed names again and use numbers instead of the original names. So if anyone has any concerns about the ability of Hashed Mojmap then, I'm certain there's ways to work around it, if it really ends up being a problem.

**OroArmor**: Yes, and I would like to say that it's definitely not something easy to say to other people. It's like saying, "Oh yes, `c_asdfghj`," which is not as easy to say as like `class_310`. But I would like to say on the other hand that I was able to- Because I've worked with hashed names a lot, I was able to pick up some of them and it was pretty easy to understand what was going on anyway.

**CheaterCodes**: You know, there's some fun names in Hashed Mojmap as well. You know, if you use random letters and put them behind each other there's some really fun names to memorise. I'm not going to use them here because they're not all PG, so- There's some fun to be had there as well.

**Gdude**: That's very you, **CheaterCodes**, that's very you. OK.

**CheaterCodes**: I think we could probably answer **Glitch**'s question without an admin here, even though it would be better with an admin.

**Gdude**: Yeah, it would be better if they were here, but they're quite busy at the moment. You would be more familiar than I would with the entry method, if you want to handle that one.

**CheaterCodes**: Yeah, I'll take the first one. Then other people can join in if they want to, so then what's the first question that was asked today?

**Glitch**: "I want to contribute to `PROJECT`. Where do I get started? Also, how do I join triage teams for QSL and Mappings?"

So, first off, thank you for wanting to contribute to some project, **Glitch**. I'm sure you'll be around much. Uh, if you want to contribute to a project, the best way to get involved is to go into Discord, find the corresponding chat, go into that chat and say, "Hey, I want to help here." It'll take, less than - I don't know how long, not very long - for people who'll be very happy to have you there, very happy to have helping hands. And you can't possibly answer for all projects together. So go into the respective channel, ask there. It's very nice and chill if you go into a specialised channel, you actually have people there who are very specialised in that topic and actually know what they're talking about. So, works great.

Whr do you get started? Again, ask there, but if you want to have a general overview without like asking too deep of questions, you could always to go to Github: [QuiltMC · GitHub](https://github.com/QuiltMC). Look at the projects, whatever interests you. Maybe look at the PRs page, look at the Issues page. Um, we're trying again, we're trying actually to open more issues so that people can contribute more easily. Github or Discord are the top two ways. And for the Triage Teams, I think I'll leave this one for someone else. Someone from Quilt Mappings, QSL. Though I guess technically that is me as well.

**OroArmor**: I can speak for Mappings. Right now anyone that's interested in being on the Mappings Triage Team, I'm welcoming because I want to grow that team up so we have more people. The more eyes, the better in my opinion. So if you want to look at mappings and triage them, that would be greatly appreciated. I think it's probably the same for QSL. If anyone wants to talk about that, you can.

*Silence*

**Gdude**: OK too.

**CheaterCodes**: In general, the same logic applies: Go into the channel Discord, say, "I want to join the Triage Team," and you're most probably just going to get it.

**Gdude**: Alright. I guess I'll take this one. So **asie** themselves asks, "Have you looked into clearer communication outside of the Quilt community regarding the project's goals? I find that there's poor awareness of Quilt's technological goals, particularly its improvements and proposals. Just now, someone told me they thought Quilt is still in the 'many RFCs, little code' stage. I think it would be good for the project to communicate what benefits it brings to the player, modder and/or modpack creator over (or just like) prior solutions."

So this is a really interesting question. It's really difficult for me to answer without an admin here, since they have a little bit more familiarty with the subject in general. But there are a few things we're doing. Obviously these public meetings are one of the most recent attempts for us to get more people invovled in what's going on in the development side of things.

It's kind of tricky to get too specific in other communities. There are a lot of other spaces that do tangentially talk about Quilt and where Quilt is going and what they think about Quilt. It turns out, this is a lot of spaces.

(**Southpaw**: "Gdude your microphone is doing real bad pops")

**Gdude**: My microphone should be fine, **Southpaw**, please, please. What, is it too loud?

(!alpha: "yea its peaking a lot"
LudoCrypt: "its popping" **Glitch**: "it's popping a lot" **EarthComputer**: "it's not awful")

**CheaterCodes**: Kind of. Just keep going for now, it's not that bad.

**Gdude**: Uh, maybe my Internet's dying. Does that help a bit, does that sound a bit better? Alright, there we go. OK, sorry about that.

Yes, I was saying that there's a lot of spaces that do talk about Quilt and where Quilt is going. It's a little bit difficult to insert yourself into those discussions. I think it is important. I've actually been doing it somewhat. Actually I've seen the same things you've seen, where people think we're still early-planning stage which, yeah, you're right is not true. That's not where we are. But it's quite hard to get the word out in that sense. I guess we should probably use stuff like Twitter more, give people easy ways to share the information that we have. Unfortunately again, I have RSI now, so it's kind of hard for me to handle managing all those things at the moment. I would maybe want to delegate some of that? But we'll see.

But as for broader strokes, it's kind of hard for me to come up with specifics without the Admin Team around, which is unfortunate. Yeah, I'm not sure how else to address that. You're (**asie**) typing for a while, so I'm assuming you have comments on what I just said.

**CheaterCodes**: Right, who else is talking about popcorn?

**Gdude**: **asie** says, for context-
(**asie**: "Honestly I thought you are in the 'little code' stage still until today!
The public meetings are a good idea in-community. It would be good to mirror them to social media platforms to allow people to distribute them outside the QuiltComm bubble. Personally, what I'd recommend is maybe reworking the front page of Quilt to be less "description" and more "pitch"?")

(**Southpaw**: "I've had an idea of throwing it into a podcast feed")

Yeah, I agree with that. And as **Southpaw** said in chat, we had the idea of throwing it into a podcast feed. I was looking into that before I somehow hurt myself. Yeah, again, I agree with you, it's something that we should do. We should make these things more accessible and easier to listen to. Not just for a case of getting things out on the platforms, but maybe re-formatting them after the fact to be more listen-able. Because you know, there's a lot of thinking between questions when we're doing it live.

As for the website, nobody's touched it for a while, and I'm kind of sad to admit that. But I've been busy, I got RSI, **Fork**'s been busy, and **Fork** is the main person that's been doing the website. We have big disagreements on how websites should be designed, but he knows way more about front-end than I do, so I just kind of let him at it.

(**burger**: "the statistics stuff is cool")

**Gdude**: Heh, **burger**'s talking about the statistics stuff. Yeah, it is cool. You know, that all it is for most of you.

**CheaterCodes**: Yeah, we should also try to be a little bit careful with this, I think. Because yes, while some hype would be good to get us going, eventually we are most worried about being over-hyped recently, especially with the 1.18 release coming out. We're a little worried that people expect us to be fully ready for 1.18 and we're not, and then it's going to be *much* worse.

**Gdude**: Yeah, fully agree.

**CheaterCodes**: While I do agree that it would be good to have some more people being aware of it, we don't want people to be sitting there for like 2 years constantly checking like, "When is Quilt ready, when is Quilt ready?" And then just forget about us. Yeah, so that's another thing. "We have too little exposure," was never something that was on my mind. I was more worried about, you know people want us to be ready now. What can we do to not over-promise anything?

(**asie**: "Forge (and many other non-modding projects?) do summaries of meetings as another option.
Either way, good luck with this project, everyone. I'm glad you're taking a concept I contributed to and taking it into new directions ing that's how we can get not just iteration, but innovation. I support Quilt's continued existence \uD83D\uDE1B")

**CheaterCodes**: Yeah, yeah, what you're saying is totally true. More people should be at least aware that we are progressing and not just- "Oh, I remember hearing about Quilt, but I don't think it went anywhere." Yep, no, totally, totally agree.

**Gdude**: Yeah, I agree with you but I forgot to say that. We've always been pretty conscious of over-doing the hype. And you know, some people were hoping we'd have a full release by 1.18, or release the Beta. We're not at that point. We'd hope to be, but you know things aren't always going to work out the way you think they'd work out, and this kind of work is always the kind of thing that's going to take a while to do.

But yes, I agree, we should spread ourselves out a bit more. I think we can do that without over-doing the hype. I think a lot of it is going to be about, well not mood necessarily, but just ~~tithing~~ how we promote things. But I don't think we need to go super hard on that still. Just utilising what we have more and then feeds up would be a great thing, I think.

**CheaterCodes**: Yeah, I mean, eventually we could just publish the devlogs to Twitter or something, I don't know. That would be a fun idea. I think **AlexIIL** can do that one. You already kind of answered it.

**AlexIIL**: Yes, OK, so **Lith/Helium** asks, "Are there still plans on auto dependencies downloading?"
And the answer is, yes, this is what loader plugins will allow us to do, in a sort of general fashion, I guess. So yes, that's definitely- we definitely still want to have auto dependency-downloading. We're just not quite there yet.

**CheaterCodes**: I think I'll just take **kb1000**'s, because it very team-agnostic again, so it's not like a single person could answer it anyway. But I'll give it my best. **kb1000** asked, "What teams need help the most?"

I'd say, top spot by far, Build Tools. ~~Bcz currently~~ no one wants to do Build Tools. So if you're into Build Tools, if for some reason you like using Gradle, like developing Gradle plugins, please, please hit us up.

I think the other one is like, QSL and Mappings could always use help. It's a very easily parallelisable task, so there's never a point where it's like right, you can't work on this right now. So QSL and Mappings for sure.

For CHASM I can just say, I'm just hoping for inputs. There's some issues where I'm just hoping for more deeper discussions, I really hope people can just give inputs on those. Otherwise, that's in a fairly good spot right now. I'm sure there will be more issues in the future. Um, I'm not sure if- I think Quilt Loader's a little hard right now because they're an emerging process. I'm sure I forgot something. Nah, I think that's pretty much all of them.

So I'd say most help is neded on Build Tools, but you can always help with QSL or Mappings because they never run out of work anyway.

**Emmaffle**: Right, thank you. It doesn't look like we have any more questions. So it is about time to end. So, if- Unless anybody else has anything else to say, or any other questions to ask, then do that now or forever hold your peace.

**CheaterCodes**: Yeah, I think we went through about all of the questions.

**Emmaffle**: Well, in that case, I guess we can conclude this. Well, thank you everyone for coming. And hopefully we can see some of you the week after next.

**CheaterCodes**: Looking forward to it.

**EarthComputer**, **OroArmor**, **LambdAurora**: Bye.

**Emmaffle**: Bye bye.
