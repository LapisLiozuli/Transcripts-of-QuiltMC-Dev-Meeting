[23/04/2022: I Just Call Him Chris](https://anchor.fm/quiltmc-dev-meetings/episodes/23042022-I-Just-Call-Him-Chris-e1hv5po)  
In this episode, the team discuss Build Tools, Chasm, Loader, Mappings QSL, and a new team Quilted Fabric API. They also discuss new contributors being overwhelmed, and how to minimise burnout.  
[https://quiltmc.org](https://quiltmc.org/)  
[QuiltMC on GitHub](https://github.com/QuiltMC)  
[Quilt Community Discord](https://discord.quiltmc.org/)  
[Quilt Toolchain Discord](https://discord.quiltmc.org/toolchain)  
[Quilt Openings](https://quiltmc.org/openings)  
[Quilt Beta is launched!](https://twitter.com/quilt_mc/status/1516821689341984772?s=20&t=v6-iwNoYmbpjjbTONenUxA)  
[Create: Above and Beyond on CurseForge](https://www.curseforge.com/minecraft/modpacks/create-above-and-beyond)  
[Quilt Loom on GitHub](https://github.com/QuiltMC/quilt-loom)  
[Chasm on GitHub](https://github.com/QuiltMC/chasm)  
[Chasm Gradle Plugin on GitHub](https://github.com/QuiltMC/chasm-gradle-plugin)  
[Chasm Issues with Help Wanted (GitHub)](https://github.com/QuiltMC/chasm/labels/help%20wanted)  
[Welcome Channel Management Module on GitHub](https://github.com/QuiltMC/cozy-discord/tree/root/module-welcome)  
[Welcome Channel Management Module on Maven](https://maven.quiltmc.org/repository/snapshot/org/quiltmc/community/module-tags/)  
[Quilt Install Page](https://quiltmc.org/install/)  
[CurseForge Ideas: Add Quilt Support (now Planned!)](https://curseforge-ideas.overwolf.com/ideas/CF-I-2662)  
[Quilt Loader on GitHub](https://github.com/quiltmc/quilt-loader)  
[Quilt Mappings on GitHub](https://github.com/QuiltMC/quilt-mappings)  
[Quilt Mappings PR #5: Rendering](https://github.com/QuiltMC/quilt-mappings/pull/156)  
[Quilt Standard Libraries on GitHub](https://github.com/quiltmc/quilt-standard-libraries)  
[QSL PR #109: Fix issues with the recipe API](https://github.com/QuiltMC/quilt-standard-libraries/pull/109)  
[QSL on Modrinth](https://modrinth.com/mod/qsl)  
[QSL PR #29: Registry Entry Attachments API](https://github.com/QuiltMC/quilt-standard-libraries/pull/29)  
[Quilted Fabric API on Modrinth](https://github.com/quiltmc/quilted-fabric-api)  
[Quilt Stats Dashboard](https://stats-quilt.gserv.me/public/dashboard/9b181b97-bd7f-4ab0-87ed-3239f9149932)  
[Quilt Beta Thread on r/feedthebeast](https://www.reddit.com/r/feedthebeast/comments/u87izy/the_quilt_modloader_officially_enters_the_beta/)  
[Quilt Newcomer’s Guide](https://quiltmc.org/about/newcomer-guide/)  
[Donate to Quilt (OpenCollective)](http://opencollective.com/quiltmc)  
[VanillaGradle by Spongepowered on GitHub](https://github.com/SpongePowered/VanillaGradle)  
[Screenshot of GitHub Teams page](https://cdn.discordapp.com/attachments/908095149706444822/967465805077938257/unknown.png)

=========================

**Gdude**: Hello and welcome to the QuiltMC Developer Meetings Podcast. The podcast that... isn’t really a podcast. If you’re new here, this is just a collection of recordings of each public Quilt Project Developer Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks, relayed from a Mumble server and recorded live by a fleet of Discord bots. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to [https://quiltmc.org](https://quiltmc.org).

=========================

SPEAKERS:

- **AlexIIL**
- **CheaterCodes**
- **Gdude**
- **LambdAurora**
- **OroArmor**

ATTENDEES:

- **Exo**
- **glitch**
- **Jaai**
- **Janetyqua**
- **kb1000**
- **lenrik**
- **sciwhiz12**
- **sschr15**
- **Southpaw**
- **XanderStuff**
- **Zaeroses**

MENTIONS:

- **Starchild**

=========================

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

With the road to Beta, I suppose, there were quite a few things to do and I kind of ran out of time. But I did still manage to get quite a few things done. On Discord you'll notice that Cozy has replaced our old tag system. The tag module is also available for anyone to use if they're writing a Kordex (Kord Extensions) bot, which is the framework that I wrote. That's on Github, it's not documented yet, but it's there and there's examples, so if anyone wants to steal that, go ahead. It's on the Maven.

I've also been working on the `#welcome` channel system. That works. I actually added a role-picker to it, but we're not quite ready to use that yet. But again, that's on the Maven if you want to look at it, and the `#welcome` channel has already been set-up. It's kind of like a data-driven channel system.

As for the website, I've been working on the installation pages over the past week or two, I guess. That took a fair bit of work to figure out a layout that works just to realised that it doesn't really work that well. I am going to change it, but for the time being it works, I guess.

Somewhat related, if anyone is a CurseForge user and wants to see us supported by CurseForge, please do give us a vote at the [link that I just put in chat](https://curseforge-ideas.overwolf.com/ideas/CF-I-2662). It helps a lot. I'm not sure- I don't think there's anything else for Community Tools Team at the moment. I've still got a few things to do on the site. I'm working on like a guide for newcomers, and there's obviously a lot more Cozy stuff to go. So yeah, there's still a few things happening there, but it's going to be a fair few things. I just didn't have enough time unfortunate.

Alright, **AlexIIL**, would you like to talk for Quilt Loader?

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

**Gdude**: Busy. I should pull out the stats, but it's been crazy, honestly. It hasn't been too much extra stress for us, aside from dealing with all the newcomers because it's been huge. I'm just going to take a [screenshot]([Discord](https://discord.com/channels/833872081585700874/908095149706444822/967460802137313420)) of the statistics here and you can see what I mean. 

Looking at the joins for the past, I don't know, I'm just going to say several months, you can see that we really peaked pretty much when Beta was announced. Which yeah. I think we peaked at about 170 in Dec, and now we're at nearly 360 joins this month because of the Beta, which is just insane. Yep, it's the highest join rate since the start of the server, as **Southpaw** says.

**Southpaw** *—* Today at 12:24 AM
It's the highest join rate since the start of the server

**Gdude**: Which is great to see. Obviously it's a bit more work for us. But you know, we're prepared for it, no big deal. It's just really like, since we're testing all the application system for Discord, we're really just sort of puting it through its paces now. But it's been good, there haven't really been that many problems. Yeah, I have to say that it's been great. Even the message rate is like much higher than expected. Like in last month - in geez, I can't remember, I'd say March - we had about 95K messages. Then over the last week we've had about like 30K to 40K. It's kind of nuts honestly. But I'm happy, it's all good news.

**CheaterCodes**: Yeah, just to sound out on this server, I really appreciate how chill it is. There's not really much bad stuff happening so that's really cool.

**Gdude**: I mean, I think I have to say, I mean, as much as you can credit the work we do, a lot of our users are also pretty fantastic people. One of the things we really wanted to do is to encourage community members to help out with some parts of moderation because obviously we can't be everywhere at the same time. That's a thing that's been a problem in some of the previous communities I've run, but actually the people have been pretty excellent about that with Quilt, and it's helped a huge amount, honestly. Please keep sending us modmails, hehe. So yeah, thanks for asking, it's been good.

Right, this is a stack of questions. Let's have a look at them, shall we?

**XanderStuff#4796** (171375148006506496)
any ideas on how could quilt overcome the fears of new contributors? "Unfortunately" quilt has some very talented individuals working on the various team, so I feel like it might make joining a team be perceived as "you have to be similar in abilities to the current team members". I don't know, maybe that's just me?

**CheaterCodes**: I think I want to answer the first question right away. Firstly, I'll ask people: Does anyone know me? I'm not really well-known in the modded community. There are a few very talented people on the team, and a few difficult tasks like my baby CHASM. But the rest is just normal coding. But if you capable of Java progressing, you're capable of contributing. And if you're not, Mappings contribution doesn't need Java knowledge. And if you feel that you're getting the hang of it, you can join and do more. Sure there's stuff that's hard, but we just need help. Not necessarily the smartest people, but we just need help. There's enough stuff to do in Quilt.

**Gdude**: Yeah, the thing with Quilt is that we have so much work that we need anyone who's OK with Java. I think we could do a bit better with Github like having better issues set up. But if you want to help out, just let us know. Tell us what you're good at and we'll find a place for you. Thanks for that, **CheaterCodes**. I think I can answer a couple of these.

**Zaeroses#6355** (806065199609937980)
how has the reception of quilt been in the community so far (before and after the beta)? we aren't part of the community outside of the toolchain server, so we don't really have any picture of the popularity or opinions of mod develops or players

**Gdude**: That's a really interesting question honestly. Being a project born from what we're born from, there are a few people not willing to consider us and that's fine. Recently there was a [rather controversial post](https://www.reddit.com/r/feedthebeast/comments/u87izy/the_quilt_modloader_officially_enters_the_beta/) on the /r/feedthebeast subreddit. There are people wondering why we're splitting the community, or not getting into old drama. I'm actually writing a post on this to clear up things. It's hard to get into the details because it's such a big community. But I have been promised that a lot of people have been supporting us. I was surprise to see that ATLauncher quietly added support for us. PolyMC too, Modrinth.

I don't think the opinions have changed too much between pre-Beta and current. I will say there have been people that were like, "I'm not sure if this is going to release," and then came in and said, "Yes! there's a Beta now, I'm going to use this now." It's been great to see too of course. But yeah, overall it's been pretty good. Certainly there's been some negative reception but overall I think that's the outliers. It's been great to see. Here's the link. That's not the link I want. Thank you Browser.

I'll take this one quickly and one of you should take the ETA one.

**CheaterCodes**: Definitely mine as well, but after you.

**Exo#9052** (604653220341743618)
Where can I donate?

**Gdude**: We were kind of holding back on this for a while now because we hadn't released a release. As some of you might know, most of if not all of the Quilt infrastructure is actually paid out of **Haven King**'s pocket. To try and release some of that stress, we actually set up an Open Collective which I'll link in chat. We're using this not just for donations, but also show that we can be transparent with our fncs. Because we don't want to get into a situation where like we're geting donations and no one knows where's the money going or anything like that. So if you really want to donate, you can. It's completely optional, of course, we'll keep trucking along. But it'll be great to take some of the stress off of **Haven King**'s wallet, especially considering how much time and money he's put into this.

But yeah, thanks for that question. **CheaterCodes**, would you like to take one?

**CheaterCodes**: Yep, absolutely. You may pronounce his name, because I cannot.

**Gdude**: I just call him (**sschr15**) Chris. That's not his real name but...

**CheaterCodes**: Let's just call him Chris. "Chris is my name," well, there you go. The question is:

**sschr15#4563** (300606625297727489)
Any ETA on VanillaGradle or Chasm being publicly available for mods to use in development?

Well, no clearly. VanillaGradle, I've not paid too much to recent developments. There hasn't been too much happening on the Sponge Discord which is where I usually look for updates. But commits are happening every now and then. So I cannot answer too much about VanillaGradle. I think what it's mostly missing is re-mapping jars at the end, because I think input mapping is fine. But yes, that's missing.

Rgrding CHASM, as said before, I'm working on geting into Quilt Loader. I'm not sure how soon it'll be available. It's going to be either just a branch of Quilt Loader where I make some unoffiical builds so people can test it out. But the more I look at it now, the more likely it is that I'll actually have to completely remove remove Mixin and access wideners to add CHASM. Which means for testing, it's going to be a while until Mixin and CHASM are back. So definitely not going to happen on the main Loader any time soon. It's going to be definitely a few months more.

**Gdude**: Alright, thanks for that **CheaterCodes**. These really seem to be largely community-themed questions for a change. **Lenrik** asked a question, I'm not really sure how to answer that though.

**CheaterCodes**: We don't really have an answer to that, at least not right now.

**Gdude**: We kind of don't, but I would like to have one.

**CheaterCodes**: Well, let's take the question and talk about it. So **lenrik** asked:

**lenrik#5193** (437296242817761292)
is there any way that you can/are making sure that people are not overworking themselves while working on the project?

**CheaterCodes**: So I think one easy way is that we have a pretty chill community on the Toolchain Discord, so there's usually not too much pressure from other people to get something done quick. But if you are thinking of anything in particular, any options you have to make sure that people don't over-work themselves, please let us know. It's not something we've really looked into, I think.

**Gdude**: Yeah, I mean I would quite like to see some ideas on that, because it does bother me. As a serial over-worker myself, Ik that people can get into that situation. And like we mentioned earlier, **Glitch** is kind of burned out because of the amount of work that neded to be done to reach the Beta target. We have to be thinking about that a bit more carefully if we do that again with another deadline. But yeah, it would be great to hear some ideas. If anyone has any ideas on that, we'll take them onboard to listen to them.

**Southpaw** — Today at 12:36 AM
We have zero expectations of your performance

**glitch** *—* Today at 12:37 AM
i mean the beta turned into a grind at the end

**sciwhiz12#1286** (607058472709652501)
What contingency plans, if any, do you have in situations where Discord goes offline due to technical difficulties/outages?
Or I assume a roving band of mutants.

**Gdude**: Well, we have a few ideas. We did look into alternate chat platforms a little while ago. We actually were on Matrix for a while, but that turned out to be basically impossible to moderate properly. Just from a technical perspective, it just wasn't up to scratch and we weren't going to host one just for 3 channels. I looked into ~~Zewdlip~~: While it worked quite well, it was a little weird and it also gave everyone's email addresss to staff members and I was not happy about that. Another thing is Revolt, which I consistently forget to check on. But Revolt is a Discord clone I've been keeping an eye out on. There is a server there unofficially that I've set up for Quilt, but it's not ready for use. It's just not, it'll get there, but it's not there yet.

Another alternative I mentioned, even if Discord does go a bit dark - We do have Github Discussions. Everyone's there, more or less, so we are able to function still. And we are also planning on geting a forum up soon, hopefully anyway. I know the **Starchild** system is working on that. So those are the things we're looking at at the moment.

I really wanted Matrix to work. It doesn't. I wish it did because it would be like the easy option for us, but yeah, it's just not going to do it. There's other options of course, stuff like ~~Githere~~ and ~~MatterMost~~ and Slack, god forbid. But we'll see. I don't think it's going to be a realistic issue. Like we have the website, so if something does happen, we can quickly set up something if we need to. I'm not super worried right now, to be super honest. Oh, that's some news I can insert.

**kb1000** *—* Today at 12:39 AM
multimc just merged my quilt PRs btw

**Gdude**: That's good news. I guess we'll be geting Quilt support in that shortly. But keep an eye on the website for that one, I'll update the page when we have more information on it. Another question from sciwhiz:

**sciwhiz12#1286** (607058472709652501)
Does the Community Team have a team on GitHub, for the use of the relatively newingish organization moderators feature?

**Gdude**: Not specifically for that propose. I've looked at it, but it doesn't really help us unfortunately. The main issue is, it kind of halfway bridges the gap, but we need to be able to delete issues. And the only way to do that is with ~~RecoAdmin~~ at the moment. So our current approach is going to be adding function to Cozy that can do that on our behalf rather than give all the Community Team full access to everything. The Infrastructure Team has a Cozy account on Github that I set up, so that's probably what we're going to use for that. 

It would be nice if Github Permissions didn't suck. Really annoyingly, on Github Enterprise, you can set them up exactly how you want them. So I don't know why you can't just do that on Github. But yeah, it's not an ideal setup. The moderation thing helps, but we do need to be able to delete issues, so yeah, it's still not quite there unfortunate.

**Sciwhiz** with the community questions. These are almost all community questions. I mean I'm fine with that, but it's just unusual.

**CheaterCodes**: Because the community's so amazing.

**Gdude**: Yeah, you're right. They are, they are amazing.

**sciwhiz12#1286** (607058472709652501)
Why is the icon for the Toolchain Server webhook in the community server different from the Toolchain server's avatar? :)

**Gdude**: It's just Discord rounding the corners too much. It should be exactly the same, IDK why it looks like that. It is the same icon.

**sciwhiz12#1286** (607058472709652501)
Any possibility of a screenshot of the QuiltMC teams page (with all subteams visible), for curiosity's sake?

**Gdude**: Have you seen the Teams page? Everything is visible. I mean, we keep that up-to-date. But if you really want a screenshot, I mean sure. Let me just crash Discord for a moment. [Here you go]([Discord](https://discord.com/channels/833872081585700874/908095149706444822/967465582784024621)), knock yourself out.

Ik it looks weird, but that's what happens when you do that, so hehe, good luck.

**CheaterCodes**: I think the question was regarding the Github Organization. Yeah, but everything on the Github Organization page is also here, so...

**Gdude**: Yeah, there's just no difference, really.

**CheaterCodes**: We can't show a screenshot of that because of all the upset anyway, I guess.

**Gdude**: Ah, thank you for that **Emmaffle**. Those titles look weird on this. Ah, I'll fix those later.

**CheaterCodes**: If you're OK with me leaking this, I'll post the [screenshot]([Discord](https://discord.com/channels/833872081585700874/908095149706444822/967465805946179645)) as well.

**OroArmor**: I think it's fine.

**Gdude**: I don't mind but yeah, if **OroArmor** says it's fine, then it's fine.

**CheaterCodes**: I think it's all on the website anyway, so it shouldn't be a problem.

**Gdude**: It is, yeah.

**OroArmor**: Just make sure to blur out that one. I'm joking.

**CheaterCodes**: "Oh no, everyone knows about the secret Everyone Team."

**OroArmor**: Oh, you can't see the other secret team, only I can see that.

**CheaterCodes**: Oh right, because you're Administrator, I forgot.

**OroArmor**: Yeah. Don't worry, these are the only important ones.

**CheaterCodes**: The Everyone team is actually new, is it? I haven't seen that before. Or maybe it's new that Github shows it?

**Gdude**: I don't know, I think I made that ages- No, I made that when Discord had a massive outage, that was me. And I was like, we should have somewhere to talk, and then someone pointed out we had the testing forum we could test, so we used it. I do not know about that sciwhiz, you'll have to tell me about that later. OK, I guess I could take the next one, IDK if there's anyone better suited to answer it than me. Maybe **OroArmor**? It's kind of hard to understand the wording of that one. Or I just take it.

**OroArmor**: Uhhh, I think I can.

**Gdude**: Sure, go ahead. You click it.

**Zaeroses#6355** (806065199609937980)
does quilt have a more general goal as far as the player experience as a whole goes? like, a general goal linking together how players would interact with various areas of quilt in practice?

**OroArmor**: Oh yeah, you need to click it, hehe. I don't think necessarily interact with the different areas of Quilt, but we want to provide a more unified way for people to just play. So, one of the main things with that, our Loader plugins, so that you can load Fabric mods. Where the player experience isn't so much formed around us interacting with pull-up?, but we provide features to players that allow them to play with mods in their own different ways. If that makes sense, I can't think of that others since I'm more of a developer, but Ik that Loader plugins will be something unique that Quilt brings to the player experience.

**Gdude**: I mean, I think it's a good question. A few things that come to mind for me are UX things, like fixing the terrible erorr popup, and geting a nicer installer and all that. I mean, a lot of the things that Quilt is doing is sort iterating on older things that were never that good, but really could do with attention and improve things. At least from what I've seen. It's interesting that **Zaeroses** because **Zaeroses** is working on error stuff at the moment, or at least planning to, as far as I know. It's kind of a difficult question to answer with the way it's phrased, but that's what comes to mind for me.

Alrt, **LambdAurora**, go ahead and take that one. It's OK, click the other one, nobody will notice, hehe.

**Jaai#9049** (730700346069876776)

What is QSL I don't know im new to devloping?

**LambdAurora**: So basically QSL is the Quilt Standard Libraries. They are tools for developers to interact with the games more easily. Or unified ways to try to bridge to other mods. For example, one of the APIs provides ways for mods to- My thought process got interrupted, so what was I saying? So they can provide ways for mods to... like create blocks, but in ways where it won't conflict with other mods and stuff.

**Gdude**: Alright, all good. Yeah, **AlexIIL**, you can take that. You can click the button again as well.

**sschr15#4563** (300606625297727489)

I heard before that Quilt is meant to support multiple games besides Minecraft. Any hint on what kind of other games? (@Lapis Liozuli)

**AlexIIL**: This is something very specific to Quilt Loader. That it's meant to be able to customise Quilt loader in a way that you could use it for other Java-based games. But I don't think the QuiltMC Team is directly doing this in addition. We're still abstracting a lot of Quilt loader stuff away from MC specifically to make this possible. So it's not like something that we provide. But the main hint about what kind of games is other Java-based games.

**Jaai#9049** (730700346069876776)

Would be adding a standard like must download package for devloping stuff? (like Aurora just stated)

**Gdude**: I have a question with some typos in. I think can guess what this means. That's basically what the Build Tools are. IDK what else to say about that. The way you develop mods for Quilt, and ideally you follow the setup in our example mod, using the example mod with our Build Tools. It's kind of hard to answer a question phrased like that, but that's how you write Quilt mods.

That brings us to the bottom of the list of questions. We do still have a few minutes if anyone has any further questions, or if there's anything that people want to discuss. That goes for people on Mumble as well of course.

**CheaterCodes**: I want to say a quick thank you to the community for actually helping in the Beta test and helping to give fedback on stuff that's broken.

**Gdude**: Yeah, it's extremely helpful. This one wasn't asked with `/ask` but I'll answer it.

**Janetyqua** — Today at 12:52 AM
when quilt will stop support fabric how will the migration work?

**Gdude**: We're not planning on dropping support in the sense that like there's a timeline for it. We're just going to maintain it until it becomes too much for us to maintain, I guess. If it gets to the point where maintaining Fabric support is detrimental to the rest of the Quilt project, then what we'll do is, we'll stop maintaining it, and we'll hand it over to the community to maintain on their own. 

Obviously it won't be entirely on their own. We'll support them through it, but it's not just something we want to see disappear, even if it gets hard to maintain. It's just that we'll have to plan for that eventuality more than anything. That will also be on the newcomers' guide that I'm writing by the way, and I'll update the FAQ as well. Because I did not word those very well the last time I wrote them. Thanks for that question **sciwhiz**, I must decline your offer to show Kotlin, hehehehe.

**CheaterCodes**: I think we're good.

**Gdude**: Yeah, that seems like everything. I'll just mention a comment made in chat. Zoe points out xey think that it would be interesting to have a team for managing things to do with the other teams. So ~~XanderPoes~~ correctly pointing out that the teams manage themselves more or less. But I could see a secretarial team being more or less useful, just to handle the busywork of project management, so that the developers can develop. However, I'm not sure we need it right now. It would be interesting, and it could be quite useful, but it's hard to say in the moment whether it'll be a good idea.

**XanderStuff** — Today at 12:48 AM
ideas on lessening burnout: 
quilt devops team, and/or people dedicated to checkingingin on quilt team members, making sure they're not being burned out, and asking questions to suspicious out anything that could be an indicator of burnout or dissatisfaction with interacting with other team members.
note: actually this could maybe be a nice thing for more than just dev team, could be for mod and administrator team as well.
kinda reminds me of one of the roles of the ship's councilor in startrek

**CheaterCodes**: It seems to originates from the entire burnout thing. So I think that's different from what you're thinking.

**Gdude**: You think so? Oh, I see.

**CheaterCodes**: I think it was mostly about having someone to like make sure that people aren't burnt out. The thing is, that would be a very, very unthankful job and you just need the correct person for that. That's not just something where you could just throw any volunteer in. Dealing with burnout is like... If it's proper burnout, it's a medical condition, essentially. It's a mental health issue, not just someone neds a little bit of help. It's not something I would just want to throw anyone in.

**Gdude**: Yeah, exactly.

**CheaterCodes**: And people who like then have to deal with burnout people are very vulnerable to burnout themselves as well. So you need a professional for that, and we don't have a professional for that.

**Gdude**: That's also true. It's an interesting idea, but that is a lot of good points you make there, hehe.

**CheaterCodes**: I mean, there is an alternative of just doing peer stuff. Just be sure to talk to people around you so they can notice it and they can help clear on. Just spread the load among the entire team and then it's fine. But, yeah. Yeah!

**Gdude**: Yeah, I mean I will say, it's not like we're not here for each other. As **CheaterCodes** said, there is a pretty chill community on Toolchain and internally in general. Like, nobody's left on their own to deal with things, but it just sometimes it gets to the point where there's not like enough people on something. 

It would be good, and I think probably the easiest way to mitigate that is with more people to help out with the different projects. Like pretty much all of the projects could do with a few extra pairs of hands. The Community Team could do with a few extra pairs of hands, a couple extra moderators. Pretty much everyone could do with a few more helpers. That's probably the easiest way to avoid people burning out: It's to spread the load as **CheaterCodes** says.

Alrighty, yeah, it's been about an hour, so I think we're going to call it here. Thanks for coming everyone. As is tradition, I'm sure they'll be a sort of after-party in the `#voice` channels. Maybe there won't, but who knows? And yeah, we'll see you again in 2 weeks, of course. And thanks for coming. And as **CheaterCodes** says, it's been great that everyone's been willing to help with the Beta. Please keep using it, and keep throwing issues at us. It's good to get things fixed, and we can't test everything on our own, so thanks. We'll see you in 2 weeks.
