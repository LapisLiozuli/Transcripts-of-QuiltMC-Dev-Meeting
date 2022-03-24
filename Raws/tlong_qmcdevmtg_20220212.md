20220212

**Gdude**: Did I accidental click the "Ping Everyone" button again? Yeah, I think I did, haha. Can someone on the Mumble side say something to make sure it's working?

A: Hello

B: Something.

C: Hello

**Gdude**: Excellent, thank you. Meeting blows up, immediately deflates. Yeah, you see, that's what happens when I accidental ping everyone. Someone's going to complain, I bet. Yes, so for those of you that aren't familiar or haven't been here for the last meeting, the bot we were using to record the meetings was thrtning to be dead. It turns out that it's not= that I'm not paying for it at the moment, so we're using Mumble so that we can record instead. Um, it does a lot of the stuff that we need for **Southpaw** to make the podcast, so, that's why we're useing it.

So everyone is there on the Mumble server, on the other side of that Mumble bot. That's basically the gist of it. Make spaceinglaser noises because people are seting Avatar, not Avatar, what's the word, bios, profile bios. You can turn that off. Anyway, I'll give it a couple more minute and then we can get started. Same format as always, of course. I'm going to try and remind people to say who they are the first time they talk, so that everyone knows for the sake of the podcast. Hope you people don't mind, but that's alright I'm sure. And we'll try to read out the question as well.

Spking of question, if you have any, use the /ask command, and we'll get to them at the end of the meeting. Probably, hopefully. Don't worry, I've got a list. For those of you on Mumble BTW, I think I'm going to stay on Discord for audio. It's just much harder to mess up my audio setup that way. Is that OK? Can you record that OK, **Southpaw**? I assume you can. Nobody else will be talking on this side.

**Southpaw**: Alright, works for me.

**Gdude**: What good is an alt if it's not on the server, right? Alright, in about a minute, we'll start.

**Southpaw**: You make it sound like some kind of perfume. Permission, by **Gdude**.

**Gdude**: Alright, I guess we can start. Y'all ready? Alright, let's get started. First on my list = I tend to go in alphabetical order, you may have noticed = Build Tools. **Glitch**, would you like to have a word?

**Glitch**: OK, sure. As always, there hasn't been much in the ways of Build Tools. I ended up doing some work since last time I talked, on VanillaGradle, being able to remap the cmpled mod to Hashed or Intermediary or something like that. But that ended up going on the wayside because I rlzed I can make Loader mostly work with Fabric Loom. So I ended up spending my time working on Loader instead, because once Loader's working, we technically don't need to use a custom Build Tool. We just have to give up some things, like we can't use Hashed, and that's pretty much it, really.

**Gdude**: Alright. I mean, hey, progress is progress, and it sounds like some has been hppning, which is excellent. Uh, next on the list is Community Tools, me. Sprz sprz. Cozyingwise, not much. We've been looking into a new thing we're testing, which Discord is, has= well, we're testbed for yet another thing, I guess. We're testing slash command permission which is a new thing on the community server. There's not much to do with Cozy right now, because it's not on both server, so I can't like change anything to use it. But we've set it up, and you'll see like, some of the slash command are greyed out, and eventually they'll be hidden, we hope. Otherwise, Community Tooling hasn't been doing a ton.

I have been redoing the website. It's going quite well, I think, anyway. I'll give you a link. I've put up this like, sort of testing site so that you can see how it's going. Yeah, I'm having fun. But there's still a lot to do. I'm working on the About pages right now, and I haven't pushed them to the side because we need everyone to agree on them. But yeah, when they're done, they'll be up. There'll be a nice timeline and all sorts of things, like ~~Fat~~. Still going to be a while, if anyone has any feedback that's the link. Let me know how bad it is. Otherwise, that's about it at the moment. I'm actually resting today, so don't yell too loudly, hehe.

Alrt, next on my list, is Loader. **AlexIIL**?

**AlexIIL**: Yes, as **Glitch** mentioned, he's been upd8ing from Fabric upstream. That work isn't quite done yet. I'm working on it a little bit as well. We're quite close to being able to be upd8ed, which is good. I think that's about it for Loader.

**Gdude**: Alright, good stuff. Thanks **AlexIIL**. **OroArmor**, would you like to talk about Mappings?

**OroArmor**: Yeah, just give me one sec. Alright, yeah, so Mappings obviously we had 21w05a and 22w06a. There weren't a lot of changes for 05a, but 06a obviously w all the tag changes that introed a lot of stuff that could be lost. Luckily for us, w **LambdAurora**'s amazing mapping matcher we were able to save, about, like just over a third, maybe 40% of the mappings that we could lose, so that was very good. So we have those still. We got lots of PRs that were merged in, even more from 22w06a, so that QSL work could start. It's definitely a really nice uptick in the work.

And then, another thing is **CheaterCodes**  and I are currently in the very early stages of changing how mappings and the Quilt environment work. One thing is multiingversion mappings so that the same mappings can target multiple version, so that when changing between version you don't have to lose mappings or old version still get updated. And another thing on top of that is we're also considering that mving away from Tiny as the frmt for mappings on the Quilt ecosystem just because it's an extra step and all the data that Enigma has, Tiny also has, essentially. So yeah, those are the gist of what Mappings has been going through.

**Gdude**: Thanks for that **OroArmor**, sounds like a lot of progress either way. And good work on that **LambdAurora**. Speaking of that **LambdAurora** ld you like to talk about QSL?

**LambdAurora**: Yes yes yes, so in the last weeks, we had ~~12~~ snapshots. So I don't remember exactly when the last meeting was.

Last meeting was the 29th, I think.

Since then, we merged the Tooltip API, which introed some new cool bugs like the item tooltip one, and some related to tooltip component, w convertible tooltip data in the files for tooltip data. So a lot of new utility, some nice stuff. And either one of the dfrc with Fabric API and that API is, we can use some of the new features ``feat and interface. For a long time, it wasn't possible to injk into interface. So now it's possible so it's much cleaner.

And the other module that has been merged is Networking API. What's wrong that has been due to w 22w06a, which was quite painful, because Mojang mved a lot of stuff and kind of wrecked tags. But it's for the better. Now we can actually have tags for any ~~linking trees. What I found awful there, in the API~~, so that's nice. But it czed some issues w QSL porting. Bsc[[ we had to disable the Tags API for now until it gets properly rewritten.

And there was a little db8 we had a month ago, that had to be brought up into the table again, which was more than two point in QSL. The main issue was, we think game entrypoints loader doesn't make a lot of sense, because it doesn't make it really gameingagnostic, or version ingagnostic as it need a quite lengthy injection method, which uses raw ASM. So that's terrible for maintenance and it means that for new version that change the entrypoint logic, it require a loader update. The thing is, game entrypoints loader are kind of useless in some way, it's because normally when you use an entrypoint, it's because you have an API to call stuff to look into. If you don't have an API, you are most likely to use entr[ mixins.

So we did a little vote and turns out a lot of people think that it's fine to move them to QSL, so we did that. And just to be clear, the preinglaunching point still in the loader, which still can be used for loading if you have a big mod. And the module the entrypoints has been moved to is the most small module of QSL. Basically it doesn't have any dependencies. It only contain the event framework. Little utility for multiple testing server and well now, the game entrypoints. So it's generally easy to jaringiningjar it if needed. That's all for now. There are still a lot of new PRs to go through. Yeah, I think that's it.

**Gdude**: Thanks for that. That's certainty quite a lot to be geting on w in one fortnight, isn't it? Excellent, good work. Now before we move on, do any of the project have any outstanding PRs or anything that need looking at by the rest of the community?

**Glitch**: QSL can always use looks on everything. Please feel free to look through. Even chking grammar on Javadocs is helpful. You don't have to understand what's going on to review a PR. And every bit helps.

**OroArmor**: I'll also say that if you want to look at Mappings, PR #5 on Quilt Mappings can always use review. Yes, it's 2000 lines long. Yes, it touches every single part of what Quilt Mappings does. Yes, it's scope has creeped. But those rendering mappings need updating, and I kind of just fixed a bunch of things as well as I came across them. So if you find any issues in that, I will definitely be glad because there's a lot to look at, and we haven't impled a spellchecker yet. But that's something that will come eventually.

14:15

**Gdude**: Alright, that's good. Now, we should probably talk about what hppned inrl[ recently, right? It was proposed.

It fits you.

**OroArmor**: Should I start talking about it? Or, I don't know.

**Gdude**: You can talk about it, I don't mind. Basically, this is an organizational change. Everyone here knows i5, obviously. He isn't here at the meeting today, he's actually quite busy. He is stepping down from the adminr position at Quilt, because he's mving on from MC modding in general. But he's still going to be around just to answer question, but he's not going to be active here. Now, as you may know, if you've read our RFCs, we need at least 3 admins, and we need an odd number of admins. This means, of course, that we have to hold an election. If you've seen the recent changes to the governance RFC by **CheaterCodes**  = I think the PR is still open, it hasn't been merged yet = we dcded to follow it and go w ranked choice voting. Now, turns out we only had two candidates, so it was a bit of moot choice for us, but we dcded to use it anyway and it worked out just fine.

We have a whole system where we use a website which generate a unique voting link for everyone, so everyone gets their own link. And only once the thing is closed can we get at the results. So there's no, "Oh, this person's getting more votes, I'm going to stack a vote on top." you know. So nobody can see who's voted for what and nobody can see what the votes are looking like until the poll closes, include the person that started it.

Anw, long story short=

**OroArmor**: Who gets to vote?

**Gdude**: Everyone who's part of the Community Team, or the Development Teams gets to vote. So any Quilt Developer Team, anyone in the Community Team, moderators, events people and of course the adminrs. I'll drag it up in a few minutes or somebody else can, if they want to check, it's pinned to the thread. Anyway, so we had two candidates and the candidate who ended up winning the vote by a margin of like 3 votes was **OroArmor**. So congrat**OroArmor**ro. This is no srpz to you at all, but hey.

**OroArmor**: thank you TY thank you.

**Gdude**: Indeed. So, we'll be setting **OroArmor** up sooningish. We need i5 to transfer a few things over. But yeah, that should be nice and smooth. We don't have an ETA but it should be fairly smooth, hopefully. And yeah, we're looking forward to working wit**OroArmor**ro, to be honest. Great choice, great choice. If anyone wants the results link, you can have it. But it's two candidat**OroArmor** Oro won by 3 votes.

Alrt, so if anyone has any questions they want answered, use the /ask command. We got a couple in already, so we'll start going through those in a sec. It's /ask. You can ask bsc[[ anything you want, although try and keep it somewhat relevant. OK, let's have a look here. **CheaterCodes** , do you want to take that one? Don't forget to read it out.

**CheaterCodes** : Yes, I will take it in 2 minutes.

**Gdude**: Ok, that's alright. Let's look at the other one here. Uh, I will throw this one out. Silas is bsc[[ asking about the possibility of security disclosure system. Uh, yeah, we're going to have something. We haven't really talked about it yet, hehe. I do believe that Github has a system for it. Yeah, **Southpaw** says, Github has a system for it. It'll almost certainty just use that. Honestly, we haven't talked about it yet. If you have any suggestion, we'll take them of course. But yeah, I imagine Github system is probably the most likely thing we'll end up using for that one. Yeah, they do, I haven't used it much, but they definitely do have one. Because I know= I have some friends on the Python server that have used it. There's a button you can click which makes it CVE. Yeah, so there's a whole thing there, I just haven't used it much. Are you ready for that question, **CheaterCodes** ?

**CheaterCodes** : Uh, let's do it now. Alright, so, question by Trollzer, "Why are we switching to a less supted file w less fetrs?"
Now, this is what we're talking about before, that we're considering dropping Tiny and just using Enigma mappings instead. So I want to go over quickly about the reason. I guess why I brought it up, really. If you're aware of how the Quilt Mappings works, you'll know that the Quilt Mappings repository is in an Enigma frmt. So, Enigma support splitting the mapping files up into a directory tree of files, so each class gets its own file, which is not supted by Tiny. This is much more convenient for Github PRs. It's more easily visible who changes what file when you make a PR. So it makes more sense to use Enigma.

And if you then compare Enigma and Tiny, you'll notice then that they're bsc[[ exactly the same. So, there's 3 differences really. Difference #1 is that Enigma uses complete words like 'class', 'method' and 'arg', instead of single letters like Tiny does. The second difference is that Enigma handles nested classes as nested classes. So mappings for inner classes are members of the outer class mappings, whras Tiny has changes that amount to flat mappings. And the third difference which is possibly the most relevant one is that Tiny support multiple namespaces.

So in general, the frmts are quite similar. And what we've talked about is adjing Quilt Mappings to allow for soingcalled multiple MC version in a single thing, which would mean we could extend Enigma to use specified version ranges for mappings or transitive mappings or something. Another thing is that we've consider puting ~~Amplick~~ into the mappings frmt itself or the annotations, like changing Obfuscated to over it only. Annotations also put that into Quilt Mappings.

And if we did that, we would also have to change Enigma mappings, because that's what the repository uses, and we'd also have to change the Tiny mappings. It also means we have to continue mntning the Tiny ecosystem, which is Tiny Mappings Parser, Tiny Remap Pile, there's like 5 or 6 of them. Each of them has their own Tiny Mappings Parser, and readings and writing system. They're all undocumented, not written by us, and we would have to maintain them for no reason. So we csdred droping this in order to lessen the maintenance burden.

What is the reason, we asked, what is the reason we even have Tiny in the first place? But we couldn't really get a conclusive answer. There were some who were like, "It's better for compressibility." Which is not wrong. "It's better for parsing, it's easier." Which is not true because they are bsc[[ the same file frmt. So the only thing is multiple mappings, multiple namespaces. But single files = thanks Skyrising = the arg] was that can have a single file, but Enigma also has single file frmt. There's not much benefit to using Tiny, but we would have to maintain a lot more stuff. We don't feel like mntning software which we have no use for.

**OroArmor**: **CheaterCodes** , there's another question that's fairly similar. I think I'll pop in here a little bit too. From Sher15, I always forget what we call you, "If fully switching to Enigma mappings, would new features be added to the frmt or would it be more of a fork in the future?"

We've talked about this a little bit, Chris, yeah. There are a couple things we do want to add to the frmt. Not too much, and it's something that can be done through a property tag on something instead of a more complete xpnding of the frmt. There's not too much we want to add, but there's just a little couple things that we definitely could add that would definitely improve the frmt. But as it stands, I don't think we were super into considering that. I don't exactly remember from our conversation yesterday, or two days ago.

**CheaterCodes** : That was two days ago. I couldn't actually find upstream of Enigma anymore. I'm not sure if it still exists. The Bitbucket link is dead, and the website links to the same Bitbucket link which is dead. So upstream Enigma doesn't really exist, so... We're now on anyway.

And, of course, I don't think we could just keep calling it Enigma. We could just make it Enigma v2, we have to see how that works out. There's definitely going to be an RFC, and you can comment on that once we have that. We just wanted to give you a quick headsup on what we're talking about inrl[.

**Gdude**: Alright, thanks for ansing those. I'll take this one. Jello is asking, "What is the ETA for the Cozy Discord modularisation issue? What modules are planning to be created?"
As always, no ETA. Again, it's really just me working on these. It's going to take a while. I'm planning on factoring out pretty much everything that isn't Quiltingspecific though. So the filtering system, the user cleanup system is already done, kind of. What else is in there? The thread management system. Bsc[[, everything that Cozy does will be modularised deliberately to make it possible for other bots to use the modules. So yeah, if you like something that Cozy does and you're not using a fork like Chris is, then this will be interesting for you. But it's going to be a while, because I have a lot to do. **LambdAurora**, you want to take that one?

**LambdAurora**: So, "Will Quilt end up with a Biome API/Wanderer API to make working with 1.18+ version biomes far easier?"
Curr[, it's really hard to say when it will happen. Because there's a lot of modules to work on w QSL. The thing is, in the current ecosystem, there's not a lot of version people, so unless there's one that sits down and starts writing something, it might not happen right now. It's really hard to answer that question because we don't know when it will happen.

**Gdude**: Thanks for that one **LambdAurora**. There's another one there from Trollzer, can anyone take that?

**Glitch**: Trollzer asked, "Will Loader still support the Tiny Mappings?"
I can't see a reason why we'd remove support for the Tiny Mappings, so yeah, I can't see why we would do that, bsc[[.

**Gdude**: There's no reason to not support that, so probably it will support them. Yeah, that makes sense.

**CheaterCodes** : The big difference, I want to add to this. We would not be actively mntning most of the Tiny toolchain, like, it would not get any active new feature, anything. It's bsc[[ just delegate to just kping the status quo and maybe just kping Fabric compatibility.

**Glitch**: Yeah, we can just use the Fabric libraries for parsing Tiny for that, so that won't be too much of an issue at all.

**OroArmor**: We also, yeah, I'm not exactly sure what my plans are, but we will probably be mking something similar to mapping.io and we can have our parser in there and then not have to necessarily use the Fabric library anymore and then kind of remove some of the old dead !! toolchain stuff.

**Gdude**: While we're here, **LambdAurora**, that looks like one for you, maybe.

**LambdAurora**: "Curr[ QSL is not up to feature parity with Fabric API. Are PRs for modules with no analogs to Fabric API modules be csdred at the same priority level for future release alongside those other fundamental modules?"
It's kind of hard to tell, because it really depend on the feature. There can be some feature that can be csdred essential but isn't in Fabric API. I can't think of an eg right now, but there might be some. If you take for example, the Tags API, it's not a straight port. There's lots of new features that do not exist totally in Fabric API. And currently Fabric API do not even have a Tag API anymore. So there's no analog. I think it should still be csdred w a high priority because tags are really important.

Mb take for example, there's a PR called common module "R cells and Argen types"? That's quite a useful feature, so I think whatever comes should be csdred maybe w the same priority level. I think it really depend on the feature. Some feature from Fabric API itself, are not really important to port like right now. ~~For initial readings~~, the priority is to have out something usable. it's not to have an exact oneingtoingone port. So if you want new feature, feel free to PR it, or discuss it just= It really depend. There's a possibility that new feature are csdred as equal priority to existing feature in Fabric API.

**Glitch**: To kind of add onto that, having= Being Fabric API at initial release is not a goal for us, because there's no real reason to use QSL. We're more concerned with new feature right now. But there will be a time when we're trying to drop having to maintain Fabric support, that catching up w Fabric and grabing everything we missed will become a priority. Because we don't want to strip away Fabric API and leave people w only half of a usable API.

**LambdAurora**: I have something else to add. If you take for example, the Keybindings API PR, it both support new feature too. It ports the basics of the Fabric API Keybinds stuff, but it adds much more. Like for example, the ability to dynamically disable keybinds, or the ability to show tooltips on keybinds that conflict to show which keybinds conflict exactly. And stuff like that. So some stuff are better for mod intering compatibility. It's not just straight ports. It's really new stuff, or existing stuff that isn't present in QSL. The idea is to bring in as much features as we can in the API to ease development.

**Gdude**: Thanks for that, folks. Silas is asking, "Will we continue to hold meetings like this, or will we go back to Discord?"
We don't really have a good answer for that one. Mumble is working quite well. It doesn't rely on somebody else's bot. I'm actually hosting the Mumble bot and the Mumble server. Now, while it was convenient to use Carl on Discord, there still ~~left with~~ a lot of work on it. Sorry, Craig, not Carl, thanks **Southpaw**. Basically what hppned was, Craig was destined to get yeeted basically. The developer was kind of done with it. Some other people have tkn it over, but they're doing a lot of work on it at the moment, so we don't know whether it's likely that we'll go back yet. We may decide to, we may not.

Either way, we're always going to keep it accessible on the #stage channel. So, like, you'll still be here to listen to it. But yeah, I'm really not sure, I don't have the crystal ball for that unfortunately. I understand that there's definitely an aces] bonus for it. We had the idea of actually screensharing the Mumble chat, but then we rlzed that stages don't actually have that feature. So yeah, maybe if Discord implement it , we'll do that. Maybe we'll go back to Craig. We just don't know yet, unfortunately. **AlexIIL**, would you like to take on Octal's question?

**AlexIIL**: Sure, so Octal asks, "Are there plans for the QSL module downloading?"
The answer is yes. Yes, there is. This is part of= This is going to happen w Loader plugins, or just after Loader plugins. It's not specific to QSL. As it is, currently the idea is you'll be able to set any libraries to be automatic downloaded if they're not present in the user's mod folder. There hasn't been any progress on this in the last 2 weeks, so I didn't mention it, but yes, there are still plans and it will still be impled, just not yet.

**OroArmor**: Adding on, security and things like that are a big concern for us. When we talk about, for like 30 seconds on an idea, what this is going to look like, it is not a full picture of all the precautions we will be taking, and things like that.

**Gdude**: Woody asks, "Will there ever be transcription?"
I'll has to check w the coalition. Would you like to make them? Hehe. Uh, it's a lot of work. There are no good atm8ed solution, or at least the ones that are good are quite expensive. So, yeah, like, we don't really has plans to do that. Nobody has the time to do it. Uh, if somebody does it, great. We can't. nnal, I think that one's yours?

nnal: Alright, **Southpaw** asks, "If any libraries could be automatic downloaded, how does Loader know where to find them?"
How exactly this will work is going to be put into an RFC, and talked about properly, so that we have a much more specific idea of how this is going to work, and how we're going to keep it secure. Basically, how we're going to download the correct libraries and whatnot. So, it's a bit early to talk about this specifically, but just know that we will be talking about this, or we will be dscsing this in more detail when we get to the point where we can actually implement this.

**Gdude**: Uh, Woody, yes, manual transcription are out of the question, it's just too much work. I has a lot to do, the others has a lot to do, **Southpaw** does the podcast and they already has to put in quite a lot of effort there. Again, if someone wants to listen to the podcast and do it, great, but we don't has time. We just don't has time. **LambdAurora**, yeah, you can take that one if you like.

**LambdAurora**: So, "What is the I/O process to go about reqing modules to QSL? ~~Issues first~~, I asked on Discord for proper PRs, OK."
I would say to avoid proper PRs in some way, unless it's support, but even then, dscsing first might be better, because there might be some= Because usually when you PR, it's about code review and stuff, it's not about the concept itself. It means you already put a lot of work into it, so it's kind of a risk to take. Because it means that if it doesn't fit, or if there are a lot of design issues, it might require a rewrite. I don't think anyone wants to do that. So my ideal process is issue first, or ask on Discord. It's up to you. Just keep in mind that if there are some people who cannot use Discord for X or Y reason, Github Issues might be more visible. But at the same time, Quilt is really a very Discordingcentric community. But I would say on Discord, you might expect much quicker resps.

**Gdude**: Thanks **LambdAurora**. **Glitch**, do you want to take that one?

**Glitch**: OK, Chris asks, "For the uninformed, can anyone submit RFCs if they has a good idea?"
The answer is yes, you are allowed to make any proposals you like, whether that be, you want to write on an RFC on a new API, or you want to chg how adminrs are elected. Anyone is allowed to propose anything they want, obviously it doesn't need to be acpted, but we don't has any restriction on that.

**Gdude**: Obviously any proposal that is in faith a good propose, we'll definitely give it a go. NoComment asked, "Will there be a wiki similar to the Fabric Wiki?"
Yes? We're planning on two wikis, actually. We're going to has a Developer Wiki. I think **OroArmor** has some work done on that already, right?

**OroArmor**: It's very basic, just kind of like prototyping a prototype kind of work. Obviously this is my vision for what I would want the Developer Wiki to look like, and it would have multiple version similar to what the Forge Wiki. But what would be nice is if it would be built into a Gradle project, so that it forces chgs. you know, like chgs into Loom or something like that. Force us to make sure that whatever is written still works, so that there's no tutorials that just no longer work. Like they don't compile, or the mappings has chged, stuff like that. So every time you go and look at the wiki, that whatever code you see there, does work on the version you're looking at. So that's something that I want to make sure that we has. So right now, I think we has a very basic thing where it's a Gradle project that reads some MD files, parses that, and makes some HTML files. But it's not very good right now, and it's like, in one file it's 300 lines long. So it works, but it's not great.

**Gdude**: Right, so that was regarding the Developer's Wiki. We were also planning on having a separate one for useringfacing things. It could be a simpler setup, since we don't need all the developer side stuff for that. It might be a bit more accessible for modifying it as well. Again, like this is stuff that we can kind of sort of work on at the moment, but there's other things that we should also be doing at the same time. So I think like, we will get them done, ideally before release, but we'll has to see how things go.

Arathain, you asked a question. Was that trgted at anyone specific?

**Glitch**: Uh, I'll just claim it for now, I think. Uh, just to get a general idea of the question by Arathain: "What's currently the higher priority for release: Developing a working base product and rlsing it, or waiting until at least all planed feature are done, then rlsing it? Haven't been able to find an answer on the toolchain."
So, I want to answer this because I keep pestering people about Quilt Beta. Because, for a release, there's a lot of stuff that needs to be done. For example, for proper 1.0 release that should be basically feature complete, for that we want CHASM working, maybe a Loom replacement, we want Loader with Loader plugins w dependency downloading. There's kind of a lot of stuff we want for version 1, but we also want people to start using it at some point so we can get inputs. So I really hope we can get a Beta version out at some point for that.

So I guess my answer to the question is both. But as **Gdude** said, if you're asking more specifically, for example if you're asking specifically for QSL, then it's a bit of a different question that should be answered then.

**OroArmor**: So obviously, ETAs are never accurate. But to kind of give an idea of the difference in work nded for a basic product, and a full release, I can't make any promises, but we could probably has a base working product of like Loader and QSL in a couple of mths, asuming nothing goes wrong between here and then. But a full release is definitely very far out because we has limited people and a lot of stuff we would like to get done. And you know, we can't wait like a year to give anyone a working product, obviously.

**Gdude**: Alright, thanks for that folks. We're out of question, but we do has a couple more minutes. If anyone has anything they want to sneak in at the end?

**OroArmor**: Please go and review QSL PRs.

**Gdude**: Yeah, please go and review QSL PRs. And also the RFC PRs, if you're interested in that sort of thing.

**AlexIIL**: And Quilt Mappings PRs.

**LambdAurora**: And for the QSL PRs, if you're a PR contributor, maybe go look if your PR is still working on 22w06a because some stuff may has broken.

**Gdude**: Alright, I'm not seeing anymore questions coming in.

**Glitch**: Look at Outreach Team RFC.

**Gdude**: Yeah, that would be a good one to look at. Geting Outreach Team set up would help a lot.

Yeah, especially if someone wants to work on it, that would be highly apc8ed. Because you don't need technical knowledge for community involvement.

**Gdude**: Yeah, it's not necessarily developer oriented, it's more website and public relations kind of stuff, social media. If anyone's interested in that, there's a draft PR open on the RFC repository. It would help a lot, especially it would help me because a lot of the things that I'm doing currently would be better suited to a team of people.

**Glitch**: It's actually no longer a draft. I think it was merged like 2 days ago or something.

**Gdude**: Oh, good stuff. Whangdoodle was asking, "When the CHASM specification will be read out in ASMR frmt?"
IDK if there's anyone that can answer that one. Well, Whangdoodle, the question is, who do you want to do it?

**Glitch**: Whenever you do it, Whangdoodle, Whenever you do it. You just need the specification first.

**OroArmor**: Yes, we'll play it for everyone after the meeting, how about that.

**Glitch**: I haven't talked about CHASMR. Just saying you can expect a CHASM ~~length~~ RFC soon. But not yet.

**Gdude**: Alright, we're pretty close to the end of the meeting time. We usually don't run over, which is good because we seem to just get all the questions in anyway. As always, keep an eye out for the podcast. **Southpaw** will has that up whenever they has time to do it. Yeah, the questions about transcription are good, I would like them. but someone has to do it, and it doesn't have to be one of us. So if anyone listening wants to do it, go ahead, drop a DM or a Modmail, we'll take a look. I guess we're pretty much done then. Is there anything anyone on Mumble wants to say before we finish? Well, no news is good news. Alright, thanks for coming everyone. We're going to wrap it up. See you in 2 weeks' time.

**OroArmor**: We're in the #development channel for the afteringparty.

**Glitch**: Yes, #devt channel.

**Gdude**: Yes, the voice after=party

**Glitch**: Yes, voice chat after=party.

**Gdude**: Thanks for coming, everyone.
