**Gdude**: Anyway, how are you all finding the Beta? I was talking to y'all in chat, how's the Beta folks. I think I wasn't speaking into the microphone close enough last time. Yeah, I figured there'd be a few issues with the complex stuff, but that's the way betas go right? I have certainly seen some people working overtime to get things done though, which is really nice. Although I hope they don't burn out. Ah, Discord once again destroying all my shortcuts. Excellent.

Yeah, soon(TM). We'll get there, no worries. Although I'd be surprised if some of the others didn't want to have a break after the kind of crunchy week we had. I would not blame them at all. I'll be honest, I'm a complete traitor, I've been playing Create: Above and Beyond, so... I mean, I haven't played MC in years so this is great.

**sschr15**: ## sschr15 *—* Today at 12:04 AM

i saw effort being put into getting chasm functional under quilt loader already so that's something

**Gdude**: That's right, we'll be talking about that a bit later I'm sure. Alright, before we get started, Mumble side, how's the audio?

???: Good

**CheaterCodes**: Sounds great.

**Gdude**: So do you, thank you. I think we are about in time to get started. Just a second. Yeah, let's get started Alright everyone, welcome to the meeting as always. If you're new here, we do this every 2 weeks ideally. It usually lasts for about an hour. It somehow always seems to fit within an hour even if we are like up to the wire. If you'd like to ask any questions, use the `/ask` command. That will put a question in the queue and we can answer them after we've gone through all of the teams. **sschr15** is doing my job in chat, thanks **sschr15**. Let's get started then. **CheaterCodes**, would you like to talk on behalf on Build Tools Teams then for a minute?

**CheaterCodes**: Unfortunately, our main Build Tools guy, **Glitch**, is not here. He's been kind of running a marathon before Beta, so most of the commits that happened were by him and I'm not aware of what actually happened. But I want to just use this opportunity to thank him for Build Tools and just want to point out that it's been surprisingly smooth, except for a single hotfix that I guess was technically wasn't even necessary but made it nice, so everything went fine on Build Tools Teams's side I think. 

There are some details, I actually forgot to pin it. We have transitive dependencies pulling in Fabric API has been one of the biggest Build Tools issues. Which can be disabled using - what's it called - dependency substitution. I would strongly recommend NOT to using not to disable transitive dependencies, that can mess stuff up. I have it somewhere in the Community Discord, I might ask someone to pin it later. But if you're having any trouble with Build Tools, feel free to ping **CheaterCodes** if he's available, that's me. And I'll try to help with that stuff. But so far it's been fairly smooth, luckily.

**Gdude**: Alright, thanks very much for that. I believe you're also down for CHASM, so keep going if you like.

**CheaterCodes**: CHASM was not actually a part of Beta, so there wasn't like a big sprint or anything to make it happen. Well, I've been spending the past few days trying to get it into Loom. Which was surprising[ easy, given how clean the CHASM-Gradle plugin was from the Gradle perspective. It just integrated perfectly fine into Loom, which was a very nice surprise. Now I'm trying to get it loaded into Quilt Loader, which is a bit more work just because I've never loaded Quilt Loader before properly, so that's going to take a bit longer. 

And alongside doing this- I'm basically just doing this to find issues with CHASM, try to fix it and eventually get it out so that people can patch stuff. And I've been fixing a few bugs here adn there, nothing big. But yeah, now that Beta is over, I'm excited to get back and take a look at CHASM because it's been kind of put off since it wasn't realistic for Beta. But now we can go full force again. 

I would like to point out here that right now I'm basically solo-ing CHASM, and I would very much appreciate if anyone is interested in helping. I think the worst part is out of the way anyway, but there's just a ton of stuff left to do that I would appreciate help with.

**Gdude**: That's great if we could see more people working on CHASM honestly. It's going to be a fantastic tool, and it's one that's uniquely applicable to pretty much the entrance Java ecosystem and not just Quilt. So it'd be really nice to get a couple of people working on that if anyone is available and interested. Okay, thank you for that **CheaterCodes**. We'll move onto Community Tools, and that's me of course. 

W the road to Beta, I suppose, there were quite a few things to do and I kind of ran out of time. But I did still manage to get quite a few things done. On Discord you'll notice that Cozy has replaced our old tag system. The tag module is also available for anyone to use if they're writing a Kordex bot, which is the framework that I wrote. That's on Github, it's not documented yet, but it's there and there's examples, so if anyone wants to steal that, go ahead. It's on the Maven.

I've also been working on the `#welcome` channel system. That works. I actually added a role-picker to it, but we're not quite ready to use that yet. But again, that's on the Maven if you want to look at it, and the `#welcome` channel has already been set-up. It's kind of like a data-driven channel system. 

As for the website, I've been working on the installation pages over the past week or two, I guess. That took a fair bit of work to figure out a layout that works just to realised that it doesn't really work that well. I am going to change it, but for the time being it works, I guess.

Somewhat related, if anyone is a CurseForge user and wants to see us supported by CurseForge, please do give us a vote at the link that I just put in chat. It helps a lot. I'm not sure- I don't think there's anything else for Community Tools Team at the moment. I've still got a few things to do on the site. I'm working on like a guide for newcomers, and there's obviously a lot more Cozy stuff to go. So yeah, there's still a few things happening there, but it's going to be a fair few things. I just didn't have enough time unfortunate.

https://curseforgingideas.overwolf.com/ideas/CFingIing2662

Alrt, **AlexIIL**, would you like to talk for Quilt Loader?

**AlexIIL**: We've had- Well, **Glitch** has done a lot of internal fixes, which were good. But the public changes has been that the Quilt pre-launch entrypoint had to change its name, because sadly it turns out we cannot use the same one as Fabric's. It just doesn't work internally with method preferences, I think. So Quilt's is now `quilt-launch`, not that many mods should be using it, but that's changed anyway. 

The modlist in logs is now sorted alphabetically. That's only in logs, but it's a lot nicer to read now. We've got a few mixin compatible fixes which are important for Fabric mods, I think. As well as there's been a bunch of internal fixes but I won't talk about them here. The commit list is where you'd want to go to see what they are. I think that's about it.

**Gdude**: Alright, thanks **AlexIIL**. I'm got to say it, it's been quite impressive to see so many Fabric mods pretty much working out of the box, even like this early into the Beta. It's like, honestly, the fact that everyone's managed to pull together and make that happen is frankly astounding, hehe. So good work.

**AlexIIL**: I think you can thank Quilted FAPI for most of that though, as most mods don't touch Quilt Loader that much.

**Gdude**: Absolutely, they've been a huge contribution too. But if Quilt Loader can't load them up, then it's not geting that far. Anyway thanks for that **AlexIIL**. **OroArmor**, it's your turn for Mappings I believe.

**OroArmor**: Yeah. I guess there's not too much for Mappings. You know, your general stuff, we're in supply-phase right now, so we're chugging along with those. I would like to say that the Rendering Mappings PR - that has been in work since August - was merged sometime in the past week, I don't remember exactly when it was merged. But we have that merged in so the rendering names for Quilt Mappings should be accurate and up-to-date, which Iike was a big problem with Yarn. So that's really great. And yeah, we're working hard on trying to get everything mapped right now, especially in 1.19 supply as Mojang just keep adding more and more stuff, but it's coming along very well.

**Gdude**: Alright, that's great to hear, thanks for that **OroArmor**. Next is **LambdAurora** with the QSL Team.

**LambdAurora**: Not a lot of things have happened since Beta. So since the last meeting, the Recipe API got merged, it's quite a big API, and QSL also got published for Beta. But we published the Quilted FAPI model. And since Beta, we had 10 betas for Quilted FAPI and 6 betas for QSL. Another big PR has been merged, which is Registry Entry Attachments API which could be kind of compared to a registry dictionary or something like that. 

O/w there's not much to say. But a huge thanks to all the contributors since bringing Quilted FAPI to Beta was a lot of work, and was quite stressful, and I don't actually know if I'm supposed to talk about Quilted FAPI right now. But for QSL, aside for asking for more contribution, like reviewing PRs because it really helps, I don't have much more to say.

**Gdude**: Alright, thank you for that. Wait... Did they respond? They did not respond. Dangit, I'm going to have to mispronounce this now. Some of you may know, we have a new team. It is the Quilted Fabric API team which contains **Emmaffle** and a name that I can't pronounce properly, I'm just going to say **Ennui**. They do have a section but neither of them are available to do this section. However, we have kidnapped **sschr15** to fill in for them, so if you wouldn't mind going ahead.

**sschr15**: Alright then. So Quilted Fabric API is now a thing that's developed by **Emmaffle** and **Ennui** primarily. So anyone can contribute as like any other project that's part of Quilt. It used to be called Fabric API-QSL, but then it was re-organised by Ennui and is now the Quilted Fabric API. The main system is that now reviews are completely separated from Fabric API to allow quicker updates and such, which is helpful when QSL adds features that break Fabric API. 

Then, in order to prevent issues with other Fabric mods that depend on the API not having the same version, the Quilted Fabric API uses special metadata within Quilt to specify the upstream version as if that mod actually was there. QSL itself is bundled with Quilted Fabric API, so you do not have to install multiple things if you are going that route. And **Emmaffle** has been helpful recently to supply Quilted Fabric API to be targeting by Fabric API 0.15.1, which as far as we know is the latest public release.

**Gdude**: Alright, fabulous, thank you for that. Alrighty, that comes to the end of the list but there's still a little bit more obviously. I've already asked how most of you are doing with the Beta. It seems like it's mostly been positive feEdback. Obviously some things aren't quite working yet, that's, you know, to be expected working with a beta. But obviously, you know, as we've seen, especially in certain parts of the project, people have been kind of working overtime just to fix all the bugs, which is fantastic to see, so thanks for that. 

So **OroArmor**, how would you say things have been since the start of the Beta?

**OroArmor**: A lot. I know there was a very big rush, and I want to congratulate everyone from all the different teams for the amazing job they did for making it to that ddln, and ik it was a tight fit and we managed to do it. There were obviously issues, and we all expected there to be issues. But what also surprised me is that everyone who pushed hard managed to keep pushing, and we managed to fix most of the problems that were immediately at launch, and we've been continuing that energy and moving it forward. 

And now we're on a Beta 6 for QSL. I think we're at Beta 9 for Quilted Fabric API, stuff like that. So we're constantly making changes fixing. And I'm not going to make any claims, but at the rate we're going, I definitely think a 1.19 release might be feasible. However, I do think QSL neds to mature a bit more, But yeah, with the energy that we have right now, we can do a lot.

**Gdude**: I agree with you, honestly. It's interesting how much the velocity of the project has just kind of picked up over the last month and so. Everything just kind of seems to be falling into place, honestly, it's great to see. And obviously it's because of all the hard work that people are puting into it. And it's just great to see that like all this work is paying off you know. Alright, thanks for that **OroArmor**. That comes to the end of the planned segment, and it's the segment where everyone ruins our day with questions. So if anyone of you has questions, then please use the `/ask` command. We'll try to get as many as we can so long as they're appropriate and not terribly shitpost-y.

**CheaterCodes**: In the meantime, how was Beta on the Community Team?

**Gdude**: Busy. I should pull out the stats, but it's been crazy, honestly. It hasn't been too much extra stress for us, aside from dealing with all the newcomers because it's been huge. I'm just going to take a screenshot of the statistics here and you can see what I mean. Looking at the joins for the past, I don't know, I'm just going to say several months, you can see that we really peaked pretty much when Beta was announced. Which yeah. I think we peaked at about 170 in Dec, and now we're at nearly 360 joins this month because of the Beta, which is just insane. Yep, it's the highest join rate since the start of the server, as **Southpaw** says. 

[Discord](https://discord.com/channels/833872081585700874/908095149706444822/967460802137313420)

(## Southpaw *—* Today at 12:24 AM

It's the highest join rate since the start of the server)

Which is great to see. Obviously it's a bit more work for us. But you know, we're prepared for it, no big deal. It's just really like, since we're testing all the application system for Discord, we're really just sort of puting it through its paces now. But it's been good, there haven't really been that many problems. Yeah, I have to say that it's been great. Even the message rate is like much higher than expected. Like in last month - in geez, I can't remember, I'd say March - we had about 95K messages. Then over the last week we've had about like 30K to 40K. It's kind of nuts honestly. But I'm happy, it's all good news.

**CheaterCodes**: Yeah, just to sound out on this server, I really appreciate how chill it is. There's not really much bad stuff happening so that's really cool.

**Gdude**: I mean, I think I have to say, I mean, as much as you can credit the work we do, a lot of our users are also pretty fantastic people. One of the things we really wanted to do is to encourage community members to help out with some parts of moderation because obviously we can't be everywhere at the same time. That's a thing that's been a problem in some of the previous communities I've run, but actually the people have been pretty excellent about that with Quilt, and it's helped a huge amount, honestly. Please keep sending us modmails, hehe. So yeah, thanks for asking, it's been good.

Right, this is a stack of questions. Let's have a look at them, shall we?

**XanderStuff#4796** (171375148006506496)

any ideas on how could quilt overcome the fears of new contributors? "Unfortunately" quilt has some very talented individuals working on the various team, so I feel like it might make joining a team be perceived as "you have to be similar in abilities to the current team members". I don't know, maybe that's just me?

**CheaterCodes**: I think I want to answer the first question right away. Firstly, I'll ask people: Does anyone know me? I'm not really well-known in the modded community. There are a few very talented people on the team, and a few difficult tasks like my baby CHASM. But the rest is just normal coding. But if you capable of Java progressing, you're capable of contributing. And if you're not, Mappings contribution doesn't need Java knowledge. And if you feel that you're getting the hang of it, you can join and do more. Sure there's stuff that's hard, but we just need help. Not necessarily the smartest people, but we just need help. There's enough stuff to do in Quilt.

**Gdude**: Yeah, the thing with Quilt is that we have so much work that we need anyone who's OK with Java. I think we could do a bit better with Github like having better issues set up. But if you want to help out, just let us know. Tell us what you're good at and we'll find a place for you. Thanks for that, **CheaterCodes**. I think I can answer a couple of these.
