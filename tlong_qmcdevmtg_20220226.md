**Gdude**: Hello and welcome to the QuiltMC Developers’ Meeting Podcast. The podcast that isn’t really a podcast. If you’re new here, this is just a collection of recordings of each publicly recorded Developers’ Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed on a Mumble server and recorded live. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to QuiltMC.org.

**Gdude**: Well well well, it's me. I appreciate how quickly people join when the event starts. It's just like yeah, wait that's happening now, isn't it? Hehe. Oh hey everyone, we're doing the same thing we did last week, or last fortnight. Last biweek. I will be here on Discord. Everyone else is on the other end of Mumble where **Saf** is recording everything to make sure, you know, we're able to put out the podcast later on. It's still a little early out so we're going to give it a few minutes. Can somebody on Mumble say something? Hehe.

**Haven King**: Hey, hello everyone.

**Gdude**: OK, excellent.

**Alex**: Hi everyone.

**Gdude**: Oh no, 'fortnight'.

**Haven King**: It's 'fortnight' with the traditional spelling of 'night'. Not the trendy game style.

**Gdude**: Mm hmm. I think my list is up to date. Excellent. I see your Mythbusters, **Silas**. Haha. OK, **Emma**. 

**Haven King**: That would be a pretty good April Fools, **Skyrising**. Try and ~~mod a new religion~~. Haha.

**Gdude**: It would be pretty good, you have to admit.

**Haven King**: That would be very difficult, but it would be pretty funny.

**Gdude**: You know what, I'm not surprised somehow. Someone's going to end up doing that at some point. Let's give it a couple more minutes as we wait for people to get in here. Alright, I think we can probably get started. It's been about 5 min. So yeah, welcome to another public QuiltMC Developers’ Meeting. I'm going to try that again later, don't worry. And we'll just get right into it, I guess. **Earthcomputer**, I guess you're ready to talk about CHASM?

**Earthcomputer**: Yeah, let me just find the notes.

**Gdude**: And while **Earthcomputer** does that, if you want to ask any question, you can use the slash cmd, /ask, and we'll get to them at the end of the meeting. Alright **Earthcomputer**, whenever you're ready.

**Earthcomputer**: Yeah, so **CheaterCodes** has left me some notes on CHASM. He wasn't able to make it for the meeting. So what's been going on? He's been developing a CHASM-Gradle plugin to allow the co-pilot to see changes made by CHASM. For example, like added methods and etc. ~~Quite stuff~~ like access wideners will also be available for ~~nicks, nicks~~ and interfaces in the chat as necessary. Uh, not sure about necessary, but there you go.

Um, the plugin works-TM, and I encourage- **CheaterCodes** encourages, if you're interested in play- around with CHASM, that he doesn't expect the current version to be super stable. You can find it on the CHASM repositoriesitory, on a separate branch. He's work- on a anothversion rs that integ with Gradle and hopefully IDs that will come to a repositoriesitory near you soon. That's good enough I think.

**Gdude**: Sounds good to me. I'm sure thr's been a lot of progress on CHASM. Thr's been devlogs going out on those as well, if anyone's missed those, always worth a read. Uh, OK, thanks **Earthcomputer**. Next is me, right? Community Tooling. Um yeah, most of what we've been doing with tooling is mostly the website. Mostly me, but I've had some help of course. For people who are interested in that, there was an announcement posted on the community server about it. I'm always looking for fdbk, however I need to update that link since we changed how the preview worked, but it's more of less up to date anyway. But yeah, if you are interested in seeing what the new site is going to look like and what's on it, take a look at that announcement on Community and give me some fdbk because I could really use it.

**SuperCoder**, are you there? Decompilers?

**SuperCoder**: Yeah, I'm here. Um, it's been kind of a quiet two weeks. We've been working on improved pattern mathing on both switch and if statements to make the Minecraft decompilation better, hopefully. And that's about it.

**Gdude**: That's still important work for that project though, good stuff. **Haven King**, do you have anything to talk regarding Infrastructure?

**Haven King**: Nothing super significant, I've done a little more work on my Maven app. But when I say a little, it's like a really small amount. I know I'm going to fetch and process like proxy repositories, but that's basically the only progress I've made.

**Gdude**: Alrighty. **Alex**, would you like to talk about Loader?

**Alex**: Sure, so Glitch's done a lot of work getting us up to date from upstream, which is- it gets us a lot more closer to getting Quilt Loader to run on newer versions of Minecraft. We've also started publishing non-snapshot releases to Maven. It's still not fully ready, but it's test[ at the moment. There are also two other quite useful changes: The envt in a Qmodjson file now uses dedicated underscore server rather than just server, because we noticed that was confuse- some people a bit. So that just clarifies that, to make sure so that you don't just like accident[ change your- set your own envt of your mod to Server, xpk- that to work for the integ_ server when tt's not quite how it works. 

We've also made it so that mixins and by extend] CHASM when we get it work-, mixins/CHASM can target MOjang-rel_ lib. DFUs (DataFixerUppers), brigaders, Java bridge and AuthLib, with mixins, which is quite useful. Esp as they are pretty much made for Minecraft, they are not general lib. Tt's the other thing, you can't target general library with mixins at the moment. I'm not sure if this is functionality need, because most library are pretty general, but you can't do that at the moment.

Thr's also two issues with Quilt Loader, or discussion I want more people to look at. And tt's whether we load mods from subfolders in the mod's folder. Tt's Quilt Loader issue #38. Um, it's mostly for whether people want to org their mods in a better way. Basic[ I'd quite like a settlement on that before we release Quilt Loader properly so that we don't have to change that in the future. And possibly, whether we lim some folders by Minecraft vers. I'm less sure about that, but anw tt's issue #38 and #50 basically. I think tt's about it for Quilt Loader, basically quite a lot of progress.

**Gdude**: Tt's great, excellent work there. I guess pushing to non-snapshots is why people were posting screenshots on ATLauncher show- 'Oh, here's how you use Quilt.'  But I don't think they've actually activated that functionality on their launcher yet. But it's good to see that they pretty much already have support. Alright, thanks **Alex**. Uh, Aurora, would you like to talk on QSL?

Aurora: Yeah, I just need to think like what to say. We got new PRs ~~in the final player~~. So we have only 3 modules in events. We got the Tags API, but it's straight for 1.18.2. We got the ~~PR pussy~~ merged. We also got a PR of QSL ~~done eating~~ into Quilt Loader. We also got a lot of PR where you ~~use tools yet~~. We also got Items in ~~API for the final period. Tt's also something thr~~. Tt's kind of it now. Uh, also, we also got a PR for ~~Voice~~ API in the meantime. Yeah, tt's it.

**Gdude**: Alright, thanks for that Aurora. As for the Community Team, not too much news, as some of you have seen from the announcements on the community server, I created an #openings channel there. That basic[ lists all the staff and other teams that need more member. Thr's quite a few thing to look at in there. We've got most, actually all the community teams, exc for manager. Build Tools, Mappings, then Triage and Worldgen, the QSL teams. Thr's a lot of stuff tobe done, and we could always use the help. So if you're interested, you can head over to the community server, go to the #openings channel, thr's a listing there that you can use. And we've also mentioned the new site here which is part of Community Tooling. I think tt's about it for Community. Can't think of anything else, at least, not yet.

Alright, is there anything that anyone there on Mumble wants to talk about today?

**Haven King**: I guess we have an announcement of some kind? Do you want to handle it? Shld I or should you aft the question?

**Gdude**: I have no idea what you're talk- about **Haven King**, I'm sry. But we can mv into the question now if you'd pref.

**Haven King**: Sure.

**Gdude**: Alright, then let us take a look. So as always, I'm going to read the question out, and if I **Haven King**'t talk_, I'll say my name. I assume the others will do that as well. But I'll read the question out and I'll read out who asked the question. Alright, haha, I guess we'll go through these now. 

Silas asks, "When is the new site designed by His Eminence **Gdude** be made the public design of QMC?" PR's open at the moment. I'll grab a link for you if somebody doesn't beat me to it. There is one in there, anw. If you go to the QMC.org referral on Github. I'm manage- too many thing to get the link for you right now. Oh, there you go, thanks Emma. Once this goes thru, it'll be up once it's merged basically. I'm not sure what the criteria is because thr's not many people around that have the time and ability to review this kind of PR but we'll see how thing go at least.

I can take the next one as well. Silas is ask-, "For each meeting, is there an agenda of items to ask being made internally?" Uh, no, I'm afraid not. The way we usually do it, since people are work- like pretty much up to the time of meeting, is if I don't forget to set a reminder usually, we meet about 15 minutes early internally, and then we just go through all of the teams and see who has something to talk about. Otherwise we don't really have much of an agenda. I imagine some of the teams are keep- track of thing on their own but otherwise thr's no like specific defined internal structure for thing like that. It's not a bad idea, I'm just not sure how we could do it.

**Haven King**: Well, we were first doing the meeting internally before they went public. But if there was like a big issue, or a big convo we wanted to have, we would have it schedule_ beforehd. You know, say, "We'll be talk- about it at this meeting." We still can do that, but it just hasn't been something that has come up as often. There is also that pause of meeting around Dec because of hte hols and whatnot, so even though there were some big dcd] being made then, we just weren't around to talk about them. But we could do that again, but it just hasn't come up again.

**Gdude**: Tt's a fair point. I'm losing track of thing here. Well, Silas is ask- another question, "When are we get- another new blog entry on the site?" Well, I think ToffeeMax is actually work- on one. I don’t know if he's around at the moment, I think he's busy. But this kind of ties into the Outreach Team. Lk we are plan- on build- a team. I think it's pretty much done actually, we just need to get the RFC merged, which would handle stuff like blogposts. ~~We should still put stuff there.~~ Obv[ we want the site to be rebuilt by then as well since the current site doesn't have pagination or anything just yet. But once tt's over, we can dcd it, then we get the Outreach Team, you should start seeing more content then.

**Alex**: Ember asks, "Wld it be possible to have version specific mod folders like Forge?" So I briefly touched on this during what I was say-. So currently there's a discussion issue about this. It's Quilt Loader #50. So basically the answer is yes, it should be possible, but I don’t know if this functionality should be enabled by def. 

**Gdude**: I can hear **Alex** typing, so I'm asum- he got cut off.

**Alex**: Oh sorry, I think tt's just me hold- down my push-to-talk key. So I think tt's the question answered?

**Gdude**: Yeah, I think so. **Haven King**, do you want to take the next one?

**Haven King**: Sure, as soon as I find the question so I can see exactually what it was. There it is OK, so Silas asked, "So QMC has an ~~open colkv~~ page and it basically answer to the community. And am I the admin there because I'm on the admin board, or because I'm on the infrastructure team?" And the answer is: There are plans to announce to the community. I'm try- to keep it not private obv[, it's public and people can go there. And it's evident because if you have one contributeutor people can't contribute. But because we aren't launched yet, I didn't want to go around ask- for money without a pdt that people could be using in xchg for their donations, you know, or in relation to it at least. So tt's why it's not public, or rather not publicised yet. 

As for why I'm the admin there, it's because I'm on the admin board, and I should get the other admins setup there as well. Rly tho, as a member of the Infrastructure Team, I need to submit expenses. If anyone else had Quilt-rel expenses, they could be add_ as member so that they could submit those as well. But as far as I know nobody else has. I think **Gdude** has some hosting expenses he could potl[ put there as well. But tt's kind of the state of Open Collective at the moment is that nobody else has any expenses to put there yet.

**Gdude**: Thanks for that **Haven King**. Aurora, would you like to take that one?

Aurora: Yep. "Are there any plans to ~~add Forge-style initialisations~~ stages to Quilt? It would potl[ make a lot of API stuff much more opointi_ by allow- two dynamically generated constants ~~extra~~." So I had pull up Forge docu because I used Forge a long time ago, so I don't remember exactually all the specifics. But, how to say that, but one of hte reasons they have to use stages and stuff is because the energy thread modloading, it's not really need_ in our case since we got multi-thread modloading. And so lk, registry stuff, we don't use a ~~deferred~~ registry. The goal is to use the ~~many-armed~~ sys, so for that thr's an entrypoint to be able for us to do stuff. 

But currently thr's four initialisation stages. You could say stages, but it's not really stages. So we have four entrypoints. We have the pre-launching point, which is before Minecraft is even loaded. Tt's for rly, rly, for stuff that is really before. Then we have the main entrypoint, which is run on every site. Currently, it's in QSL, and it runs before the registries get locked. Then we have the client entrypoint, which w Minecraft the MC client instance is created, it's not really well-defined where ~~CUTS OUT~~ or when it runs th Minecraft always the MC client instance runnin MinecraftAnd thr's the dedi MC server entrypoint. It's kind of not used, since it's kind of rare to use it. It makes stuff that is strictly lim_ to dedi servers. Each ones, I think, before or after the path loading, I think before. So if you want to add a path mod that has an API, the way it works is that tt mod defines its own entrypoint. Because we do not have a well-dfn_ mod loading order, so we can't really xpk a mod to be loaded before you also ~~begin the verse~~. 

So yeah, the way we do it is, it's the thing in Fabric land, the API mod dfn its own entrypoint for that kind of stuff. So ModMenu dfn its own entrypoint for config providers. I think maybe Trinkets dfn its own entrypoint for Trinkets stuff. Tt's the way we do it. Yeah, and mods are kind of in this waitlist in the wait file load order tt's not really specified in this ~~CUTS OUT~~. The way I'm working on is dfn_ in the mod manifest. And then, thr's method and loader which allows you to get all the entrypoints by their keys. You can iterate and call that into point manually. And tt's what API mods do. They have their own entrypoints with their own interfaces, then they call their own entrypoints tslv. So it's counted that their target mod is loaded. Not sure we design needs, that the design might not need an entrypoint, so it's kind of better to use entrypoints. Because if the mod isn't present, then the entrypoint won't be called. So it's really useful. I think it answer that. We don't really have any staging stages. At least, it's not dfn_, but entrypoints kind of replace that by virtue of entirely replacing it.

**Gdude**: Thanks Aurora, that was a very dtl_ ans. Tywus is asking, "Whether we've considered a system wherein a repositoriesitory contain the official listing of Quilt staffers in a human-readable and computer-readable format? Basically for automaticmation and for display on the site." Uh yeah, tt's in our plans. We don't really know how we want to do it just yet, and also actually writing that system has a lower priority than get- stuff like the site ready. But it's something we definitely want to do, we just don't have an idea of how we want to do it just yet. If you have suggestions tho, you know, we'll take them of course.

**Alex**: DEXD asked, "Whether Quilt will have support for all the version of Minecraft unlike Fabric?" So very few of the project will support all tversio Minecrafts of MC. Only Loader might have support, and tt's in the sense that we're keep- Loader on Java 8 so that this is a possibility, but we're not actively put- in any work to actually loader Quilt Loader on alve Minecrafton  vers of MC. It's just potl[ something that Quilt Loader could do in the future. But project like QSL will definitely not suppo Minecraftersion the vers of MC. So any Minecraftds version ll the vers of MC that were built on Quilt Loader that were made in the future would have to do all the work tslv. They would efkv[ only have mixins/CHASM basically.

**Gdude**: Yeah, thanks for ans- that. Yeah, I mean I can't really see Quilt officially support- all the version anw. The amount of extra work that tt take on its own is like a lot. And I imagine the same thing will happen as what happen_ with Fabric, asum- we have enough users for it to be a popr idea. You know, with community proj. But I just can't see it as being a priority for us.

Um, I'm look- at the question queue and thr's no question left guys. Does anyone have anything else they want to ask? If you got something you want to ask, use the /ask cmd. We still have plenty of time, so don't be too shy.

Aurora: Also I just wanted to mention, because I'm big dum-dum, I forgot that the final commendarion for ItemSettings API ended today. So the ItemSettings API got merged in QSL.

**Gdude**: Something happen_ to the bot there. So hey, Mumble, can you hear me? OK, good, good stuff. OK, tt's a good num of question. There we go. Yeah, Aurora, you can go ahead and take that one.

Aurora: So, where can I find the API submission guideline, I guess? So for QSL thr's a contribute- file that dictates the PR process, the conventions and more. So tt's one of the entrypoints to see how we do stuff. The other good thing is to look around in the existing APIs to see how it's done. Then the other stuff that is not truly written, at least, I don't remember, oh, it is, it is written. It is first to discuss the fitter, by opening an issue on Github or on Discord too, then we can look into it. Then we make sure that there is no PR that is made directly. If a PR up for discussion was made, the big risk is that you either make an API that is not need_ for QSL, or it's an API tt's not fit for use. So it's always best to discuss APIs before make- a PR. So an issue on Github or a discussion on Discord is really nice. But tt's for QSL.

For APIs in Loader, it's a bit different, but I think it's kind of the same. But contribute- guideline are not the same. But there might be one Quilt Loader but I'm not sure. Globally it's kind of the same. It's discuss the API, then we can look into if a PR can be made ~~as strong~~. We do not this hesitat to discuss this kind of question.

**Gdude**: Thanks for that. Well, you know what, I asked for question and we sure got question. Chris asked, "Will Hashed exist for old version of Mojmap in the future?" Rly no reason why it wldn't. Tt's kind of the idea, right? 

Silas is asking, "Who's currently in ctrl of hte QMC acct?" Well, I think right now i5 is the one with the logins as he set it up originally. We're wait- for him to not be too busy with uni so that he can tfr all the logins into our 1Password. Aft that it will be in ctrl of the Outreach Team and whoever they dcd to put it in there, or whoever we dcd I guess, since I'll be in there as well. In add] I have access to it via Tweet Deck, but it's kind of lim_ since I can't mod the profile or anything like that. So if you see abdy like retweeting or tweeting on there, it's probably me right now, but we'll see about it later on once the Outreach Team is in place.

Favrito is asking where help is need_ at the moment. I mentioned it earlier, but again, the #opening channel on the community server lists the teams that need people. You can also have a look at the various issues on any project that you're interested in. I could also use a bit of help on the Community Toolings Team but I'm not really too worried right now. It's chugging along just fine. And yes, sign up for Build Tools of course, that's in there, it's in the list. So yeah, not much there to say for that one, I think. **Haven King**, I think that one's yours.

**Haven King**: Yep, waiting for it to pop up in chat. If it's going to. Or if it's- I don’t know.

**Gdude**: Click the stage button. Ah, there we go. OK.

**Haven King**: So Lembic asks, "If there is a community wish to create such a backport, would there be a chance that it would be considered official aft careful analysis?" This is a tough question, because the bit about careful analysis make it seem like that you're looking for lk, if thr's a really good reason, could we make it official? And I think the answer is going to be, probably not, because of the different need that a backport would hv, right? 

You see for a std workflow, we have QSL and Mappings that need to be updated on a rolling update basis. When you're look- at a backport like for older vers, any API updates are going to be stagnant, you're not going to have to worry about pruning them. You know, Minecraft updates or anything like that. So really it's just an entirely different body of work tt's being done. So the reason I wldn't make it official is because it's totally segmented as far as what need to happen and the std core of devs is probably not going to be very interested in work- on a backport like that. 

So tt's probably the main reason I would be very hesitant to make such a backport, even if it gains a very large amount of traction, official.

**Gdude**: Thanks for that, **Haven King**. Yeah, Aurora, you could take that one if you lk.

Aurora: OK, ~~~~do you all have any idea how many days there are left to~~? Or is it too far away RN? It really dpd on the proj. For QSL it's usable. We still need to test a lot to see if it's stable, but it's usable. Cmpr_ to FAPI thr's not as many features, but it's usable. For Quilt Mappings, it's definitely usable, though there might be issues with the mob stuff. But that boils down to people actually mapping stuff. But it's well usable right now. Compiler is already used in a lot of proj. For Loader, I'm not entirely aware where it is, but seems to be really close to be able to test it. So tt's great. Build Tools, well, tt's another story, because thr's people work- on vanilla Gradle, but I don’t know where that is currently. As spoke earlier in the meeting, CHASM has made progress_, but I don’t know if it's going to be usable in like QSL and stuff really soon, so kind of no for me. So it really dpd on the project for now. But we are slowly coming to something useful globally.

**Gdude**: Thanks Aurora. We're at the end of the queue again. Are there any more question to be ask_?  Slab says, No. But for transparency, the devs don't actually see the questions until someone from our Community Team approve them, so they're not necessary[ guaranteed to be answered. Use the /ask slash cmd if you want to ask a question.

**Haven King**: Alright, so the Nukelore asks, "Lkly it's been asked before, as well as answered in an issue, but is there any sort ModMenu or library in Quilt itself? I assume not but you nvr know." There hasn't been an official dcd] or anything on this. Currently, a lot of us- The plan tt's being talk_ about the most is to have ModMenu like more automaticmatable. That will operate sort of similarly to how we're planning for FREX (freaks) to operate, where it will be maintain_ by a outside party, but available as an automatic download in a similar way to how QSL will be. It is also possible that yeah FREX equals F.R.E.X., Xander - Grondax's tool. At least tt's how I pronounce it, I'm not sure how other people are pronouncing it. But basically, a approve_ or indoors library by Quilt that can be used and included similarly to QSL module, even if it's not actively maintain_ by Quilt developers. However, that is tentative planning and it can definitely change. We could end up having our own ModMenu for whatever, but tt's how I see the situation right now.

**Gdude**: Thanks **Haven King**. I see a lot of people talk- about how you pronounced FREX (freks) there. But you know how it is.

**Haven King**: Apparently my pronunciation of FREX (freaks) is different from everyone else's, heh heh.

**Gdude**: Silas was ask- where the ~~SeshPod~~ disappeared to. It's still there, we're not really using it right now. We used to, but then Discord Events become a thing, and we kind of just use those now. It's still useful for polls, but we don't really do that many of those on this server, so it's just kind of sitting there until we need it. Also, I was current but now I'm not because I needed to cut down on those a bit. So I'm not sure whether it's still suitable for those, but it probably is. We'll have a look at it when we run the next poll, I imagine.

I was about to say we have no more question but another one's just come thru. AManCalledSteve who is currently here, "Are there any upcoming dates we should remember?" Um, that's a good question.  **Haven King**, what do you think?

**Haven King**: Yeah, you know, we have one date in particular tt's coming up. It could be important, some people might care about it. 

**Gdude**: Yeah, maybe, I guess a few people might. Hehe.

**Haven King**: So we hv, internally, between talk- to the developer and everyone, tentatively dcd_ that April 20 makes sense as a initial beta release for us to work towards here at Quilt. There have been a lot of good progress from Loader, there have been a lot of good progress from QSL, so we're really rly opointimistic about being able to get everything work- by then. you know we're not talk- about- like dependency downloading won't be ready, plugins probably won't be ready. But it is a beta release date that will be usable for mod devt and testing is the goal.

**Gdude**: We can't guarantee any specific level of done-ness for some of the extra project, but we're pretty happy that tt's going to be a rough date for the beta at least. Sorry, I think I cut into you a little bit there, **Haven King**.

**Haven King**: Ah no, it's OK. I was just saying, I'm really happy. As people have pointed out in chat, it'll be marking about a year since we launched publicly these community spaces. So it'll be really fun to have something tt's out in the hands of developers that maybe aren't involved in Quilt development specifically but are interest in following the proj. So that's you know, look- forward to seeing what everyone does and when everyone gets involved.

**Gdude**: Will this be on the timeline? I mean, the timeline is going back and not forward. But yeah, we can put it on there. For those that don't know, the timeline is on the new website as well. So yeah, tt's some news that some of you might have been interest_ in. I'll write that up somewhere as well at some point. It'll be on the Community Server aft the meeting. I think I'll just write it out because I think not everyone is going to hear it here. Or maybe I'll just make them listen to the podcast, hmm.

We have a few question to go through here, so we'll keep gg. But if you have any question about the release, of course, feel free to put those through as well.

Silas is ask- if the moderator team is diverse enough in time zones to guarantee that thr's always someone around. Tt's a good question. I believe we checked, I can't remember what the answer was at the time, but we do have pretty good coverage to have at least one per aroundard. Also, for the times that I'm awake, I'm pretty much always available, or nearly alavailable available. And for the times that I'm not, if it does happen that there's no moderators or managers around, the admins sort of have emergency access to act as moderators as well in the worst-case scenario. But I'm not especially worried about it. We haven't had any problems with it so far. Although I still would of course like to expand the moderation team especially considering the server is going to grow aft that beta release. We're going to need more people at that point, so you know don't waste time if you're planning to sign up or apeopley. Go right ahead, please.

**Haven King**: Cool. So this next question from the Nukelore is, "What's the plan with the whole dependency download? Lk will it be limited to QSL? Or all library and APIs that have been confirmed to not be a danger to the end-user?" So dependency downloading, everything we're going to say about it is very much in flux. Thr's no RFC yet, so nothing is finalised, or even really had extensive discussion about it until we have an RFC. So take everything we say with a grain of... salt, yeah, in that it's very much still being dev_ even as an idea.

So the way that I planned for dependency downloading to kind of work, at least in the early stages of Quilt, is QSL only. In quotes really, it'll be restricted to the Quilt Maven repositoriesitory only, so realistically anything that we've hosted on there, whether tt's QSL or eventually, FREX (freaks) right, or some obscure like JSON library for some reason. If you wanted to dpd on that, because it's on our Maven repositoriesitory, you'll be able to, even in the early stages of dependency download-. 

My idea is that we'll roll out the ability to have dependencies downloaded from other repositoriesitory as we develop the download- infrastructure and make sure that we can ensure the security of that, right, because that is a concern. That being said, there will be blacklisted sites. Lk, Maven Central doesn't like having end-users download software from them, so we would not allow people to specify dependency from Maven Central. If you wanted to download something that was available there, you would have to set up your own Maven repositoriesitory. But lk, proxies are just so that we're not hitting Central with a bunch of traffic. But in short, the end goal is that you should be able to use dependency download- for any libraries or APIs: QSL, stuff like Cloth Config, ModMenu, what have you. you know, your tiny little homebrewed library that you just want to be able to use automatic dependency download- for all of your other projects that might use it, even if you're the only one using it, you should be able to do it in the end. Tt's the goal. **Alex**, do you want to talk a little bit about what you had in mind?

**Alex**: Uh, yes, so, it's still very much in flux. I really don't have much to add to that without being misleading.

**Gdude**: Fair enough. What about Chris's question? Am I right in my assumpointion with tt?

**Haven King**: Chris's question? I guess I'll just state this. "On building the dependency download- in question, will verified developer also be a possibility? If so, how will it be done?" I think this is an interesting question and it kind of speaks back what we were talking about with FREX (freaks or freks or however you want to say it) and Grondag being basically what we would consider a verified developer. 

And the answer is, other verified developer are a possibility, right. If Grondag can do it, surely others can. I think the question is, it's really based on need. We don't want to have verified developer left right and centre, right. We want to have people who are adding to the QSL experience. In the case of FREX, it's a rendering library and we need a rendering lib, so we'll bring Grondag in. Later down the road, it's possible that there'll be verified developer just for hosting things on our Maven repositoriesitory. 

I know that some people who were around very early probably heard about the registry being thrown around a bit as being like a Maven repositoriesitory being available for anyone to upload to. Tt's something I'd still like to do at some point. It doesn't play into this dependency download- paradigm directly, because it would not be as thoroughly vetted as what we we're going to say verified developer are. But it would be an easy way for people to not have to host their own stuff. Tt's a lot of different system in play as to what a verified developer really is and what they mean, and none of tt's really been figured out in a very concrete way. Does that kind of answer your question, Chris? I'm lost in chat, so if you want clarification on something, feel free to ask. But if not, I'll assume we're good and we can move on to the next question, which I guess I'll also take.

**Gdude**: It's definitely one of yours.

**Haven King**: Yeah. So the question is what happen when/if the Maven fails? Well, the Maven fails. So right now the Maven is hosted using a SonioType Nexus. It's hosted on one individual server, which could theoretically fail. But if you've been around, and if you've been around for this meeting and for past meetings, and you've heard me talk- about my own Maven apeopleication system that I'm work- on which will not be bound to instances, like VM (virtual machine) or anything at all. It'll kind of be in the aether of AWS's (US telco provider) infra. So that you know, if the Maven fails, in that case then we have bigger problems than- you know, a good amount of the Internet is going down as well. Because that would reqr AWS itself to fail. Or for me to f*** up, which can happen. Hope[[ won't, once we are in a production-rdy phase. but it's possible.

But if we're talk- about long-term, like archival, like ten years' down the road from now, what happen if the Maven fails? That's a great question as well, and not something I that I'm able to answer super well, because it's hard to predict where we'll be ten years from now, but hopefully I'll be able to keep the Maven running for a while. A big goal of my own Maven system is that it'll be much more cost-efkv, down to the point to that if nobody is req- files, it'll cost me a couple of dollars per month, as opposed to currently sixty, so that I can keep it on for a long long period of time. Great. Hope[[ that answer your question well enough, Fabrito. Let's see what else we have here.

**Gdude**: I think **Alex** has something to add on to that one.

**Haven King**: Yeah, sure, go for it.

**Alex**: Yes, so, part of that question could be: What happen if it can't connect to the Maven while doing dependency download-? So what would happen then, if like automatic dependency download- cannot work, it just well, fails to download and will prompoint you to go download it yourself, efkv[. So if dependency download- doesn't work, or the Maven doesn't work, you should be able to go to a site like CurseForge to get the actual JAR, or possibly in the future, if there are archival sites for this sort of th. So basically, there should always be a way for you to get the libraries you actually need, even if the Maven doesn't work in future.

**Haven King**: Tt's a good callout, which does prompoint me to explain a little bit more on how I envisioned dependency download- working. I don't think you would declare... you know it's going to be kind of similar to how ~~Maven~~ works, where you don't say you need this artifact from this repositoriesitory. You cld, maybe tt's something we'll look into, but really it's going to be you declare what your dependencies are and separately declare what repositoriesitorys you want to look in. And so we'll look for all the dependency and all the repositoriesitory until we find them and if we don't find them we'll just give you the std error like Fabric does, like 'Hey, you don't have this mod. You need to install it." Right? Tt's kind of how I see that weekfl gg.

**Gdude**: Thanks for that, you two. Uh, looks like I've got a question here. Silas asks, "What time zone is the most active for Quilt?" Uh, Silas, have you seen this? Haha, because that should definitely answer your question. For those who **Haven King**'t seen it, what I just linked is the stats dashboard for both Discord servers. It mostly looks aft itself, but I keep an eye on it. And honestly it's quite interesting to just look it over and see what's happen-. Aside from message acty and usage acty on both servers, it also includes the suggestions. So if anyone wants like an easy way to browse through all the suggestions, there are as well. 

To answer your question, the community server is most actv around 7 pm my time, which is GMT/UTC. And the development server/toolchain is most actv around 4 pm UTC. Oh, and the massive influx of leaves aren't really leaves. That started happen- because we started kick- people who didn't pass member screening within a few days. So tt's what those are. It's not actually people like staying around and then leaving. It's us kick- people that nvr get through member screening.

Nobody's offered to take that question, haha. Will I take it?

**Haven King**: What question is it? Oh, bus factor one? Yeah, bus factor for Infrastructure, currently one, because tt's me. Community Team and Mng], tt's, I mean, a lot of people would hv- It would have to be a really big bus, in a lot of different time zones too. Community Team and Mng], we're not at a huge risk. As integral and peaceful as **Gdude** is, he's not everyone and we have a great support- community set up as well. So I think we would be able to survive even if **Gdude** sadly didn't. The Development Team, I think there are a couple of people, like if **Alex** were to leave, unfortunately, Loader would need... at this point, it's good enough, that we would be able to get things working, and Glitch has done well, so I don't think we're at a huge risk in the development space either.

I think the weakest link is Infrastructure, which is me, which you know, it's hard to shore that one up. It's hard to find someone who knows the AWS side of things and is willing to work on it for free. But there is an initiative, or at least that is there should be, there will be at some point, an initiative to get the access keys out there, so that if something does happen, someone can keep the lights running even if they're not entirely sure what everything is doing. That is something that should be done at some point and only hasn't because of restrictions on my own time.

**Gdude**: As Saf mentioned, now that the 1Password is setup, because there is an Infrastructure vault on there now, so if you did want to you could just put them in there, I think only the admins have access to it.

**Haven King**: OK, I should do that.

**Gdude**: I'll just quickly take this one, because it's been answered a few times. "Is the Maven a mod downloader?"" No, it's specifically, it's where we're placing Quilt components and libraries to be download_. It's not for mods. For mods, you use CurseForge for that.

**Haven King**: Right, this one is: "W**Haven King**ill Haven be taking an apprentice for the Quilt Infra?" I mean, if somebody really wants to learn infrastructure, and wants to learn AWS and stuff, I could point you in the direction of some learning materials. Thr's a lot going on there. And then eventually, once you have a solid enough footing in AWS in general, I'll be happy to give a little bit of- I mean, really if anyone wants to know how anything that we're dealing with works, I'll be happy to describe it and give you an idea of what the architecture looks like and how things are interacting. It just probably won't be useful or very easy to understand unless you have a reasonable AWS backing. Or at least, you know, IT or whatnot.

**Gdude**: Actually, on that **Haven King**, all that stuff is very interesting to me as well, it's just a case of time. But it would be good to get more people on that. It's just a very involved set of technology to get to know about. 

OK, I believe we've gone through eth. As you've just realised, I just closed the AmA. We're a couple of minutes over, about four minutes over. Usually we finish at about 5'o clock my time. Is there anything that anyone on Mumble wants to say?

**Haven King**: I guess I can follow up the infrastructure question real quick. If you are really interest_, feel free to DM me. Or ping me in the #infra channel, either one.

**Gdude**: Excellent. Alright, I think that concludes this meeting. It's been great to have everyone here. Thanks for coming, thanks for everyone on Mumble side for coming as well. As announced_, we're aiming for the 20th for Beta. Not just because it's the funny number, but because it's the same date last year that Quilt become public. So we're looking forward to that, and of course well be back again in two weeks, as always. Az will work on their own time and get the podcast up when they're able to. So yeah, thanks for coming and see you.
