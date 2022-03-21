20220212

Gdude: Did I acdt[ click the "Ping Eone" button agn? Yeah, I thk I did, haha. C sone on the Mumble side say sth to mk sure it's work-?

A: Hello

B: Sth.

C: Hello

Gdude: Xcl[, ty. Mtg blows up, imd8[ deflates. Yeah, you see, tt's what hppns when I acdt[ ping eone. Sone's gonna cpln, I bet. Yes, so for those of you tt aren't fmlr or haven't been here for the last mtg, the bot we were using to rcrd the mtgs was thrtn- to be dead. It turns out tt it's not= tt I'm not pay- for it ATM, so we're using Mumble so tt we c rcrd istd. Um, it does a lot of the stuff tt we nd for Southpaw to mk the podcast, so, tt's why we're use- it. 

So eone is thr on the Mumble server, on the other side of tt Mumble bot. Tt's bsc[ the gist of it. Make space-laser noises bcz ppl are set- Avatar, not Avatar, what's the word, bios, prfl bios. You c turn tt off. Anw, I'll gv it a couple more min and then we c get start_. Same format as alw, of course. I'm gonna try and rmnd ppl to say who they are the first t they talk, so tt eone knows for the sake of the podcast. Hope you ppl don't mind, but tt's alrt I'm sure. And we'll try to rd out the qn as well.

Spk- of qn, if you have any, use the /ask cmd, and we'll get to them at the end of the mtg. Prob, hope[[. Don't worry, I've got a list. For those of you on Mumble BTW, I thk I'm gg to stay on Discord for audio. It's j much harder to mess up my audio setup tt way. Is tt OK? C you rcrd tt OK, Southpaw? I asum you c. Nbdy else will be talk- on this side. 

Southpaw: Alrt, works for me.

Gdude: What gd is an alt if it's not on the srvr, right? Alrt, in abt a min, we'll start.

Southpaw: You mk it sound lk some kind of perfume. Perm, by Gdude.

Gdude: Alrt, ig we c start. Y'all rdy? Alrt, let's get started. First on my list = I tend to go in alphabetical order, you m hv noticed = Build Tools. Glitch, wld you lk to hv a word?

Glitch: OK, sure. As alw, thr hasn't been much in the ways of Build Tools. I ended up doing some work since last t I talked, on VanillaGradle, being able to remap the cmpl_ mod to Hashed or Intermediary or sth lk tt. But tt ended up gg on the wayside bcz I rlz_ I c mk Loader mostly work with Floom. So I ended up spending my t work- on Loader istd, bcz once Loader's work-, we tknl[ don't nd to use a cstm Build Tool. We j hv to gv up some ths, lk we can't use Hashed, and tt's pretty much it, rly.

!!! New shortforms: Intermediary, VanillaGradle, Hashed, team names, has been, alphabet, - tense

Gdude: Alrt. I mean, hey, prog is prog, and it sounds lk some has been hppn-, which is xcl[. Uh, next on the list is Comy Tools, me. Sprz sprz. Cozy-wise, not much. We've been look- into a new th we're test-, which Discord is, has= well, we're testbed for yet anor thing, ig. We're test- slash cmd perm which is a new th on the comy srvr. Thr's not much to do with Cozy rn, bcz it's not on both srvr, so I can't lk change ath to use it. But we've set it up, and you'll see lk, some of the slash cmd are greyed out, and evtl[ they'll be hidden, we hope. O/w, Comy Tooling hasn't been doing a ton. 

I hv been redoing the website. It's gg quite well, I thk, anw. I'll gv you a link. I've put up this lk, sort of test- site so tt you c see how it's gg. Yeah, I'm having fun. But thr's still a lot to do. I'm work- on the Abt pages rn, and I haven't pushed them to the side bcz we nd eone to agree on them. But yeah, when they're done, they'll be up. There'll be a nice tmln and all sorts of ths, lk ~~Fat~~. Still gonna be a while, if aone has any fdbk tt's the link. Let me know how bad it is. O/w, tt's abt it ATM. I'm actl[ rest- today, so don't yell too loudly, hehe.

Alrt, next on my list, is Loader. Alex?

Alex: Yes, as Glitch mentioned, he's been upd8- from Fabric upstream. Tt work isn't q done yet. I'm work- on it a lil bit as well. We're q close to being able to be upd8_, which is gd. I thk tt's abt it for Loader.

Gdude: Alrt, gd stuff. Thx Alex. Oro, would you lk to talk abt Mappings?

OroArmor: Yeah, j gv me one sec. Alrt, yeah, so Mappings obv[ we had 21w05a and 22w06a. Thr weren't a lot of changes for 05a, but 06a obv[ w all the tag changes tt intro_ a lot of stuff tt cld be lost. Luckily for us, w LambAurora's amzg mapping matcher we were able to save, abt, lk j over a third, mb 40% of the mappings tt we cld lose, so tt was v gd. So we hv those still. We got lots of PRs tt were merged in, even more from 22w06a, so tt QSL work cld start. It's dfnt[ a rly nice uptick in the work. 

And then, anor th is CheaterCodes and I are curr[ in the v early stages of changing how mappings and the Quilt env work. One th is multi-version mappings so tt the same mappings can trgt multiple vrsn, so tt when changing betw vrsn you don't hv to lose mappings or old vrsn still get updated. And anor th on top of tt is we're also csdr- tt mv- away fr Tiny as the frmt for mappings on the Quilt eco j bcz it's an extra step and all the data tt Enigma has, Tiny also has, esnc[[. So yeah, those are the gist of what Mappings has been gg thru.

Gdude: Thx for tt Oro, sounds lk a lot of prog either way. And gd work on tt LambdAurora. Speaking of tt LambdAurora, wld you lk to talk abt QSL?

LambdAurora: Yes yes yes, so in the last weeks, we had ~~12~~ snapshots. So I don't rmb exactly when the last mtg was.

Last mtg was the 29th, I thk.

Since then, we merged the Tooltip API, which intro_ some new cool bugs lk the item tooltip one, and some rel_ to tooltip cmpnnt, w convertible tooltip data in the files for tooltip data. So a lot of new util, some nice stuff. And either one of the dfrc with FAPI and tt API is, we c use some of the new features ``feat and irfc. For a long t, it wasn't psbl to injk into irfc. So now it's psbl so it's much cleaner. 

And the other module tt has been merged is Ntwk- API. What's wrong tt has been due to w 22w06a, which was q painful, bcz Mojang mv_ a lot of stuff and kinda wrecked tags. But it's for the btr. Now we can actl[ hv tags for any ~~linking trees. What I found awful thr, in the API~~, so tt's nice. But it cz_ some issues w QSL porting. Bsc[[ we had to dsbl the Tags API for now until it gets prpr[ rewritten. 

And thr was a lil db8 we had a mth ago, tt had to be brought up into the table agn, which was more than two pt in QSL. The main issue was, we thk game entrypoints loader doesn't mk a lot of sense, bcz it doesn't mk it rly game-agnostic, or vrsn -agnostic as it nd a q lengthy injection mthd, which uses raw ASM. So tt's terb for mntn] and it means tt for new vrsn tt change the entrypoint lgc, it rqr a loader upd8. The th is, game entrypoints loader are kinda useless in some way, it's bcz normally when you use an entrypoint, it's bcz you have an API to call stuff to look into. If you don't hv an API, you are most lkly to use entr[ mixins. 

So we did a lil vote and turns out a lot of ppl thk tt it's fine to mv them to QSL, so we did tt. And j to be clear, the pre-launching point still in the loader, which still can be used for loading if you have a big mod. And the module the entrypoints has been moved to is the most small module of QSL. Bsc[ it doesn't hv any deps. It only cntn the event fmwk. Lil util for multiple test- srvr and well now, the game entrypoints. So it's gnrl[ ez to jar-in-jar it if needed. Tt's all for now. Thr are still a lot of new PRs to go thru. Yeah, I thk tt's it.

!!! JiJ, has, mappings, NAMES, MC, may, governance, of course

Gdude: Thx for tt. Tt's crtn[ q a lot to be get- on w in one fortnight, isn't it? Xcl[, gd work. Now b4 we mv on, do any of the proj hv any o/s PRs or ath tt nd look- at by the rest of the comy?

Glitch: QSL c alw use looks on eth. Plz feel free to look thru. Even chk- grammar on Javadocs is help[. You don't hv to ustd what's gg on to rvw a PR. And e bit helps.

Oro: I'll also say tt if you want to look at Mappings, PR #5 on Qmap c alw use rvw. Yes, it's 2000 lines long. Yes, it touches e single part of what Qmap does. Yes, it's scope has creeped. But those rendering mappings nd updating, and I kinda j fixed a bunch of ths as well as I came across them. So if you find any issues in tt, I will dfnt[ be glad bcz thr's a lot to look at, and we haven't impl_ a spellchecker yet. But tt's sth tt will come evtl[.

14:15

Gdude: Alrt, tt's gd. Now, we shld prob talk abt what hppn_ inrl[ rcnt[, right? It was prps_. 

It fits you.

Oro: Shld I start talk- abt it? Or, IDK.

Gdude: You can talk abt it, IDM. Bsc[, this is an orgn[ change. Eone here knows i5, obv[. He isn't here at the mtg today, he's actl[ q bz. He is stepping down fr the adminr pos at Quilt, bcz he's mv- on fr MC modding in gnrl. But he's still gg tb ard j to ans qn, but he's not gg tb actv here. Now, as you m know, if you've read our RFCs, we nd at least 3 admins, and we nd an odd num of admins. This means, of course, tt we hv to hold an election. If you've seen the rcnt changes to the governance RFC by CheaterCodes = I thk the PR is still open, it hasn't been merged yet = we dcd_ to folw it and go w ranked choice voting. Now, turns out we only had two candidates, so it was a bit of moot choice for us, but we dcd_ to use it anw and it worked out j fine. 

We hv a whole sys whr we use a website which gnr8 a unq voting link for eone, so eone gets their own link. And only once the th is closed c we get at the results. So thr's no, "Oh, this person's getting more votes, I'm gg to stack a vote on top." YK. So nbdy c see who's voted for what and nbdy c see what the votes are look- lk until the poll closes, incl the person tt started it.

Anw, long story short=

Oro: Who gets to vote?

Gdude: Eone who's part of the Comy Team, or the Dev] Teams gets to vote. So any Quilt Devr Team, anyone in the Comy Team, moderators, events ppl and of course the adminrs. I'll drag it up in a few mins or sbdy else c, if they wanna check, it's pinned to the thread. Anw, so we had two candidates and the candidate who ended up winning the vote by a margin of lk 3 votes was Oro. So congrats Oro. This is no srpz to you at all, but hey.

Oro: TY TY TY.

Gdude: Indeed. So, we'll be setting Oro up soon-ish. We need i5 to tfr a few ths over. But yeah, tt shld be nice and smooth. We don't hv an ETA but it shld be fairly smooth, hope[[. And yeah, we're look- fwd to work- with Oro, TBH. Great choice, great choice. If aone wants the results link, you c hv it. But it's two candidates, Oro won by 3 votes.

Alrt, so if aone has any qns they want ans_, use the /ask cmd. We got a couple in alr, so we'll start gg thru those in a sec. It's /ask. You can ask bsc[[ ath you want, altho try and kp it smwt rlvt. OK, let's have a look here. Cheater, do you want to take tt one? Don't 4get to read it out.

Cheater: Yes, I will tk it in 2 mins. 

Gdude: Ok, tt's alrt. Let's look at the other one here. Uh, I will throw this one out. Silas is bsc[[ ask- abt the psbl] of security disclosure sys. Uh, yeah, we're gonna hv sth. We haven't rly talked abt it yet, hehe. I do blv tt Github has a sys for it. Yeah, Southpaw says, Github has a sys for it. It'll alm crtn[ j use tt. Honestly, we haven't talked abt it yet. If you have any sgst],  we'll tk them of course. But yeah, I imgn Github sys is prob the most lkly th we'll end up using for tt one. Yeah, they do, I haven't used it much, but they dfnt[ do hv one. Bcz I know= I hv some frens on the Python srvr tt hv used it. Thr's a button you c click which makes it CVE. Yeah, so thr's a whole th thr, I j haven't used it much. Are you rdy for tt qn, Cheater?

Cheater: Uh, let's do it now. Alrt, so, qn by Trollzer, "Why are we switching to a less supt_ file w less fetrs?"
Now, this is what we're talk- abt b4, tt we're csdr- dropping Tiny and j using Enigma mappings istd. So I wanna go over qk[ abt the rsn. Ig why I brought it up, rly. If you're aware of how the Qmap works, you'll know tt the Qmap repo is in an Enigma frmt. So, Enigma supt splitting the mapping files up into a diry tree of files, so each class gets its own file, which is not supt_ by Tiny. This is much more !!! convenient for Github PRs. It's more ez[ vsbl who changes what file when you mk a PR. So it makes more sense to use Enigma.

And if you then cmpr Enigma and Tiny, you'll notice then tt they're bsc[[ !!! exactly the same. So, thr's 3 dffr]s rly. Dffr] #1 is tt Enigma uses cplt words like 'class', 'method' and 'arg', istd of single letters lk Tiny does. The second dffr] is tt Enigma handles nested classes as nested classes. So mappings for inner classes are mmbrs of the outer class mappings, whras Tiny has changes tt amt to flat mappings. And the third dffr] which is psbl[ the most rlvt one is tt Tiny supt mtpl namespaces.

So in gnrl, the frmts are q smlr. And what we've talked abt is adj- Qmap to allow for so-called mtpl MC vrsn in a single th, which wld mean we cld xtd Enigma to use specified vrsn ranges for mappings or !!! transitive mappings or sth. Anor th is tt we've csdr put- ~~Amplick~~ into the mappings frmt itself or the annotations, lk changing !! Obfuscated to over it only. Annotations also put tt into Qmap.

And if we did tt, we wld also hv to change Enigma mappings, bcz tt's what the repo uses, and we'd also hv to change the Tiny mappings. It also means we hv to cont mntn- the Tiny eco, which is Tiny Mappings Parser, Tiny Remap Pile, thr's lk 5 or 6 of them. Each of them has their own Tiny Mappings Parser, and readings and writing sys. They're all undocumented, not written by us, and we wld hv to mntn them for no rsn. So we csdr_ drop- this !!! in order to lessen the mntn] brdn.

What is the rsn, we asked, what is the rsn we even hv Tiny in the first place? But we couldn't rly get a conclusive ans. Thr were some who were lk, "It's better for compressibility." Which is not wrong. "It's better for parsing, it's easier." Which is not true bcz they are bsc[[ the same file frmt. So the only th is mtpl mappings, mtpl namespaces. But single files = thx Skyrising = the arg] was tt c hv a single file, but Enigma also has single file frmt. Thr's not much bnft to using Tiny, but we wld hv to mntn a lot more stuff. We don't feel lk mntn- sfwr which we hv no use for.

Oro: Cheater, thr's anor qn tt's fairly smlr. I thk I'll pop in here a lil bit too. Fr Sher15, I alw 4get what we call you, "If fully switching to Enigma mappings, wld new fetrs be added to the frmt or wld it be more of a fork in the futr?"

We've talked abt this a lil bit, Chris, yeah. Thr are a couple ths we do want to add to the frmt. Not too much, and it's sth tt cb done thru a ppty tag on sth istd of a more cplt xpnd- of the frmt. Thr's not too much we want to add, but thr's j a lil couple ths tt we dfnt[ cld add tt wld dfnt[ impv the frmt. But as it stands, I don't thk we were super into csdr- tt. I don't exactly rmb from our convo ytd, or two days ago.

Cheater: Tt was two days ago. I couldn't actl[ find upstream of Enigma !! anymore. I'm not sure if it still exists. The Bitbucket link is dead, and the website links to the same Bitbucket link which is dead. So upstream Enigma doesn't rly exist, so... We're now on anw.

And, of course, I don't thk we cld j kp calling it Enigma. We cld j mk it Enigma v2, we hv to see how tt works out. Thr's dfnt[ gg tb an RFC, and you c cmnt on tt once we hv tt. We j wanted to gv you a quick headsup on what we're talk- abt inrl[.

Gdude: Alrt, thx for ans- those. I'll tk this one. Jello is asking, "What is the ETA for the Cozy Discord modularisation issue? What modules are planning tb created?"
As alw, no ETA. Agn, it's rly j me work- on these. It's gg to tk a while. I'm plan- on factoring out pretty much eth tt isn't Quilt-specific though. So the filtering sys, the user cleanup sys is alr done, kinda. What else is in thr? The thread mng] sys. Bsc[[, eth tt Cozy does will be modularised delib[ to mk it psbl for other bots to use the modules. So yeah, if you lk sth tt Cozy does and you're not using a fork like Chris is, then this will be interesting for you. But it's gonna be a while, bcz I hv a lot to do. Aurora, you wanna tk tt one?

Aurora: So, "Will Quilt end up with a Biome API/Wanderer API to mk work- with 1.18+ vrsn biomes far easier?"
Curr[, it's rly hard to say when it will hppn. Bcz thr's a lot of modules to work on w QSL. The th is, in the curr eco, thr's not a lot of vrsn ppl, so unless thr's one tt sits down and starts writing sth, it might not hppn right now. It's rly hard to ans tt qn bcz we don't know when it will hppn.

Gdude: Thx for tt one Aurora. Thr's anor one thr from Trollzer, c aone tk tt?

Glitch: Trollzer asked, "Will Loader still supt the Tiny Mappings?"
I can't see a rsn why we'd rmv supt for the Tiny Mappings, so yeah, I can't see why we wld do tt, bsc[[.

Gdude: Thr's no rsn to not supt tt, so prob it will supt them. Yeah, tt makes sense.

Cheater: The big dffr], I want to add to this. We wld not be actv[ mntn- most of the Tiny toolchain, lk, it wld not get any actv new fetr, ath. It's bsc[[ j dlg8 to j kp- the status quo and mb j kp- Fabric compat.

Glitch: Yeah, we c j use the Fabric libs for parsing Tiny for tt, so tt won't be too much of an issue at all.

Oro: We also, yeah, I'm not exactly sure what my plans are, but we will prob be mk- sth smlr to mapping.io and we can have our parser in thr and then not hv to ncsy[ use the Fabric lib anymore and then kinda rmv some of the old dead !! toolchain stuff.

Gdude: While we're here, Aurora, tt looks lk one for you, mb.

Aurora: "Curr[ QSL is not up to fetr parity with FAPI. Are PRs for modules with no analogs to FAPI modules be csdr_ at the same prio lvl for futr rls a/s those other funda modules?"
It's kinda hard to tell, bcz it rly dpd on the fetr. Thr cb some fetr tt cb csdr_ esnc[ but isn't in FAPI. I can't thk of an eg rn, but thr might be some. If you tk foreg, the Tags API, it's not a straight port. Thr's lots of new features tt do not exist totally in FAPI. And curr[ FAPI do not even have a Tag API anymore. So thr's no analog. I thk it shld still be csdr_ w a high prio bcz tags are rly impt.

Mb tk foreg, thr's a PR called cmmn module "R cells and Argen types"? Tt's q a useful fetr, so I thk wtvr comes shld be csdr_ mb w the same prio lvl. I thk it rly dpd on the fetr. Some fetr fr FAPI islf, are not rly impt to port lk rn. ~~For initial readings~~, the prio is to have out sth usable. it's not to have an exact one-to-one port. So if you want new fetr, feel free to !!! PR it, or discuss it j= It rly dpd. Thr's a psbl] tt new fetr are csdr_ as equal prio to existing fetr in FAPI.

Glitch: To kinda add onto tt, having= Being FAPI at init rls is not a goal for us, bcz thr's no real rsn to use QSL. We're more concerned with new fetr rn. But thr will be a t when we're try- to drop having to mntn Fabric supt, tt catching up w Fabric and grab- eth we missed will bcm a prio. Bcz we don't want to strip away FAPI and leave ppl w only half of a usable API.

Aurora: I hv sth else to add. If you tk foreg, the Keybindings API PR, it both supt new fetr too. It ports the basics of the FAPI Keybinds stuff, but it adds much more. Lk foreg, the ability to dyn[[ dsbl keybinds, or the ability to show tooltips on keybinds tt conflict to show which keybinds conflict exactly. And stuff lk tt. So some stuff are btr for mod inter- compat. It's not j straight ports. It's rly new stuff, or existing stuff tt isn't present in QSL. The idea is to bring in as much fetrs as we can in the API to ease dev].

Gdude: Thx for tt, folks. Silas is asking, "Will we cont to hold mtgs lk this, or will we go back to Discord?"
We don't rly hv a gd ans for tt one. Mumble is work- q well. It doesn't rely on sbdy else's bot. I'm actl[ host- the Mumble bot and the Mumble srvr. Now, while it was convenient to use Carl on Discord, thr still ~~left with~~ a lot of work on it. Sorry, Craig, not Carl, thx Southpaw. Bsc[ what hppn_ was, Craig was destined to get yeeted bsc[. The devr was kinda done with it. Some other ppl hv tkn it over, but they're doing a lot of work on it ATM, so we don't know whether it's lkly tt we'll go back yet. We m dcd to, we m not. 

Either way, we're alw gg to kp it aces[ on the #stage chnl. So, lk, you'll still be here to listen to it. But yeah, I'm rly not sure, I don't hv the crystal ball for tt x4tun[[. I ustd tt thr's dfnt[ an aces] bonus for it. We had the idea of actually screensharing the Mumble chat, but then we rlz_ tt stages don't actually have tt fetr. So yeah, mb if Discord impl it , we'll do tt. Mb we'll go back to Craig. We j don't know yet, x4tun[[. Alex, wld you lk to take on Octal's qn?

Alex: Sure, so Octal asks, "Are there plans for the QSL module dl-?"
The ans is yes.

34:40
























