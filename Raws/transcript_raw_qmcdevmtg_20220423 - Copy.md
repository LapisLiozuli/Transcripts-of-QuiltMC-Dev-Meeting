nngdu: Anw, how are you all finding the Beta? I was talk- to y'all in chat, how's the Beta folks. I thk I wasn't spk- into the mic close enuf last time. Yeah, I figr_ there'd be a few issues w the cplx stuff, but that's teh way betas go right? I hv crtn[ seen some ppl work- overtime to get ths done tho, which is rly nice. Altho I hope they don't burn out. Ah, Discord once agn destroy- all my shortcuts. Excellent.

Yeah, soonTM. We'll get there, no worries. Altho I'd be supz_ if some of the others didn't want to have a break aft the kinda crunchy week we had. I wld not blame them at all. I'll be honest, I'm a cplt traitor, I've been play- Create: Above and Beyond, so... Imn, I haven't played MC in years so this is great.

nnscr: ## sschr15 *—* Today at 12:04 AM

i saw effort being put into getting chasm functional under quilt loader already so that's something

nngdu: Tt's right, we'll be talk- abt tt a bit ltr I'm sure. Alrt, b4 we get start_, Mumble side, how's the audio?

???: Good

nncheat: Sounds great.

nngdu: So do you, ty. I thk we are abt in t to get started. J a second. Yeah, let's get start_ Alrt eone, wlcm to the mtg as alw. If you're new here, we do this every 2 weeks ideally. It usually lasts for abt an hour. It smhw alw seems to fit within an hour even if we are like up to the wire. If you'd lk to ask any qns, use the `/ask` cmd. Tt will put a qn in the queue and we c ans them aft we've gone thru all of the teams. sschr is doing my job in chat, thx nnscr. Let's get started then. nncheat, wld you lk to talk on behalf on ttbuto then for a min?

nncheat: X4tun[[, our main pgbuto guy, nngli, is not here. He's been kinda run- a marathon b4 Beta, so most of the commits tt hppn_ were by him and I'm not aware of what actually hppn_. But I wanna j use this oppy to thank him for buto and j wanna point out tt it's been supz-[ smooth, except for a single hotfix tt ig was tknl[ wasn't even necs but made it nice, so eth went fine on ttbuto's side I thk. 

Thr are some details, I actl[ 4got to pin it. We have transitive dependencies pull- in fapi hb one of hte biggest buto issues. Which cb disabled using = what's it called = dep substitution. I wld strongly rcmd NOT to use- not to disable transitive dependencies, tt can mess stuff up. I have it swhr in the Community Discord, I might ask sone to pin it ltr. But if you're hv- any trbl w buto, feel free to ping nncheat if he's avbl, that's me. And I'll try to help w tt stuff. But so far it's been fairly smooth, luckily.

nngdu: Alrt, thx v much for tt. I blv you're also down for CHASM, so kp gg if you lk.

nncheat: CHASM was not actl[ a part of Beta, so thr wasn't lk a big sprint or ath to mk it hppn. Well, I've been spend- the past few days try- to get it into Loom. Which was supz-[ ez, gvn how clean the CHASM=Gradle plugin was from the Gradle perspective. It j integ_  prfk[ fine into Loom, which was a v nice supz. Now I'm try- to get it load_ into Qload, which is a bit more work j bcz I've nvr loaded Qload b4 prpr[, so tt's gonna tk a bit longer. 

And a/s doing this= I'm bsc[ j doing this to find issues w CHASM, try to fix it and evtl[ get it out so tt ppl c patch stuff. And I've been fix- a few bugs here adn thr, nth big. But yeah, now tt Beta is over, I'm excited to get back and take a look at CHASM bcz it's been kinda put off since it wasn't realistic for Beta. But now we can go full force agn. 

I wld lk to pt out here tt rn I'm bsc[ solo- CHASM, and I wld v much apc8 if aone is itrs_ in help-. I thk the worst part is out of the way anw, but thr's j a ton of stuff left to do tt I wld apc8 help w.

nngdu: Tt's great if we cld see more ppl work- on CHASM honestly. It's gg tb a fantastic tool, and it's one tt's unq[ applicable to pretty much the entr Java ecosys and not just Quilt. So it'd be rly nice to get a couple of ppl work- on tt if aone is avbl and itrs_. Okay, ty for tt nncheat. We'll mv onto Comy Tools, and tt's me of course. 

W the road to Beta, I suppose, thr were q a few ths to do and I kinda ran out of t. But I did still mng to get q a few ths done. On Discord you'll notice tt Cozy h replaced our old tag sys. The tag module is also avbl for aone to use if they're writing a Kordex bot, which is the fmwk tt I wrote. Tt's on Github, it's not docu_ yet, but it's thr and there's egs, so if aone wants to steal tt, go ahead. It's on the Maven.

I've also been work- on the `#wlcm-chnl` sys. Tt works. I actl[ add_ a role=picker to it, but we're not q rdy to use tt yet. But agn, tt's on the Maven if you wanna look at it, and the `#wlcm-chnl` h alr been set=up. It's kinda lk a data=driven chnl sys. 

As for the website, I've been work- on the install] pages over hte past wk or two, Ig. Tt took a fair bit of work to figr out a layout tt works j to rlz_ tt it doesn't rly work tt well. I am going to chg it, but for the t being it works, ig.

Smwt rel_, if aone is a CurseForge user and wants to see us supt_ by CurseForge, plz do gv us a vote at the link tt I j put in chat. It helps a lot. I'm not sure=  I don't thk thr's ath else for ttcotl atm. I've still got a few ths to do on the site. I'm work- on lk a guide for newcomers, and thr's obv[ a lot more Cozy stuff to go. So yeah, thr's still a few ths hppn- thr, but it's gonna be a fair few ths. I j didn't hv enuf t x4tun[.

https://curseforge-ideas.overwolf.com/ideas/CF-I-2662

Alrt, nnax, wld you lk to talk for qload?

nnax: We've had= Well, nngli has done a lot of inrl fixes, which were gd. But the public chgs hb tt the Quilt pre-launch entrypoint had to chg its name, bcz sadly it turns out we cannot use the same one as Fabric's. It j doesn't work inrl[ w method prfr], I thk. So Quilt's is now `quilt_launch`, not that many mods shld be using it, but tt's chg_ anw. 

The modlist in logs is now sorted ab[[. Tt's only in logs, but it's a lot nicer to read now. We've got a few mixin compat fixes which are impt for Fabric mods, I thk. As well as there's been a bunch of inrl fixes but I won't talk abt them here. The commit list is whr you'd wanna go to see what they are. I thk tt's abt it.

nngdu: Alrt, thx nnax. I'm gotta say it, it's been q impressive to see so many Fabric mods pretty much work- out of the box, even lk this early into the Beta. It's lk, honestly, the fact tt eone's mng_ to pull tgt and mk tt hppn is frankly astounding, hehe. So gd work.

nnax: I thk you c thank Quilted FAPI for most of tt tho, as most mods don't touch qload tt much.

nngdu: Abs[, they've been a huge contrib] too. But if qload can't load them up, then it's not get- tt far. Anw thx for tt nnax. nnoro, it's your turn for Mapg I blv.

nnoro: Yeah. Ig thr's not too much for mapg. Yk, your gnrl stuff, we're in ss=phase rn, so we're chugg- along with those. I wld lk to say tt the Rendering Mapg PR = tt hb in work since August = was merged sometime in the past week, I don't rmb xk[ when it was merged. But we hv tt merged in so the render- names for qmap shld be accu and up=to=date, which Ik was a big prbm w Yarn. So tt's rly great. And yeah, we're work- hard on try- to get eth mapped rn, esp in 1.19 ss as Mojang j kp add- more and more stuff, but it's coming along v well.

nngdu: Alrt, tt's great to hear, thx for tt nnoro. Next is nnaurora w the ttqsl.

nnaurora: Not a lot of ths hv hppn_ since Beta. So since the last mtg, the Recipe API got merged, it's quite a big API, and QSL also got published for Beta. But we published the Quilted FAPI model. And since Beta, we had 10 betas for Quilted FAPI and 6 betas for QSL. Anor big PR hb merged, which is Registry Entry Attachments API which cld be kinda compared to a registry dict or sth lk tt. 

O/w thr's not much to say. But a huge thx to all the contributors since bring- Quilted FAPI to Beta was a lot of work, and was q stressful, and I don't actl[ know if I'm supposed to talk abt Quilted FAPI rn. But for qsl, aside for ask- for more ctrb], lk rvw- PRs bcz it rly helps, I don't hv much more to say.

nngdu: Alrt, ty for tt. Wait... Did they resp? They did not resp. Dangit, I'm gonna hv to mispronounce this now. Some of you m know, we have a new team. It is the Quilted fapi team which contains nnem and a name tt I can't pronounce prpr[, I'm j gonna say Ennui. They do hv a sxn but neither of them are avbl to do this sxn. However, we have kidnapped nnscr to fill in for them, so if you wouldn't mind gg ahd.

nnscr: Alrt then. So qfapi is now a th tt's dev_ by nnem and Ennui primarily. So aone c ctrb as lk any other proj tt's part of Quilt. It used tb called fapi=qsl, but then it was re=organised by Ennui and is now the qfapi. The main system is that now reviews are cplt[ sep8_ from fapi to allow quicker updates and such, which is helpful when qsl adds fetrs tt break fapi. Then, in order to prvt issues w other Fabric mods tt dpd on the api not hv- the same vrsn, the qfapi uses special metadata within Quilt to specify the upstream version as if tt mod actl[ was thr. qsl islf is bundled with qfapi, so you do not hv to istl mtpl ths if you are gg tt route. And nnem hb helpful rcnt[ to supply qfapi to be targeting by fapi 0.15.1, which as far as we know is the latest public rls.

nngdu: Alrt, fabulous, ty for tt. Alrighty, tt comes to the end of the list but thr's still a lil bit more obv[. I've alr asked how most of you are doing w the Beta. It seems lk it's mostly been positive fdbk. Obv[ some ths aren't q work- yet, tt's, yk, tb xpk_ work- w a beta. But obv[, yk, as we've seen, esp in crtn parts of the proj, ppl hvb kinda work- overtime j to fix all the bugs, which is fantastic to see, so thx for tt. 

So nnoro, how wld you say ths hvb since the start of the Beta?

nnoro: A lot. I know thr was a v big rush, and I wanna congratulate eone from all the dffr[ teams for the amzg job they did for mk- it to tt ddln, and ik it was a tight fit and we mng_ to do it. Thr were obv[ issues, and we all xpk_ thr tb issues. But what also supz_ me is tt eone who pushed hard mng_ to kp push-, and we managed to fix most of the prbms tt were imd8[ at launch, and we've been cont- tt energy and mv- it fwd. 

And now we're on a Beta 6 for qsl. I thk we're at Beta 9 for qfapi, stuff lk tt. So we're constantly mk- chgs fix-. And I'm not gonna mk any claims, but at the rate we're gg, I definitely thk a 1.19 rls might be fsbl. However, I do thk qsl needs to mature a bit more, But yeah, w the energy tt we hv rn, we c do a lot.

nngdu: I agree w you, honestly. It's itrs- how much teh velocity of the proj h j kinda picked up over the last mth and so. Eth j kinda seems tb fall- into place, honestly, it's great to see. And obv[ it's bcz of all the hard work tt ppl are put- into it. And it's j great to see tt lk all this work is pay- off yk. Alrt, thx for tt nnoro. Tt comes to the end of the planned segment, and it's the segment whr eone ruins our day w qns. So if aone of you h qns, then plz use the `/ask` cmd. We'll try to get as many as we c so long as they're aprp and not terribly shitpost=y.

nncheat: In the mntm, how was Beta on the ttcomy?

nngdu: Bz. I shld pull out the stats, but it's been crazy, honestly. It hasn't been too much extra stress for us, aside from deal- w all the newcomers bcz it's been huge. I'm j gonna tk a sccreenshot of the stats here and you c see what Imn. Look- at the joins for the past, idk, I'm j gonna say svrl mths, you c see tt we rly peaked pretty much when Beta was annc_. Which yeah. I thk we peaked at abt 170 in Dec, and now we're at nearly 360 joins this mth bcz of the Beta, which is j insane. Yep, it's the highest join rate since the start of the server, as nnsouth says. 

[Discord](https://discord.com/channels/833872081585700874/908095149706444822/967460802137313420)

(## Southpaw *—* Today at 12:24 AM

It's the highest join rate since the start of the server)

Which is great to see. Obv[ it's a bit more work for us. But yk, we're prep_ for it, no big deal. It's j rly lk, since we're test- all the application sys for Discord, we're rly j sorta put- it thru its paces now. But it's been good, thr haven't rly been tt many prbms. Yeah, I hv to say tt it's been great. Even the msg rate is lk much higher than xpk_. Lk in last mth = in geez, I can't rmb, I'd say March = we had about 95K msg. Then over the last week we've had about lk 30K to 40K. It's kinda nuts honestly. But I'm happy, it's all gd news.

nncheat: Yeah, j to sound out on this server, I rly apc8 how chill it is. Thr's not rly much bad stuff hppn- so tt's rly cool.

nngdu: Imn, I thk I hv to say, Imn, as much as you c credit the work we do, a lot of our users are also pretty fanta ppl. One of the ths we rly wanted to do is to encg comy mmbrs to help out w some parts of moderation bcz obv[ we can't be ewhr at the same time. Tt's a th tt's been a prbm in some of the prev comys I've run, but actl[ the ppl hvb pretty excellent abt tt w Quilt, and it's helped a huge amt, honestly. Pls kp send- us modmails, hehe. So yeah, thx for ask-, it's been good.

Right, this is a stack of qns. Let's hv a look at them, shall we?

XanderStuff#4796 (171375148006506496)

any ideas on how could quilt overcome the fears of new contributors? "Unfortunately" quilt has some very talented individuals working on the various team, so I feel like it might make joining a team be perceived as "you have to be similar in abilities to the current team members". idk, maybe that's just me?

nncheat: I thk I wanna ans the first qn right away. Firstly, I'll ask ppl: Does aone know me? I'm not rly well=known in the modded comy. Thr are a few v talented ppl on the team, and a few dfcl tasks lk my baby CHASM. But the rest is j normal coding. But if you cpbl of Java prog-, you're cpbl of ctrb-. And if you're not, mapg ctrb] doesn't nd Java knlg. And if you feel tt you're gett- the hang of it, you c join and do more. Sure thr's stuff tt's hard, but we j nd help. Not necs[ the smartest ppl, but we j nd help. Thr's enuf stuff to do in Quilt.

nngdu: Yeah, the th w Quilt is tt we have so much work tt we nd aone who's OK w Java. I thk we cld do a bit btr w Github lk having better issues set up. But if you wanna help out, j let us know. Tell us what you're gd at and we'll find a place for you. Thx for tt, nncheat. I thk I c ans a couple of these.

Zaeroses 🌷#6355 (806065199609937980)

how has the reception of quilt been in the community so far (before and after the beta)? we aren't part of the community outside of the toolchain server, so we don't really have any picture of the popularity or opinions of mod devs or players

Tt's a rly itrs- qn honestly. Being a proj born fr what we're born fr, thr are a few ppl not willing to csdr us and tt's fine. Rcnt[ thr was a rather controversial post on the /r/ftb. Thr are ppl wonder- why we're splitt- the comy, or not gett- into old drama. I'm actl[ writing a post on this to clear up ths. It's hard to get into the dtls bcz it's such a big comy. But I hv been promised tt a lot of ppl hvb supt- us. I was supz to see tt ATLauncher quietly add supt for us. PolyMC too, Modrinth.

I don't thk the opinions hv chg_ too much betw pre=Beta and current. I will say thr hvb ppl tt were lk, "I'm not sure if this is gonna rls ," and then came in and said, "Yes! there's a Beta now, I'm gonna use this now." It's been great to see too o/c. But yeah, overall it's been pretty gd. Crtn[ thr's been some negative reception but overall I thk tt's the outliers. It's been great to see. Here's the link. Tt's not the link I want. Ty Browser.

I'll tk this one qk[ and one of you shld tk teh ETA one.

nncheat: Dfnt[ mine as well, but aft you.

Exo#9052 (604653220341743618)

Where can I donate?

We were kinda hold- back on this for a while now bcz we hadn't rls_ a rls. As some of you might know, most of if not all of the Quilt infra is actl[ paid out of nnhav's pocket. To try and rls some of tt stress, we actl[ set up an Open Collective which I'll link in chat. We're use- this not j for donations, but also show tt we cb tpnt w our fncs. Bcz we don't wanna get into a sitn whr lk we're get- donations and no one knows whr's the money gg or ath lk tt. So if you rly want to donate, you c. It's cplt[ optional, o/c, we'll kp truck- along. But it'll be great to take some of the stress off of nnhav's wallet, esp csdr- how much time and money he's put into this.

But yeah, thx for tt qn. nncheat, wld you lk to tk one?

nncheat: Yep, abs[. You may pronounce his name, bcz I cannot.

nngdu: I j call him Chris. That's not his real name but...

nncheat: Let's j call him Chris. "Chris is my name," well, thr you go. The qn is:

sschr15#4563 (300606625297727489)

Any ETA on VanillaGradle or Chasm being publicly available for mods to use in development?

Well, no clearly. Pgvg, I've not paid too much to rcnt dev]s. Thr hasn't been too much hppn- on the Sponge Discord which is whr I usually look for upd8s. But commits are hppn- e now and then. So I cannot ans too much about pgvg. I thk what it's mostly miss- is re=mapping jars at the end, bcz I thk input mapping is fine. But yes, tt's miss-.

Rgrd- CHASM, as said b4, I'm work- on get- into qload. I'm not sure how soon it'll be avbl. It's gonna be either j a branch of qload whr I make some unoffiical builds so ppl c test it out. But the more I look at it now, the more lkly it is tt I'll actl[ hv to cplt[ rmv remove Mixin and access wideners to add CHASM. Which means for test-, it's gonna be a while until Mixin and CHASM are back. So dfnt[ not gonna hppn on the main Loader any time soon. It's gonna be dfnt[ a few months more.

nngdu: Alrt, thx for tt nncheat. These rly seem tb largely comy=themed qns for a chg. Lenrik asked a qn, I'm not rly sure how to ans tt tho.

nncheat: We don't rly hv an ans to tt, at least not rn.

nngdu: We kinda don't, but I wld lk to hv one.

nncheat: Well, let's tk the qn and talk abt it. So lenrik asked:

lenrik#5193 (437296242817761292)

is there any way that you can/are making sure that people are not overworking themselves while working on the project?

So I thk one ez way is tt we hv a pretty chill comy on the Tlcn Discord, so thr's usually not too much pressure fr other ppl to get sth done qk. But if you are thk- of ath in ptcr, any options you hv to mk sure tt ppl don't over=work tslv, plz let us know. It's not sth we've rly looked into, I thk.

nngdu: Yeah, Imn I wld q lk to see some ideas on tt, bcz it does bother me. As a serial over=worker mslf, Ik tt ppl c get into tt sitn. And lk we metn_ earlier, nngli is kinda burned out bcz of the amt of work tt nd_ tb done to rch the Beta trgt. We hv tb thk- abt tt a bit more care[[ if we do tt agn w anor ddln. But yeah, it wld be great to hear some ideas. If aone has any ideas on tt, we'll tk them onboard to listen to them.

Southpaw — Today at 12:36 AM
We have zero expectations of your performance

## glitch *—* Today at 12:37 AM

i mean the beta turned into a grind at the end

sciwhiz12#1286 (607058472709652501)

What contingency plans, if any, do you have in situations where Discord goes offline due to technical difficulties/outages?

Or I asum a roving band of mutants.

Well, we hv a few ideas. We did look into alt chat ptfms a lil while ago. We actl[ were on Matrix for a while, but tt turned out tb bsc[ impossible to moderate prpr[. J from a tknl perspective, it j wasn't up to scratch and we weren't gg to host one j for 3 chnls. I looked into Zewdlip: While it worked q well, it was a lil weird and it also gave eone's email addrs to staff mmbrs and I was not happy abt tt. Anor th is Revolt, which I csis[[ 4get to chk on. But Revolt is a Discord clone I've been kp- an eye out on. Thr is a server thr unofficially tt I've set up for Quilt, but it's not rdy for use. It's j not, it'll get thr, but it's not thr yet.

Anor altv I metn = even if Discord does go a bit dark = we do have Github Discussions. Eone's thr, more or less, so we are able to fn still. And we are also plan- on get- a forum up soon, hope[[ anw. Ik the **Starchild** sys is work- on tt. So those are the ths we're look- at atm.

I rly wanted Matrix to work. It doesn't. I wish it did bcz it wld be lk the ez option for us, but yeah, it's j not gonna do it. Thr's other options o/c, stuff lk Githere? and MatterMost? and Slack, god forbid. But we'll see. Idth it's gonna be a realistic issue. Lk we hv the website, so if sth does hppn, we c qk[ set up sth if we nd to. I'm not super worried rn, tb super honest. Oh, that's some news I c ins.

## kb1000 *—* Today at 12:39 AM

multimc just merged my quilt PRs btw

Tt's gd news. Ig we'll be get- Quilt supt in tt shortly. But kp an eye on the website for tt one, I'll upd8 the page when we hv more info on it. Anor qn from sciwhiz:

sciwhiz12#1286 (607058472709652501)

Does the Community Team have a team on GitHub, for the use of the relatively new-ish organization moderators feature?

Not spfc[ for tt prps. I've look_ at it, but it doesn't rly help us x4tun[[. The main issue is, it kinda halfway bridges the gap, but we nd tb able to del issues. And the only way to do tt is w RecoAdmin? atm. So our curr apch is gonna be add- fn to Cozy tt c do tt on our behalf rather than gv all the ttcomy full access to eth. The ttinfra h a Cozy a/c on Github tt I setup, so tt's prob what we're gonna use for tt. It wld be nice if Github Perms didn't suck. Rly annoyingly, on Github Enterprise, you c set them up xk[ how you want them. So idk why you can't j do tt on Github. But yeah, it's not an ideal setup. The moderation thing helps, but we do nd tb able to del issues, so yeah, it's still not q thr x4tun[.

Sciwhiz w the comy qns. These are alm all comy qns. Imn I'm fine w tt, but it's j unusual.

nncheat: Bcz the comy's so amzg.

nngdu: Yeah, you're right. They are, they are amzg.

sciwhiz12#1286 (607058472709652501)

Why is the icon for the Toolchain Server webhook in the community server different from the Toolchain server's avatar? :)

It's j Discord round- the corners too much. It shld be xk[ the same, IDK why it looks lk tt. It is the same icon.

sciwhiz12#1286 (607058472709652501)

Any possibility of a screenshot of the QuiltMC teams page (with all subteams visible), for curiosity's sake?

Hv you seen the Teams page? Eth is visible. Imn, we keep tt up=to=date. But if you rly want a screenshot, Imn sure. Lemme j crash Discord for a moment. Here you go, knock yslf out.

[Discord](https://discord.com/channels/833872081585700874/908095149706444822/967465582784024621)

Ik it looks weird, but tt's what hppns when you do tt, so hehe, good luck.

nncheat: I thk the qn was rgrd- the Github Org]s. Yeah, but eth on the Github Org] page is also here, so...

nngdu: Yeah, thr's j no dffr], rly.

nncheat: We can't show a screenshot of tt bcz of all the upset anw, Ig.

nngdu: Ah, ty for tt nnem. Those titles look weird on this. Ah, I'll fix those later.

nncheat: If you're OK w me leak- this, I'll post teh screenshot as well.

[Discord](https://discord.com/channels/833872081585700874/908095149706444822/967465805946179645)

nnoro: I thk it's fine.

nngdu: I don't mind but yeah, if nnoro says it's fine, then it's fine.

nncheat: I thk it's all on the website anw, so it shouldn't be a prbm.

nngdu: It is, yeah.

nnoro: J mk sure to blur out tt one. I'm joking.

nncheat: "Oh no, eone knows about the secret Eone Team."

nnoro: Oh, you can't see the other secret team, only I can see that.

nncheat: Oh right, bcz you're Admin, I 4got.

nnoro: Yeah. Don't worry, these are the only impt ones.

nncheat: The Eone team is actl[ new, is it? I haven't seen tt b4. Or maybe it's new tt Github shows it?

nngdu: Idk, I thk I made tt ages= No, I made tt when Discord had a massive outage, tt was me. And I was lk, we shld hv swhr to talk, and then sone pointed out we had the test- forum we cld test, so we used it. I do not know abt tt sciwhiz, you'll hv to tell me abt tt ltr. OK, Ig I cld take the next one, IDK if thr's aone btr suited to ans it than me. Maybe nnoro? It's kinda hard to ustd the word- of tt one. Or I j take it.

nnoro: Uhhh, I thk I c.

nngdu: Sure, go ahead. You click it.

Zaeroses 🌷#6355 (806065199609937980)
does quilt have a more general goal as far as the player experience as a whole goes? like, a general goal linking together how players would interact with various areas of quilt in practice?

nnoro: Oh yeah, you nd to click it, hehe. Idth necs[ irxt w the dffr[ areas of Quilt, but we wanna prvd a more unified way for ppl to j play. So, one of the main ths w tt, our Loader plugins, so tt you c load Fabric mods. Whr the player exp isn't so much formed ard us irxt- w pull=up?, but we prvd fetrs to players tt allow them to play w mods in their own dffr[ ways. If tt makes sense, I can't thk of tt others since I'm more of a devr, but Ik tt Loader plugins will be sth unq tt Quilt brings to the player exp.

nngdu: Imn, I thk it's a gd qn. A few ths tt come to mind for me are UX ths, lk fix- the terrible erorr popup, and get- a nicer installer and all tt. Imn, a lot of the ths tt Quilt is do- is sort iterating on older ths tt were nvr tt gd, but rly cld do w attn and impv ths. At least fr what I've seen. It's itrs- tt **Zaeroses** bcz **Zaeroses** is work- on error stuff atm, or at least plan- to, as far as I know. It's kinda a dfcl qn to ans w the way it's phrased, but tt's what comes to mind for me.

Alrt, nnaurora, go ahd and take tt one. It's OK, click the other one, nbdy will notice, hehe.

Jaai#9049 (730700346069876776)

What is qsl idk im new to devloping?

nnaurora: So bsc[ qsl is the Quilt Std Libs. They are tools for devrs to irxt w the games more ezy. Or unified ways to try to bridge to other mods. Foreg, one of the APIs prvds ways for mods to= My thot prcs got interrupted, so what was I say-? So they can prvd ways for mods to... lk create blocks, but in ways whr it won't conflict w other mods and stuff.

nngdu: Alrt, all gd. Yeah, nnax, you c tk tt. You c click the button again as well.

sschr15#4563 (300606625297727489)

I heard before that Quilt is meant to support multiple games besides Minecraft. Any hint on what kind of other games? (@Lapis Liozuli)

nnax: This is sth v spfc to qload. Tt it's meant tb able to customise Qload in a way tt you cld use it for other Java=based games. But I don't thk the QuiltMC Team is directly doing this in add]. We're still abstract- a lot of Qload stuff away from MC spfc[ to mk this psbl. So it's not lk sth tt we prvd. But the main hint abt what kind of games is other Java=based games.

Jaai#9049 (730700346069876776)

Would be adding a standard like must download package for devloping stuff? (like Aurora just stated)

nngdu: I hv a qn w some typos in. I thk c guess what this means. Tt's bsc[ what the pgbuto are. IDK what else to say abt tt. The way you dev mods for Quilt, and ideally you folw the setup in our example mod, using the eg mod w our pgbuto. It's kinda hard to ans a qn phrased lk tt, but tt's how you write Quilt mods.

Tt brings us to the btm of the list of qns. We do still hv a few mins if anyone h any further qns, or if thr's ath tt ppl wanna discuss. Tt goes for ppl on Mumble as well o/c.

nncheat: I wanna say a qk ty to the comy for actl[ helping in the Beta test and help- to gv fdbk on stuff tt's broken.

nngdu: Yeah, it's xtrm[ helpful. This one wasn't asked with `/ask` but I'll ans it.

Janetyqua — Today at 12:52 AM
when quilt will stop support fabric how will the migration work?

We're not plan- on drop- supt in the sense tt lk thr's a tmln for it. We're j gonna mntn it until it bcms too much for us to mntn, Ig. If it gets to the pt whr mntn- Fabric supt is detrimental to the rest of the Quilt proj, then what we'll do is, we'll stop mntn- it, and we'll hand it over to the comy to mntn on their own. Obv[ it won't be etir[ on their own. We'll supt them thru it, but it's not j sth we wanna see disappear, even if it gets hard to mntn. It's j tt we'll hv to plan for tt eventuality more than ath. Tt will also be on the newcomers' guide tt I'm writing btw, and I'll update the FAQ as well. Bcz I did not word those v well the last t I wrote them. Thx for tt qn sciwhiz, I must decline your offer to show Kotlin, hehehehe.

nncheat: I thk we're gd.

nngdu: Yeah, tt seems lk eth. I'll j ment a comment made in chat. Zoe points out xey thk tt it wld be itrs- to hv a team for mng- ths to do w the other teams. So XanderPoes? correctly point- out tt the teams mng tslv more or less. But I cld see a secretarial team being more or less useful, j to handle the busywork of proj mng], so tt the devrs can dev. Hwvr, I'm not sure we nd it rn. It wld be itrs-, and it cld be q useful, but it's hard to say in the moment whether it'll be a good idea.

XanderStuff — Today at 12:48 AM
ideas on lessening burnout: 
quilt devops team, and/or people dedicated to checking-in on quilt team members, making sure they're not being burned out, and asking questions to sus out anything that could be an indicator of burnout or dissatisfaction with interacting with other team members.

note: actually this could maybe be a nice thing for more than just dev team, could be for mod and admin team as well.

kinda reminds me of one of the roles of the ship's councilor in startrek

nncheat: It seems to originates from the etir burnout th. So I thk tt's dffr[ fr what you're thk-.

nngdu: You thk so? Oh, I see.

nncheat: I thk it was mostly abt hv- someone to lk mk sure tt ppl aren't burnt out. The th is, tt wld be a v, v unthankful job and you j nd the correct person for tt. Tt's not j sth whr you could j throw any volunteer in. Deal- w burnout is lk... If it's proper burnout, it's a medical condition, esnc[[. It's a mental health issue, not j someone nds a lil bit of help. It's not sth I wld j wanna throw aone in.

nngdu: Yeah, xk[.

nncheat: And ppl who lk then hv to deal with burnout ppl are v vulnerable to burnout tslv as well. So you need a professional for tt, and we don't hv a professional for tt.

nngdu: Tt's also true. It's an itrs- idea, but tt is a lot of gd points you mk thr, hehe.

nncheat: Imn, thr is an altv of j doing peer stuff. J be sure to talk to ppl ard you so they can notice it and they c help clear on. J spread the load among the etir team and then it's fine. But, yeah. Yeah!

nngdu: Yeah, Imn I will say, it's not lk we're not here for each other. As nncheat said, thr is a pretty chill comy on Tlcn and inrl[ in gnrl. Lk, nbdy's left on their own to deal with ths, but it j sometimes it gets to the point whr thr's not lk enuf ppl on sth. It wld be gd, and I thk prob the easiest way to mitigate tt is w more ppl to help out w the dffr[ projs. Lk pretty much all of the projs cld do w a few extra pairs of hands. The ttcomy cld do w a few extra pairs of hands, a couple extra moderators. Pretty much eone cld do w a few more helpers. Tt's probably the easiest way to avd ppl burn- out: It's to spread the load as nncheat says.

Alrighty, yeah, it's been abt an hour, so I thk we're gonna call it here. Thx for coming eone. As is trad, I'm sure they'll be a sorta after=party in the `#voice-chat` channels. Mb thr won't, but who knows? And yeah, we'll see you agn in 2 weeks, o/c. And thx for coming. And as nncheat says, it's been great tt eone's been will- to help w the Beta. Plz kp using it, and kp throw- issues at us. It's gd to get ths fixed, and we can't test eth on our own, so thx. We'll see you in two weeks.
