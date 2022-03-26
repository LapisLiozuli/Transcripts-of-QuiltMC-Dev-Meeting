**Gdude**: So, this is going to be a somewhat different meeting. We'll wait a just a little bit for more people to show up, but they should get some pings. Hey Ara. So, the format of this meeting hasn't changeed. However, you won't see the speakers on Discord. They'll be talking via the Cozy Mumble bot that we have set up, that is currently not set as a speaker so we can'thear them right now. In a couple minutes we will change that, and we'll see who shows up. 

Also just to be clear, you can type in the #meeting=chat channel, right? Yep, OK, good. Hey Livia, hey Merchrome. Welcome welcome. For the sake of not makeing this look so empty, I stay| in the stage, but I'm going to be muteing and deafening myself and talking via Mumble. There maybe a small bit of latency but I don't imagine it'll be too bad. This is the first time we've done this. We did test it, but you know how it goes. I'm going to set that up right about now. Alright, that appear to be working. We'll just give it a couple more minutes. But yeah, hey everyone from the other side of breach. Hey Trollzer, hey Pinkosick. Yeah, it's weird isn't it? Don't worry, it usually takes people a few minutes.

**OroArmor**: Maybe we should make a meeting role, and then ping that for attenders of this meeting.

**Gdude**: If you RSVP=ed to it, you would have gotten a ping when I started the event. We will tell you who we are, don't worry kb1000. You will not be lost, hopefully.

I'm lost.

I'm muted.

I'm disappointed in the number of groans I got about that. We usually do it for about an hr, Parzi. I haven't seen it run over quite a long time, so we should be fine. Although we'll see. Hey Kropp.

Kropp: Nobody's talking?

**Gdude**: We haven't started. We're about to though. Since you're here, do you have anything about CHASM?

Kropp: No.

**Gdude**: That's alright. Well, we may as well get started then. Hello everyone. Hopefully you know my dumbass voice by now. It's **Gdude**. This is the first meeting we've had since Christmas, since before Christmas even. Obviously it's tkn some time for people to get back in the swing of things, that's fine. I think we've mentioned this before, but we tend to skip over teams that don't have too much to say. We'll be doing that today, there's a couple teams that there's not really much to talk about, and there's a couple teams where people just aren't here at the moment. "Try again in two weeks." But we should be good.

So we have nobody here from Build Tools Teams, and CHASM hasn't been too busy, so I guess we're starting with Community Tools Team, which is basically my team. Community Tools Team is mostly Cozy right now. There have been some work. A lot of what I've been doing have been infrastructure =level kind of stuff, so instead of drct[ working on fetrs, I've been primarily rewriting parts of Cozy. That's happening primarily to break up the code a bit into modules, which has the advtg of allowing other people to make use of features of Cozy in their own bots if they want to. Assumeing they're using the same features as us, which there's a lot of bots using that around here , so I figured why not.

**Glitch** have been doing work on the Github integ] stuff. It's slow work because there's no API wrapper that does everything. It turns out that Github's APIs are quite xcsis[. There are things you can only do via Rest in the Github API and things you can only do via GraphQL. So **Glitch** is having to combine both of those together. It's a pain. It is a pain. But it's geting there.

Obv[ there is a lot of Cozy stuff to do. I am working on modules at the moment, but I think I will probably be takeing a break from that soon. Especially because Discord has given us a few more toys to play with, moderation=wise, that need to be set up. Can't really give you much information on that right now, but we'll get there. I think that's all about it for Community Tools Team at the moment. It looks like Infrastructure Team is next. **Haven King**, would you like to introduce yourself?

**Haven King**: Yeah, hey everyone, this is **Haven King**. Infrastructure's going to be pretty short, just some minor thing. I guess **Southpaw** didn't think it was minor, but I've set up Open Collective, which is a way for us to  basically publish financial stuff, so this is only very minorly related to Infrastructure, because Infrastructure is the only area where Quilt currently has expenses. So I don't think we're going to be asking for donations until we have a stable product. But in theory, we can ask for donations and publish the expenses.

**Gdude**: Yeah, it's quite an exciting thing in some ways, because as some of you may know, **Haven King** have been pretty much paying for everything out of his own pocket. It would be nice for that not to be the case. Open Collective will hopefully give us a way to fix that problem while being transparent about where the money is going and how it's used. So hopefully that turns out well. I imagine we still have to look at that a little bit more since i haven't seen it yet, but we'll get there. Who's next, Mpngs? **OroArmor**, would you like to have a chat?

**OroArmor**: Yes, not much has happened in the past month and a half=ish. I looked at the diffs. There's only been a couple minor PRs merged. The biggest thing is that we're now in another wave of pgsnaps, so we're work on maping those, and yeah, that's about it.

**Gdude**: Alrighty, progress continues as always. Uh, QSL, **LambdAurora**, would you like to have a chat?

**LambdAurora**: Yeah, so, I just need to move up... So currently we are= I think since last time we launched ~~3~~ modules. Also, we have now the command modules. We have a new feature for baked events. Now they can be used as entrypoints, and there's ~~curr[ a fly method to uningreg~~ a bunch of listeners for a bunch of errors. We also have the Item Group API which is now merged. And currently we have two PRs in ~~final com period~~ which is the Tooltip API and the Networking API. Otherwise we have a lot of PRs waiting for rvws. I think that's kind of it.

**Gdude**: Good stuff, sounds like certainty a fair bit of progress. Good work geting that stuff merged as well, nice work. I guess I can talk about Community a little bit. For those of you that haven't been following the annc]s, we decideed to finally replace the #showcase=dscs] channel. So the #gallery channel will automatically have threads set up. You guys have used threads at this point, we use them everywhere on Community. The mappings have been updateed again, they now support Quilt Mappings now thanks to update to LInkie by Shedaniel, and also a ton of work by Chris, who is actually named sschr, but hey we'll just use that name, he doesn't mind. 

Thr's also been some work on governance, there is a governance PR at the moment. I'm not sure if we merged that. No, I don't believe we have. That's RFC #47. If anyone is interested how Quilt is run, then definitely go check that PR out. 100%, it's an important one. There is another one as well, the Outreach Team which is currently in drafts. Outreach Team is, well, it's basically designed to be a team that takes care of things like social media a/cs, the website, that sort of thing. That will still need irfcs. But if anyone's interested in that, go take a look. Obviously we'll need people on that team ltr as well. I think that more or less covers it. It hasn't been super busy since Christmas since everyone's been geting back into the swing of things. If anyone has any questions, go ahead and hit up that /ask command, I see there's a couple in there. Does anyone else have anything to bring up before we move into that? Alright, I guess not. 

OK, Parzi. Parzi's asking if there's any news relateing to the Cozy ban=sharing or showcase sharing?
Not yet. Regarding ban=sharing, there was something we were planning to do, sort of inrl[, and then bring out into the wider community. But when I got to chating w the Geezer people about it, they were at a project that they'd started for it. So the plan was to use their project, basically. Now the person who was maintaining that has ended up quiting for their own personal reason, just in general from programming. So at the moment nothing is happening on there, because I don't have enough time to do that and everything else. As for showcase sharing, nothing yet. I don't consider it a high priority since we haven't got Quilt set up yet. But we'll get there. There's just more important things to do at the moment.

**Haven King**, do you want to take that one?

~~What was the question exactly? Parzi asked something like "What are the current infrastructure costs for Quilt?"~~
**Haven King**: Yeah, do I click the stage button? Or you click the stage button? Cool. So Maven's costs currently are the Maven server, which is a little bit oversized, probably a little bit bigger than it needs to be for the sake of safety. That being said, I'm doing work to replace the Maven server eventually. But work on that is slowinggoing because I'm doing a lot of things at once, juggling a lot of balls there. So short answer, mostly the Maven server, but there's other small things that add up as well. Right now it's about 70 dollars per month, Parzi.

**Gdude**: About 70? Yeah. I think part of that was email, wasn't it, because we needed that for the=

**Haven King**: Yeah, emails, about 12 dollars. to be honest I could probably cut out 8 of it, because really the only one who needs an a/c is TheSheikh.

**Gdude**: Yeah. Olivia's got a question. I think this is sort of a bit of a group question, but I can try and take a stab at it. Olivia is asking, "What is the RFC system? I don't really understand how it works, why it's there and what are the professionals and cons?"
Well, RFC is short for 'Request for Comment', and the idea behind RFC is that major organizational or professor changes get documented on Github. They allow people to go there and comment regardless of whether they're part of the staff teams or not. There they can, say, provide advice, and just generally see how decision are made. Now, not everything's up there, Community Team especially. We our processs there, but a lot of our other things like moderation stuff isn't there because it needs to move faster than the RFC process allows for. I can't quite remember the exact reasons we went w it. Do you remember them, **Haven King**?

**Haven King**: Yeah, we needed a space to hold and lock our official docus. Right, so that was going to be a big thing. Whether that is = like you mentioned = policy chgs, technical specifications, they're all on a central repository, as well as a way for us to have a formal process for decideing on them. So whether it's decideing how QSL modules should be specified or merged, decideing how we should hire new staff mmbrs. All those things have to be codified swhr, and this is a great way for us to have a formal way of decideing what we should do and keeping track of it, right. That was the gist.

**Gdude**: That's right, I remember most of that actually. As for the professionals and cons, well, obvious cons is that it takes a while to get things pushed through. But I think there are a lot of advtgs to it as well, especially haveing those discussion available in the public eye, where everyone can see and contrib to them. I think that's really important, especially given where we came from. Transparency's been something we've really been thinking about, pretty much since the start of the project, and I think this helps a lot w it, honestly. I think this one's for you, **Haven King**.

(~~Something to do with sharing the Open Collective for Quilt~~)

**Haven King**: Yeah, in theory it's set up. I don't think I'm going to share it for a bit. Again, I could, but again, I don't feel like we should ask for money until we have something to show for our efforts. If people insist, I guess I can share that but I want to do a little bit more work inrl[ before doing so.

**Gdude**: That's fair, that's fair. I wonder, do you know if they have an API? Did you notice anything like that?

**Haven King**: I have no idea.

**Gdude**: Might be something to integ into one of the welcome channels ltr on. That might be interesting. We're at the end of the queue already, that was quick guys. DAE have any questions they want answered? If so, hit up that /ask command, I'll give you a few minutes. Yeah, it have been the shortest meeting in a long time. I had a feeling it would be, because people are still recovering from the holiday season. People ask, "Where is Quilt?" But nobody asks, "How is Quilt?" That's a classic meme, Parzi.

**Haven King**: That's a much harder question to answer.

**Gdude**: Does anyone want to take the next incoming question?

**Haven King**: Basically, because that's what Fabric's was. I don't think we did anything more than that, we basically just cloned their repository.

**Gdude**: That makes sense.

**OroArmor**: I can take **CheaterCodes** 's. "Do you have an ETA for an ETA for Quilt?"
Yes. Well, not quite. We have an ETA for the ETA for the ETA. And that is always 2 weeks from whenever you're listening to this.

**Gdude**: Yeah, it's kind of hard to have an estimate, isn't it? Main thing holding us back is, as always, Build Tools. It's just really hard to get Gradle experts to help. If you know any, send them our way, please. But once we have Build Tools done= I think **CheaterCodes** mentioned on Community, that if we wanted to, a few weeks' of crunch on the other projects would probably get those to release once we have Build Tools. Obviously I don't think we really want to do that, but it really shows how far behind Build Tools is compareed to everything else. It's just unfortunate that it's that way at the moment. Yep, agreed, Gradle really is just an eldritch demon, says Ara. 

I like this question. Parzi asks, "Are there any plans going forward to do TED talks where modders come in and talk about general feature design, or specific implementation of interesting / noteworthy fetrs?"
In short, yes. We have things planed w the Events Team. We actually just started planning something recently, but it's going to be a while before we get to the point where we can actually talk about it. But yeah, events, they're certainty a thing we want to be doing. Talks were definitely something I had in mind when we were forming the Events Team at least. I don't know if any of them are listening at the moment. But yeah, we're going to figure out a few things like that planned. No doubt about that. I think this one is for **OroArmor**.

**OroArmor**: What do you mean by "Renamed Quilt's Intermediary Mappings when?" What do you mean, like renaming Hashed Mojmap? Or Hashed Mojmap is a good name?

**Gdude**: Hashed Mojmap is a good name. It's not a fun name, but it's kind of the point, isn't it.

**OroArmor**: See here's the thing, Fabric kind of messed things up by calling it Intermediary, because Intermediary is literally what that style of mappings is. So we have to go w Hashed Mojmap. I don't want to call everything Intermediary because that gets confused w Fabric Intermediary. So we kind of have this weird issue.

**Gdude**: We has some discussions about mappings before, about what to call it. Uh, I can't remember exactly what names we came up w, but I think we ended up decideing at that moment that we wanted to keep the names descriptive. I can't remember 100% why we did that, but I think it turned out to be a good choice in the end. Yeah, Hashed Mojmap, that's accurate, that is what it is.

**OroArmor**: I mean, it is published under Hashed namespace though, so...

**Gdude**: Does anyone want to take this one? Don't think we have anything on Blurry. Or do we have anyone from Blurry here?

**Haven King**: There isn't really any update in that area. It's the basic TLDR.

**Gdude**: We have talked a little bit about it inrl[, but then again it's still early. There is some things to think about that as well, regarding platforms like CurseForge. We're not really sure where that's going to go yet. They have requested a specification document from us, but we're just not at the point where we're ready to provide that yet. So, we'll see. We're not sure yet. We're still thinking it's going to happen though. So it's a case of geting to that point.

"~~No forgiveness ~~for Build Tools." I mean, something to think about more than anything, when you think about something like CHASM which used to be called ASMR= I'm not sure where the CHASM name came from aside from a convenient acronym. But it sure beats what Forge have been doing w their project names. Um, can any of us answer that one?

**Haven King**: Basically, the plan is for it to be a 'privileged' library. There's not a name, or a formal structure for that or anything. But it's going to have a lot of the same benefits that QSL does in that it can be automatic=resolved, or automatic=dled. So the basic idea is that it'll be automatic=resolved or automatic=dled like QSL Module is, so it can be used in devt environment for mods by default without haveing to set dependencies, or use `includes` or anything right off the bat. But also=

**Gdude**: Uh, I think **Haven King**'s just crashed. He suddenly left the Mumble server. RIP. 

**OroArmor**: Does anyone think they can grab what he was about to say?

**Gdude**: I'm afraid not. Oh no! Windows Updates! Oh, OK. Sad, sad. OK, well.

Parzi asks, "Pointless question, but why does the MC Update RSS bot sometimes take so long?"
The dirty secret is, because it's not an RSS bot. It's actually polling the launcher patch notes. So there's two reasons that it's slow. The first reason is that Mojang just doesn't publish them sometimes, or they take ages to publish them. Like it took them a week to publish the second=to=most=recent snapshot. The second thing is, Mojang = and Microsoft in general = have a ~~fren cache~~ set up. And it doesn't expire for, I think they have it set to an hour or something. So depending on how their servers are feeling, it can take up to an hour after they publish it for the bot to pick up on it. And even then you'll find that if you're around when the bot picks up on it and posts the embed, if you click towards the patch notes on the side, you may still not see them because their cache hasn't updateed in your region yet. It's a pain in the ass, honestly. 

I've been thinking of a way to make it more reliable, but ultimately we want the patch notes on Discord, and there isn't really a better way of geting them. So, I'm not really sure. But hey, if you have any ideas, I'll hear them. Yeah, that's what I used to do. I used ot write them manually, Ara. But it's been a while since I've had the time. Automateing what I can is certainty where we want to be w that. Parzi says, "Pay lobbyists to stand outside their windows and take pictures of their editors." Yeah, maybe. Skyrising, doing some cache=busting. I'm also doing some cache=busting. It doesn't help.

~~A~~: Yeah, about that, ~~gets launcher meta within a second of publishing, but nodule content~~ takes 1 hour, so...

**Gdude**: Yeah. Meta, you can get, but launcher content won't, it just won't. It's really annoying, actually. The things that we put up w for Mojang, right? Like, it wouldn't be so bad if we wanted to use the update notification. We could just check meta. But we want the patch notes, and that's actually= On the Community Server, that's like= If I just open Insights here for a second, actl]... Uh, where am I? Server Insights... If I go to the #annc] channel on Insights, I can see the most recent post in #comy=news made it to 27 srvrs. And the most recent post in #minecraft=news made 63 srvrs. So, people want the patch notes, clearly. Uh, that's like 6 more servers than December too. Er, so there are 2 servers w over 10,000 users following us. That's kind of scary.

Uh, that's what cache=busting usually ivlvs, **kb1000**. Usually you just add a query parameter w the current time in it. Um, that doesn't work. It makes sense that it wouldn't, but still annoying. I appreciate that question. Uh, by the way **EarthComputer**, did you end up geting back?

**EarthComputer**: Yes, I did.

**Gdude**: Oh nice. Well, welcome back.

**EarthComputer**: Hello. Well, I could make some of the mtgs.

**Gdude**: Congrats, you did it. Eh, why not? We might as well. "How are you guys today? How's 2022 treating you guys?" From Olivia.
Uh, personally or project=wise? Personally, it's fine. It's another year, you know. Hopefully less Covid, probably not. How about the others in here? Anyone want to check in?

**OroArmor**: Pretty good, yeah. Went to some family event.

**Gdude**: That's good to hear. Uh, project=wise, we're still geting back into the swing of things, as I've said. No major worries. It would be nice to get Build Tools done. Well, functional. 

I see Leo saying on Mumble, "NFTs haven't died yet, so this year still sucks." I mean, fair. Yeah, there's an awful lot of NFT stuff going on. There's actually= I saw some tweets posted earlier to Community, where several of the major Discord bots by Botlab have started advertising crypto=bots. Those play=to=run bots. That could only go bad.

**OroArmor**: Isn't that a scam?

**Gdude**: Not necessarily? It's peggy, which is ~~out~~ for a long time.

"Is cereal soup?" says Arathain.

**OroArmor**: Yes.

~~(One half of a conversation happening here)~~

**Gdude**: No, I think it's more of a salad, and milk is the dressing. "Salad is just unmixed soup." I mean, I guess. Oh, the ~~culebroom~~. I had heard of that, I just never saw it. "Salads in a breadbowl are quiche." You know what, we can't be frens, I'm sorry. Think goodness for starch. Yeah, it's great, isn't it?

Uh, OK. Are there any more questions? Any more on=topic questions, hopefully? Anything you want to yell at me about on the Community Team? I see Favrito just got here. Hi Favri= Yeah, I'm going to try that again. Hi Favrito. "What's currently blocking the Quilt launch?"
pgbuto. Build Tools, Build Tools, Build Tools. Um, we say that a lot because we need Gradle people. If we had Gradle people, we'd be a lot further ahead, I think. Um, it's just how it is. At this point, maybe we should just cobble something together and get something functional, without the bells and whistles, but=

**EarthComputer**: Yeah, at least I have the feeling that if we get at least something functional, then new people can progress w the other projects and help to attract more contributors, because we have actually stuff to do= more stuff to do on the other projects. Then we can see it used in practice. Then maybe any of about 1 in 500 of those people might want to work on something w Gradle.

**Gdude**: Yeah, precisely. "I wish I could offer my skills, but my Gradle skills are pretty bad."
Yeah, Gradle's the only realistic tool, I think. It's the one most people are used to. Mostly the other alternatives are... strange. Or just too domain=spfc, really.

**OroArmor**: Or extremely proprietary.

**Gdude**: Or extremely proprietary, yeah. Or just really old. Really, it [Gradle] just ends up being the best option. A lot of people have suggested Braquira, but it's way too domain=spfc, and kind of niche. I think, anyway. Like, sure, OK, you build mods with Braquira (Transcriptor's Note: I couldn't find anything about this), but think about how that limits you when it comes to general devt. ~~Bundle something else~~. Like if you have an executable mod for example, you know OK, they could add it, but what else is going to be missing, you know? It doesn't support Kotlin or other languages yet either. Maybe it'll be something to look at, but we're just going to have to stick w Gradle for the time being. Sorry, that's my dog.

**EarthComputer**: There's also a MC=spfc build system that's being built by someone, I can't remember what it's called. Apologies, but again, that's a little bit too= most of us think that's a little bit too new to jump onboard with.

**Gdude**: Are you thinking of Braquira?

**EarthComputer**: It might be the same thing.

**Gdude**: I think it is. The alternative is Basil, but not really many people understand it. Basil is not MC=spfc, but it's very new and strange and kind of limiting.

**LambdAurora**: I'm not sure that it's really new, because I had heard about it years ago. But it's= In my experience, it wasn't right w like IntelliJ.

**Gdude**: Uh, yeah, that makes sense.

**LambdAurora**: And for stuff, like in the case of dependencies, at least, by default it doesn't support Maven and stuff. So it's really manual, it's not practical.

**Gdude**: And there goes **kb1000**, our Basil evangelist, saying it's probably not a good choice. I've a Gravel understanding from a user perspective. I've tried to write plugins and failed miserably, so that tells you about all you need to know about that. You are the ~~one percent~~, Parzi. Just waiting for someone to suggest makefiles. Because you know it's going to happen.

**OroArmor**: For those in the podcast, who can't see the chat, the chat just exploded w 'NO's in respond to **Gdude** 's suggestion. There's at least one, "I'd quit modding." Yep. Alright, well, we're scheduleed for about 10 more minutes if anyone has anymore questions.

**Southpaw** does not like ~~Glinting~~, poor **Southpaw**. Hey, you're lucky. I almost moved to Spotless, and that's even worse. Well, **EarthComputer**...

**EarthComputer**: I'm not going to answer anything right this minute.

**Gdude**: I just find it funny that you mentioned that yourself earlier as well.

**EarthComputer**: Yeah, we mentioned literally that inrl[. Oh, hang on, is that= We haven't even=

**Gdude**: I'm not going to click it because we need **Haven King** to answer that really. So we got your question, Parzi. We can't answer it right now. Yeah, we can save it for next week. We'll just leave it in there, we can go back to it. Yeah, but it's a difficult one. A difficult one. Technically it's up to **Haven King** or well, the Administrator Team, but we'll need to see what happens w Open Collective first, I think. Yeah, I like KoingFi, but I don't know, Open Collective will definitely suit us better if we end up using it. But, uh congratulations Parzi, you've spawned a whole internal conversation, without even realiseing it. Congrats. 

I appreciate the off=topic questions, Olivia, but if we have on=topic ones, I want to do those first because we don't have much time left. OK, I guess we will then. Well, Alizay likes sushi, apparently. I'm a burger kind of person myself. I used to like pizza, but I don't eat it anymore because I'm lactose=intolerant now. **Haven King** says, "Liming me to one favourite meal is simply impossible." That's what Olivia asked, I forgot to say. It's not so bad. I mean, you get used to it when you have no choice. Lactose intolerance is just one of those things, you know. And there's a lot of good vegan alternatives and those are all lactose=free because obviously.

**OroArmor**: Yeah, being lactose=intolerant isn't going to be like the worst, since there's a lot of options. I'm gluten=free so I know what it's like to not be able to have a lot of stuff. But I feel like being both lactose=intolerant and gluten=free would be absolutely horrible.

**Gdude**: It would be pretty bad, honestly. It would. You know breakfast cereals? It turns out a lot of them have powdered milk in them, for some reason. And when you look at like gluten=free cereals for example, which do exist, most of them also have milk powder in them to bulk them out. So that way, you'd be eating a lot of your stuff yourself, I think. Or just eating vegetables all day, which, fine, I guess. 5 minutes, if there's any lastingmin questions.

**EarthComputer**: Soy as well. There's other soy things as well. Soy lechitin, soy proteins. It's just everywhere.

**Gdude**: Oh, here's a question. I think I can answer this one. **Southpaw** asks, "Did we ever figure out whether the Quilt Client was ever going to send a list of installed mods to the Quilt server?"
I don't think we finalised it entirely. But the plan was basically that we were going to use plugin chnls. If you have QSL installed, or a mod using QSL = therefore we install QSL for you = when you connect to a server that also has QSL installed, then the client would tell the server what mods it has installed. Just the mod IDs. Now, this is an interesting medium in my opinion, because you end up w a situation where this only happens when the client and the server have QSL installed. So if the server doesn't have QSL = unless it's Hypixel = it's probably not listening for the mods in the first place. So we just never send them. That's about the long and short of it. QSL isn't going action the list. It's just going to receive it, and other mods will be able to get at it if they want to.

**LambdAurora**: Well, if the channel is registered, anyone, any server ~~cld register, there's no reason for it~~. So it could get the modlist. Even Spigot could get the modlist.

**Gdude**: Yeah, of course the server could register the channel. But the point was more that if the channel's not registered, we don't even try and send it. So it's really up to the server.

**LambdAurora**: I mean, that's literally default MC behaviour.

**Gdude**: Yeah, of course. Ah, hello **Haven King**.

**Haven King**: Hi, I have returned.

**Gdude**: You have returned, welcome back.

**Haven King**: Seems like we're pretty much wraping up here.

**Gdude**: Yeah, more or less. More or less. There's one more question we can do, if no one wants to take that.

**Haven King**: Oh, the Config API one? Sure, I can talk about that a little bit. I guess I'll reiterate. Hi, this is **Haven King**. I have returned from my Windows Update kerfuffle. The question is, "On a scale of Cloth Config to Omega Config, how detailed and complex will the Config API be?"
Tt's a question that has a couple different anss, partially because there's no real consensus yet, and partially because of my plans that I have = that basically exist in only my head and that I haven't formalised ahwr = for it to be more of an open backend w a fairly reasonable default frontend for people like develops to use. But like w a lot of xpnd]s. 

Foreg, don't intend on the default way of making configs being similar to Cloth Config / AutoConfig. I don't want it to be annotation=based. I don't like annotation=based things, so if I make a default frontend it won't be annotation=based. That being said, the backend should be open enough that someone could come in and write a frontend for dvlping configs that could be annotation=based and still make use of all of the features such as: Like I was saying, I plan on haveing config synchronising, and config screens that can be built atm8[. Integ] w whatever ModMenu=type thing we end up haveing. So I can't exactly say on a scale of Cloth Config to Omega Config, how detailed it'll be, but those are my general plans right now. If that helps answer that question.

**Gdude**: Alright, thanks for that **Haven King**. So we have hit the houringmark. We usually end at about this time, but is there anyone on the Mumble here who wants to get anything out before we do? Nope, doesn't look like it. I have to say, I didn't expect this meeting to be mostly questions, but that's how it goes.

**Haven King**: Yeah, it's alright.

**Gdude**: Exactly. Alright, well, I guess we'll wrap it up then. Thanks everyone for coming. As always, we'll be back in 2 weeks with the next meeting. And we'll get this cut down and put into a podcast. Hopefully at some point today if we have time. Hopefully we will. I think we will, but we'll see how we go. Anyway, thanks for coming.


















