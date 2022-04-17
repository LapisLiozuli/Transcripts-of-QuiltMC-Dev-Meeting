[Meeting: 27th Nov 2021](https://anchor.fm/quiltmc-dev-meetings/episodes/Meeting-27th-Nov-2021-e1au58n)  
Another public developer meeting - uploaded for your convenience! In all Quilt developer meetings, we start by asking all the development teams what they've been up to. After that, the community team talks a little about what's been going on, and then we accept questions!  
If you'd like to listen to our meetings live, or you have questions to submit, please feel free to join us - every two weeks, [on Discord](https://discord.quiltmc.org/).

=========================

nngdu: If you’re new here, this is just a collection of recordings of each public Quilt Project Developer Meeting, lightly edited for comfort and uploaded as a podcast for ease of accessibility. Our meetings are held on Discord every two weeks and recorded live by a fleet of Discord bots. Hence the lower audio quality. For more information on what the Quilt Project is and what we do here, please head to [https://quiltmc.org](https://quiltmc.org).

=========================

nngdu: Alrt, let's get started, shall we? Uh, it's gd to hv eone here agn. I didn't ping eone this time, which I'm sure ppl will be apc8[ of, smwt. Let's get started with... nncheat, do you wanna talk abt CHASM a bit? What's gg on?

nncheat: Yes, I wld like to talk abt CHASM a lil bit. Lots hb hppn- on CHASM during the last 2 weeks. Last t I talked a lil bit abt how I slowly kept work- away on the new vrsn of CHASM tt's hope[[ no longer ~~poor tide~~, and thr's rly a lo of prog. As ppl may or may not hv seen, we successfully had our first actl ~~Bedrock~~ tfrm]s on the new vrsn, and it works v well. Aft fix- some initial perf bottlenecks, we're now ezy do- millions of tfrm]s per second, so perf shouldn't be a prbm which was a lil bit of a concern in the past bcz we had no info on tt.

I hvb work- on the CHASM-Lang a lil bit, which is not public yet. Not sure if it's gonna be the final vrsn, but nd sth for dev]. And yeah, all in all, good prog. Feel free to chk it out. It's worked rly well. Ctrb]s hvb great. I opened a bunch of issues on the first day for the public, and ppl are v eager to help join in and tackle some of the ezr and more cplx tasks, which is rly great. We're try- to do this for some other projs now, so if you're itrs_ in doing some lil ths tt alw help out, thr's alw, alw a bunch of stuff tt ppl don't wanna do bcz it's j a bunch of work tt are not rly hard.

(nngdu chuckles.)

Lk foreg for CHASM, it was... What was the top one? Ah, it was j re=format a big class tt h lk a single method with hundreds of lines of code split up into mtpl methods, and it made the code so much btr. Aone c do tt, but I'm more worried abt gett- the rest gg. So tt work_ rly well, and we'll try to do tt for other projs as well. So tt's cool. Um, yeah. It's  not lk we're gonna hv a full rls on Tuesday for 1.18, but we're gett- prog done. Rly gd prog, which is rly cool.

nngdu: Yeah, it's q impressive work, actl[, csdr- how much longer you guys thot it was gonna tk to get to this stage.

nncheat: It felt lk= It rly was lk, yk this th whr it's lk 80% planning and then it's 20% execution? It's lk, CHASM hb abt 99% planned=out until now. Protoype was mainly thr for j more plann-, and it's j such a gd picture in mind of whr you wanna be and the impl] is j hack- away at the keyboard and not thk- too much abt it. So yeah.

nngdu: Do you thk the og[ est of, was it lk 2 years, was a bit over=the=top mb?

nncheat: I don't know when tt est was. Yeah, thr's still a bunch of stuff to do. Thr's still a bunch of stuff to do, bcz foreg we don't hv the logs impl_ yet. And we're not entirely sure how to rep local variables or method parameters. All tt stuff still nds tb figured out. But yes, for the most common ths, the injects, for the simplest inject, tt wld alr be work-. So yeah. Looking very cool. Very excited.

nngdu: Great, tt's excellent, great work hb done thr. Yeah, I'm excited too. nnsup, wld you lk to hv a qk chat abt Decompilers?

nnsup: Um, yes. First of all, I wld lk to say tt the Quiltflower-IDEA plugin is now avbl for eone to use on the store made by nnearth. It's rly gd, I wld rcmd it. We also hv a snapshot repo if you haven't been look- at the devlog. It h bleeding=edge builds for eth tt we've been working on, which incls impv_ ~~tribal~~ rescs, switch expressions, improved ~~gline~~ mapp- once agn by nnearth, the formatter by nnearth agn, some more miscellaneous fixes and some optimisation.

Thr's also a 1.6.1 rls to fix a few of the most glaring bugs with 1.6.0. It might be gd if you're look- to recompile the game or sth, but it's not too impt, I thk. I wld wait for 1.7.0, bcz then you'll get all the cool stuff. I thk tt's it.

nngdu: Tt sounds great. It's alw rly impressive to see all the work coming from tt proj, esp coming from your hands. It's kinda ridiculous honestly, kinda gd stuff.

nnsup: Ty.

nngdu: I thk eone agrees thr. Alrt, nnalex, nnearth, I thk one of you is to talk abt qload. Maybe nnalex?

nnearth: Nah, I'll talk abt what I've done. Imn, I've been work- on merge- usrm bcz lk we've been fall- q bhd on usrm. Um, pfft, j read- what nncheat said.

(nncheat: "dunno, I feel like I always pick up the projects earth got burned out on :pineapple:")

Yeah, so I got abt halfway thru tt, fixed all the merge conflicts, and then I bcm kinda bz w upd8- my own mods for 1.18 bcz I don't want them to fall bhd either. So nngli offered to tk over the merge- usrm and he was gg to do it b4 college og[[, but apar[ h not. He's not managed to dl it, but anw tt's being done. Lkly won't be out for 1.18 straightaway at least. nnalex, do you wanna talk abt some of the stuff you've done as well, bcz Idk ath abt tt.

nnalex: Sure. So I've been doing a bit of work on loader plugins. They're still in fairly early dev] atm, it's not rly usable, but they're prog-. Tt's abt it sadly.

nngdu: Tt's alrt, prog is still prog after all. Uh, OK, nnoro, wld you lk to talk abt qmap? Yes, I said "Prog is still prog" and now I'm blocked by **haykam**, who cares hehe.

nnoro: Haha, yeah. Qmap hb gg on rly well. We've been gett- lots of PRs in the past 2 weeks. I thk thr's 4 rn tt are alm rdy tb merged in b4 1.18. I thk thr's one tt I nd to go and fix up, tt's a huge re=factoring of render-, but I j don't hv t for tt but it prob shld be done bcz render- code's not v great but wtvr. 

Other stuff, the build script for qmap since last week hb cplt[ redone. I hv PR tt re=wrote all of it into Java istd of Groovy, and it's a lot btr now. It's a lot ezr for the qmap Team to add new featr to tt build script. So one of the ths tt we did is we made it so tt you cld xcpil the game in both Quilt file and CFR. Prev[ it was j CFR, so tt's nice. Anor th tt we're work- on rn is add- ways to chk tt mapg are spelled correctly, tt public static final fields are all=caps and underscored., stuff lk tt. So at least the names, er, not the names but the actl words and stuff lk tt hv consistency. So you don't j see a field and see it as a constant even tho it's sth tt cld chg.

nngdu: OK, crtn[ sounds lk good prog as well. The render- names are sth tt ppl hv had sorta a pain pt for a long t with Yarn, hasn't it. 

nnoro: Yes, I c attest to this personally. I hv worked on Blaze4D, which we chose to switch to Mojmap bcz of some of the poor names. Hope[[ I c get our team to switch back but I'm not sure abt it. This PR is also j the first phase whr I go for 100% mapp- cvrg in the render- and ~~usual~~ stuff. 

Oh yeah, tt's actl[ a big th I 4got abt. Bcz we hv access to Mojmap, sth we've dcd_ to do is mgr8 the Blaze3D pckgs = tt's Mojang's Render- API = into their own pckg if they are part of tt pckg in Mojmap. So a lot of the classes in Yarn tt are in NatMinecraftClientGL are actl[ part of the Blaze3D stuff. And so this PR takes all the render- ones for tt and moves them into `com.mojang.blaze3d`. And tt's to make sure tt yk, what you're look- at is more rep[ of what MC's code is. Bcz Blaze3D was evtl[ plann_ on being taken out. So if it does down the futr, hv- it kinda in its own pckg is helpful. So tt's nice.

And I thk yeah, thr's anor th here. Qmap on Loom got an upd8 a while ago. It now works a lil bit btr and hope[[ doesn't hv as many issues, tho I still see ppl kp popp- up w issues and I'm lk, "Oh no, I don't lk work- with Loom." Bcz it's a very big mess.

nngdu: Well, tt seems tb the inevitability of Gradle plugins at this pt, doesn't it.

nncheat: If Gradle lk fixes my issue tt I opened on their Github, mb I'll go back to pgbuto.

nngdu: Alrt, tt sounds lk a lot of great prog on qmap. We'll come back to you a bit ltr o/c since thr's a few more ths to talk abt, but tt c wait a lil bit. Um OK, nnaurora, wld you lk to talk abt qsl a lil bit?

nnaurora: Yeah. So, QSL. Since last mtg, I thk we merged the Tags API, which means now thr's a way to get tags ezy. And the dffr] w fapi is tt it h tag types, which means you c hv clients in the tags, you c hv clients ~~for bug~~ tags, and you c save your tags as reqr_ or ~~severed~~ by the client. Which are kinda esnc[ fetrs when you thk abt it, so yeah. It's cool. 

It's not yet usable with fapi bcz thr isn't a= Bcz fapi Compat] Lib isn't done yet. But it's also being work_ on bcz since Qload won't be avbl for 1.18, we'll try to at least mk qsl avbl on Fabric istd thru the compat]= thru the fapi Compat] Lib. Which means it's a re=impl] of fapi, but some parts we use qsl istd of its own impl]. So it both ensures compat] and it ~~tells us~~ to use qsl.

And now, thr's still a lot of PRs open which kinda reqr a lot of rvws. The most urgent one curr[ is the event phases one bcz it intros some re=factors. And once it's in, it will simplify a lot of ths, and it will simplify the fapi Compat] Lib. So here are a list of the qsl PRs tt nd some attention. And it's ~~???~~, so hope[[ we c get sth for 1.18 qk[. And the main goal is to hv event phases b4 Nov 13th so tt we c do the fapi compat] qk[. It shld also be avbl shortly, and I thk tt I've said it all.

Oh yes, thr was also some chgs. Thr's a run config in Loom which is 'Run auto=test server'. But in normal envs, it won't run. It won't be auto bcz it will nvr stop. But now w QSL Base, if you incl the quilt.auto_test w a number of ticks, it will auto[ stop the server aft the given tick time. So now the task c actl[ be used otsd of test mods. So hope[[ tt cb useful for some ppl. The other th I wld lk to rvw j as fast as we can is the Game Test API, so we can hv some game tests in qsl fr the start, so we c ensure eth is tested correctly. 

And anor th we cld do is mk a common repo of test structures to ensure tt mods don't break sth. We cld gv to modders so tt they can test stuff ezy w/o hv- to reiterate common tests. So yeah. Idth I hv more to say now, so yeah, tt's it.

nngdu: Tt is a fantastic amt of stuff, I can't lie. You've been super bz, clearly. If aone missed it, nnaurora did post a nice big list of PRs tt nd attention. I've pinned it in the #meeting=chat chnl. So if you're a devr, you're itrs_ in qsl, pls go hv a look. Go help those PRs get some rvws, get some fdbk. Alw apc8_.

(nnaurora: "List of interesting QSL PRs requesting attention:
<https://github.com/QuiltMC/quilt-standard-libraries/pull/53> - Event phases [Urgent]<https://github.com/QuiltMC/quilt-standard-libraries/pull/40> - Item Group API
<https://github.com/QuiltMC/quilt-standard-libraries/pull/33> - Command API
<https://github.com/QuiltMC/quilt-standard-libraries/pull/41> - Block Extensions API
<https://github.com/QuiltMC/quilt-standard-libraries/pull/54> - Loot Table API [port]
<https://github.com/QuiltMC/quilt-standard-libraries/pull/42> - Entity Events [WIP]")

nngdu: Alrt, Ig I'm next. As for the ttcomy, not a whole ton of ths hvb hppn-. I'd say the big one tt aone wld hv noticed is the chg to the mapg cmds. Now thr is still issues w these cmds mostly bcz pghs isn't quite stbl yet. Which means Linkie=Core is= Well, it's not etir[ working w it. As pghs progs, hope[[ we'll work w **Shedaniel** to fix tt. But in the mntm, we've upd8 them to slash cmds and a whole bunch of fixes hvb put in mostly by **sschr15**, or who we often wrongfully ref to as Chris.

(nncheat: "@gdude I think #devlogs are also your domain for this meeting?")

Done a crapton of PRs in the bg tt you guys haven't seen. Yeah, tt's right nncheat. As nncheat ments, we've set up dffr[ #devlog chnls for each of the dffr[ Quilt teams. So for their projs, you c subscribe to the indv chnls if your comys or projs hv spfc itrss in any team's work. They're also fwd_ to the #devlogs chnl on the Comy Server right on the top thr under info.

We've also onboarded a few more staff mmbrs. **Akarys** and **Alizée** who are part of the same plural sys hv joined the trainee team on, I thk it was the 18th. And they're doing well, they've been help- us out, v professional work. O/c nnem h j graduated today. Congratulations, nnem.

nnem: Hello, ty.

nngdu: So ths are moving along. Personally I hv RSI, so I haven't been able to do too much this week or last week, but I'm gett- btr and I'll get back on track w tt agn.. O/c most of what I hv to do is Cozy=rel_. 

We also had a dscs] abt the plurality tools we're using, spfc[ Tupperbox. Some issues were brought up w Tupperbox and the approach we were take- to it. When I'm doing a bit btr, I'm gg to replace tt w PluralKit, which as you m know is an open bot. And I'll integ tt w Cozy a bit btr, so tt shld be a bit nicer for our plural users. 

And o/c, we had Trans Day of Remembrance on the 20th. **LemmaEOF** put out a great annc] abt tt w a few words, if you haven't seen tt, go and tk a look at tt. It's a super impt day bsc[ for our comy. Uh, I thk tt abt covers eth tt I c rmb. C you thk of ath else nnem?

nnem: I thk you covered eth.

nngdu: Alrt, cool. As others have ment_, if you hv any qns to ask any of the teams, incl- ttcomy, you can use the /ask cmd in the #meeting=chat chnl. We're not q at the pt whr we're gonna ans qns yet. I had a chat w nnoro earlier abt how pghs hb= how updates hv hppn_, and I thk he'd lk to talk a lil bit abt tt.

nnoro: Yeah, so, while I am talk- abt how pghs auto=updates and eth lk tt, you guys can send us in some qns so tt aft we're done we c go right into tt. So, pghs is= The way tt pghs is able to so ezy auto=upd8 is bcz Mojang doesn't chg the names tt they use v often, so tt means tt betw vrsns, names wil be v consistent, so tt you cld compile down to the Mojmap names and your mod will work across mtpl vrsns. The only prbm w cpil- w Mojmap names is tt... Crash of course would be in Mojmap, I thk thr were issues able potl re=distro]. Bsc[, no one wants to cpil down j to Mojmap.

So what we dcd_ to do is tt we c take the names and run them thru a hash- algorithm, and then tt hash- algorithm is then what we use. So bcz we only tk the names fr each vrsn, tt means tt pghs has no concept of upd8 betw vrsns, which is one of the issues in pgim, whr you hv to match betw vrsns manually. Which means tt yes, theoretically tt pghs will hv more mismatches and you m nd to cpil your mod mtpl times. But it also means that Mojang most lkly chg_ their fn and it h tb upd8 anw. nncheat, you wanna say sth?

nncheat: Yeah sure. I thk I wanna clean up a lil bit on lk a few more rsns why we don't want Mojmap in gnrl as well as an underlying th. One of the big rsns for me is, work- in a dev] env, if qmap is not perfectly or 100% cplt. Which it never is bcz thr's alw new stuff add_ by Mojang, it cld be v confusing if you suddenly run into Mojmap names when work- w qmap at any t. So tt's one of the rsns why we don't want Mojmap.

The other rsn we don't want Mojmap is bcz it's not prfk[ stbl. You might thk it's prfk[ stbl bcz it's the official name. But one of the v common ths tt hppns is tt Mojang moves classes ard in pckgs and tt will alw break all the mods tt are built for tt vrsn. For pghs we don't hv tt trouble bcz we alw omit the pckg so tt can't hppn to us. And you might thk, "Oh well, tt can't be tt bad if j a few classes are moved ard." But yeah, it also chgs all the decryptions and eth, thr's a bunch of stuff tt c go wrong. So pghs is gd for tt. Also hv- unq names is great.

nnoro: Yep. And since pghs is esnc[ just gnr8_ purely fr Mojmap names, and it doesn't rely on mtpl vrsns, tt means we c upd8 the names alm as soon as a new vrsn or a new pgsnap comes out. So one of the ths we curr[ hv is a Github Action tt is supposed to run every 10 mins, but it's not as consistent as tt. But as soon as a new MC vrsn comes out, tt ~~hashed for Quilt~~ runs auto[ which allows us to upd8 pghs w/o even nd- any human input. 

Which is rly big bcz tt allows not j modders to start work-= Tho thr wld be issues w tt bcz thr wld be no qmap = but bcz it allows ppl to start play- on the new vrsn w mods cpil_ on the prev vrsn, instantly. I see tt as rly useful for a lot of the technical YouTubers who wanna check out new fetrs, and for ppl who use mods like Replay or Iris when the new pgsnap comes out. 

We also plan on hv- smlr workflow for qmap. That is less planned out rn, but it is sth tt we're thk- abt. So sth tt cld potl[ hppn in the near futr is tt the etir qmap tlcn = so both pghs and qmap = will be able tb auto=upd8_ hope[[ within 15 mins of the pgsnap coming out. Cplt[ rmv- the human factor of avbl] fr tt, which is sth tt both qmap has had, not q issues w, but lk we haven't been super fast sometimes. And I'm sure tt's also hppn_ w Fabric. I thk thr is a t tt whr it took lk a day for new mapg to come out for a pgsnap. 

But by doing this auto stuff we allow for you guys, the devrs, to start work- alm imd8[ w new pgsnaps, new vrsns. So we don't hv to wait for, yk, someone to show up and do tt. Which is big bcz Idth thr's any= Thr's no modding tlcn for MC tt does this yet. So by doing tt, it gives Quilt q an advg over the other tlcns.

nncheat: Yep. If I may also add sth onto this, one side is the user side, I thk it's nice. Anor th is also= To be fair, I thk it's mostly bragg- rights if you upd8 w/i 1 min over upd8- lk an hour. But one rsn tt I lk it so much more is bcz rn thr's alw this pressure on the Qmap Team mmbrs. It's lk, "Oh, thr's a pgsnap out. C any one of you mk it w/i lk the next hr to upd8 this?" 

Sometimes tt's fine, sometimes it's, yk, you hppn to be on the PC anw. Sometimes lk, the last few days, where it gets rly at noon for my time, or early in the morning for lk American tmzns, it's rly j not gd to hv this pressure on the devrs to force them tb avbl at tt time. So we rly want this tb fully auto to the pt whr nbdy has to worry abt it. Thr's still alw gonna be some manual match- involved w Yarn, Imn Qmap. But the reqr] shld not be to push out a manual mapg upd8 the first day. But it's fine if it takes 2, 3 days for the first upd8 to come out bcz the initial upd8 is at least good enuf for most ppl to work w. Which is rly j, yeah, it shld rly relieve the pressure.

nnoro: And also the actl rls vrsns of MC, bcz they hv RCs and pre=releases for them, we will reach higher and higher mapg cvrg and thr will be less and less of mapg dropped. So when a full rls comes out, you won't be missing, yk, 10% of mapg versus lk, "Oh, they j refactored how all of entities work. Thr goes a third of the entity mapg in the pgsnap." So it's not sth tt if you work on rlss will be a big issues, but in pgsnaps thr will dfnt[ be stuff tt chgs. And it won't be too hard for us to chg it ard, but it won't be imd8.

nncheat: Yeah, I forgot one th. But I thk I forgot it, so wtvr.

nngdu: It's OK. Well, I see qns coming in. Is thr ath else you two wanna cover on mapg? Alrt, I'll tk tt as a No. OK, in tt case let's mv onto the qns. Let's j hv one second here. nnaurora has deafened, hang on a second. nnoro, wld you lk to tk tt qn rel- to pghs?

nnoro: Yeah, uh, let's see. Is tt the latest one? 
(**!alpha**: "How do you guys plan on handling conflicts on hashed? Hashing does not guarantee uniqueness.")
Yeah, so, thr are a couple of conflicts tt c hppn. One of the conflicts is we hv two classes w the same name. The way we deal w tt is tt= So for classes whr we j hv the raw class name. So if it's lk `net.minecraft.client.MinecraftClient`. So we'll hash j the `MinecraftClient` part. Hwvr if thr's two classes tt have the same name = thr's a couple of instances of tt. Thr's some w `Tag`, thr's some w `BlockStatePredicates`, sth lk tt. If we hv those, we then hash the etir name, incl- the pckg. 

As for methods, if thr are two dffr[ methods with the same name, but dffr[ signatures, we add the signature into the hash. Idth thr's ath for fields. nncheat?

nncheat: Thr's tknl[ no fields. I thk, if I m take over, you're abs[ correct w eth you say. I thk you j missed the pt of the qn. Sorry. I'm pretty sure the qn is actl[ abt hash collisions. Um, bcz, when hashing o/c, it cld hppn tt two dffr[ inputs gv the xk same output. Sorry to cut you off thr. Actl[ nnearth did a real qk calculation back in the day on the first RFC. I was j try- to find it. Couldn't rly find it qk[ tho.

nngdu: Oh, I vaguely rmb tt, yeah.

(Transcriber's Note: I also vaguely recalled this discussion and dug up this [link from a year ago.](https://discord.com/channels/833872081585700874/833876911868346368/841410345876062219))

nncheat: Yeah, I found it, I found it. It's a rly, rly low probability. OK, I found it. OK, he said, "Using the est tt thr are 5,000 classes in MC=" which is abt right, and we want a probability of 0.01, we get tt many bits and then he said, "7.6 digits is appropriate." And then I actl[ used 8 digits now, base=26 digits, which is actl[ more than this. So he est_ tt if [in] every pgsnap, if all the mapg were chg_, and thr wld be a pgsnap every week, then we wld xpk the t until we hv a name collision in 190 years. 

So we dcd_ tt's a non=issue. It cld theoretically hppn, but we dcd_ tt for one pgsnap we hv a name collision. But even if we had a name collision, the chances of them being in the same class, the same method and actl[ being collisions is rly, rly low. So it shld not be an issue.

nnearth: Yeah, and tt's if every single mapp- was chg_ every single pgsnap. You gotta rmb tt most of the mapg stay the same every pgsnap.

nncheat: I thk the qn above tt is more nnoro's area, expertise.

nngdu: Wld you lk to tk **burger**'s qn, nnoro?

nnoro: **burger**'s qn: "> Can hashed work as an intermediary without qmap? I forgot but you probably already said."
I'm asum- your qn is ref- to: Can other mapg be built on top of pghs? And the ans to tt is yes, abs[. One of the rsns I hv also been re=factoring the qmap build script is so tt other ppl can go and write their own mapg using this build script. Bcz if you try to use= Lk it took me forever to figr out how to use the build script bcz it was taken dir[ from Yarn, and it was v= Imn, when I got it, it was 1000 lines long, and thr hvb a couple of ths add_ since then. And so by re=writing in Java, I'm open- it up to more ppl so tt they can use it ezr as well. And yes, pls mk your own custom mapg for pghs. Yk, j by hv- more ppl look- at the code, mb you'll pick up a v gd name, and qmap will dcd to incorporate it bcz we j lk it so much.

nncheat: OK, yeah, I'll tk the CHASM one for the t being. So the qn by **!alpha** is "Why does CHASM need a custom language?"
OK, so, I'll mk this one a lil bit longer of an answer. The short ans to tt is tt it doesn't. It j doesn't need a custom language. The long ans starts w when we made the first prototype of CHASM. Thr was some db8 on what file 4mat we shld use, bcz you smhw nd to= The mod smhw nds to explain what kind of bg stuff and tfrm] it wants to do. So the reqrs for language were bsc[, "It shld be Turing=complete." Tt's bsc[ all the reqr] we had og[[. 

So the first idea was, yk, if we nd a Turing=complete language, why don't we j use JVM=bytecode. Tt's Turing=complete, it works prfk[ fine most of the t. Tt shld be gd. So we xpmt_ w tt a bit. Then we talk_ abt caching. We nd to mk sure tt if our input doesn't chg= Well one goal of CHASM is tt we c hash it. So if you don't chg, mods don't chg your config files or wtvr, you don't nd to re=apply all the tfrm]s. The idea is tt hope[[ it helps w startup t. So we wanted it tb cacheable. So tt meant tt wtvr dcrbs the tfrm]s you want to perf nds tb the same every single t. 

So OK, we nd to mk sure tt ppl don't use System.Random in their transformers. And bytecode meant tt we had to manually chk the bytecode and verify tt it doesn't use ath we don't want it to use. And JVM=bytecode,you c literally import it wtvr you want and thr's hardly restrictions on it. So we had to make a bytecode analyzer tt verifies tt nth fishy is gg on in the transformer. And one of the dcd]s we made aft tt long dscs] was tt we shld prob not use the JVM=bytecode=

(nnearth: "ah yes the fridge verifier")

nncheat: We shld prob not use the JVM=bytecode and istd j make= use some other language tt on its own guarantees tt it doesn't lk import System.Random, tt we c ezy guarantee it's fn[[ pure. So tt bsc[ was the dcd] to make a custom language. Now what kinda form the custom language is, is not xk[ sure. 

(**asie**: "When proposing asm-regex, I was torn between validating JVM bytecode and providing a custom bytecode myself"

nnearth: "wasn't the main reason because bytecode is annoying to generate? and because it requires us to make a stable API")

nncheat: The other rsn= Thx, I alm 4got abt tt. The other rsn I didn't lk JVM=bytecode is bcz= Two other rsns, thx, cplt[ 4got. Using the JVM meant tt we had to prvd a Java=facing API for CHASM which had many issues. We had to verify tt eth was called at the correct t, tt it doesn't call fns it's not supposed to call. Rly restrict the API. 

And the other rsn was tt bsc[ eone who tried sth in ASMR ended up writing the transformer in Java and cpil- it to bytecode. Which was not the pt of the tfrm]. The pt was tt some front=end wld gnr8. But it turned out rly the only conv way to gnr8 a JVM=bytecode is prvd- it in Java. And esnc[ tt wld mean tt eone who makes a front=end, nds to mk a Java compiler and tt's rly not what I wanted for the proj. 

Yeah, so thr's mtpl rsns we wanted a non=JVM language. I was look- at other language options, lk thr's a bunch of stuff, and at the end dcd_, "Yk, I j alw wanted to write a language on my own. I'm j gonna write one by mslf for now bcz it's fun." And thr's no promises tt this is the one we're gonna use at the end. nnkrop also has one tt looks itrs-. It's cplt[ dffr[, so no promises thr. We'll see what ends up being the actl language.

nngdu: Thr's a couple other qns here, but Idk if we c ans them w/o the Admin Team.

nnoro: Madeleine, I'm sure tt thr cld be some way to= Bcz of how Loom works w layered mapg which is a blessing = even tho it's horrible = tt you cld create a fully=encompassing mapg set tt does convert the two. I'm sure someone will mk a plugin tt also takes the hashed names and converts them to pgim so tt you c see the= ezr to visualise namespace. pghs is dfnt[ not sth for ppl to use. It's dfnt[ a backend. But yes, thr cld potl[ be ways to do tt. 

And if I'm gg tbh, I wld much rather see qmap reach 100% cvrg rather than have to make sth ezr to read. IDK when we c reach the 100% cvrg, but mb by 1.20? Oh, tt sounds weird to say.

nncheat: Hehehe. And yeah, one more th to add onto pghs. Bcz one of the concerns tt ppl had was abt readability of hashed names. I personally thk it's a non=issue, but I'm not gg to tell ppl it's not. Mb it turns out tb, mb it's just for them annoying. But ppl complained tt they thk tt letters make it less readable, and they'd rather have more numbers lk in pgim. 

J wanna say tt obv[ you can apply another layer on top and then v ezy you might want to rehash the hashed names agn and use numbers istd of the og[ names. So if aone has any concerns abt the ability of pghs then, I'm crtn thr's ways to work ard it, if it rly ends up being a prbm.

nnoro: Yes, and I wld lk to say tt it's dfnt[ not sth ez to say to other ppl. It's lk saying, "Oh yes, c_asdfghj," which is not as ez to say as lk class three=ten. But I wld lk to say on the other hand tt I was able to= Bcz I've worked w hashed names a lot, I was able to pick up some of them and it was pretty ez to ustd what was gg on anw.

nncheat: Yk, thr's some fun names in pghs as well. Yk, if you use random letters and put them bhd each other thr's some rly fun names to memorise. I'm not gonna use them here bcz they're not all PG, so= Thr's some fun tb had thr as well.

nngdu: Tt's v you, nncheat, tt's v you. OK.

nncheat: I thk we could prob ans nngli's qn w/o an admin here, even tho it wld be btr w an admin.

nngdu: Yeah, it wld be btr if they were here, but they're q bz atm. You wld be more fmlr than I wld w the entry method, if you wanna handle tt one.

nncheat: Yeah, I'll tk the first one. Then other ppl c join in if they want to, so then what's the first qn tt was asked today?
nngli: "I want to contribute to <PROJECT>. Where do I get started? Also, how do I join triage teams for QSL and Mappings?"
So, first off, ty for want- to ctrb to some proj, nngli. I'm sure you'll be ard much. Uh, if you wanna ctrb to a proj, the best way to get involved is to go into Discord, find the corresponding chat, go into that chat and say, "Hey, I wanna help here." It'll tk, less than, IDK how long, not very long, for ppl who'll be v happy to hv you thr, v happy to hv help- hands. And you can't psbl[ ans for all projs tgt. So go into the respective chnl, ask thr. It's v nice and chill if you go into a specialised chnl, you actl[ hv ppl thr who are v specialised in tt topic and actl[ know what they're talk- abt. So, works great.

Whr do you get started? Agn, ask thr, but if you wanna hv a gnrl overview w/o lk asking too deep of qns, you cld always to go to Github: https://github.com/QuiltMC. Look at the projs, wtvr itrss you. Mb look at the PRs page, look at the Issues page. Um, we're try- agn, we're try- actl[ to open more issues so tt ppl can ctrb more ezy. Github or Discord are the top two ways. And for the Triage Teams, I thk I'll leave this one for someone else. Sone from qmap, qsl. Tho I guess tknl tt is me as well.

nnoro: I c spk for Mapg. Rn aone tt's itrs_ in being on the Mapg Triage Team, I'm wlcm- bcz I wanna grow tt team up so we hv more ppl. The more eyes, the btr imo. So if you wanna look at mapg and triage them, tt wld be greatly apc8_. I thk it's prob the same for qsl. If aone wants to talk abt tt, you can.

*Silence*

nngdu: OK too.

nncheat: In gnrl, the same ~~speak~~ applies: Go into the chnl Discord, say, "I wanna join the Triage Team," and you're most prob j gonna get it.

nngdu: Alrt. Ig I'll tk this one. So **asie** tslv asks, "Have you looked into clearer communication outside of the Quilt community regarding the project's goals? I find that there's poor awareness of Quilt's technological goals, particularly its improvements and proposals. Just now, someone told me they thought Quilt is still in the \"many RFCs, little code\" stage. I think it would be good for the project to communicate what benefits it brings to the player, modder and/or modpack creator over (or just like) prior solutions."
So this is a rly itrs- qn. It's rly dfcl for me to ans w/o an admin here, since they hv a lil bit more familiarty with the subject in gnrl. But thr are a few ths we're doing. Obv[ these public mtgs are one of the most recent attempts for us to get more ppl invovled in what's gg on in the dev] side of ths. 

It's kinda tricky to get too spfc in other comys. Thr are a lot of other spaces tt do tangentially talk abt Quilt and whr Quilt is gg and what they thk abt Quilt. It turns out, this is a lot of spaces. 

(nnsouth: "Gdude your microphone is doing real bad pops")

nngdu: My microphone shld be fine, nnsouth, pls, pls. What, is it too loud?

(!alpha: "yea its peaking a lot"
LudoCrypt: "its popping"
nngli: "it's popping a lot"
nnearth: "it's not awful")

nncheat: Kinda. J kp gg for now, it's not tt bad.

nngdu: Uh, mb my Internet's dying. Does that help a bit, does tt sound a bit btr? Alrt, thr we go. OK, sorry abt tt. Yes, I was say- tt thr's a lot of spaces tt do talk abt Quilt and whr Quilt is gg. It's a lil bit dfcl to insert yslf into those dscs]s. I thk it is impt. I've actl[ been doing it smwt. Actl[ I've seen teh same ths you've seen, whr ppl thk we're still early=planning stage which, yeah, you're right is not true. Tt's not whr we are. But it's q hard to get the word out in tt sense. Ig we shld prob use stuff lk Twitter more, gv ppl ez ways to share the info tt we hv. X4tun[[ agn, I hv RSI now, so it's kinda hard for me to handle managing all those ths atm. I wld mb wanna delegate some of that? But we'll see.

But as for broader strokes, it's kinda hard for me to come up w spfcs w/o the Admin Team ard, which is x4tun[. Yeah, I'm not sure how else to addr tt. You're typing for a while, so I'm asum- you hv comments on what I j said.

nncheat: Right, who else is talk- abt popcorn?

nngdu: asie says, for context=
(**asie**: "Honestly I thought you are in the "little code" stage still until today!
The public meetings are a good idea *in-community*. It would be good to mirror them to social media platforms to allow people to distribute them outside the QuiltComm bubble. Personally, what I'd recommend is maybe reworking the front page of Quilt to be less "description" and more "pitch"?")
(nnsouth: "I've had an idea of throwing it into a podcast feed")
Yeah, I agree w tt. And as nnsouth said in chat, we had the idea of throw- it into a podcast feed. I was look- into tt b4 I smhw hurt mslf. Yeah, agn, I agree w you, it's sth tt we shld do. We shld make these things more accessible and ezr to listen to. Not j for a case of gett- ths out on the platforms, but mb re=formatting them aft the fact tb more listen=able. Bcz yk, thr's a lot of thk- betw qns when we're doing it live.

As for the website, nbdy's touched it for a while, and I'm kinda sad to admit tt. But I've been bz, I got RSI, **Fork**'s been bz, and **Fork** is the main person tt's been doing the website. We hv big disagreements on how websites shld be designed, but he knows way more abt front=end than I do, so I j kinda let him at it.

(**burger**: "the stats stuff is cool")

nngdu: Heh, **burger**'s talk- abt the stat stuff. Yeah, it is cool. Yk, tt all it is for most of you.

nncheat: Yeah, we shld also try tb a lil bit careful with this, I thk. Bcz yes, while some hype wld be gd to get us gg, evtl[ we are most worried abt being over=hyped recently, esp w the 1.18 rls coming out. We're a lil worried tt ppl xpk us tb fully rdy for 1.18 and we're not, and then it's gonna be *much* worse.

nngdu: Yeah, fully agree.

nncheat: While I do agree tt it wld be gd to have some more ppl being aware of it, we don't want ppl tb sitt- thr for lk 2 years constantly chk- lk, "When is Quilt rdy, when is Quilt rdy?" And then j 4get abt us. Yeah, so tt's anor th. "We hv too lil exposure," was nvr sth tt was on my mind. I was more worried abt, yk ppl want us tb rdy now. What c we do to not over=promise ath?

(**asie**: "Forge (and many other non-modding projects?) do summaries of meetings as another option.\n\nEither way, good luck with this project, everyone. I'm glad you're taking a concept I contributed to and taking it into new directions - that's how we can get not just iteration, but innovation. I support Quilt's continued existence \uD83D\uDE1B")

nncheat: Yeah, yeah, what you're say- is totally true. More ppl shld be at least aware tt we are prog- and not j= "Oh, I rmb hear- abt Quilt, but Idth it went awhr." Yep, no, totally, totally agree.

nngdu: Yeah, I agree w you but I 4got to say tt. We've alw been pretty conscious of over=doing the hype. And yk, some ppl were hoping we'd have a full rls by 1.18, or rls the Beta. We're not at tt pt. We'd hope to be, but yk ths aren't alw gg to work out the way you thk they'd work out, and this kinda work is alw the kinda th tt's gonna tk a while to do. 

But yes, I agree, we shld spread oslv out a bit more. I thk we c do tt w/o over=doing the hype. I thk a lot of it is gonna be abt, well not mood necs[, but j ~~tithing~~ how we promote ths. But idth we nd to go super hard on tt still. J utilising what he hv more and then feeds up wld be a great th, I thk.

nncheat: Yeah, Imn, evtl[ we cld j pbsh the devlogs to Twitter or sth, idk. That wld be a fun idea. I thk nnalex c do tt one. You alr kinda ans_ it.

nnalex: Yes, OK, so **Lith/Helium** asks, "Are there still plans on auto dependencies downloading?"
And the ans is, yes, this is what loader plugins will allow us to do, in a sorta gnrl fashion, ig. So yes, tt's dfnt[= we dfnt[ still wanna hv auto dep=dl-. We're j not q thr yet.

nncheat: I thk I'll j take nnkb's, bcz it v team=agnostic agn, so it's not lk a single person cld ans it anw. But I'll gv it my best. nnkb asked, "What teams need help the most?"
I'd say, top spot by far, pgbuto. ~~Bcz curr[~~ no one wants to do pgbuto. So if you're into pgbuto, if for some rsn you lk using Gradle, lk dev- Gradle plugins, pls, pls hit us up. 
I thk the other one is lk, QSL and Mapg cld alw use help. It's a v ezy parallelisable task, so thr's nvr a pt whr it's lk right, you can't work on this rn. So qsl and Mapg for sure. 
For CHASM I c j say, I'm j hoping for inputs. Thr's some issues whr I'm j hoping for more deeper dscs]s, I rly hope ppl c j gv inputs on those. O/w, tt's in a fairly gd spot rn. I'm sure thr will be more issues in the futr. Um, I'm not sure if= I thk qload's a lil hard rn bcz they're an emerging prcs. I'm sure I forgot sth. Nah, I thk tt's pretty much all of them.
So I'd say most help is needed on pgbuto, but you c alw help with qsl or Mapg bcz they nvr run out of work anw.

nnem: Right, ty. It doesn't look lk we hv any more qns. So it is abt time to end. So, if= Unless abdy else h ath else to say, or any other qns to ask, then do tt now or forever hold your peace. 

nncheat: Yeah, I thk we went thru abt all of the qns.

nnem: Well, in tt case, Ig we can conclude this. Well, ty eone for coming. And hope[[ we c see some of you the week after next.

nncheat: Looking fwd to it.

nnearth, nnoro, nnaurora: Bye.

nnem: Bye bye.



nnaurora: "Could CHASM be used to determine any patches at compile time and maybe generate a GraalVM native image with all the patches applied?"

yitzy: "what will quiltflower 1.8 bring?",

Kichura: "What adventages does a mod developer gain when using quilt instead of forge/fabric libraries?", 

"I'm glad to see Quilt is approaching release. I was worried there would be a loss momentum after a while. How old is Quilt in it's current form, then?", 
