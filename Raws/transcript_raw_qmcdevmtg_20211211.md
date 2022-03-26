nncheat: Alrt. I thk we c start, the t is now. Hello eone and wlcm to the last QDM of 2021. I'll say tt rn bcz the next mtg wld be [in] 2 weeks, that'll be the 25th of Dec. I srs[ doubt if aone is will- to come to a dev mtg on the 25th of Dev, so tt's gonna be skipped. For this wk I'm sorry tt nngdu isn't avbl rn. So I hv to fill in. I hope tt I c do the mtg justice. So, we're j gonna do the same th we do e week. We go thru each team, each team c do a lil talk, a lil upd8 abt what's hppn-. 

And we're gonna start right at the top, w our first team, ttbuto. Thr's actl[ nbdy here tt's ofcl[ part of ttbuto, but I j wanna talk a lil bit abt it bcz I've been work- on pgbuto a lil bit over the past week. X4tun[[, Gradle is still a pain as alw. Ik tt on the pgvg side thr hb some chgs, tt are prog fwd, b also x4tun[[ reverted some. The promising PR from nnearth [~~tt~~] might still hppn in the futr. I want to use this oppy agn: If aone is itrs_ in help- out with pgbuto bcz we rly nd sone who knows how to deal w Gradle. OK, tt's fr ttbuto.

Next team= Oh, we hv a new team. nni5, do you wanna intro the new team?

nni5: OK, so, we actl[ hv a new team now, and this is actl[ the ttcotl. So it's esnc[[ gonna be the team for the Cozy Discord bot and any of the other tools the ttcomy's gonna be using for enforcing the rules and ensuring the comy is kept in shape. I thk tt the two ppl on it rn are nngdu and nnapl. Yeah, 'Comy Tools', IDK why I said the wrong word. I thk tt's all I rly hv to say atm abt the new team. If nngdu or nnapl were here, they cld hv prvd_ more info, but well, they don't appr tb here atm.

nncheat: Yeah, j as a qk rsn-. It's j bcm apnt tt Cozy's get- q big, and it wld be gd to hv some ctbr] on our ofcl repo for tt. So if aone wants to help w Cozy, or any sort of any other comy tools we might nd, feel free to drop into the curr chnls tt exist alr. The Comy Toolings chnl, chk them out. Ask if you c help them in some way or itrs. We wld dfnt[ apc8 any help. Alrt, then, on a not so new team. nnax, any news on Loader?

nnalex: So thr's some news. Nth ptcr[ itrs_ tho. Thr's been some prog on the big Fabric upstream mrg, but nth= Well it's not done yet, rly. I've also been work- on impl- Loader plugins, still. B agn, it's still prog, it's not rly ath usable yet. Tt's abt it, rly.

nncheat: Imn, thr's gonna be ~~holidays~~ soon, so mb we c see more prog then? But rly, you're in a team in a ~~gnrl[ gd pos and rly cool numbers~~, so... Loader was doing a ton of prog rcnt[, it's j... It doesn't look tt way rn x4tun[[ rn bcz of [how] mrg conflicts are not push_ on Github, obv[. 

Alrt, nxt team: Decompilers. X4tun[[, our lead compiling goddess, nnsuper, is not here today. Hwvr, nnearth voluns tb the voice.

nnearth: 'Volun_', tt's an itrs- word to dcrb it.

nncheat: Been volun_.

nnearth: Anw, QuiltFlower 1.7 was rls_ in the last fortnight, so tt's thr for eone. It's avbl on a ~~linked QUO file,~~ and via IntelliJ as alw. So prog on 1.8 is steady, b don't xpk it anyt soon. Well lk, obv[ not this year. 1.7.1 rls| soon to fix some debugs. Tt's most of it. I suppose we c leave the rest to qn.

nncheat: Alrt, ty. Yeah, if you haven't noticed, x4tun[[ thr's a few mmbrs missing today, so it's gonna be a bit of a shorter mtg than you may be used to. B j lk nncheat also pt_ out, plz if you hv any qns, j ask. You c use the /ask cmd in the #meeting-chat. We'll get to the qns at the end of the mtg. 

Right, I thk tt's my turn: CHASM. Team CHASM. Well, last week, I haven't done tt much, but the week b4, CHASM Line was born. The Github repo got move_ ard a lil. CHASM went to its own submodule, CHASM Line got a new submodule. And it honestly felt rly fun to use. CHASM Processor is like, I won't call it cplt, b most of the impt rep] is work-. nnearth has last week been work- on get- local vrbls prpr[ rep_. It's not mrg_ yet, b I thk it'll be mrg_ soon, I hope.

nnearth: Not q finished.

nncheat: Not q finished. The checkstyle is not happy yet as well. B we'll hv local vrbl rep] soon, and then I thk we'll have cplt rep] of the class tree? And CHASM Line is work-, so technically at tt pt, CHASM is fully fn[, b thr's still a ton of stuff to be fleshed out w the prcs- of the I/O perf and mostly w the lang. B it's rly cool alr, thr's some tests on= thr's some testing repo for whr I know how CHASM will look and work. You c look at the CHASM langtests. Thr's a Brainfuck impl] tt's... you c j ignore tt, tt's for proving a pt. And some lil transformers tt are kinda cool.

Alrt. Let's see. In QSL.

nnaurora: QSL Time~ We hv mtpl ppl to talk abt it, so we'll start qk[. I thk we hv some PRs. The Keybind  IAPI 1, which intro_ a lot of stuff lk= It does some chgs to the Keybinding GUI, lk show- conflict- keys w a tooltip, exposing some APIs, and allow- to dyn[[ enable or dsbl some keybindings. Thr are more coming, but not in tt PR. So tt's dfnt[ a th to look out for. 

And for Resource Loader, thr will be some work in the coming weeks, lk= What I want to do is caching. I want to mod resource packs to build a diry tree which will be used for caching, which will allow the resc conds to be impl_, bcz the issue w resc conds is it will slow down Resc Loader. So to combat this, caching will nd tb done, and tt's sth I want to impl. My goal is to see if it wld slow down Resc Loader too. To test, I will use the All of Fabric modpack and tt itrs|. I hope it will mk stuff faster. Aft tt, I also want to impl a symbolic link- which willalloww to re=dir a resc to anor. It might be a bit niche, but it will be useful for some stuff and for lk, APIs which mgr8 to a new vrsn. It will be useful for like FAPI=QSL addition, so it's sth to look out for to. And tt is sth tt will also nd a caching sys to work nicely. 

And ~~cond[ resc~~ will allow us to= So the goal is to hv a regy of predicates, and the goal is you c use those predicates to say, if these dirys or resc files exist or not dpd- on the conds you wld list in a special file. I thk tt's all for Resc Loader. I know tt **Leo** has some stuff to talk about regy dictionaries. They can't talk, so it'll be on the text chnl. B I c read it out once he's typed it out.

Regy Dictionaries API = orig[[ known as Regy and Tree Atrbs API = is pretty much fetr=cplt, besides ntwk-. Rcnt[, an impl_ fetr allows you to use tags as keys, meaning you c gv much more entries in the same value if all the entries are in a specific tag. ~~Cplt tags aren't cplt[ test_~~ b they are impl_ and thru ~~workifying~~, ustd how tags work. If you're ask- what's the Regy Dictionaries API, it's bsc[[ the same as tags xcpt we c also gv values to each entry. So the use case cb lk a biome dict which cld be used to also gv= Well, it cb used to det which biomes the mod will spawn along w weights. To call the ~~interred~~ lk tt. The goal is tb able to view tt in code and via datapacks. I thk w 32. Unless nni5 h sth to say, then tt's all.

nni5: I blv we'll be fine, yep. If thr's other qns, we c ans them closer to the end of the mtg.

nncheat: Imn, tt was a lot of news, so ty for tt. Yep, prfk. Well, thx for the update. Tt was v xtd[ and rly informative, tyvm. 

So, we hv two teams left. I'll qk[ talk abt the ttmap. First off, my ~~child Hashed~~ has now stabilised, so pghs is now found in the rls Maven repo. This does mean for the t being tt we switch back to manually trigger- the xn for upd8- pghs. It's still no big deal. ttmap is most of the time manual anw. So they j run the actl first. Rsn for this is tt we don't rly lk the big delay tt we get from Github Xns when run- is atm8_. So we're look- to trigger them ~~per files~~ in the futr by some bot tt pulls the vrsn manifest. 

On Qmap islf, thr's obv[ been prog. Since I'm not rly doing much for Qmap mslf, I'm not gonna talk in dtl abt it. B you c chk out the #devlog=mappings in the tlcn srvr, or j the #devlog on the comy srvr. And you c see e t thr's new mapg add_, they put it into the devlog for the next rls of pgsnaps. So obv[ the big one was 1.18, which had a lot of dffr]s from 1.17 o/c. And then the rcnt 1.18.1 prereleases didn't have too many mapp- chgs. But nth too much hppn- thr. But Qmap isn't the pt tt while it's not cplt, not 100% done, it's normal op] now. Thr's no big tooling chgs tt nd tb done rn imd8[ tt lk, blk PRs or ath. So great t to ctrb and get your stuff in. Ath tt you thk is impt to be in b4 Quilt rls, now is the t to do it.

Last team, thr's nth to say rly. ttinfra is not present, b also hasn't done ath bcz thr wasn't rly ath to do. ttinfra is o/c mostly a supt- team. Managing our Maven, and I'm guess- the website, I'm not ptcr[ caught up. B obv[ they only rly do stuff if thr's some chgs reqr_, and rcnt[ thr's been nth, so thr hasn't been ath hppn- on tt team. Altho I want to say it wld be great agn, if aone has exp on AWS, or rly wants to get some exp, we wld be v happy to xpnd the ttinfra.

OK, tt was all the teams for the mtg updates section, and now we c mv over to the qns sxn. I've alr claimed a qn, so go ahd and ans tt one.

nnearth: Hello, so how do I even do tt? Do I press 'Stage'?

nncheat: Yes, press 'Stage' and then you talk abt it.

nnearth: So, the qn is, "Cld CHASM be used to det any patches at compile t and mb gnr8 a GraalVM native image w all of the patches applied?"
So yeah, so one of the advgs of CHASM is tt it cb applied at compile t and not j run t bcz of its pure nature. So the output is cplt[ det_ by obv[ the Minecraft jar, the mod jar, then the transformers and any other settings. Psbl[ some other ths we dsin in the futr. So yeah, it'll be able to run at compile t. It c then be decompiled in Gradle and you'll be able to see the tfrm]s in the src lk you c w Forge patches alr. And I don't see a rsn why sone wouldn't be able to mk a GraalVM native image. Altho, I'm not ptcr[ sure why you'd want tt bcz it'll all be cache anw. But Imn, if you want to, go ahd.

nncheat: It's a big motto of CHASM. "Yeah, you c do it, b mb you shouldn't."

nnearth: Er haha, I wouldn't mb encg tt bcz it's not q the same as coremodding. Well, it is still coremod-, b it's not in the trad[ sense bcz it is collision handling. It's not rly psbl to= Well, at least it's dfcl to use it in a way tt's not collision handling, and you can't blame mods and stuff.

nncheat: Alrt, thx for tt. Next up, our most super of coders has appr_.

nnsuper: Hello. Yes, so for the QuiltFlower 1.0 th, I thk at this pt we've kinda reach_ the pt whr we've impl_ all the modern Java fetrs, so we're j gonna fix bugs, impv lk local vrbls, generics. And my evtl goal is to bsc[ mk it recompile, and aft tt, mk it recompile into a prfk match of the binary. Which is a lofty goal. B I thk w some effort, we cld prob get thr in a bit.

nncheat: Alrt, cool. Mb for cplt], bcz we forgot tt b4, mb read out the qns if it's not= I mean, this wasn't rly a qn, so it's fine. B the next 2 qns, we cld read them out as well. So, let's tk this one by Kitchura, I thk. "What advgs does a modder gain when using Quilt istd of Forge/Fabric lib?"
Now we asum this is talk- spfc[ abt QSL. And nnaurora is gonna talk abt this.

nnaurora: So, at least for qsl, the biggest arg]s for qsl over Forge and Fabric libs is we hv a big focus on the data part of MC. Bcz thr's more and more ths tt get data=driven. So having gd APIs tk- advg of tt part is v impt. And the other th is, not eth shld be only JSON only bcz it's often a big pain to deal w. We hv a lot of cntt. So thr's also a focus on making it avbl ~~incontenally~~. Thr's also advg, at least cmpr_ to Forge, we want to be able to listen to regy and then act upon what's in the reg. 

So you c, foreg, reg a new wood type ~~tt cld gnr8~~ in other mods tt add wooden cntt wld be able to gnr8 new stuff using the new wood type. Tt's why data is rly impt, bcz if you hv a gd data lib, we c mk this much easier. Bcz I've done it w Fabric but it's not ez. Not sure if it's sth we can ask the API for. But by doing this proj, it allowed me to thk of new fetrs tt shld be in the libs to allow this .(data=driven aspect). much easier. Thr are also some advgs for resc loaders, since I'm not rly ctrb- to the Fabric one now. Thr will be new fetrs tt will be kinda impt. 

The other advg is, is we want to kinda xpnd. Not j lim oslv to ~~upstream notechunking~~. As much as ~~when we call~~. Foreg for the Keybinding API, my thoughts, bcz we are rmv_ tt  lim tt FAPI has, we c chg some lil stuff to mk the exp btr for the user too. Not j the mod devr. Tt will be advg for both mod devrs and users. Talk- abt this, it's not an excuse to modify vanilla bhvr, so tt's no chg. ATM I can't thk of other stuff, b thr might be other stuff, b curr[ I can't thk of any. So I thk tt's it.

nncheat: Prfk, tyvm. Next qn is by Byte. "I'm glad to see Quilt is approach- rls. I was worried thr wld be a loss of momentum aft a while. How old is Quilt in its curr form?"
I thk our admins are prfk[ cpbl of ans- tt. nni5?

nni5: OK, so give me a second to get my throat. OK, so Quilt in its curr form was actl[ start_ in early Feb this year. We did hv to go public I thk in Mar, bcz we did run out of inrl Github Xn mins. And well, I wld dfnt[ say it was worth gg public when we did, bcz we were able to utlz the comy more twd prog- Quilt at a faster rate.

nncheat: Anor qk and ez qn tt we're gonna mv ahd I thk. Manzobotik asks, "Does CHASM cplt[ replace the ASMR prototype?"
And nnearth, what's the ans?

nnearth: Yes.

nncheat: TY.

nnearth: Haha, I c gv a bit more dtl. The ASMR prototype was meant for us to be able to lk, figure out what the prbms we're gonna hit are. It was not dsin_ tb long-term mntn able or ath. CHASM does steal the bits of the ASMR prototype that works, and tt ~~reworks~~, and some of the bits tt didn't. So, tt's what the prototype is for. And yes, it's deprecated.

nncheat: A simple qn w a short ans. Next up, I thk nnsuper can tk this one by Byte agn.

nnsuper: Yes, Byte asks, "Hv you thought of mrg- QuiltFlower chgs to FernFlower?"
I'm not sure if Jetbrains even mntns it anym tho tbh. I thk evtl[, once we reach a stage whr we c call our work lk more or less done, we m start mrg- our chgs w FernFlower. B in the mntm, we've been ctrb- back to ForgeFlower to help out our mod- frens w stuff lk optimisation, new fetrs and stuff lk tt.

nncheat: Yeah, I thk thr's been rcnt[ also upstream chgs to FernFlower, weren't thr? Or did I mis=ustd tt?

nnsuper: Yeah, I thk one of ForgeFlower's PRs got acpt_. B it was kinda a minor one.

nncheat: Ah, OK. Alrt, anor qn by Byte. "Is app- tfrm] at compile t sth tt only is in dev], or c you also ship your mods as patches?"
nnearth?

nnearth: Hold on, let me j find it. Yes, so most of the time for compile t, Imn, if you want to, you cld ship your mods as patches. B given the only way to app the patches will be thru = I was abt to say ASMR = CHASM anw, thr's not rly much pt. Agn, bcz CHASM catches the output of the tfrm]. It's not even lk it gives any bnft. So, you can, but you don't hv to.

nncheat: Yeah, agn, the motto of CHASM. "You c, but you prob shouldn't."

nnearth: I= But= Why?! Lk what it wld look lk, is prob it's j some= it wld tk a transformer and convert it to anor transformer. And it wld be less compat[ w other ppl's transformers. So plz, don't do tt plz. You wld lose intelligent conflict handling. So a tfrmr c spfy, "Oh, I want this block of code not to chg for my tfrmr not to work." And tt info is lost with patches. You gotta thk tt patches are not cplt dcrb] of tfrm]. They don't fully dcrb the intent. If you're add- a line of code, is the intent to add it aft the prev line, or add it before the next line? So you gotta bear tt in mind.

nncheat: So we hv one more qn by Byte. "So Mojang has made more and more stuff data=driven, so you're focusing on APIs for those ths in qsl, and esp creating resc is problematical bcz JSON files are such a pain sumt. Right?"

nnaurora: Yes! Yes, so we're focusing on those APIs, and creating rescs programmatically is impt. Thr will be data gnr8] APIs. Thr will be runtime resc packing dictionary APIs, and for tt one is sth tt I've been plan- for a mth, and I still haven't got ard to making one. And thr is also tt controversial Recipe API tt is still in my mind. B tt one nds a lot of fmwk tb ez to use and compat and doesn't rmv fetrs from other mods. The th is, giant JSON files are great for datapack makers. But for dev] it's kinda a pain when you're not right. So not duplicating a lot of data is impt too.

nncheat: 'Kay, tyvm. So thr's been some last min qns tt we c still ans, and I thk aft those qns, we'll call the mtg a day. Let's do the second one, I thk tt one's easier, by Fish. "Can we still go from Quilt to Fabric fairly ezy?"
I'll start w this one. If aone wants to add sth, let me know. First off, I know tt the fapi compat] w qsl is still impt and still hppn-. So tt shld be fine, mb qsl c ltr spfy on tt. I wanna qk[ say tt mixins shld be mostly supt_, hwvr thr are some qns we'll hv to figr out. Foreg, local vrbl bytecode indices is sth tt's not v stable, and not v gd to use anw. So we might hv to deprecate those. Thr might be a compat] layer thr tt's either slow or in=cplt. We'll see abt tt b=

nnearth: Yeah, it's bad practice to use them anw. I thk the bigger one is the integer priorities in mixins. We want to dpk8 them. They cz issues, in short.

nncheat: Integer priorities are anor th we cld potl[ kinda impl as a patch to allow Fabric mixins or Sponge mixins to work. But it's dfnt[ sth we don't want in Quilt CHASM mixer. And thr was one more= Oh yeah, and mixin plugins are still a no=go. Thr shld be oher ways to do those. You shld not need mixin plugins anym. And we c mb supt a subset of those, b prob not rly. We'll see abt tt.

nnaurora: And for tt qn, I also hv to add, for qsl, thr's the fapi=qsl th, and you c use tt to run stuff tt nds qsl on fabric for now. If not, ~~they for are~~ avbl on Fabric but it is kinda avbl. So switch-, so tt's sth tt cb used.

nncheat: Hey! My ultrasound j went off bcz tt's my th. Trunek asks, "What's a replacement for mixin plugins if we nd cond[ mixins?"
Well, the replacement will be cond[ mixins. Lk actl cond[ mixins rather than a mixin plugin. So, idk xk[ how it looks, but iot to mb help w bits of mixin compat], probl j an ant8] you mk for the mixin, prob j anor field tt j says, "Execute if anor th's prst." In CHASM thr is ways to do cond[ tfrm]s. So we j nd to jmpl some .(cond[ tfrm]s). with mixin=csis[ 4mt. So I thk you j add in an ant8] tt is ignored by Sponge mixins. So your mixin plugin works thr. And on Quilt, you j literally say, "If mod is loaded." Which is, I thk, by far the most cmmn use case for cond[ mixins.

I thk I c also ans this one bcz it's fair[ ez. "Is thr plans to hv compat] w Forge?"
No, not ofcl[. It's j not fsbl to hv an ofcl supt for tt. Hwvr, Patchwork, as far as I'm aware, is sitll plan- to hppn on Quilt in the futr.

nni5: J to clarify abt Patchwork, even tho nngli isn't here, I blv he is gonna be cont- work on Patchwork when Quilt is rls_. So, this isn't rly an imd8 prio for nngli to try for Forge compat] atm.

nncheat: Yes, Forge compat] is kinda hard bcz it's j v dffr[ dsin_ cmpr_ to Quilt and Fabric.

Jules asks, "Will creating resc prgm[ in qsl at runtime thk tt ~~I'm mod common MSM~~, thk tt I pref creating edge resc data, then deserialising it? Versus chk- it into the recipe and asset mngrs dir[?"

nnaurora: Tt dpds on the resc. For texture gnr8], you will hv to create sth tt will deserialise it. We'll nd to store bytes within a virtual resc pack. Bcz doing it anor way wld be way too dfcl. But stuff lk recipes, foreg lk a Recipe API is tb able to modify recipes and add recipes. The goal is not hv to use actl resc data and j injk rpt[ into the mngr, bcz it's faster. It's way faster to do tt than spend- t we cld o/w on deserialising it, storing duplicate data in an virtual resc pack. Gnr8- stuff gnrl[ shld be pref_. If it's not psbl, it won't be done. But if it's psbl, it will be pref_. And tt's it

nncheat: Cool. Anor real qk one. Fish asks, "Plan- fetrs for hte futr of Quilt?"
I'll j say, we'll mv this qn to the next mtg. Curr[ we're hv- some dscs]s abt tt, b yk, next t.

Alrt, I thk this is ans_ now? Due to it being ans_ in the chat, I'll j read it out for cplt]. TropheusJay asked, "Will these mtgs alw be at the same t, bcz if they do, I won't be able to mk it to any of them for mths and I'm sure I'm not the only one in this sitn."
And nngdu 's ans_ w, "It's the t tt worked best for team mmbrs when we first started doing mtgs. Since this is the last mtg of the year, we'll prob tk some t to regroup and figr out of if thr's a btr t mv- fwd."
O/c, tzon mk it a lil hard to orgz them, but yeah, we'll figr sth out I'm sure. Thr are some ppl who don't lk get- up this early, some countries tt don't want to stay up this late.

Alrt, we hv one more qn tt's fair[ a gnrl one. So I'll j read it out and talk a bit, and if aone h sth else to add... Fish asks, "What's the biggest dffr] betw Fabric and Quilt ito code? And would reqr the most re=strc= in a mod?"
Now I'll be talk- abt this from a CHASM perspective since tt's my th. O/c, CHASM doesn't exist in Fabric, so tt's a big dffr]. Mixins will exist in Quilt, it'll j look a lil bit dffr[. As we metn_ b4, thr will be some re=strc- req_ rgrd- mixins whr you shld not use integer priorities and you shld not use integer indices for local vrbls and tt sort of stuff. And you'll hv to mv your cond[ mixins to an actl cond[ mixin rather than doing the mixin plugins. Aone wants to add sth w rgrds?

nni5: Rgrd- the re=strc-, I imgn we will prob write some sorta guide closer to rls abt what chgs you'd prob wanna mk to your mod when port- over. B I imgn tt's sth for ltr.

nnaurora: I hv an actl eg of one part of porting. In Aurora's Decorations, I dcd_ to use Block Extensions API of QSL, so I hv a commit so you c see what parts hv chg_. But for fapi and qsl, for a while we will be able to use the qsl-fabric compat] sys. B it won't stay lk tt.

nncheat: Alrt. We've also closed the AmA so thx eone for participating. Thr's still v much prog in Quilt, and it's very exciting and I hope we c kp it up in the futr. Oh, I 4got the teams of Community. B I don't thk aone knew abdy from there. I'm sure they hv sth to add next t. Some exciting stuff aft the holidays. Yeah, ty eone for show- up in the mtg. I thk we c bsc[ mk it a trad now and we'll go into an after=party in the dev=chat. So if you wanna hang out and talk a bit, feel free to come. B rgrd- the ofcl mtg, tyvm and hv a v nice evening, or day, or morning, dpd- on whr you live.

nnearth: See ya.










































