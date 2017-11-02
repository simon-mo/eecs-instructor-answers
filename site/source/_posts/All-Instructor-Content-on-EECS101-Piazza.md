---
title: All Instructor Content on EECS101 Piazza
date: 2017-11-02 07:40:40
tags:
toc: true
---


## Should people interested in systems take 189?

2017-10-25
99% of this piazza is people saying they're interested in AI/ML.  
But for us 0.00001 people who are more into systems/software (e.g. I'm in 162
right now and enjoy the class a lot, I also plan on doing 164 because
compilers are awesome, etc.), should we also take 189, given that ML seems to
be taking over all of CS?  
I used to think ML was like a 'weird' area of CS that was more like Applied
Math/Statistics than 'standard' CS.  
But looking at the systems research being done here: the 162 professor
(Stoica) does research in systems for... _**machine learning and big**
**data?!**_ And the other professor who teaches 162, Joseph, does research in
security for ... _**machine** **learning?!?!**_ And of course in computer
architecture, you 've got Google's TPU for machine learning etc.  
Clearly 189 would be important for systems people too, but I'm already a
junior and haven't even taken the preparatory courses for 189: Math 53,
EE16A/B, EECS 126, 127 or Math 110. Should I still try to take those courses?

### Anant Sahai's answer
I think that CS systems people are incredibly important. (And I say this as
someone who is not in CS systems.) From a distance, what is happening is that
CS systems is becoming exactly like what EE circuits has been like for a while
--- the details of the algorithms and problems matter because there are
incredible synergies to the implementation and algorithms need to be changed
to be implementable. This means that a CS systems person needs to be educated
in the mold of a traditional EE circuits education --- and that means getting
a healthy dose of mathy courses to go alongside a core set of CS systems
courses.

Fortunately, the lower-division core that everyone takes has already been
shifted in anticipation of this. All CS Systems students need to take Math 53,
EE16A, EE16B, and 70 along with 61A, 61B, and 61C. This goes without saying.
From there, it is about choosing courses that are both core as well some that
go deep into their area. Of course 162 is an amazing course that is core and
central to CS systems. A CS Systems student should take other 16X courses as
well for depth in systems. 149 is another core course for the emerging area of
CS systems in embedded systems --- since being tied to servers and PCs is way
too limiting an education for the future.

But beyond that, a CS Systems student should take core courses elsewhere as
well. The core upper-div algorithms course is 170, and all CS systems students
should take that. The core upper-div ML course is 127, and I personally think
that all CS systems students should take that too (because it is the
*optimization* part of ML that the systems person has to support in their
system design, as well as the *optimization* aspect of ML that a systems
person is going to be leveraging to make their systems work better.). The core
upper-div digital design course is 151, and arguably, a CS systems student
should take that or 152. You need to be a able to understand FPGAs. You can
rent FPGAs on AWS now. This isn't something esoteric as a compute platform.

So should a CS systems person take 189? Should they take 126? There is no way
that either of these courses can compete with 127 for a CS system person's
love (and I say this as someone who has taught both 126 and 189). They're
great courses, but not as important. It is all about opportunity costs. Put
126 up head-to-head against say 164.... It is hard to say that 126 wins for a
CS Systems person. So 189 clearly loses that competition.

So, sure, if a CS Systems oriented person has taken a solid foundation
(including 127) and has gone into depth in CS Systems, then they can take
further courses as per their interest. If that means taking 189, go for it.
Presumably, that person enjoyed 127 and wanted to go further. To learn more
about this particular application area for systems that lean heavily on
optimization and data.

### Followup:
Student:
We have an entire third/quarter of the class devoted to distributed systems
(we're about to start it in a couple weeks!), and given that it's the only
undergraduate non-special topics course that covers distributed, I'd say it's
_pretty_ good!

CS168 is cool, but it concerns itself with more classical networking concepts
and doesn't really cover a lot of the distributed systems/cluster management
networking issues until the last few lectures, as a part of "future topics".

## AI/ML Upper Div Class Path for LSCS

2017-08-01
What is a typical class path to take for someone in LSCS who is interested in
doing research in Machine Learning, AI, and Data Science?

By the time I declare, I will have taken 61abc, ee16ab, cs c8, cs70, and maybe
cs c100. What are some essential Upper Div classes for these fields I should
take after I declare and what should be the order of taking those classes?

Also, is taking Math 53 necessary for someone going into this path?

### Anant Sahai's answer
Math 53 is vital. The basic answer is the core fundamental upper-divs in this
area are: EECS 126, 127, 189, and 188. 170 is essentially always useful for
everyone wherever their interests end up in majors offered by the EECS
department. Of these, 170, 126, and 127 can be taken immediately after the
lower-division and you will get a lot out of them. You will get a lot more out
of 188 and 189 if you take them after these three. (Your goal in research is
not to become a good minion as fast as you can, it is to understand the
fundamentals so you can absorb more during your inevitable minion-phase.)
106AB (robotics) is also pretty important. And 120 going to 128 can be
helpful, particularly so on the research side. Math 110 is pretty vital if you
really want to be on the research path here. Graduate courses: 229a, 223, 227B
are good for theoretical strength and 280, 287, etc. for things connected to
specific application domains. There are also a bunch of special topics
graduate courses. But by the time you are thinking of taking any graduate
course, there should be a graduate student mentor or professor advising you.

## CS 189 preparation: Stat 134, Math 110, CS 188

2017-08-02
Have taken Stat 134, Math 110 and CS 188 and looking to take CS 189 next
semester. I know Professor Sahai has repeatedly stressed that taking 126, 127
and 170 is ideal before 189. My questions are:

    1. Is my preparation enough for 189? or should I take 127 and 170 next semester first before I go for 189 (I plan to take 127 and 170 eventually anyways but don’t want to miss out Professor Sahai’s 189)
    2. How exactly does taking 127 and 170 before 189 benefit me in learning 189? Since it seems like many people take 127 after 189. 
    3. Does it make sense to take 126 after Stat 134? Or should I just take Stat 150/135

Thanks!

### Anant Sahai's answer
If you have 134 and 110 under your belt, you probably won't get wiped out.
Because you'll be comfortable with the probability and the linear algebra, you
will be able to concentrate on the machine learning concepts and take them in.
Not having optimization will mean that there will be a few times when the
simultaneous presence of optimization ideas and new machine learning ideas
will cause you to have to work significantly harder, and you might not get as
much out of that part as someone with stronger foundations there. The real
concern is students who have none of Math110, EECS126/Stat134, EECS127, and
CS170. They might be in for real trouble as they have to simultaneously
understand probability, linear algebra, optimization, and machine learning. If
they also haven't had EE16AB, then it's probably completely hopeless to
actually understand the concepts. After all, machine learning is essentially
the application of optimization within a framework deeply informed by linear-
algebraic and probabilistic intuition to problems of data-driven pattern
recognition using computers. A certain level of comfort with the tools is
extremely helpful. Otherwise, it's like taking a Sanskrit literature class
given in Sanskrit without really understanding Sanskrit. Sure, the point of
the Sanskrit literature class is the literature, but not knowing Sanskrit
really well is going to cause difficulty.

The unambiguous recommendation for students who have taken 70 is to take 126
as their main probability course. This is because 126 can count on 70 and
thereby go beyond in many ways, including in connecting more deeply to EECS-
relevant applications and probabilistic modeling itself. If you've already
taken 134, you should have a conversation with the 126 Prof to see whether it
is a good fit for you or not.

### Followup:
Anant Sahai:
That's the thing. It is very hard to self-study the foundations of probability
and optimization, because it is a way of thinking and a perspective rather
than specific concepts per se. From a practical perspective, it is probably
far more profitable to spend time really reviewing EE16AB, CS70, and Math 53
material to make sure you know it very well. There you have the advantage of
actually being able to build on courses that you actually took with lectures
and discussions that you actually attended to let the ways of thinking seep
into your brain, reinforced by homeworks, labs, and exams that you also
struggled with and completed. The basic foundations of optimization thinking
were laid down for you in 16A (positioning module where least squares was
introduced) and 16B (least-norm solutions, psuedoinverses, etc.), The SVD/PCA
foundations laid in 16B are of course critical, and the exposure to k-means
(Lloyd-Max) in 16B (and 61A for that matter) is helpful. As is using all this
stuff in lab and for the project. The foundations of probability were laid
down for you in 70, including a probabilistic perspective on the least-squares
thinking that you had learned in 16A. From 53, you need to really understand
what differentiation means for functions of vectors. (Of course, you saw a bit
of this in 16B as well.)

Reviewing your lower-division is something that is actually doable. Beyond
that, the next biggest bang-for-the-buck probably comes from understanding
multivariate Gaussian distributions, and in particular, the effect of linear
transformations on the densities of such Gaussians.

Everything beyond that is likely not worth trying to learn on your own. In
that your time would be better spent on strengthening the foundations you have
already been exposed to.

### Followup:
Student:
Forgot to mention that I've taken Math 53 and 54

## Major Route Suggestions

2017-07-24
Hi everyone, I am a rising sophomore EECS major who is very interested in
robotics/AI/ML (currently doing robotics research for the summer)

I have two options that I am trying to decide between and could use some
advice.

Option 1:

    1. CS170 - Algorithms
    2. CS188 - AI
    3. CS189 – Intro to ML
    4. CS162 - OS
    5. CS161 - Security
    6. CS294 – Deep RL
    7. CS287 – Advanced Robotics
    8. CS61C – Machine Structures
    9. EE127 – Convex Optimization
    10. E157AC -
    11. HSS -
    12. EE16B – Designing Information Devices and Systems II
    13. MATH53 – Multivariable Calculus
    14. PHYSICS7B – E and M
    15. EE106A
    16. EE106B
    17. EE192 - Mechatronics
    18. EE128 – Feedback Control
    19. STAT134 – Continuous Probability
    20. STAT150 – Stochastic Processes
    21. STAT155 – Game Theory
    22. CS152 – Computer Architecture
    23. CS168 – Networking and Internet Protocols
    24. CS191 – Quantum Computing
    25. STAT281A* - Statistical Machine Learning
    26. STAT281B* - Statistical ML

* = optional

This is basically my EECS + a little stats route - i realize this is a lot of
classes but with four techs per semester ill be fine :)

the other option is as follows:

    1. CS170 - Algorithms
    2. CS188 - AI
    3. CS189 – Intro to ML
    4. CS162 - OS
    5. CS161 - Security
    6. CS294 – Deep RL
    7. CS287 – Advanced Robotics
    8. CS61C – Machine Structures
    9. EE127 – Convex Optimization
    10. E157AC -
    11. HSS -
    12. EE16B – Designing Information Devices and Systems II
    13. MATH53 – Multivariable Calculus
    14. PHYSICS7B – E and M
    15. MATH110 – Advanced Linear Algebra
    16. MATH104
    17. MATH105
    18. MATH128
    19. PHYSICS7C
    20. STAT134
    21. SOME MATH COURSE
    22. SOME STATS COURSE
    23. STAT150
    24. CS192
    25. CS168*
    26. CS152*

This would be a double major with engineering math and stats.

**I have some extra cs courses that aren't ML/AI but just purely interest
based

anyways sorry for the long post - if you guys have any good ideas on which one
would be more useful for grad school in AI/robotics research that would be
awesome

### Anant Sahai's answer
The ML/AI inner core in EECS is pretty clear. In the lower-division, it is
Math 53, EE16A, EE16B, and CS70. In the upper-division, it is EECS 126
(clearly indicated over Stat 140 or 134 for students that have had 70), 127,
and 189. To this, one should almost certainly add 170 and 188. At the
undergrad level, this should be rounded out by 106AB in upper division for
robotics. (And probably 120 because it is such a common language that you will
find others relying on it later.)

But if you really want to pursue this area, then you probably need to go to
graduate school. This adds another set of courses and considerations. First,
you really want to deepen your mathematical training. For this, the courses
Math 110 and 104 are probably essential. You'll definitely take more Math/Stat
in graduate school. So probably taking Math 113 is a good idea for Math
breadth, because you might not end up taking it later in graduate school.

The other key to your undergrad training is the selective taking of
foundational graduate courses in EECS. The best choices are probably among
EE223 (when it is offered --- really hard to beat this in terms of
foundations), EE229A (information theory), EE227B or 227C (more optimization
beyond 127). You don't have to take all of these by any means --- one to two
is fine. This is assuming that you are doing undergrad research in the typical
way, which means that you are probably learning about more applied things
directly. If you want to add in one of the relevant graduate special topics
courses that are offered in the learning space (e.g. Deep X), then do it. But
really, the cutting edge of the field will keep evolving and so taking the
special topics courses when you are a graduate student is probably a better
bet. The only reason to take them earlier (while an undergrad here) is that
you will probably have to go elsewhere for graduate school. The foundational
grad courses in Stat Learning like 281AB can arguably wait for grad school
itself since you're likely to take them then.

The above is a core AI/ML oriented perspective. If you want to add a different
tightly synergistic dimension, high performance systems (162, 267, Math 128x)
is one nice choice. Another is formal methods (144, 164, 172, etc.). Another
is deepening your exposure to control (128, 221A, 222, etc.). Especially if
you want to go in the vision or audio or multimedia-related AI/ML side, then
deepening your SP exposure (123, 184, 225x, etc.) is a very good idea. There
are other choices too that are synergistic.

As you can see, there is plenty to take. Double majoring or anything like that
is almost certainly a really bad idea.

### Followup:
Student:
I also don't think Math 128A was that valuable, except maybe the numerical
linear algebra section (chapter 6). Math 104 I found was good for building my
mathematical maturity, but not sure what it's used for other than in the
definitions of statistical estimators (and also CLT definitions and related
use real analysis language I guess). I had a question regarding CS 186 though,
as someone who wants to pursue data science and has taken Stat 134 (kind of
accidentally), is it more important to learn about database construction in
186 or would it be better for me to take EE126 and learn some probability
applications and stochastic processes? Also, is EE16B useful for machine
learning at all because I feel like the SVD will be covered by 127 which I'm
100 percent sure I'm taking in spring. Kind of wish we could replace EE16B
(definitely would want to skip 16A) with an upper div EE so I could take both
CS 186 and EE126 (have limited room in my schedule). Since I've taken both
Math 54 and 110 I would much rather take EE126 than 16B but I guess that's not
possible with the current CS major policies.

Anant Sahai:
It is harder for an undergraduate to appreciate this, but you need to take a
bit of a dynamic programming perspective. If you really want to get into these
areas, you are going to go to graduate school. This means that you will have
plenty of opportunities to take courses then as well. So the question becomes,
what do you take now vs what do you take later? This perspective informed my
answer. Statistics foundations are something that you certainly have to build
at some point (to have a well-rounded education in this space), so the
question is when. I believe that there are good reasons that those foundations
are better built when you are a graduate student. While the ones that I listed
were more important to prioritize as an undergraduate. A part of the reason is
that foundational breadth also impacts your choice of potential advisers and
projects as you begin graduate school. Not having Stat 135 almost certainly
closes no doors. Not having 126 or 127 can definitely close doors (to take an
extreme example). There is often a qualitative difference between the first
couple of things that you do as a PhD student and the last couple of things.
What is good to take early are things that are qualitatively maturity-
enhancing, broadly useful skill-granting, and/or mind-expanding.

Student:
Here are some of my opinions:

You listed robotics/AI/ML, but I think that's a pretty large area. Not saying
that you need a specific focus so early in your undergraduate career, but you
should probably narrow it down eventually.

The utility of Stat 135 depends on how much _statistical learning_ you want to
do. Think of it this way: If you are interested in AI/ML because you want to
build learning algorithms or intelligent agents, then perhaps it 's not as
important to you. I think you could get by with knowledge of optimization and
probability. On the other hand, if you are interested in foundational
questions (such as: is it even possible to learn? what is the nature of a good
statistical estimator? what is the behavior of common estimators
asymptotically?) then you'll probably want to take more statistics courses.
The former is about ML as a part of AI; the latter is about ML as a part of
statistical inference.

I don't think Math 128A is very valuable. Perhaps 128B or 221 will be better
for your purposes.

Also some general thoughts. As contradictory as this sounds, I think you
should try to prioritize both a strong foundation and depth. Foundation
meaning courses like Math 104. While you're taking Math 104 you may not see
why it is important or useful, but you don't want to go into graduate courses
feeling shaky about fundamental math concepts. Undergraduate is your time to
build these fundamentals anyway. By depth I mean figuring out a more specific
interest (e.g. spectral graph theory) and then learning more about it. For a
topic as specific as that, you probably won't find much besides special topics
courses and maybe one introductory graduate course, so you might need to pick
up some books for outside reading.

It might seem like I'm saying you should do everything, so to make it clearer,
I don't recommend that you take a lot of non-foundational undergraduate
courses. For example I wouldn't recommend that you take (this is just a crazy
example) EE 105, 106A/B, 113, 117, 120, 121, 130, 134, and then CS 169, 172,
186, ... That would be a plan without much synergy or thought, and I don't
think it would prepare you very well for anything.

Student:


Student:
I would say if you're a rising sophomore, in EECS, sign up for faculty
advising and ask these questions to your advisor. There are certain back and
forth question schemes that are ill suited to piazza. Your faculty advisor
should be able to answer these questions.

Student:
there's a cs289b?

Student:
Also, as a follow up: you mentioned several synergistic clusters in
specialized fields. I'll be taking Math128A next semester which seemingly fits
into the "high performance systems" cluster; however, is there a class or
venue where I can explore the different topics and figure out what I have
interest in?

### Followup:
Student:
Again I think it depends on what area of ML/AI you're going into. If you
really want to do a lot of statistical learning (asymptotic behavior of
estimators, for example) then you probably want to go for Stat 135, Stat
210A/B (and whatever preparation you need to get there). If you want to tackle
even more foundational issues (e.g. an important example is [de Finetti's
theorem](https://en.wikipedia.org/wiki/De_Finetti%27s_theorem) and it's
relationship to Bayesian statistics), then you may want to take Stat 205A/B
(which probably means taking Math 202A at least).

### Followup:
Student:
Why is EECS 149 useful?

Anant Sahai:
yes

## EE 16AB for 189

2017-04-25
Hi, this question is directed towards Professor Sahai. I have seen posts that
mention the course will involve a mastery of the concepts from 16AB, 70 and
53. I think I have taken 70, 53 but not the 16AB series. I am very confident
   in my linear algebra skills (taking math 110 currently). I was wondering if I
   should go over the material from 16AB and what specific material in order to
   prepare for 189. If not, is there any other material I should prepare before I
   take the class?

### Anant Sahai's answer
**@ Anant Sahai**

Multiple topics from 16AB are very relevant to 189. First, there is the spirit
of casting problems into optimization problems. This will be leveraged and
built upon. This shows up in the Linear Regression parts of 16A. It also shows
up in the SVD sections of 16B. These are perhaps the most directly relevant.
After that, there is the whole circuits perspective on information processing
which shows up in the neural nets parts of 189 --- which are basically
circuits that do information processing. The sections of 16B (and a tad in the
locationing lab for 16A) where you see how nonlinear functions can be
linearized in a neighborhood is also quite important in 189.

## EECS Research

2017-04-10
Can someone who is currently or has worked in an EECS Research Lab, such as
BAIR Lab, tell how they got involved? What classes did you take before
contacting a professor? Did you focus your domain specific knowledge on the
state of the art work in the field, or did you specifically read that
lab/professor's papers? For reference, I'm currently a freshman interested in
ML research, and I have had some experience in the field. Is it too late to
approach professors for the summer? If I'm looking for next school year, what
are things I can do during the summer to increase my chances?

### Anant Sahai's answer
**@ Anant Sahai**

Multiple topics from 16AB are very relevant to 189. First, there is the spirit
of casting problems into optimization problems. This will be leveraged and
built upon. This shows up in the Linear Regression parts of 16A. It also shows
up in the SVD sections of 16B. These are perhaps the most directly relevant.
After that, there is the whole circuits perspective on information processing
which shows up in the neural nets parts of 189 --- which are basically
circuits that do information processing. The sections of 16B (and a tad in the
locationing lab for 16A) where you see how nonlinear functions can be
linearized in a neighborhood is also quite important in 189.
### Followup:
Kris Pister:
Take on a project that you think you can handle.

Ask for help when you get stuck.

Try to make some tangible progress every single week, no matter how little it
may be.

Let the right people (e.g. grad student and professor) know if you are really
stuck.

Repeat as necessary.

If you can do that over the course of a semester or a year, you're almost
certain to

have had an important positive impact on a research project. Sometimes that
gets

your name on a research paper, which is great. Sometimes not, which is ok too.

Student:
Professor, what do you consider success in undergrad research?

Kris Pister:
Tenacity. Determination. Persistence. Irrational refusal to admit defeat.

I had an undergrad researcher who came to me recently with a very real list

of the reasons why he had not been able to accomplish much, asking if I could

please still write him a letter of reference. I told him that I could write
him a weak

letter, but that he had a great opportunity: if he could succeed *now*, with
both

of us knowing that the easy path wasn't going to work, then I could write him
a

really strong letter, and he would get a lot of psychic benefit. Two weeks
later:

it worked!

That's what research is all about. Stare at the brick wall and try to figure
out which

brick is likely to move the most when you smash your head into it.

(It's a little easier for undergrads. We try to find one that's already loose
for you.)

Student:
What qualifications did they recommend you have? Did they look at your
coursework, past experience, etc.?

## Prof. Sahai's CS 189 philosophy?

2017-03-30
I'm interested in learning what Prof. Sahai's CS 189 teaching philosophy will
be, as he's teaching the course in the fall. What does he interpret machine
learning as? Prof. Recht viewed ML as EE 126 + EE 127 + backprop (read this
somewhere on this piazza). Prof. Shewchuk supposedly focuses more on ML
concepts.

[Disclaimer: I never taken CS 189 hence I don't know how true these statements
are.]

### Anant Sahai's answer
I am talking to the past instructors of the course because I believe that it
is important to have some degree of consistency, but my basic philosophy is
that ML is fundamentally about learning, which is about discovering patterns
in a way that can be represented and leveraged in a useful manner --- for both
active interaction and passive understanding. In that way, ML is at the
intersection of control and signal processing, with an underlying connection
to information theory and statistics. I would want my students to understand
the fundamentals here, including the core tradeoffs. I also want them to
understand how the optimization paradigm applies to this domain because this
helps gain some understanding of informational vs computational limits. The
different ML techniques and approaches are vehicles for conveying an
understanding of how to think better, not some grab-bag of tools.

In my ideal world, I would teach 189 to students who have already taken both
126 and 127 (so that I could concentrate on the ML aspects as opposed to
probability and optimization aspects bottlenecking student understanding), as
well as of course the full EECS lower division. But that would be too radical
of a change from precedent and policy. However, following department policy, I
am going to freely assume and rely on a mastery of the EECS lower division,
where because of the nature of the material this is going to fall most
specifically on 16AB and 70 as well as Math 53. I am also going to assume
maturity corresponding to the nature of the course --- 189 is not like 126,
127, and 170 which are meant to be taken among the first set of upper-division
courses. 189 is meant to be taken with more maturity. In terms of teaching
philosophy, my belief remains that students learn best when they work hard and
are challenged.

## Prerequisites for EE 223

2017-10-31
I noticed that on the course listing for EE223, it was encouraged to be
concurrently taking EE226A. Would it be acceptable to take EE126 concurrently?

### Anant Sahai's answer
No chance. 223 is a reasonably advanced graduate course. You better know 126
and 127 stone cold.

### Followup:
Anant Sahai:
Most definitely not. 226A is a decidedly more advanced course with completely
separate lectures, etc...

## Taking 170 and 189 Together

2017-10-26
I was planning on taking 170 and 189 together next semester, but the lecture
times conflict. Is it likely that 189 will have an alternate final time?

### Anant Sahai's answer
No.

## Is EE130 likely to expand?

2017-10-23
This class (at least the undergrad section) is full as of a couple of days
ago. The waitlist is still rather small, but is it likely that the class will
expand to accomodate waitlisted students or that seats in the grad section
will be shifted over?

### Kris Pister's answer
Unlike CS UD, all seats in EE courses are released at the beginning. I
wouldn't count on anything being expanded.

ksjp: This is something that we should definitely try to fix. I will look into
it.

### Followup:
Student:
Thanks for the response, professor!

Student:
just realized that class size might be limited by discussion room...

## CS 189 Instructor

2017-10-23
Will we know who the instructors are for CS189 soon?

### Anant Sahai's answer
Probably me. But things will be official when things are official. There are
lots of courses and the scheduling officers for EECS have to put this puzzle
together.

It's not like we are hiding things from students when we really know for sure.

## CS61C + MATH 110 + EECS 126 + EECS 127

2017-10-20
Planning on taking these 4 classes next semester (sophomore), how heavy would
the workload be for those who have taken? Also if I were to choose one (126 or
127), which one would be a better pick to prepare for 189.

### Anant Sahai's answer
From my perspective as someone who teaches 189, the following makes the most
sense:

1) If you have taken 16AB and 110, and have strong vector calculus, the single
most important course to prepare for 189 is 126. This continues to hold as
long as you have taken 16AB and do not have have some weakness in vector
calculus or linear algebra. Being able to reason probabilistically and have
intuition about it is very important. 70 is not really enough.

2) If you have weakness in linear algebra or vector calculus or have not taken
16AB, then 127 is the most important course to prepare for 189. You will
experience significant difficulties without that understanding.

3) If you have taken 16AB and 127, for many students, taking 110 could become
largely redundant. A student in that position should take the 110 textbook and
read it on their own. See if you need more.

Of course, hopefully everyone understands that both 126 and 127 are *more*
fundamental courses to take than 189 if you are interested in machine
learning. And if you have to pick only one of the three courses: 126, 127, and
189; then 127 is clearly the most important one to take for students
regardless of their area. There are lots of machine learning applications in
127.

In light of this, the most reasonable course of action is for interested
students to take both 126 and 127 before 189. And if because of time pressure
to graduate they want to take one concurrently with 189, that course is likely
189. (Although it is better understood as taking 189 concurrently with 127.)

Courses are far more rewarding if you can really understand what is going on.
None of these courses are gratuitously difficult or anything like that, but
truly engaging with the material does require hard work and building up your
understanding.

I understand that the fashionable name and interesting subject matter of 189
is appealing, but when you're seven weeks into the course, trust me, no amount
of fashionability is going to help you out or even make you feel any better.
Understanding probability and optimization well will.

### Followup:
Student:
The reason I asked it here is that professors/course staff would know better
how much overlap there is between said courses.

Student:
Your first assumption cannot be justified wholly.

Also, this is a question for the Math department, not EECS Piazza.

## Which classes to Phase I / II

2017-10-16
I want to take the following classes:

CS 61B

EE 16B

CS 189

Physics 5B

I was wondering which class would be best to phase II, as I'm only allowed
13.5 units for phase 1, and these classes are 15 units combined. How difficult
is it to get into 189 during phase 2?

### Anant Sahai's answer
Unless there is something radically unusual about your mathematical
background, please don't attempt to take 189 early. 189's core lower-div
prereqs are 16A *and* 16B. Absolute mastery of both those courses is critical.
189 definitely counts on significantly more than 70 in terms of maturity and
background. You also need to be able to program easily at the level of having
mastered 61B. And vector calculus to a level *beyond* that done in Math 53.

Remember, if you have to take only two machine-learning relevant courses from
EECS, those two courses are 126 and 127. They are more fundamental than 189
and ideally, you will have taken at least one of them (ideally both) before
taking 189. Both of them are filled with diverse applications, real code
writing, real data, etc....

Here is a difficulty ramp:

Easiest = 16A, then 16B, then 70, then 126/127, then 189 = Hardest. Each step
up on this ramp should make you work and grow, in a way that you'll be sore
but not injured.

189 is not a joke. It does nobody any good to have you take 189 and not
understand what is going on. You are not here to learn buzzwords, be
fashionable, or make cocktail party conversation. You're here to really learn
stuff that will form the foundations of a multi-decade career.

## STAT 140 vs EE 126

2017-10-16
Can someone who has information about both of these courses comment on which
one of the two would be better to take? I have seen the previous posts about
this, but the responses don't really elaborate on the differences between the
two courses.

I am a CS/Applied Math double major, but I am considering adding/switching to
the new Data Science major once it is approved. I did reasonably well in CS
70. I am more inclined towards STAT 140, because I know that professor
   Adhikari is awesome (I have taken Data 8 with her), but STAT 140 next semester
   conflicts with CS 188 (which I also intend to take), so I am not sure.

### Anant Sahai's answer
Students who have taken 70 are strongly encouraged to take 126. This is the
combined judgement of Stat and EECS together. It is also supported in what is
proposed for the Data Sciences major. So, take 126 because you will learn
more. (Of course, since 126 leans on 70 while 140 cannot do so.)

## Classes after EE16B

2017-10-16
I am wondering what EE classes people took/are going to be taking after
completing EE16B. I do not have any EE knowledge outside of 16A and 16B and
was wondering if there were other EE classes (upper div or not) that have a
moderate workload. No particular interest in any given field of EE, just a
curious EECS major.

### Kris Pister's answer
If you're more of a math/theory person, then 120 is a good course.

If you're more of a circuits person, then 105 is a good course.

Both of those are pre-reqs for several other courses.

105 --> 113, 140, 142. Power electronics, analog integrated circuits, RF
circuits.

120 --> 106A, 123, 128. Intro to robotics, digital signal processing, feedback
control

But there are a bunch of courses that just need 16AB (and maybe 70). These are
the ones

that I wish that I could take (or take again):

117 Electromagnetic Fields and Waves

118 Intro to Optical Engineering

121 Intro to Digital Communication Systems

122 Intro to Communication Networks

130 Integrated Circuit Devices

134 Fundamentals of Photovoltaic Devices

137 Intro to Electric Power Systems

147 Intro to Micro ElectroMechanical Systems (come build micro robots!)

149 Embedded Systems

Ha! I think that I listed pretty much every course. They are all awesome!

## Courses Similar to CS 70

2017-10-09
I am really enjoying CS 70 this semester (I think it's probably my favourite
class) and I was wondering what other classes people would recommend in the CS
or math department that I should look into?

Of course, CS 170 would seem like the next step, but apart from that, I was
hoping I could get some recommendations!

### Anant Sahai's answer
The default and recommended next class after 70 is 126. If you liked 70, it's
the one that takes the ball and moves it forward most directly. 170 is a
successor to 61b and 70 together.

## EE16B workload

2017-10-10
I plan to take ee16b and cs189 next semester, is this a manageable workload?
How is ee16b workload compare to math53 or cs188?

### Anant Sahai's answer
Understand that 16B is essentially a hard prerequisite to 189. So, if you take
them simultaneously, unless you have stronger linear algebra from other
sources, you are probably asking for trouble.

Remember, 16A and 16B are the lower-division courses that are closest
intellectually to 189.

### Followup:
Student:
I haven't taken 54, but I've taken 110 and 16B and absolutely 110 teaches you
much more linear algebra than both. It really takes that much linear algebra
to make good sense of the calculus you are learning—e.g. what is a derivative?
In more general manifolds like you encounter in later classes, it takes more
linear algebra to make sense of concepts that you formerly visualized in two
dimensions.

## Course Advice: CS170 + STAT134/EE126?

2017-10-07
Hi, I'm thinking about taking CS170 and a probability course next semester.
I'm not sure whether to take STAT134 or EE126 because I've heard that EE126
covers more material but is harder. Any thoughts on which class to take?

I'm also planning to take COGSCI1 and a language course along with these two.

Any advice would be appreciated.

### Anant Sahai's answer
The consensus advice from faculty in EECS and Stat is that everyone who has
taken 70 should take 126. That is the core probability course for EECS and
LSCS majors.

### Followup:
Student:
Currently taking CS 170 and EE 126. IMO, if you're interested in probability,
and especially if you're interested in communications/networks and AI/ML, you
should take it. It's harder than CS 70, but you build a lot of problem solving
skills as it relates to probability. As for the combined workload, it's
basically two CS 70s.

## Most Important CS Upper Divs for Industry

2017-10-07
What are the classes in the CS department that help you most to get
internships/perform well during internships? My goal is to be a software
engineer, if that helps at all. Asking because I heard today that 188 isn't
very useful at all, so I'm just wondering what would be best for industry.

### Anant Sahai's answer
170 is core for everyone.

162 and 149 are arguably the most core for someone who wants to be a versatile
"non-mathy" software engineer, to which one could add 169, 160 and probably
168 as well. 161 and 186 are also solid courses for this path.

126 and 127 are arguably the most core for someone who wants to generally be
versatile on the AI/ML path. To which one should add 189. 188 and 106AB are
also good courses for this path, but not at the same level of core as the 126,
127, 189 triad.

In general, you should have a mix of solid fundamentals and particular areas
that you are drawn to or specific faculty members that you want to take
courses with.

Very advanced jobs in all areas will demand graduate school.

### Followup:
Student:
To add to this, I think 161/168 (security/networks) are good for general
purpose. IMO these are good considerations if you are aiming to do some sort
of web development (CS169 might also be good for this since it's fairly
similar to what you'll be doing in the webdev industry but that's also a
reason not to take it so you can take more things that are interesting to
you).

Apart from these, it really depends on what field you want to go into. For
example, if you want to go into AI/ML, you should probably take 188/189. If
you want to go into graphics or VR, 184/194-26/(Grad Computer Vision Course;
forgot the course number) would be good to take. Etc.

### Followup:
Student:
Thank you!

Anant Sahai:
The answer to this is also very clear.

If you want to get the most out of 189, take both 126 and 127 before taking
189. Then, your understanding of 189 will be significantly deeper.

If you have taken the standard sequence: 16A, 16B, and 70, (with math 53 in
there as well) the next course to take is 126. Full stop. Then, if you feel
very comfortable with the linear algebra and have absorbed the basic
optimization problem modeling ideas from 16AB, you can in principle take 189.
You'd be better off having taken 127 (which by the way is filled with lots of
machine learning applications) as well, but you will still get a lot out of
189 and not be lost.

If for whatever reason you have not taken 16AB, then definitely take 127
first. Then, you can take 189 if you feel that your probability intuition is
strong. (Not sure how it would actually get strong without having had 126, but
maybe you took some other set of courses that really strengthened your
probability intuition.) If your probability intuition is weak, then there are
going to be parts of 189 where you will basically get slammed and there will
be aspects of the story that you won't be able to properly internalize. But,
with 127 under your belt, you'll still be able to make it through.

Again, best case: take 126 and 127 first, then take 189. After that, if you've
taken 16AB, 126 probably is more important than 127 as a foundation, but 127
has way more machine learning in it.

If you can only choose two of the three to take, the answer is unambiguously
to take 126 and 127. With those solidly under your belt, you can essentially
self-study 189 if you need to. The reverse is not possible. There's a way of
thinking that 126 and 127 convey that is very hard to get without taking the
course. Meanwhile, the way of thinking that 189 teaches that goes beyond
126/127 is largely obtainable by the world teaching you.

To use a machine learning perspective, if your prior is initialized properly
by 126 and 127, then stochastic gradient descent by doing real world problems
and reading papers will make your inner understanding converge to what 189 is
trying to teach you. But if you don't have 126 and 127, you will very likely
get stuck in a bad local minimum. All 189 does is speed up the convergence.

## Can EECS151 Substitute as a Requirement for EE16A?

2017-09-28
Hello, I'm an L&S CS senior that will be graduating next semester (Spring
2018). I remember EECS151 could be used as a substitute for EE16A in previous
semesters and was wondering if that's still the case.

### Anant Sahai's answer
170 is core for everyone.

162 and 149 are arguably the most core for someone who wants to be a versatile
"non-mathy" software engineer, to which one could add 169, 160 and probably
168 as well. 161 and 186 are also solid courses for this path.

126 and 127 are arguably the most core for someone who wants to generally be
versatile on the AI/ML path. To which one should add 189. 188 and 106AB are
also good courses for this path, but not at the same level of core as the 126,
127, 189 triad.

In general, you should have a mix of solid fundamentals and particular areas
that you are drawn to or specific faculty members that you want to take
courses with.

Very advanced jobs in all areas will demand graduate school.
### Followup:
Student:
You could try.
https://docs.google.com/forms/d/e/1FAIpQLScFl9sCqUmLq6pAqoFSHYubHg9KCVAvI7D2TaGivNOnb10AZg/viewform

Student:
Is there some way I can petition to make it count for my lower-div EE
requirement?

Elad Alon:
Yes, 151 does require 16B; if you actually had the circuits background to be
ready for 151 (and presumably finished Math 54 already), 16B is in all
likelihood the right class to take to finish the requirement.

  

(I can't speak for the dept. as a whole, but as far as I am aware, no, the
one-time exception will not be continued beyond students graduating this
semester.)

Student:
doesn't 151 require 16B?

## Is CS 189 Helpful/Useful in Industry?

2017-09-13
Hello, I'm currently a senior trying to see which classes will be the most
helpful in industry, as I'm graduating/job hunting pretty soon.

A little bit about myself: I'm an applied math major with a stats minor doing
my cluster in statistical learning. I've taken Stat 153 and CS 170 as part of
my 3-course cluster, and currently trying to decide which one to take for my
3rd. I am very interested in ML/prediction models (in any field, really). I've
only taken 61A/B, and I don't feel very passionate about programming as a
career, so working as a software engineer isn't really an option for me.
Unfortunately, as much as I'd like, going to grad school isn't currently an
option for me either, at least in the foreseeable future (due to various
issues surrounding finance, immigration status, etc.).

With all this being said, how helpful would CS 189 be for me? Is it more of an
introductory grad-school ML course, heavy on theory and little applications?
I've heard this class involves A LOT of work, and as much as I'd like to take
it as an academic interest, time is a big factor and I don't think I'm able to
do that if there's a "better" option for me.

Would those teaching/have taught CS 189 and have taken it recommend I go with
CS 189 with industry in mind, or maybe take something like EE 127 instead?
Thanks for your time.

### Anant Sahai's answer
189 is a balanced course: a reasonably solid grounding in basic theory plus
basic implementation plus application to different settings. It is cross-
listed as 289A and is generally an advanced upper-division course, expecting
students to have significant mathematical maturity. There is no getting around
the fact that it is a lot of work. You learn a lot, but you have to work
really hard.

From an industry point of view, there is no doubt that it helps to have a
machine learning course under your belt, at least at the very beginning. For
students without a large amount of mathematical background, we recommend
taking either 126 or 127 before taking 189. Both of these courses are
conceptually core to the machine learning area. The probability and facility
in working with probability in 126 helps you think and reason in a way that
helps. The optimization intuition and problem modeling practice from 127 helps
with both thinking and understanding. From a fundamentals perspective, if you
have a solid understanding of 126 and 127, you can learn machine learning from
books and other resources. The reverse is definitely not true.

In your case, it all depends on your facility with probability and modeling
thinking --- how much did Stat 153 hit? You haven't had EE16AB that hit a
bunch of optimization thinking and problem modeling. EECS 127 is a safe bet.
189 might be risky.

## Applied Math Double Major question.

2017-09-08
Is it worth taking a couple classes I'm not particularly interested in to
obtain a double major in Applied Math? For example, although I'm very
interested in Math 104, 110, and somewhat interested in classes in the
Statistics cluster for the major (153, 155), I'm not sure if it's worth taking
Math 113, 128A, 185. I'm a second year, so admittedly I have quite a bit of
time, but I'm curious is it generally better to just take the classes you
really want to, even if it means just coming shy of obtaining another degree?
I'd probably try to do a Master's, but I can't say at this point if I want to
do a PhD, so I'm not sure if mathematical maturity justifies classes like 113
and 185. It also sucks that they take the place of some (graduate) classes I
find more interesting in the Math/Stats department (Math 170, Math 202A, Stat
205A, etc.)

### Anant Sahai's answer
If you are interested at all in Math, you really really need to take 113.
You'd be walking around half-blind mathematically without it.

  

In general though, my opinion is that double majors are not a good idea unless
you should want to take all the required courses anyway, with possibly one
course of exception. Why should? Because you might not actually know how your
interests translate into courses that you should take. So get advice from
faculty.

## EE127 without Math 53

2017-09-07
Does EE127 require vector calculus, like Math 53?

### Instructor answer
I have not taken the class, but check out
[this](https://www2.eecs.berkeley.edu/Courses/EECS127/) website.

### Followup:
Student:
Try learning about partial differentiation, gradients, and the Hessian matrix.

### Followup:
Student:
Thank you, appreciate the advice!

Student:
I can't speak to 126 as I haven't taken it, but I'm currently taking 120 and
127; they are both very doable if you've taken 16A and 16B as they lean
heavily on things covered in those classes. 127 is much harder conceptually in
my opinion but definitely doable with only 1-2 other techs if you did well in
16AB. Having a strong intuition about the concepts in Math 53 is also
essential. 120 is conceptually easier IMO and picks up literally where 16B
leaves off with convolution and LTI Systems.

So, overall, they're both great classes, but 127 requires a bit more
mathematical maturity IMO.

## Considering P/NPing 162

2017-09-07
Hello all!  

I am currently taking CS162 and I am very worried about the class - it's only
been 3 lectures in, and I am confused already. I am not very good at low-level
programming concepts and I hated 61C. I enjoy theoretical computer science
(CS70, CS170, CS188) so much more and I was wondering if P/NPing 162 would
impact my job prospects or grad school prospects (MS or MBA either). I have no
intention of ever going into a hardware-oriented company or studying anything
about the OS for grad school. 162 has been stressing me out and I have a lot
of other extracurriculars on my plate and I don't want my GPA to tank because
of this course. BTW, I am a CS major.

Hoping a professor like @Anant Sahai and reply to this. It's stressing me out
a lot.

### Instructor answer
(Are students allowed to P/NP technical courses? I don't know the answer to
that question but am pretty sure that this is something that wouldn't be fair
to do to your project group if the course has projects.)

Now, I can just speak to the technical dimension. 162 is a really great course
and it is super important for anyone who wants to be a hardcore software
engineer. It should be the foundation of your software engineering upper-div
education. However, EECS isn't just for software engineers which is why we
don't require it to be taken. (By contrast, many traditional CS programs do
require the counterpart of 162. For example UCLA I believe requires operating
systems, programming languages, digital design, networking, algorithms, and
automata theory. These kinds of courses are the heart of a traditional CS
program.)

There is however, many entirely different worlds of things that you could
study. You could go hardcore into hardware and take courses like 105, 151,
149, 152, 170, 147, and 149 for another perfectly reasonable education. That
remains both practically relevant and grad-school relevant.

Or you could go into the AI/ML side and take courses like 126, 127, 189, 188,
120, 170, 106A, 106B. This is a more theoretical side orientation, with a
practical anchoring in robotics. A completely reasonable education. Definitely
employable and grad-school relevant. (Perhaps not as widely employable at the
bachelor's level yet as the traditional CS training, but that is changing
fast.)

So you don't have to take 162. But you kind of do have to take either 162&168
or 151&149 or 126&127 to be in a reasonable place. Our requirements might be
quite flexible, but it doesn't mean that anything that satisfies them is
actually a good idea. You need to have real depth and solid foundations in
something.

\---

On a policy level, L&S CS students can change their grading option to P/NP
until the deadline. However, the course will not fulfill a requirement and you
will need an additional upper division CS course in its place. EECS majors can
only P/NP technical courses if they've already fulfilled all the relevant
requirements.

### Followup:
Anant Sahai:
If you're applying in an area that is far from systems programming, frankly
speaking they're not really going to notice it too much. It might raise some
eyebrows if someone is looking closely. But not as much as a bad grade would.

## EE127 CS189 same semester

2017-08-28
Are EE127 and CS189 good classes to take concurrently, or are they better to
take in separate semesters?

### Anant Sahai's answer
For maximal understanding, take 127 first and then take 189. But you can take
them together. It's good to have at least one of 126 and 127 (the core entry-
level upper divs in the ML/AI space) before taking 189. With a solid
understanding of 16AB+70 under your belt, if I had to pick only one of them
ahead of 189, I'd pick 126. Without a solid understanding of 16AB, I'd pick
127. Without a solid understanding of 70, I'd say that 126 is essential.

### Followup:
Student:
Hm. Seems like 126 combines some parts of Stat 135 and 150 then. I have to say
that's really ambitious for one 4 unit class.

Student:
Keep in mind that EE 126 also covers estimation and hypothesis testing, which
are not part of stochastic processes.

## Stat 134 or Data 8?

2017-08-28
I am looking for another technical to take this sem. I'm enrolled in Data and
waitlisted for Stat 134 but I think there's a decent chance I might get into
Stat... anyways, I am interested in data science/machine learning and I have
taken CS 70 and CS 61A and it seems like there is quite a bit of overlap
between my past courses and both Data and Stat 134. Can anyone give me a
reason to choose one over the other? Thanks!

### Anant Sahai's answer
Students who have taken 70 really are recommended to take 126 rather than Stat
134. You'll learn more because the course can count on 70.

### Followup:
Student:
EECS 126, not Stat 126

## CS 61C, CS 70, Math 54 together?

2017-08-27
I'm considering taking the above 3 courses together this semester. Besides
those courses, I don't really have other commitments. Would you say the
workload is reasonable? or is it too much?

### Anant Sahai's answer
If you are in any major being offered by the EECS department, you really
should be taking EE16AB instead of 54.

### Followup:
Student:
Well as long as you do alright in 70 it should technically be fine right?
That's the only one of the three that is needed for your GPA for L&S

## How to read research papers

2017-08-27
Hi all,

I've been assigned to read some papers from a potential research mentor and
its been a very discouraging process so far. All of the papers reference so
many things that I haven't seen before and I'm finding myself going down a
rabbit hole of wikipedia articles, trying to understand what I'm reading. For
reference, the papers I've been assigned are on ml/reinforcement learning, and
the upperdivs I've taken are 170, 110, 188, and 126 (I'm taking 189 this
semester).

Anyway I guess I'm looking at general advice on how to read research papers,
and wondering how much struggle is normal vs how much is due to an
insufficient background).

### Anant Sahai's answer
You need to be willing to read actively. First step, don't try to read on a
screen. Print out the papers and get a notebook, a highlighter, and sticky
notes. Expect to spend something like 1 hour per page on average when you are
starting out. (It gets better.) Skim the entire paper. Just let it wash over
you first. You will understand almost nothing. That's normal. Then read the
abstract, introduction, and conclusion. Try to write in your own words what
you now expect to learn from reading the paper. Then read the paper again
slowly and make a list of questions as you go. Go one level deep of looking up
Wikipedia article. But keep writing down questions about what stuff means.

  

Then, go and talk to your mentor. Explain what you think the point of the
paper is and then ask questions about what you don't understand. They should
teach you.

  

The most important thing in starting doing research is the quality of the
mentoring. The specific topic is insignificant by comparison.

  

You have to be willing to accept that you don't understand. Without 189 and
127 under your belt, it is absolutely natural for you to have huge gaps in
your understanding. But good mentoring can help fill these gaps.

### Followup:
Student:
Thanks, I really appreciate both responses.

## CS 189 - More "Math-y" or Project-Based?

2017-08-26
This might be a silly question, but does CS 189 fall more under the "Math-y"
side of CS upper div's (like CS 170, where the class emphasizes
proofs/"paperwork" over coding projects), or is it more like 61B, where
there's a heavier emphasis on programming and projects? In between? Also, what
language does CS 189 use? The class seems to be based on psets and homework
rather than projects according to the CS 189 website, but I just want to be
sure. Thanks in advance!

### Anant Sahai's answer
189 is firmly in the mathy camp, with some programming in essentially each
homework along the way to help you understand the math properly as well as how
to use it. The closest comparison would be the HWs from the 16AB series (which
makes sense, since those are the freshman-level pre-ML/AI courses). Except for
the freshmen courses, there is a ton of scaffolding and handholding. For an
*advanced* undergraduate course like 189, there is far far less. In that
sense, there is a lot more programming in 189 than in 16AB. But we're not
talking about writing programs that are thousands of lines long by a long
shot.

## CS 189 Without CS 170?

2017-08-25
I'm reading a lot that CS 170 is an unofficial pre-req for a lot of the upper
div CS courses, according to a lot of the students/posts/professors, due to
the foundation/background it provides. I haven't taken CS 170 yet (taken 188,
61A, 61B, Stat 134, and Math 53), but I do have some experience with upper
div. Mathematics (110, 104) and Statistics (133, 134). Is this knowledge
enough for me to not fall behind in CS 189? Or should I take 170 first then
189 during my final semester? I just want to take 189 a bit earlier because
I'm afraid I won't get into the class (non-major), and enrolling in it Spring
2017 gives me another "chance" to get into it during the next Fall. Thank you.

### Anant Sahai's answer
Since you're asking about 189, I'll answer:

  

If you've had ee16a and ee16b and cs70, the single next best class to prepare
is 126.

  

If you haven't had ee16a and ee16b, the next single best class to prepare is
127.

  

In general, 126 and 127 are both way more directly relevant to 189 than any
other upper division course. Math 110 is also useful, but certainly not
necessary if the others are present.

  

For non-majors, 127 or a similar course is your best bet to prepare.

### Followup:
Student:
Wish Math 104 would matter but I don't think there's much analysis in 189,
maybe only using the language of analysis in some statistics concepts (CLT
etc.) ?

## Alternatives to EE16A for those graduating in may 2018

2017-08-25
Hi,

  

I noticed that there is a list of classes than can be taken instead of EE16a
to fulfil graduating requirements for seniors graduating this semester. Can
those same courses apply to those graduating next semester? If not, are there
any alternatives to 16a?

  

  

### Elad Alon's answer
That list of replacement courses was created as a one time exception to handle
the transition from the old courses (20/40) to 16, and we do not plan to
extend that exception beyond this semester.

  

If you've already taken Math 54 and understood it well, I'd recommend you take
16B instead of 16A (this is allowed). There are a number of threads on exactly
this topic here on piazza, so please take a look through those. You can also
contact me directly if you have remaining questions after looking through the
information that's already been posted.

## Should I drop STAT 134?

2017-08-24
I signed up for STAT 134 with Prof. Ibser this semester and I am currently
debating whether to drop it or not. Does EECS 126 cover all the topics in STAT
134 (I may want to take ECON 141 in the future)? Is EECS 126 worth taking
after STAT 134?

### Anant Sahai's answer
Take EECS 126. You can learn anything in Stat 134 that wasn't covered by
yourself by reading appropriate resources. The reverse is not true. The
unambiguous guidance for students who have taken 70 is to take 126.

### Followup:
Student:
Nevermind, you already mentioned in another post that EE126 also includes
hypothesis testing and estimation, which sounds like Stat 135 material.

Student:
^Agreed. Unless you have a solid background in analysis graduate level
probability is basically impossible. @Sinho though, I was wondering what you
would recommend for someone who has taken Stat 134, perhaps Stat 150
stochastic processes would replace the stochastic processes part of EE126?

Student:
205A is not easy.

Student:
126 cannot replace 134 for stats. you can, however, choose to take stat c205a
to replace 134 and if you know math 104 material and have some amount of math
105/202a you should be fine in 205a after 126.

Student:
+1, can CS 70/EECS 126 satisfy STAT requirement of ECON major?

## EE126 with average understanding of CS70

2017-08-24
Hi, I am planning to take EE126 this semester but not sure whether I am ready
for the class. I took CS70 in this summer and got an average grade around B
(the letter grade has not come out). I was confused about concepts like CDF,
PDF this summer.

So my question is that will I be fine to take EE126 with an average
understanding of CS70? If not, what should I do to be more prepared? Thanks.

### Anant Sahai's answer
You should review your 70 and then taking 126 will fix the gaps in your
knowledge.

You will have to spend extra time to catch up your understanding, but there is
no avoiding that.

## CS 189 Academic Intern Application

2017-08-22
Calling all former CS 189 students:

On behalf of the Fall 2017 CS 189 staff, I invite you to apply for our
Academic Intern role. Academic Interns organize and run guerrilla sections,
and help out during homework parties/office hours. We welcome anyone who has
taken CS189 to apply.

You will have the option to receive units, if you choose to serve for a
minimum number of hours per week. Also, note that we prioritize notable
academic interns when making TA recommendations to the professors.

Please find the application
[here](https://docs.google.com/forms/d/e/1FAIpQLSe068Mrjtyh2yowuEcS6_0icEnfEpimSGPTNtbl7Bp8RohPQA/viewform)

(The deadline is August 31st.)

### Anant Sahai's answer
You should review your 70 and then taking 126 will fix the gaps in your
knowledge.

You will have to spend extra time to catch up your understanding, but there is
no avoiding that.
### Followup:
Student:
Any idea when we'll hear back about specifics (schedules) of our duties?

## Taking CS170 or CS61C

2017-08-21
I am an upcoming sophomore EECS major. I am currently enrolled in CS170,
CS61B, Stat 134, and Econ 1. However, as you may have noticed, I am planning
to take CS61B concurrent with CS170. I have already seek for many opinions
that this schedule might be too difficult. Hence, I am wondering if I replace
CS61C for CS170, would that be better? Also, is 61B enough for internship
interviews (this was the only reason why I wanted to take 170 this fall).

Thanks

### Anant Sahai's answer
That's a very unusual schedule that raises multiple red flags. What does your
faculty advisor think?

  

In general, students should be taking 126 after 70, not Stat 134. Students
should be taking 170 after both 70, 61b, and 16b.

  

126 and 170 are both good theory-type intro to the upper div courses, with 126
being more relevant on the AI/ML/SP/Control/Robotics side. Both expect the
maturity from having taken the lower division though.

  

There's a reason we have faculty advising --- it is impossible to determine
what's right for anyone to take without knowing the student's context.

  

  

### Followup:
Student:
Agreed. The level of mathematical maturity required by 170 seems to be pretty
high.

## Which EECS/CS labs are working on computer vision projects?

2017-08-19
I recently did an internship where I worked on a couple interesting CV
projects (pose-estimation, augmented reality) and realized I want to pursue
this field further because it was a lot of fun. I have taken CS70 and will be
taking Math 54 next semester. I was hoping to apply to a lab where I could
learn more about CV techniques - any suggestions?

### Anant Sahai's answer
That's a very unusual schedule that raises multiple red flags. What does your
faculty advisor think?

  

In general, students should be taking 126 after 70, not Stat 134. Students
should be taking 170 after both 70, 61b, and 16b.

  

126 and 170 are both good theory-type intro to the upper div courses, with 126
being more relevant on the AI/ML/SP/Control/Robotics side. Both expect the
maturity from having taken the lower division though.

  

There's a reason we have faculty advising --- it is impossible to determine
what's right for anyone to take without knowing the student's context.

  


### Followup:
Student:
Yeah I've heard that 54+16B is an option but I've never worked with circuits
in my life so I would rather learn them well while I'm still in school.

Elad Alon:
Sure thing. If you're already planning to take 16A+16B then Math 54 will be
relatively redundant. Then again it's probably too late to get in to 16A this
semester and the foundational linear algebra is very important, so it can be
beneficial to see that material twice. You could also try self-studying the
circuits material from 16A over the winter break and jumping straight to 16B
after Math 54, but you can make that decision after seeing how comfortable you
are with the Math 54 material. Best of luck!

Student:
Thank you! I'm a junior so my plan was to take the following classes in this
order:

  

54, 16A, 16B, 189

## Should I skip EE16A and go for EE16B after taking Physics 111A?

2017-08-19
Hi all,

I'ma physics major intending to double in LSCS. I have taken both physics 89
and math 54 to cover linear algebra, and I've just finished physics 111A,
which is basically a 10 hrs/wk analog circuit building lab class with a final
project. Would you recommend that I skip EE16A, and go for EE16B? Will I need
any extra preparation?

This is the physics 111A website for your reference:

<http://instrumentationlab.berkeley.edu/labassignments>

Thank you.

### Elad Alon's answer
I'd suggest taking a look through the EE16A problems (both linear and algebra
and circuits) to make sure you're comfortable solving them, but most likely
you'll be fine. If you did well/are comfortable with 54 and 111a, at most I'd
expect you'd need to do a bit of self study from 16A and then you should be
good to go for 16B.

## Circuits portion of EE16A

2017-08-17
Hi all, I have seen multiple threads on this forum that encourage skipping
EE16A and diving straight into EE16B, if one already has Math 54 under his
belt. The downside of doing this is that one will have to self-study for the
circuits portion of EE16A before venturing into EE16B. However, most of you
(including the instructors) go on to say that there are numerous resources to
aid in closing any knowledge gaps in the circuits portion of the class. So, my
question is, can someone please post the link to said resources? (I'll be
taking EE16A this fall, and I have neither Linear Algebra nor Circuit
experience. I have, however started reviewing L.A, and would wanna start on
reviewing Circuits beforehand)

### Anant Sahai's answer
You don't need to practice circuits ahead of taking 16A. But if you want
videos, there are actually nice circuits-oriented web-accessible videos at:

<http://www.ntspress.com/publications/circuits-second-
edition/circuits-2e-faculty-resources/circuits-videos-from-berkeleys-ee-40/>

However, these are not taught in the same spirit as 16A. In fact, the spirit
is very different. So, while they can conceivably help someone prepare for 16B
in terms of circuit analysis skills assuming that person knows linear-algebra,
there are no resources that really talk about circuits the way that 16A talks
about circuits. This is because the pedagogic goals in 16A are different from
a typical "intro to circuits" class. 16A isn't an "intro to circuits" class.
It is far more accurate overall to view 16A and 16B as "pre-EECS" courses with
a strong "pre-machine-learning and pre-AI" bent.

As an incoming student who is going to be taking 16A, all you need is a solid
understanding of high-school math, humility, curiosity, an open mind, and a
willingness to work hard.

## Will the data science major be available to sophomores?

2017-08-17
Hello everyone,

I'm going to be a sophomore this fall, and I really want to major in data
science, but a friend of mine who spoke to an advisor said it most likely
wouldn't be out in the fall.

Does anyone know whether it will be out in the spring? I'm enrolled in DS 100
right now, but if there's no chance at a data science major, I'll probably
drop it and take Stat 133 instead because my backup as of now is Statistics
with a CS concentration.

Also-- I haven't taken C8 and I've heard that some get purged from the
waitlist (but not sure if that'll happen because I'm already in the class). If
it makes a difference, this is what I've taken: 61A, 61B, and Stat 134.

Any insight would be so so appreciated! My manager is trying to plan out a
work schedule and whether or not I take DS 100 makes a big difference. Thanks
in advance :)

### John DeNero's answer
I'm so sorry, but I don't think anyone really knows when the major will be
offered. One major indication of that is that there is nothing official about
it online. I know that advisors try to be as transparent as possible because
choosing a major is stressful. If I were you, I'd plan for the major not being
offered anytime soon--just to be safe. \-- Update from the data science
committee: we can't promise that the major will be approved this year, but we
are currently on track to propose an L&S major and minor to the L&S exec.
comm. this semester. If they approve it in Fall 2017, it should be available
to students as a declaration option in Spring 2018.

### Followup:
John DeNero:
This decision hasn't been made, but we're designing the program for scale, and
so I don't expect a cap.

Student:
Probably not soon because it's a new major so we don't know the exact amount
of people interested in it?

### Followup:
Student:
If you pursue a simultaneous degree, then yes, you would have to satisfy the
requirements of both colleges.

Student:
+1 for a potential timeline of when data science might be officially announced
(wondering if it is before phase 1, because the major being available in the
spring might change the potential classes I take then).

## CS 189 Drop Rate?

2017-08-15
From faculty/students' past experiences, what is the usual drop rate for CS
189 (as in, about what % of the class drops it)? I've heard that it's rather
higher than average at around 30%. Is this true? Thank you.

### Anant Sahai's answer
I expect pretty high drop rate since many people don't seem to understand that
this is an advanced-undergraduate/entry-level-graduate course. This is not an
entry-level upper-division course.

### Followup:
Anant Sahai:
I think that 154 is a great course, and the fact that it uses R instead of
Python is a small difference.

Stat 154 can't lean on the entire EECS Lower Division, but it can lean on Stat
134. This results in many differences. Stat 154 is also solidly an
    undergraduate course while 189 is also the entry-level graduate course 289A,
    and is hence arguably a few shades faster and more advanced. Basically, 189
    goes further and has less review in it. The revised 189 has more conceptual
    alignments with 154 in terms of the order in which we teach things, but 189
    goes faster and has harder homework. As a result, 189 will cover many things
    this semester that won't be touched upon in 154 --- most notably more material
    connected to neural nets. 154 seems to be more welcoming as a potential entry-
    level upper-division course overall in its structure, while 189 really needs
    students to have a level of maturity beyond what the lower-division provides.
    There are some other topics in which 154 goes into more depth.

## How useful is lecture for C106A (robotics)?

2017-08-13
I really want to take that class but 8am lecture... And Stanley is half an
hour from my place :(

### Anant Sahai's answer
The default is always to assume that lecture attendance is absolutely
mandatory and lecture is critical to understanding the material.

If you want to know more, the best thing to do is to attend the first lecture
and ask.

### Followup:
Student:
Hi there! It sounds like the students aren't able to answer your question, or
that it's fallen off their radar. I would suggest contacting the Faculty
(Ruzena Bajcsy) or the head TA for the course for their input. Sorry!

Student:
On the issue of the class timing you should contact the DSP. Berkeley has good
arrangements for students with physical/mental disabilities and hopefully you
won't be prevented from taking the class. As for getting an answer about the
actual class content, I can't provide that but I'll leave this chain
unresolved so someone can hopefully chime in.

## Are there any control theory courses that don't assume that you have prior
knowledge in EE?

2017-08-12
See title.

The reason I ask is because I am doing research in ML and using it to make
robots learn better. I see things from control theory pop up from time to time
and would like to have a more formal exposure to it. I found that the EE
department offers some courses (128 and 221A came to mind), but my EE
knowledge is pretty basic (I only took EE 16A). Do I need to take EE 16B + 120
before I would be prepared to take those courses? Or is there a course that
does not assume an EE background?

### Anant Sahai's answer
There's a reason that 16B is more than half control and ML, with another third
at least nominally related to signal processing that is also core to things
like understanding control and vision.

## Math 55 as prereq for upperdivs

2017-08-10
I want to do a cs&math double major, and was wondering how well a student with
only math 55 could do in some of the upperdivs compared to one with cs70.
Also, on the berkeley academic guide some classes such as cs 188 don't take
math 55, only cs 70. Would I be able to get into those classes with math 55?

### Instructor answer
You would be able to enroll.

### Followup:
Anant Sahai:
Take EECS126. That's the level that will serve you very well.

Student:
and i guess beyond that other upperdiv cs classes that require cs 70

### Followup:
Student:
you can still take 188, there will just be a very steep learning curve for you
compared to others who have taken 70. It is a strongly recommended to take 70
before 188 to aid in your success in the class.

## Physics class

2017-08-06
Hi,

I'm rising sophomore, intended cs major. I'm interested in ML/AI but haven't
had much exposure to these fields. I haven't taken any physics class at Cal.
I'm wondering how useful physics class (7 series) are regarding to doing ML/AI
research? (Sorry that this question might be really vague, but I haven't
figured out what I want to do. I'm looking forward to others opinion. Thank
you!)

\---------

Anon. Apologize if this edit bothers you. But I want to provide some
context/motivation that might not be your original cause.

In an interview Yaan LeCun said (Data Scientists at Work p64:
<http://www.springer.com/gp/book/9781430265986/>):

![](https://d1b10bmlvqabco.cloudfront.net/attach/hyq0br1u3kx7dg/is25wwpv21b3nn/j615o4lvcpkh/v2f8b3b30608516b140d3deee5dc242f22_b.png)

"...take all the math and physics course you can take..."

In addition, when people on reddit ask how to self-study machine learning
during AMA session, he said
(<https://www.reddit.com/r/MachineLearning/comments/25lnbt/ama_yann_lecun/>):

"It is sad to say, but unless you have taken way more math and physics courses
than the minimum required, a plain CS major from North America or Asia is not
ideal (some European programs tend to be more math-heavy).

Read math/physics textbooks, take on-line courses. Do a Master in Data
Science. NYU has one of the first ones in the country, but they are popping up
all over now....."

### Anant Sahai's answer
Advice about taking Physics courses has three different intended benefits,
relative to a hypothetical plain "computer science or math" major.

    1. Physics training boosts your generic ability to think. The traditional foundation of an engineering education, good physics courses just make you stronger.
    2. Physics training helps in modeling problems and in seeing where mathematical definitions are coming from, and helps refine a physical/mathematical intuition. In the Berkeley context, one of the reasons that we now recommend the EE16AB series to all incoming freshmen in EECS and intended CS is for hitting both (1) and (2) above. Most places have nothing like this for vanilla CS degrees. 
    3. More advanced topics in Physics like upper-division courses in classical mechanics as well as statistical mechanics bring in the connection to optimization and minimization principles. Upper-division electromagnetism courses also help one internalize the idea of dropping terms and trying to zoom in on the quantitative essence of a problem. There is a reason that EE16AB have an optimization thread running through them, but as freshmen courses, they cannot exercise the skills involved in aggressively dropping terms and caricaturing problems. (EE105 does that in the context of circuit theory.)

So, in the Berkeley context, if you're interested in AI/ML, remember the core
courses from our department: 16A, 16B, 70, 126, 127, 189. Ideally taken in
roughly that order. Outside of our department, you definitely should be taking
Math 110. It is recommended that you take Physics 7A and 7B as well (there's a
reason they're required for EECS). Ideally, you would also take upper-division
classical mechanics and statistical mechanics, but exposure to other upper-
division or graduate courses in EE can also exercise the same mental muscles.
And of course, within the department at the upper-div, we have courses like
188, 128, 106AB, as well as graduate courses like 229A that are accessible to
well prepared undergrads and extremely helpful for ML/AI type thinking.

### Followup:
Student:
The essence of this question is within another one: Do you believe you will
put in substantial effort into a course you have taken Pass/No Pass, or will
you treat it as an occasional opportunity to learn something new?

If you believe that you will put in effort into all the course material and
exercise your mental muscles regardless of the grading scheme, then it is
irrelevant whether you take it for a letter grade. On the other hand, if you
plan to put the class on your back-burner and use it to pretty-up your
transcript, or if your approach to the class is to have it "over with" but on
record, then it defeats the intellectual purpose of taking the class.

## Suggested route for EECS major interested in math

2017-08-04
I'm going to be a freshman this fall and I'm currently enrolled in CS61A,
EE16a, CS70, and Math 54. I have exempted math 1a/1b/53. I'm really interested
in math and want to take upper div math classes, but it seems that Math 54 is
a prereq for the upper div math classes like 110 and 104 and required for a
math minor which I may be interested in. Apparently, however, ee16a/b cover
almost all the material that math 54 covers. So I am asking do I still need to
take 54? If not, what sequence of math classes should I take and when should I
take them?

### Instructor answer
You do not need to take Math 54 for the EECS major. It sounds like you're
planning to take this course for math department requirements (minor, course
pre-reqs), so you will need to check with their staff.

## 189 preparation

2017-07-31
which class is more useful for prepping for 189 - stats 134 or math 53?

Also how difficult/time consuming is stats 134?

### Anant Sahai's answer
For 189, the core prep that is absolutely required is: Math 53, EE16A, EE16B,
and CS70. (Or equivalents of these --- the concepts in these courses are
leaned on very hard in 189.) On top of this, it is useful to add EECS 126
and/or EECS 127. Having these will help you concentrate on learning the actual
machine-learning parts as opposed to facing interference from having an
insufficiently intuitive grasp of probability and optimization. After those,
the next one, which is not as preferable as the ones listed above, is CS188.
This is because it provides you with an exposure to some of the relevant
ideas. Better than that would DS100. But that's not as good as 126 or 127.

### Followup:
Anant Sahai:
The entire lower-division is fair game for all upper-division courses --- the
lower division represents the background that we expect all students to
possess. (The nature of the material also has an effect. I don't expect that
we'll need to make much reference to material in say 61C, but i would have no
qualms about expecting programming maturity at that level. So, if someone
wanted to add CUDA programming as an aspect of a problem in 189, that would be
totally fair.)

Please remember also that 189 is an advanced upper-division course, it is not
an entry level upper-division course. We are going to be assuming maturity
commensurate with that. Nobody should take 189 as their first upper division
EECS department course. There are plenty of other courses that are aimed to be
entry-level upper-div: 126 and 127 (for the AI/SP/Control oriented), 170 (for
everyone), 120 (for the SP/Control/Graphics oriented), 105 (Circuits
oriented), 162 (systems programming oriented), and 100 (data science
oriented).

If you have the maturity (especially the mathematical maturity), then learning
the relevant material from the freshman-level 16AB series shouldn't be too
hard.

## Pre-EE16A course advice

2017-07-29
Hi folks, What are some of the things that I need to self-study in order to
get a leg up on EE16A next semester? (Side note: I haven't taken Math 54 yet,
which means I have zero experience with linear algebra. Is it advisable to
study Math 54 material first? If so, which areas of Math 54 should I focus on
that are of significant use in EE16A?)

### Anant Sahai's answer
16A teaches you everything linear-algebraic from first principles.

Actually, you have seen some linear algebra in high school and junior high ---
solving systems of linear equations.

$$5x + 2y + 3z = 8$$

$$2x + 2y + 3z = 8$$

$$12x - 2y + z = 0$$

That sort of thing.

If you're nervous, make sure you can do that. Review your high school
geometry, trigonometry, and basic calculus.

If you want to get ahead, and you're someone that really approaches the world
rooted in physical intuition, maybe you could review your high school physics
as it pertains to electromagnetism. The treatment in 16AB abstracts away most
of the physics, but teaches circuit analysis more from a linear algebraic
perspective that also engages with an intuition about how these quantities
behave.

16A has the same programming prereqs as 61A and also wants you to be at least
taking 61A or DS8 in parallel. It doesn't really teach you Python programming,
so if you want to review that, do so.

But relax and be willing to work hard without distractions and an open curious
mind. That's all that 16A really requires.

## Should I stay on EE16A waitlist or switch to EE16B?

2017-07-27
Sorry about another post about the EE16A/B issue, as I know there are already
a lot of them out there. But I just need some suggestions for my current
situation.

I am a rising sophomore and I have declared L&S CS and Applied Math majors. I
have taken Math 54 and 110. I enrolled in EE16A during phase 1 and am
currently at waitlist #85. I have my phase 2 tomorrow. As the instructor in
@4595 said, EE16A will not expand anymore. And as a lot of places suggest, it
is more recommended to take EE16B. Is it worth it for me to switch to EE16B
since that class is a lot less full?

### Anant Sahai's answer
It is more recommended for students who have the mathematical maturity,
clarity of thought, and linear algebra background to take EE16B. You'll get a
lot more out of it. (Of course, it is better to have taken 16AB as freshmen.
But I can understand how a student who came in as a freshman last year didn't
understand that. The freshmen coming in this year should understand this.)

Yes, the circuits material in 16A appears to span 6ish weeks of the 16A term.
However, it has to be remembered that this material is designed to be a
vehicle to help build fundamental thinking and analytic skills, as well as
mathematical and modeling maturity in freshmen students. For somebody who
already has mental muscles in these areas developed to the appropriate skill
levels, it should be much faster to self-study the material to the point that
you can successfully navigate 16B.

The basics of KCL (flow conservation in a graph) and modeling basic linear
circuit elements using linear systems of equations --- that's pretty fast
(maybe 1/3 of a page of a cheat sheet). The concept of ground is just
resolving a single degree of freedom by locking it down. Norton/Thevenin
equivalence is a simple consequence of linearity and can be viewed as
something that emerges naturally from Gaussian Elimination's step-by-step
algorithm. Series/Parallel connections of resistors is an exercise, and can be
viewed as a simplification rule to skip steps. Superposition is another simple
consequence of linearity. Golden-rule op-amps are just another element with
simple rules --- giving rise to basically three equations. (two currents are
zero and one pair of node voltages must agree). There are a couple of simple
patterns that you need to recognize. Capacitance is yet another concept that
just ties charge instead of current to voltage. Charge sharing is a simple
consequence of charge conservation. Comparators are a simple sign
nonlinearity. Everything fits on maybe 1.5 pages of a cheat sheet, if that.
There is also the very important design side of the thinking skills being
taught, and if all you've done is analysis or ad-hoc-ery in other courses,
that might provide challenges for you. But being able to do systematic design
thinking is very important to being a CS Major.

Running through the 16A circuits problems is a simple matter of practice, and
somebody who already has the mental muscles to the right place, can probably
get all of this in maybe 10-20 hours max of total investment. Certainly, that
will let you hit 16B running, and you can catch up as the 16B course is going.
If something sticks or is more challenging, then there is almost certainly
some weakness in a general-purpose mental muscle that you have been
compensating for by using other mental muscles in other courses. Good for you
to find this gap, now you can fix it and get better mental form overall.

## Will I get into ee16a?

2017-07-27
I just enrolled in ee16a and I'm on the waitlist at position 300. I'm a
junior. Is the class going to expand? Am I likely to get in?

### Instructor answer
Hello, the class will not be expanded any further due to lab space
constraints. We are at max capacity. You can use the 10% rule of thumb for
drops.

EE16a is unfortunately a Phase 1 course.

## EE 16A as a "pre-req" for CS 70

2017-07-27
I am aware that the CS department recommends taking EE 16A before CS 70, and
choosing to take EE 16A over Math 54. However, it seems like this
recommendation is more grounded in "mathematical maturity" vs. actual content
relevance and concrete preparation for CS 70.

I am curious to know why EE 16A is preferred over math 54, and how the
material specifically more closely aligns with CS 70? I am trying to decide if
it is worth it to take EE 16A before CS 70, and would love to understand more
about how they are more related to each other than math 54 and cs 70 would be.
(I completed math 1b last semester and will be a rising sophomore)

### Anant Sahai's answer
There are recursive algorithms in 16A and 16B, and they are talked about in a
way that helps you think about them better. 16A and 16B are largely about
teaching you how to think, as is 70. The focus on modeling and components of
systematic thinking is stronger in 16AB, and the course sequence was designed
to build these up. Remember, one of the main creators of the 16 sequence,
Prof. Gireeja Ranade, had experience guest teaching in 70 before she came up
with the ideas for 16. There are many subtle linkages that might not be
visible to students. (And that's fine --- we just want you to get stronger. We
don't need you to understand why you are getting stronger.) Strictly content
wise, there is a connection between polynomial material in 16B with polynomial
material in 70, as well as between least-squares material across 16A and 70.

## EE 16A + EE 127 for L&S CS major requirements

2017-07-23
In regard to the EE 16A/B requirement (for L&S CS students who entered after
Fall 2017), would it be acceptable to take EE 16A + EE 127 to fulfill the
requirement? It seems like a comparable option to EE 16A + Math 110, which I
have heard was also (unofficially) acceptable in the past.

### Instructor answer
Unfortunately you have to take EE16A and EE16B. You should totally take EE127
if it interests you though!!

### Followup:
Anant Sahai:
Having 110 will let you catch up faster with material that was introduced and
discussed in 16A and 16B. 16AB are freshman courses after all. But there is a
substantial amount of "pre-machine-learning" in 16AB --- not just specific
topics like linear regression, polynomial fitting, system identification,
singular value decompositions, PCA, and k-means, but also a way of thinking in
terms of casting problems as optimizations, etc.

Student:
+1

Student:
How exactly will the Fall 2017 CS189 depend on EE16B? I am enrolled in CS189
for the fall semester, so should I be concerned if I haven't taken EE16B? I
have completed all the other prerequisites (Math 53, CS70, CS61ABC) and have a
strong linear algebra background (Math 54, 110).

## EE126 vs CS189

2017-07-19
Hello all,

Next semester I'm planning on taking 170, 188, a P/NP Breadth, and either 189
or 126. Anyone have any advice on whether 189 with the other three courses
would be too much or the relative workloads of 189 and 126?

### Anant Sahai's answer
Students who are fairly certain that they want to understand machine learning
are better served by taking 126 first and then 189 later. Students who are
certain that they want to understand machine learning are best served by
taking 126 and 127 before taking 189.

### Followup:
Student:
+1, the end of CS188 is an intro to Machine Learning which helps transition
into 189. Taking ee126 with CS188 is pretty nice because you'll get through
all the probability you need for 188 really early on

Student:
+1

## CS 189 vs 289A

2017-07-16
I have seen that this class is cross-listed for grad students. Does that mean
the 2 classes are the same? Is there any benefit to getting instructor
permission for 289A, or is it pretty much equivalent to go through 189?

### Instructor answer
289A is for grad students, 189 is for undergrads. If an undergrad wants to do
the grad project, they are welcome to do so. Grad students don't have a
choice.

Undergrads have not in the past been allowed to take 289A unless they were
already accepted into the 5th year masters' program and wanted to use it
towards the completion of their graduate degree requirements.

## EE16A Requirement?

2017-07-03
For a student that entered Berkeley in fall 2015 (so pre fall 2017, but post
the 3.0 policy), is EE16A still a requirement to graduate in LSCS if Math 54
was already taken? There was a post earlier about the new 16A policy, but it
seems to be geared towards EECS students.

### Instructor answer
https://eecs.berkeley.edu/resources/undergrads/cs/degree-reqs-lowerdiv

### Followup:
Elad Alon:
If you have already taken Math 54 and feel comfortable with that material, I
would very strongly recommend planning to take EE16B (after either self-
studying the circuits portion of 16A, or officially enrolling in EECS 47D for
that purpose) to fulfill your requirement.

Student:
Please see the link Halley provided. It has the lower-div requirements for CS.

Student:
The page is titled "CS Major Upper Division Degree Requirements." Since ee16a
is not an upper division course, I don't see why it would be on this page

## When to take lower divs (EE16a)?

2017-06-25
Is there any official policy that requires L&S/CS majors to finish their lower
div requirements before a certain time? Also, I'm considering putting off
EE16a for a good while so that I can take an upper div during my sophomore
spring semester...thoughts?

### Instructor answer
Anant: You really should take all your lower divs before taking upper divs.
Upper-div courses are allowed to freely assume knowledge of lower-div
material.

Elad: Following up on Anant's point above, I would strongly recommend against
delaying 16A (and similarly, EE16B). These classes were not only specifically
developed to be of greatest impact early in your undergraduate career (i.e.,
as a freshman), but are targeted to help you learn how to think about problems
in a way that will be extremely useful/effective in many other classes
(including upper-divs).

Nicole: Additionally, It can be difficult for LSCS students to enroll in this
course. Delaying it to a final semester is a big risk if you're unable to get
in.

## Did 194 Cryptography get cancelled?

2017-06-24
It's not listed on the CS Fall 2017 courses anymore.

### Satish Rao's answer
Yes. We had to shuffle the schedule due to various circumstances. Apologies.

## Prep for EE126 over the summer

2017-06-14
Good morning Piazza,

I transferred to Cal last fall from a community college. I am an Applied Math
major with a focus in CS. Relevant courses I have taken are Math54, CS61AB &
70\. I plan on enrolling in EE126 in the fall because I found the probability
section of 70 to be quite interesting and I plan on taking CS189 next Spring.
I will also be taking Math 110 and Math 104 in the fall.

I realize 16a & b are pre-reqs for 126 but I do not have extra units to use
for those courses. If there are some p-sets/ readings to do on information
relevant to 126 from 16a & b, I have plenty of free time over the summer to do
so. Do any students of 126 or staff have resources for this endeavor? Or any
other suggestions for preparing for 126 without direct knowledge from 16a & b?

Removed that paragraph since 16A & B are not pre-reqs for EE126.

Thanks for your time.

### Anant Sahai's answer
An Applied Math major I am assuming has also taken Math 53 which is important
and relevant. Someone with 70 under their belt should be able to get through
126 if they are willing to work hard.

If you want to, just follow along with 16A as it is offered in the summer and
do the homeworks.

### Followup:
Student:
Thank you for your insight, professor. I still believe that the material
posted under 6.041 could be helpful preparation for 126.

Anant Sahai:
126 in its current form assumes 70 and is *significantly* more challenging
that 6.041.

Student:
I also noticed the authors of the main textbook are MIT professors but wasn't
sure how to find the MIT course number that corresponded to EE126. I'm gonna
get started on that edX ASAP. Thanks Jason!

## Info 159 Taken Concurrently with CS70?

2017-06-06
I see that CS70 is a prerequisite for Info 159. What if taken concurrently?
Would that be okay? I emailed the professor twice but he hasn't gotten back to
me.

### Anant Sahai's answer
In general, a good rule of thumb is that any brand new course is going to end
up leaning on its prerequisites very heavily and probably end up assuming
more. This is because the default position for essentially every faculty
member is making a course that is way too hard.

## Stat 134 for CS 70?

2017-06-02
Hi, I was wondering if people would recommend taking Stat 134 before 70? I
have read through several threads and have seen different responses. Either
people think that it is helpful for mastery, or people think it is too in
depth to be necessary and that the probability taught in 70 is different
enough that it is not worth it. Thanks for the help!

### Anant Sahai's answer
The strong recommendation for CS students is to take 126 after 70 instead of
taking Stat 134. EECS 126 leans on 70 more and teaches you more than 134 can
without assuming 70. EE16A and EE16B should be sufficient mathematical
maturity preparation to engage successfully with 70. Seeing specific material
before is not generally a good strategy for preparing for a course. In the
absence of suitable preparation, it can be actively harmful.

That said, if it is a matter of helping conquer apprehension regarding
probability after having taken 16A and 16B (for the prerequisite mathematical
maturity), then sitting in on Stat 134 and doing the homeworks is fine. I
think that just sitting-in on courses, attending lectures and discussions, and
doing problems to learn without any fear at all can be helpful for people.
Everyone faces a different mix of challenges --- for some folks, it is the
stress of new material in the face of a GPA-threshold that degrades
performance. Finding ways to overcome the stress is useful, and if that means
sitting-in on a course, then sit in on a course. The important thing is just
to not confuse things. Preparation is preparation. Stress is stress. These are
different things.

### Followup:
Student:
I took philosophy 140B (deals with computability and incompleteness) as a
breadth class after 70 and was able to follow it well as it delved much deeper
into the topic. (Sometimes painfully deep :) ) From Prof Mancosu, I heard 140A
also delves equally deep into its topics, so I'd recommend it after 70 if
you're interested. tl;dr don't take Phil 140AB before 70 imo

Student:
Which is one of the easiest parts of CS70 imo

Student:
I haven't taken those courses, but I believe that the overlap material between
the philosophy department and CS70 is only on propositional logic, which 70
spends a week or less on.

## CS70 or CS61C

2017-06-02
Should I take CS70 or CS61C in the fall?

### Instructor answer
This is very personal and depends on what you want. CS 70 is needed to declare
CS whereas 61c is not. Re: interviews it depends on what you're interviewing
for.

### Followup:
Student:
It depends on what upper-divs you're more interested in. If they're ones with
61C as a prereq, then you may want to take 61C earlier.

Likewise, for interviews: it depends on what sorts of positions you're
interviewing for.

Student:
I've found 61c is more useful for an internship

Student:
61c imo is more useful for interviews. 70 is useless for this.

Student:
I can't think of any common interview questions that test 70 knowledge

Student:
Not really. 70 is also used more on interviews which will be useful during
recruiting season for internships. 61C is useful, but if you had to choose
between 61C and 70 first, id do 70.

### Followup:
Anant Sahai:
This is what faculty advising is for.

Student:
They lead to fairly different subfields of CS. So again: this is much too
dependent on the person, in terms of what your interests are, what classes you
plan on taking, what sorts of jobs you intend to apply for, et cetera.

## CS70 Previous Semester Discussion Solutions

2017-05-31
I'm planning on taking CS70 this summer. I'm currently trying to learn as much
of the material as possible before the session starts.

I can't find the solutions to some of the discussions and homeworks from CS70
Fall 2016 and Fall 2014. The link seems to be broken for Fall 2016:
<https://inst.eecs.berkeley.edu/~cs70/fa16/static/discussions/dis01asol.pdf>
and I can't find links to any solutions for Fall 2014.

If anyone knows where I can get the solutions or happens to have a copy of the
solutions, that would help out a lot. Thanks!

### Anant Sahai's answer
This sort of thing has come up repeatedly, and I think that having a faculty
perspective might be helpful for students.

I understand how tempting it is to think that it might be reasonable to
prepare for a course by reading up on the problems from a previous semester's
offering of that course. After all, what could possibly be a better
preparation?

However, this perspective is dangerously wrong. First, reading problems and
solutions is generally a horrible idea. It has none of the benefits of
actually doing problems. Second, it has all the harms of interfering with your
ability to learn how to reason about something that you haven't seen before.
Third, it creates opportunities for you to propagate bad form and cement
distortions that arise from conceptual gaps --- this is because instead of
learning the concepts, skills, and ways of thinking that we are teaching you,
it is possible to simply learn how to do these particular problems. Because
you have no guidance or study group or any other resource that is normal
during the semester, there is nothing to stop this. Then, when you experience
the course itself, this half-bad understanding will actually seem to carry you
through. It is far better for you to actually experience challenge that points
out what you don't understand so that you can actually understand.

So, what should you do if you want to be proactive and prepare ahead of taking
a course? First, make sure you have the prereqs. That should go without
saying. After that, try your hand at material that exercises the same basic
underlying skills but is fundamentally different. For 70, that would be doing
things like going through every problem in the textbook by Rosen. Or reading
How To Prove It by Vellemen and doing the exercises within that. This will
avoid interfering with the ability of the actual course 70 from helping you
while still giving you a strong leg up.

### Followup:
Student:
<http://alvinwan.com/cs70/sp16/> is also a good resource!

Student:
You can always use the [old
midterms](https://hkn.eecs.berkeley.edu/exams/course/cs/70) for practice
problems with solutions.

## Math54 and EE16A allowed to complete LSCS major?

2017-05-28
I see a lot of threads and posts about EE16AB and Math54 replacement/option,
but I also have heard lots of different things about this. Like someone told
me that Math54 and EE16A are no longer completely different courses and
credits may not be given for EE16A after completing Math54 (and vise versa)

Allow me to be specific to my personal situation, but can I take Math54 and
EE16A to complete LSCS major req? I don't have to take EE16B if I take Math54
and EE16A, correct?

I am junior transfer (declared CS), and completed the first year at UC
Berkeley. I am taking a year off, and will come back and graduate in 2019.

Thank you in advance for your help.

### Instructor answer
Edit: We have some new information, so I am editing Professor Sahai's response
here. The L&S Executive committee has just approved the following changes to
the L&S program:

Students entering Fall 17 or later will take:

  * EE 16 A or Math 54, AND
  * EE 16 B

*Please note that it is strongly preferred that students take EE 16A and EE 16B.*

For current students, the options we told you about in @3372 are still true.
As Professor Sahai notes, EE 16A and B are preferred.

### Followup:
Anant Sahai:
The basic perspective is that the department is not unreasonable or unfair.
There is no summer offering of 16B this summer since the department is just
getting 16A to work this summer. The point of the policy is to not have
students feel that their plans are being changed out from under them, even if
the underlying change is due to a bug fix.

After you take 16A in the summer, you can evaluate for yourself how your plans
might change.

Student:
Not an answer to the CS major question, but I would be happy to help you run
through EE16B material if you don't get a chance to take the course. Control
theory, linear algebra, and the frequency domain are really important and I
would hate for you to not get a chance to learn the material due to financial
reasons.

Perhaps then it'd be viable to squeeze EE16B into one of your later semesters
and hopefully have it be lighter due to already understanding a portion of the
material.

Send me an email at [nzhang32@berkeley.edu](mailto:nzhang32@berkeley.edu) if
you're interested.

### Followup:
Student:
It should be approved @3372, but is very redundant. Just depends on if you
care or not.

Another option is to take EECS 47D, and then EE 16B, which is slightly more
work, but you will learn more.

### Followup:
Student:
That would be EECS 47D, should be available this fall.

### Followup:
Student:
Hi there- it doesn't matter if you take a year off; it matters when you
started.

Student:
Thanks Nathan, I greatly appreciate that. But to be honest, I have no idea of
where I can put the time to study EE16B next two years. I am taking 2
technicals this summer so I already started working on one of them. Right
after summer I am leaving to my country. After coming back I will be doing
like CS170, 162, 188 and upper History or Music Theory or something like that
on both Fall and Spring, while I am working as a part time (tutoring over
Skype).

But I will save your email and will let you know when I find time for it. I
really appreciate your offer and hate that I can't take it now. Thanks again,
Nathan!

Student:
I'll make the same offer as I did to an above poster. Not an answer to the CS
major question, but I would be happy to help you run through EE16B material if
you don't get a chance to take the course. Control theory, linear algebra, and
the frequency domain are really important and I would hate for you to not get
a chance to learn the material due to financial reasons.

Perhaps then it'd be viable to squeeze EE16B into one of your later semesters
and hopefully have it be lighter due to already understanding a portion of the
material.

Send me an email at [nzhang32@berkeley.edu](mailto:nzhang32@berkeley.edu) if
you're interested.

Since I'm no longer a student at Berkeley (and no longer in the area), this
would be done online, but I am willing to do this for free since money really
isn't an issue for me.

### Followup:
Anant Sahai:
There are multiple reasons.

EE16A has a core mission to make sure that students learn how to "think
rigorously like engineers" (where we have a very EECSy-perspective on what
that means). The entire treatment of material, style of homeworks, etc. is
designed to allow students who take it seriously to sincerely engage with
conceptual and skill gaps that they have and to overcome them on this journey.
This is simply not one of the design objectives for Math 54.

EE16A takes it for granted that students live in a world that has computers in
it and that software tools should be used to help students connect with the
ideas. Practically every week, there is something that forces you to connect
with ideas in the course using a computer. This facilitates students being
able to leverage their computational intuition to help strengthen their
mathematical intuition. This is not something that Math 54 cares about at all
and so is a major lost learning opportunity, especially for a student
interested in CS.

EE16A has labs in which you get to see the linear-algebraic concepts that you
are learning actually pay off in an application. This allows students to
connect physical intuition to further strengthen and reinforce their
mathematical intuition. Math 54 has no labs and does not usually try to engage
strongly with physical intuition or vice-versa, use mathematical intuition to
build physical intuition.

EE16A is part of a two semester sequence with EE16B --- so it knows that
students will get more deeply familiar with ideas as they are developed and
encountered over these two semesters. Consequently, EE16A can afford to reduce
the seeming coverage of certain linear-algebraic material in exchange for
actually deepening students core thinking skills. The circuits module in 16A
is really about teaching design and problem modeling and decomposition skills,
while also providing much deeper groundings for lots of core linear-algebraic
and mathematical ways of thinking. (While, yes, also teaching students about a
complementary perspective on what information processing is and how it engages
with the physical world.) Math 54 isn't able to spend time on building those
mental muscles because it has other things that must be covered. By the time
students finish EE16B, the treatment of the material has gone beyond Math 54
in multiple dimensions.

In the end, you have to remember that certain key faculty members and several
of the key TAs who shaped 16A had come directly from having taught 70 before.
They had seen exactly the kinds of mental-muscle weaknesses that had caused
students to shed tears in 70. (It's not the material in 70 that is ever the
real cause of student difficulty --- it's almost always thinking.) And 16AB
were explicitly designed to strengthen those muscles while also building
broader conceptual foundations for machine learning, robotics, circuit design,
vision, AI, etc. Math 54 wasn't designed with any of this in mind. It serves a
wide variety of engineering and physical science departments and focuses on
teaching a set of material.

Can students go from Math 54 and do well in 70? Sure they can. Lots of people
have. Will students who went through 16AB not have to work in 70? Nope! 70 is
going to be work because it takes work to learn new material and internalize
it, along with leveling up certain ways of thinking as well. But the
recommended path of 16A, 16B, and then 70 is recommended for a reason.

## Old Grading Guidelines

2017-05-25
I noticed that the grading guidelines were just updated this year, and they
are more generous than before. For reference, does anyone remember what the
previous guidelines were?

IIRC, the average GPA for a lower div was recommended to be a 2.7, with a
distribution something like 17% A's, 55% B's, 20% C's, 10% D's, 3% F's. And
the average GPA for an upper div was recommended to be a 3.0, with a
distribution something like 25% A's, 60% B's, 10% C's, 5% D's, 0% F's.

Just curious to compare, since this is the first time the guidelines have been
update since 1989.

### Elad Alon's answer
**@ John DeNero** **@ Elad Alon**

  

Elad: I don't happen to recall the exact numbers from the previous policy, but
the numbers quoted in the original post sound about right. The reason for the
change in the average target was largely driven by more accurately reflecting
actual practice, and the wider range of grades than in the past was also to
reflect actual variability across courses/populations, as well as to allow
flexibility as our degree programs become more or less selective.

### Followup:
Student:
Yup, "ratified at the faculty meeting of March 11, 1976, and updated in 1989
and 2017." Only the second time it's changed in the last 30 years!

### Followup:
Elad Alon:
Please see my response on this above.

## CS program

2017-08-09
Is it true that getting into Berkeley AI/ML CS program is more competitive
than less-popular-field CS program, like computational biology, graphics in
Berkeley?

### Anant Sahai's answer
Getting into Berkeley for a PhD is incredibly challenging. There is a very
high absolute quality bar that is applied for graduate students. This bar is
not something that really varies by much across the department. However, in
areas (like AI/ML) where there are lots of applicants that cross the very high
quality bar, hard choices have to be made because there is limited faculty
advising bandwidth. In general, these choices are made on the basis of "fit"
and depend significantly on the specific mix of interests and needs of the
faculty at the time admissions decisions are made. From the perspective of a
student applicant, this can appear arbitrary, and to an extent, it is. After
all, students' underlying research interests and inclinations tend to be broad
and flexible and a snapshot taken in a November application doesn't
necessarily predict all that well what they really want to do the next
September when they start working on potential research projects. Oh well.

That said, you should never apply to an area within which you would not want
to do research. This means potentially doing research with multiple faculty
who associate with the area, not what you might think the area means based on
its name. Similarly, you should never apply to an area within which you would
not clearly demonstrate that you are a candidate that meets the very high
quality bar. (Talk to faculty in office hours if you want to get a sense for
what that means on an area by area basis.)

### Followup:
Student:
see above

## Prereqs

2017-05-21
Hello,

Are prereqs strictly enforced? I.e will I be kicked out of a class, such as
170, if I don't complete a prereq like 70 until later?

Thanks

### Anant Sahai's answer
Getting into Berkeley for a PhD is incredibly challenging. There is a very
high absolute quality bar that is applied for graduate students. This bar is
not something that really varies by much across the department. However, in
areas (like AI/ML) where there are lots of applicants that cross the very high
quality bar, hard choices have to be made because there is limited faculty
advising bandwidth. In general, these choices are made on the basis of "fit"
and depend significantly on the specific mix of interests and needs of the
faculty at the time admissions decisions are made. From the perspective of a
student applicant, this can appear arbitrary, and to an extent, it is. After
all, students' underlying research interests and inclinations tend to be broad
and flexible and a snapshot taken in a November application doesn't
necessarily predict all that well what they really want to do the next
September when they start working on potential research projects. Oh well.

That said, you should never apply to an area within which you would not want
to do research. This means potentially doing research with multiple faculty
who associate with the area, not what you might think the area means based on
its name. Similarly, you should never apply to an area within which you would
not clearly demonstrate that you are a candidate that meets the very high
quality bar. (Talk to faculty in office hours if you want to get a sense for
what that means on an area by area basis.)
### Followup:
Anant Sahai:
The easiest thing to do is to look at 70's HW and exams --- can you do
everything easily? If so, it is probably not worth worrying about the prereq
requirement. However, in our experience, very very few students actually have
70-level understanding without taking 70. (You can't just look at the course
description and an abbreviated syllabus. For a lower-division course in
particular, there is a lot more going on in terms of maturity level and
perspectives than can ever be described concisely on any syllabus.)

Every instructor has their own perspective on how those without prereqs should
act. I know that mine is pretty simple. If anyone wants to take a course
without having had a prereq,

    1. They should agree that they will not ask questions in class or lab or discussion without having had a private conversation beforehand with the TA and/or Prof to make sure that the source of their question isn't indeed coming from a subtle or not-so-subtle gap in their background. 
    2. They should further agree not to take a slot in office hours unless nobody else is waiting. For the same reason above. Piazza should be viewed as a kind of office hours in this regard. In email, they should say "only answer if you have the time."
    3. They should disclose this fact early to any study group that they might be considering being a part of. 

Basically, someone without the prereqs shouldn't inadvertently cause a burden
on others including course staff, and should err on the side of caution in
this regard. On the flip side, someone who has taken the appropriate prereqs
should feel free to ask when they don't understand something or wonder
something. It is to protect the ability of those who legitimately have
questions that I have this perspective.

### Followup:
Student:
Did you have CS experience beforehand aside from 61a?

### Followup:
Student:
I agree that 61B is the strongest prereq to 170, and I think that the only
compelling reason to do 170 before finishing 70 is if OP is in a rush to ace
those CS internship interviews.

Student:
Last semester, CS70 spent two weeks on teaching writing proofs, and then also
the rest of the semester on actually writing proofs. Way more than a week.

And for most students, they will not have encountered proof writing in other
courses they take before CS170. Sure, this is YMMV, but this isn't from the
two classes being independent, but from students being able to learn the
material elsewhere; this doesn't make 70 less of a prereq.

Anant Sahai:
Yes, the two closest points of contact between 70 and 170 are writing proofs
and the idea of reductions (which is hit by combinatorial proofs in 70).
Graphs (depending on the 70 semester) are another point of contact as is
modulo arithmetic. The FFT material in 170 implicitly leans on 16B. However,
there is no doubt that the most direct prerequisite for 170 is actually 61B
while the most natural follow-on course for 70 is 126. However, what most
people really need from 70 is the boost from sophomore mathematical and
problem-decomposition maturity to beginning upper-division maturity. It's not
enough to be told about X in one week. You have to build the mental muscles by
doing it for a semester. What exactly you do to build those muscles matters
far less.

To first order, the principal educational components of the six EECS lower-
division courses are about building raw stamina, mathematical muscles,
modeling and problem-decomposition muscles, and programming/debugging muscles.
While also giving students exposure to key ideas, techniques, tools and
context along the way. For someone who has the stamina and those muscles, the
specific ideas, techniques, tools and context should be quite easy to acquire.
(e.g. at triple speed or faster. So instead of spending 20hrs/week, just 6-7
hrs --- skip discussion and finish HW/projects in 3-4 hrs per week.) For the
most part, all the real challenge and time in the lower-division comes from
needing to strengthen the mental muscles and build up stamina.

Student:
I don't think 70 has a monopoly on learning proof-writing techniques, and
proof writing techniques were at most a week's worth of learning as I recall.
Again, YMMV and I know that many people including you disagree with me, but I
wanted to show that a differing opinion does exist.

Student:
Er, you don't recall writing proofs in 170?

## Double Major logistics

2017-05-19
I am currently an EECS major, but am also thinking about double majoring in
math, as I find the subject both important and interesting. However, since
math is in the college of sciences, do I have to fulfill the breath
requirements for the college of sciences as well? Is this the same for a
minor?

### Anant Sahai's answer
Just take the Math courses you want to take. Math courses are incredibly
valuable. And the Math major upper div requirements are well thought out. So
following those is a pretty good idea. You'll get a great education.

  

But essentially nobody in the real world cares about whether you majored in
Math or double majored in Math. Not grad schools, not employers, not
prospective spouses, not your neighbors, nobody. Maybe there's some discount
coupon somewhere, who knows. But you get the idea. Education isn't collecting
badges.

  

## EE16A Preparation

2017-05-19
I'm taking EE16A next semester with no experience in linear algebra or
circuits. What are some ways I could prepare myself for the class over the
summer?

### Anant Sahai's answer
Understand basic calculus and know basic Python programming at the level that
taking 61a or DS8 concurrently would provide. EE16A is aimed at freshmen and
so you should never hesitate to have a conversation with a TA about your
preparation. The course staff understands that different folks come in with
different backgrounds and you're not compared with each other. Paying
attention and being willing to work hard every week is what the course
demands.

### Followup:
Student:
All I meant by "up against" is that you are in the same class as people who
might be more familiar/comfortable with the concepts. I fully agree that it
provides a lot of resources for you to ask questions/practice concepts/etc,
but if you have the time over the summer then it can still be helpful to
familiarize yourself with whatever section you feel might be the hardest for
you (LA or circuits). It's a very time consuming class, and if you are taking
two other techs with it it can often be hard to find time to go to as many
office hours as you maybe should to achieve full comprehension.

Anant Sahai:
The grading in 16A is designed to not penalize students who come in at the
designed level --- that is folks who have absolutely no background in linear
algebra besides that implied by high school math. You're not "up against"
anyone in the 16 series.

The 16 series is designed to be inclusive in character --- you are encouraged
to approach your TA or come to faculty office hours if you have a question
about background stuff. We assume you are willing to work hard and will help
you to do what needs to be done to patch any background holes you might have.

Like 61A, the main purpose of the 16 series is to get you to think about
things in better ways. Some of what is perceived as difficulty in 16 is just
the process of students learning how to think better. In some cases, having to
unlearn certain bad "micro-habits of thought." Nothing in the 16 series is
supposed to be "tricky" in nature. However, many things are designed to help
students develop the mental counterparts of "good form" in
sports/athleticism/yoga/dance/singing/etc. Cultivating an attitude of being
open to learning and willing to adjust your mental form is far more helpful
than any specific review of any specific topic.

Student:
It assumes no knowledge yeah, but you're still up against people who have a
much more solid grounding in all these things so I'd say you're certainly at a
disadvantage.

Student:
EE16A assumes no knowledge of Math 54 concepts / circuits concepts. However, a
lot of your peers in the class will have already taken Math 54, which can make
it feel like you are behind during the first few weeks of the class, so maybe
spend a bit of time learning some Linear Algebra so you don't feel overwhelmed
in the beginning weeks. The circuits section can be painful for a lot of
people (especially if you don't have a background in it, like me). However,
there a lot of resources they provide to learn the circuits portion. If you
were to study one portion over the summer, I would personally say to focus on
the circuits portion as I found it to be the most difficult part of the class
(granted, I took Math 54 beforehand, so the linear algebra portion was almost
all review for me)

Student:
Beg to disagree. A solid foundation in the physics of circuits would have been
immensely helpful when I took it. The 16 series works just fine as a freshman
class because most freshmen come in with a solid physics background. If you're
like me and came from a school weak there, I'd really recommend studying up on
it. Do Khan Academy if nothing else.

## Is CS 70 and MATH 54 enough math preparation for CS 189?

2017-05-18
For the probability part, is CS 70 enough, or is taking EECS 126, STAT 134 or
STAT 140 recommended?

For the linear algebra part, is MATH 54 enough, or is taking MATH 110
recommended?

### Anant Sahai's answer
I strongly recommend as a minimum an EE16B level understanding of linear
algebra, a mastery of probability at the level of 70, and mastery of Math 53
level understanding of multivariable calculus. For many students, that level
of probability understanding will practically require taking something like
126 to adequately consolidate and strengthen their understanding. 126 is the
recommended probability course for all EECS and LSCS students because it
builds on 70.

### Followup:
Student:
Thx!

### Followup:
Anant Sahai:
As a point of clarification, 16B does more linear algebra than most offerings
of Math 54. In particular, the SVD is covered as well as PCA. This in
particular is quite useful for 189.

Student:
Thx!

Student:
Yes it is enough, however math 110 will help. It's all up to you! :)

Student:
Thx! So is MATH 54 enough for CS 189?

Student:
I don't think so. EE16A and EE16B together are supposed to cover Math 54 (as
well as applications with linear algebra to circuitry). Math 110 is very
different as its more theoretical as an upper div math course.

## 189 Discussion Section

2017-05-16
Hi, how am I meant to enroll in a discussion for CS189? I've tried all the
ways that I could figure out but haven't been able to enroll in a section. I
was able to enroll in the lecture with the "dummy section" but I would imagine
that I also need to enroll in an actual discussion section. Thanks!

### Anant Sahai's answer
Just wait. No rush.

## Taking CS70 and EE127 concurrently

2017-05-04
Is this manageable or is this a bad idea? The academic guide lists EE16A/B as
a prerequisite, which I've filled out, but beyond that I've taken no other
math courses, so I'm wondering if this is truly the recommended prerequisite
or if it's more like a "barely sufficient"  
prerequisite.

### Anant Sahai's answer
The mathematical maturity from having completed CS70 can be assumed in any
upper-division EECS course without really calling attention to it --- the
entire lower division can be viewed as a silent prereq for any upper division
course. That said, 127 does lean on mathematical maturity.

## No upper divs sophomore year?

2017-05-04
Hi,

I'm a rising sophomore originally planning to hold off CS70 until spring '18
in order to gain mathematical maturity via Math 54. I got an A in 1A and am
expecting another A in 1B, but I don't know if this is enough. However, this
might result in no upper divs during sophomore year. Is this a significant
disadvantage when applying to summer internships?

Also, what is the viability of taking CS61C and CS70 together as someone whose
only programming experience was 61A + B? Is it viable then to take an upper
div like 188 along with 70? I need a B+ or higher to declare.

Thanks in advance.

### Anant Sahai's answer
The mathematical maturity from having completed CS70 can be assumed in any
upper-division EECS course without really calling attention to it --- the
entire lower division can be viewed as a silent prereq for any upper division
course. That said, 127 does lean on mathematical maturity.
### Followup:
Student:
Sorry, the first sentence should be "Taking CS 61C with CS 70 seems like a lot
of work."

### Followup:
Anant Sahai:
It's good to remember that the people who designed and built 16AB were deeply
familiar with 70 and 16AB were consciously designed to lead up to it in terms
of the maturity and thinking skills acquired. This wasn't just true on the
faculty side, many key early TAs also came with that background. Those of us
who had taught 70 had had our fill of student tears.

Student:
I agree!!! I am only in EE16a right now and I wish I had taken it before I
took CS70. There is a certain level of maturity in the way you write your
solutions and in the way you must approach the problems that EE16a builds. I
believe that CS70 homework would not have been as daunting if I had taken
EE16a instead of Math 54.

## What is the best preparation course for CS70?

2017-05-02
When it come to building the mathematical maturity required for CS70, should I
take Math 54 or EE16A (or maybe both at once, but that's probably a bad idea)?
I understand taking the EE16A + EE16B is recommended, but I'd have to declare
before that would be possible. And so as far as the pure mathematical
preparation of these courses, which would be more useful for CS70?

### Anant Sahai's answer
From my experience teaching 70, the issue is mathematical maturity for most
students, not any specific topic per se. Even mathematical maturity isn't
entirely about what many of you might think of as "math" (namely something to
do with numbers or variables or shapes). EE16AB are designed to help build
this and *everything* works to help do that, while also teaching you important
foundations for the upper division and beyond. Specific topics in 16B do show
up in 70 itself, but that's not the main benefit. The standard recommendation
stands: take 16ab. If you are in a rush, start with 16a and see how you feel.

  

Mathematical maturity is like athletic conditioning. Not everyone comes in at
the same level, but everyone can get themselves to where they need to be.

## Can EECS take Physics 5B instead of 7B?

2017-05-01
see title

### Instructor answer
Whatever the official answer is, if you also take the Physics 5 lab (which
they separated out into a separate course for some reason), then you can
almost certainly petition to have it count if it does not count already. If
you don't take the lab, then it shouldn't count.

Edit: Physics 5B does not automatically apply in place of Physics 7B. As
professor Sahai said, you do have the option of petitioning.

## Fall: cs61b + cs70 / Spring: cs61c + ee16a or Fall: cs61b + ee16a / Spring:
cs61c + cs 70

2017-04-30
Hello, I am currently an upcoming sophomore for the 2017-18 academic year that
is intending to major in LSCS. I am currently agonizing over whether or not to
just take the two remaining pre-requsites to know if I can get into the major
sooner, or if I am better off with the safer option of spreading out the two
pre-requisites over the next two semesters. I have been reading posts about
ee16a vs cs70 but I have not been able to relieve my anxiety over which option
would be the best option for me.

I have read that taking ee16a before cs70 would be a better option as ee16a
would help me build mathematical maturity that cs70 requires to be successful
with the fact that a lot of people stated that they found ee16a much more
easier than cs70 and I have more opportunity to get a better grade in cs61b
rather than split my focus between two very important classes. However, I have
also heard that cs61b with cs70 is the much more manageable option than cs61c
and that ee16b is much better taken right after 16a as the topics are very
important and that I might forget some of them if I put a semester in between.
Also, taking ee16a earlier than cs70 would be a waste of units if I end up not
getting into the major. It's killing me. >_<

Some important facts about me: I do not have the best time-management or study
skills but I do put in the work and time when I need to. I believe that I am
between an A-/B+ in both cs61a and math 1b but those could go up to A's if I
do well on finals (which I feel somewhat confident in). However, I do feel a
little bit weak in the math department so that could be a factor. Oh and if it
helps in any way, I do have an interest in computer hardware and am able to
build one but I do not know if that helps in cs61c or not.

I will be thankful for any input and feedback I can gain on which of the two
paths would be the most efficient one, or if I shouldn't worry to much and
just let my heart be my guiding key (I'm sorry). Thank you so much for your
time and consideration

### Anant Sahai's answer
Taking 70 when you haven't gotten to "sophomore mathematical maturity" is a
bad idea if your goal is doing well and learning the material.

## CS70 Study Strategies

2017-04-30
Can someone recommend strategies to excel in CS 70? Reading lecture notes in
advance yes but what else?

### Anant Sahai's answer
I'd be curious to hear the instructor's perspective **@ Satish Rao** **@ Anant
Sahai**

The student answer is very good. The following strategy is the basic one that
works: (In order)

Ahead of lecture: PRINT OUT THE NOTES. Read them and use a pencil to make
marks on the notes. Put question marks where you don't understand or are
confused. Write questions in the margins. If you are understanding, try to
work out the examples and proofs on a separate piece of paper after reading
them. Don't copy, but just reconstruct after reading. But it's ok if you don't
understand something. This is still before lecture after all.

ATTEND LECTURE AND PAY ATTENTION: ask questions about the things that you
don't understand. Take notes using pencil and paper in a notebook or on a pad.

After lecture: go back and look at the notes again. Are your question marks
mostly resolved? If not, spend some time re-reading and thinking about it. If
they are still questions, you really need to bring these questions with you to
discussion section.

PRINT OUT THE HOMEWORK. Look over the homework and ask yourself if you can do
each problem or at least know how to start. If possible, start in on the
easier problems at least. Make marks on the homework printout to indicate your
thoughts.

ATTEND DISCUSSION SECTION AND PARTICIPATE. At appropriate opportunities, ask
about the questions you still have regarding the notes.

If you have access to the online problems, do them. Make sure you understand
the very basics. If you get stuck somewhere, go back to the notes and read
them. If you are encountering a difficulty that you can't overcome, bring this
to your study group later.

Really attempt to do the homework on your own. Spend about 3 hours solo. Try
each problem, but if you get stuck, concentrate on writing out potential
approaches that you could try, even if you are not sure they will work. Try to
formulate the problem mathematically and take some steps if it is not already
formulated in that way. If it is formulated in that way, take some steps
without worrying about whether these are getting you to the answer just yet.
You need to explore. Don't bang your head against the wall for more than 15
minutes on any one problem or problem part without moving on. It is important
not to have any distractions: this means, no texting, no Facebook, no videos
playing, etc... Just concentrate on the homework.

Meet up with your study group for another two hours for the first group
attack. Explain to them where you are stuck. If you are actually not stuck,
but just ran out of your 3 hours, then it is fine to work solo side by side
for a while. Ask them for their thoughts about the problems. Share your
approaches and listen to them. This is the point at which you can also teach
each other the concepts and techniques that they have questions about.
Brainstorm angles of attack for a problem. Then sit and try to do them on your
own for a bit. Then return to a group dynamic. Set a 30 min limit for banging
your head on any particular problem or problem part in one go. Explain the
relevant parts of the notes to each other as you teach each other. It's
alright to joke around with each other, but don't use electronic distractions
when studying as a group.

Attend HW Party and continue the study group dynamic above, except now, you
can also ask TAs and tutors for advice. Between HW Party and a second study
group session, you should aim to have sketches of solution strategies for
every problem.

Go back and write up all the solutions on your own. (Again, no distractions.
Although in this phase, if you want to take a short break after finishing a
question, go ahead.) Ideally, you would write the solutions to the problems
without any reference to your notes from the study groups --- that is, you
would rederive them based on your improved understanding. If you get stuck,
consult your notes. Then start on a fresh piece of paper without your notes
again for that problem. In general, spending 12 hours per homework total on
average (during regular Fall or Spring) is a reasonable amount. With bursts
that go higher if something is more challenging for you.

Come up with your own problems and share them with your study group.
Variations on existing problems is fine. Ask yourself if you can come up with
problems that exercise specific concepts. If you can't come up with a problem
or a variation on a problem, you probably don't understand the material as
well as you need to.

When the solutions come out, read them carefully. Once again, printing them
out is probably a good idea. Understand the way that the solution approached
the problem, even if your approach was different and also correct. After you
read the solutions, look over your own approach. Did you actually get it
right? To what extent? If you got it wrong, redo the problem without reference
to the solution. If you can't do it without looking at the solution, you
clearly have a gap in your understanding that needs filling. You need to read
the solutions before starting the next homework set. Don't put this off even
if the course doesn't force it.

The research on education is clear: taking notes on paper/pencil is superior
to typing. Having the ability to spread notes out spatially on a desk or the
floor allows you to keep more context in your visual field --- that isn't
possible unless you have multiple tablets even with a tablet-based system.

Remember, every single thing in the lower division is something that you need
to master.

### Followup:
Student:
You could try that, but I would expect that students who find self-studying
the material an effective strategy probably aren't the ones who would be
worried about the class normally.

## CS189 Pre-requisites: Math53 VS EE16B

2017-07-27
I have taken Math54 and EE16A. What classes should I take to prepare for
CS189, Math53 or EE16B?

Math53 is an official pre-req that I have not taken. But I heard also that
EE16B is very helpful.

### Anant Sahai's answer
Both Math 53 and EE 16B will be assumed and leaned on heavily in 189. A topic
or two might be reviewed, but won't be taught fresh.

  

189 is not an entry level upper division course. It is an advanced level upper
division course. 126 and 170 are entry level upper division courses relevant
to the broad area. So are 127 and 120.

### Followup:
Student:
+1 for prof maharbiz

Student:
Maharbiz is fantastic for 16B but he just covers the circuits part. The rest
if taught by Lustig, but I think he's relatively new, so I don't think many
people have experience with him.

Student:
The only "concept" 189 uses from 53 is the calculation of gradients; that
being said, 53 teaches you to think geometrically, especially in higher
dimensional spaces. This thinking is very useful in 189, where we visualize
higher-dimensional objects through their isocontours, so 53 would help a lot.

As for 16B, the main two things from 16B that are useful in 189 are the
coverage of PCA and SVD, and the ability to think of a neural network as a
form of a circuit. I didn't take 16B before 189, and am not feeling too
uncomfortable at this point, so I'd say choose one of the two depending on
your strengths/weaknesses (for example, I feel weak with geometry-style
thinking, so I would choose 53, but this might vary from person to person).

One more thing - both 53 professors next semester are absolutely stellar (I
don't know about the 16B profs), if that motivates you to take 53.

## 134 vs 140 for data science

2017-04-28
I'm interested in majoring in data science and I added Stat 134 for next year,
but I'm worried that I have to take 140 instead. Does 134 count towards Data
science or do I have to take 140?

### Anant Sahai's answer
We don't yet know what will count for data science. If you like, you can
contact Prof Cathryn Carson; she may know.

The EECS faculty are still meeting as are the Stat faculty. However, it is the
current opinion that students in our majors should probably be taking EECS126
as the main probability course after having taken 70. Almost certainly, that
would count for any eventual data science major, which is still being designed
and has not been approved by a vote of any group of faculty yet.

## EECS 47D CCN?

2017-04-27
Hi, Prof. Elad Alon mentioned the connector course for EECS 47D "completion of
work in EE16A" is going to be offered next Fall @3828

However, I can't find it on Schedule Planner nor on EECS website. Is there any
information on that? Thank you!

### Instructor answer
EECS 47D is now available. If you want to enroll in this course, please
contact **@ Elad Alon**

## Math 110 instead of EE16A for L&S CS?

2017-04-26
Is there any way Math 110 can replace EE16A for the degree requirement? Some
background: I took Math 54 during my first semester of freshman year. I feel
taking Math 110 could be more useful and helpful(vs ee16a), especially for
courses like CS189. Thanks in advance!

### Anant Sahai's answer
Only if you are LSCS and graduating by Fall 2017 and not using Math 110 as a
tech elective.

The course that helps you in 189 is 16B.

### Followup:
Student:
What Prof. Sahai means is that while 110 is necessary (and sufficient), to
really be prepared for 189, you need to take 16B. 16B covers SVD, principal
components analysis, k-means clustering, etc. - topics that are widely used in
ML. 16B will give you an edge over those you have not taken the course.

## EE 16A + 61C + Math 54?

2017-04-26
Has anyone done this combo, and if so how was it / any tips? I wouldn't
consider myself super strong at math, and this is really math-heavy.

This is the only combo I think I can work out for this semester to graduate on
time... I'm undeclared CS/CogSci and won't declare until summer, and I just
saw the thing about non-declared people getting [dropped from the waitlist
after phase 1](http://piazza.com/class/hyq0br1u3kx7dg?cid=3831) & it kinda
screwed up my plans :(

### Anant Sahai's answer
Why are you doing this? For CS students, the strong recommendation is 16A+16B
rather than 54+16B and 16A+54 is really the worst choice of the lot.

It would be far better to just do 16A+61C and use your units for other courses
that advance your interests.

### Followup:
Student:
Elad Alon: For any incoming freshman who are reading this, I would like to
strongly re-emphasize Anant's suggestion above that EE16A + EE16B is for the
large majority of you the best overall plan. For incoming freshman, the only
two options will be 16A + 16B, or Math 54 + 16B. The latter option however
will require some self-learning of the circuits content from 16A, and while we
will be making resources available to help with that (please see the
posts/response in this thread), unless you are planning to potentially major
in something that specifically requires math 54, there really isn't a benefit
to taking that approach. **I 'd like to also note that we are in the process
of actively reaching out to other departments to make it so that they will
accept 16A+16B as an alternative to math 54** (for both prerequisites and
majors); if anyone has a specific major/department they'd like to make sure we
reach out to on that front, please feel free to contact me.

This is in @3372

Student:
Thanks for the info. Do you remember where you heard that?

Student:
Well I hear they are trying to get other departments to take EE16AB as a
replacement for 54, so you may not have to take it.

## Difference Between EE147 & MECH-E 119?

2017-04-25
Hi,

Does anyone know if there are fundamental differences between these 2 courses:
EE147 and MECH-E 119? Both courses are introductions to MEMS. Perhaps
professors could comment on this? I'm an EECS major but I'm also interested in
the MECH-E side of things, so I was thinking that perhaps I should take 119
instead of 147 next semester. Any advice is much appreciated!

Also, I think ME119 has a final project where as EE147 has no projects. The
project part of ME119 seems really interesting, so I'm leaning towards that at
the moment.

### Kris Pister's answer
The classes are roughly comparable. Professor Lin spends a little more time on
fabrication than I do.

I spend a little more time on the physics and design of different sensor and
actuators, and assume that

if you are interested in fabrication you'll take ee143.

If you're looking for a fun MEMS design project, take the 1 unit ee290G "Micro
Robot Design Lab"

that goes along with the 3 unit ee147 "Intro to MEMS". You and your fellow
students will spend the semester designing

micro robots, and around week 12 my grad students will fab them, and then
you'll get to test them

to see how well they work. We had several research papers come out of the
class projects last semester.

Some day Micro Robot Design Lab will turn into ee147L, but right now it's just
going to be offered as ee290G

because I haven't filled out all of the paperwork. And I haven't even
scheduled that yet, but it will show up

soon.

## Questions about EE 16B

2017-04-23
1\. How necessary is taking EE 16A before EE 16B (L&S CS)? I.e. is it okay to
go straight to EE 16B without having 16A or any circuits knowledge? If so,
what topics and how should I self-study or prepare for 16B?

2\. How useful is EE 16B for AI/ML related work? I will have already taken CS
188 and 189 and a few math/stats classes.

Thanks for your help and advice!

### Anant Sahai's answer
I will answer this question by speaking to what the courses 16A and 16B were
designed to do.

These are courses that are designed to be taken by freshmen (both EECS and
LSCS-intended) who have had high school calculus and are taking the intro
computation series (61AB) in parallel with 16AB. To this audience, they are
designed to help advance their skill in thinking about information and how it
connects to the real world, building a solid foundation in concrete linear
algebra (of Euclidean n-space and complex c-space) along the way. The 16AB
series are designed to be modern and to be the right lower-division
introduction in a world that has ML as an important topic that many students
will engage with.

The circuits content in 16AB (static linear circuits in 16A and dynamic
circuits in 16B along with transistors as switches with parasitics) is
designed to do two things. First, be synergistic with the overall themes of
thinking (modeling, design thinking, breaking problems into smaller parts,
mapping things to mathematics, etc...) and linear algebra in the rest of the
course. There is a purely pedagogical purpose here. Second, to expose students
to circuits as an alternative perspective on understanding information
processing, with a particular focus on the interface to the real world. We
believe that this alternative perspective and the mental muscles it develops
is vital since a purely imperative or symbolic-functional perspective on
information processing is too limiting for a 40-year career, especially as we
consider how information can be processed by things like neural networks both
of the present and in the future.

The dynamical behavior perspective in 16B is also very important as we think
about a future of robots, etc. and the introductory treatment of control
theory is meant to convey some insight about how the combination of
information processing and a physical system can result in a new combined
physical systems that behaves differently. This kind of thinking, we believe,
is going to be increasingly vital. It is not enough to think of a robot at the
level of a physical system that obeys commands. Instead, we have to accept
that the very nature of how the robot reacts to the world is intertwined with
the information processing that we engineer.

The linear-algebraic material includes perspectives on casting problems as
optimizations (including linear regression and minimum energy control) and
detailed discussions of things like choices of coordinates, PCA (also a kind
of optimization perspective) and the SVD, along with an exploration of how
time-invariant structure in linear operators creates symmetries that can be
exploited in the right coordinate systems. Most of the heavier lifting is done
in 16B with the preliminaries introduced in 16A. The treatment of differential
equations in 16B is consequently also very linear-algebra centered, and
follows the paradigm of showing how the simple 1d case generalizes to higher
dimensions with eigenstructure playing the starring role.

The default choice is that a student takes 16A and then 16B and then 70.
That's how we intend students to take these courses. The introduction of 16AB
in the freshman year allows upper division courses to adapt and improve
because they can now count on these perspectives as well as the understanding
that they provide. 189, for example, starting next semester will just take 16B
for granted.

What do you need for 16B from 16A? Basic linear algebra concepts and simple
linear circuits viewed statically.

## EE16b Prereq for EE120?

2017-04-21
Hi, I am wondering if the knowledge from EE16B is mandatory for EE120?
Otherwise, I am planning to take Math 110 and then EE120. Thanks!

### Anant Sahai's answer
**@ Anant Sahai** **@ Elad Alon** any insights here?

Sahai: You should take 16B ahead of taking Math 110. What students don't
realize is that the courses are constantly being updated. It is true that the
traditional form of 120 had a very slight to no dependence on the material in
16B. (Understandable, since 16B is the radical new course while 120 is a
traditional course that has existed in some form since the 1970s if not
earlier.) However, it is perfectly possible to conceive of a (better) form of
120 in which that dependence is very strong and is not just about mathematical
maturity or linear algebra in general, but down into the specific topics and
concepts taught in 16B. For example, by explicitly leveraging the finite-
dimensional stories in 16B as the jumping off point for the infinite-
dimensional stories told in 120.

### Followup:
Student:
I don't think linear algebra is very much used in 120. 120 is all about
transforms.

## Does learning classic control help significantly with AI control?

2017-04-21
I have one year left, having taken CS188 and CS189, and I have a choice of
whether to dive deep into the AI/ML style robotics (EE127, EE126, CS170)
and/or classical (EECS149, EE106A/B, EE192, EE C128). If you had to pick 4
classes out of these, what would you pick for someone interested in
AI/ML/robotics? What would the top 6 be?

### Anant Sahai's answer
The answer depends a bit on whether you're planning on going to grad school...

## CS170 for AI/ML/Robotics

2017-04-20
Is CS170 worth it? I did well in CS70 with a massive amount of work... dont
find theory very interesting... I really liked 188 and 189 and plan to take
more courses that directly relate to those areas... is CS170 worth it and why?

### Anant Sahai's answer
170 is absolutely fundamental to EECS. The ways of thinking are directly
relevant to most areas, including the whole
AI/ML/Control/Optimization/Robotics/SP/Comm supercluster.

You have to remember that you are being educated for a 40 year career with a
lifetime of learning, not your first job or interview or project. The
foundations are absolutely critical long term.

## 189 Bucketed or Curved

2017-04-20
Does anyone know if 189 is bucketed or curved with Prof Sahai? Thanks!

### Anant Sahai's answer
My general policy is not to use comparisons among students in deciding what
grade to assign to students. I have an absolute (high) standard for the level
of understanding that I consider mastery, and this standard takes into account
the level of a course. What I consider adequate mastery in a freshman course
is not the same as a sophomore course and this is not the same as for a higher
upper-division course like 189. Standards rise.

## EE16A Offered in the Summer (Session C)

2017-04-20
Hi EECSers et al.,

We are excited to announce that EE16A—Designing Information Devices and
Systems I—will be offered this summer during the eight-week summer session
(Session C: June 19 - August 11). This is the first time this class is offered
in the summer and it will be a unique opportunity for all those who are
interested.

The course will be taught by three instructors: Vasuki Narasimha Swamy, Filip
Maksimovic and yours truly. Vasuki has taught this course when it was first
offered in its pilot form in Spring 2015; and Fil and I taught it in its first
full-scale offering in Fall 2015. We have an amazing staff of TAs who are very
excited to teach EE16A, with previous experience in teaching, including EE16A
itself. It will indeed be a fun summer.

We are excited and hope to see you there with us in EE16A this summer.

The "Berkeley classes" course website is
<http://classes.berkeley.edu/content/2017-summer-eleng-16a-001-lec-001> \-- as
they say: the seats are limited, reserve yours today :).

### Anant Sahai's answer
My general policy is not to use comparisons among students in deciding what
grade to assign to students. I have an absolute (high) standard for the level
of understanding that I consider mastery, and this standard takes into account
the level of a course. What I consider adequate mastery in a freshman course
is not the same as a sophomore course and this is not the same as for a higher
upper-division course like 189. Standards rise.
### Followup:
Student:
yes

### Followup:
Student:
You are right, thanks for pointing that out.

## Help - what to take over summer (CS intended)

2017-04-19
I'm taking 61a right now and I think I'll get a B or B+. By the end of this
semester I'll have finished math 1a and 1b.

My question is, what should I take over the summer? I've heard from people
that I'm not ready for cs70, and I don't think I should take the ee16a/b
because it'll be a waste of time if I end up not being able to declare cs.
61bl is also a heavy workload over the summer, so I'm confused.

Does anyone have any advice for what I should do, and if I'm going to have a
shot at declaring cs with a B in 61a?

### Anant Sahai's answer
For most students who lack the requisite mathematical maturity, reading CS70
notes in preparation for CS70 creates the illusion of preparing without really
doing anything for you. I do not recommend reading as preparation if that's
the situation.

  

If you're concerned, build mathematical maturity: take ee16ab (recommended) or
Math 53 and 54. Pay serious attention as you do and work hard. It's up to you
on balancing time spent vs likelihood of success. If you enter 70 without the
required maturity, your likelihood of success is quite low. With the required
Math maturity and a willingness to work very hard and appropriate study
habits/process and a schedule that permits you to invest the time into the
course, I believe doing well in 70 is in reach for all Berkeley students.

### Followup:
Student:
would you recommend just taking 61b over the summer instead of just _prepping_
for it?

Student:
+1

Student:
How would you suggest preparing for CS61B?

### Followup:
Student:
Would recommend doing some statistics work / intro to probability / counting.
That stuff rekt me without any experience with it in 70, even though I thought
the first half of the class (Discrete Math) was perfectly reasonable

Anant Sahai:
Already have taken EE16AB (recommended) or Math 53 and 54. It isn't any
particular topic that tends to cause people serious difficulty in 70. The
course is pretty self contained in terms of content.

Before preparation, there is the issue of evaluating your mathematical
maturity. This is actually the weak link in anyone's ability to give advice
about this. In person, it is possible to evaluate mathematical maturity. It is
hard for someone to accurately self-evaluate it. Can you solve problems step
by step without experiencing exponential drops in confidence with every step?
Can you model a problem mathematically without being sure how to solve the
resulting mathematical problem? Are you comfortable solving pieces of the
problem without solving the whole thing? Can you concentrate for a long period
of time on trying things out systematically (instead of randomly), without
being distracted? Can you detect that you are making progress even if you
haven't reached the destination?

Negative indications vis-a-vis maturity: do you instinctively reach for a
formula to solve a problem and search for numbers to plug into that formula?
Does trying and getting an answer wrong or getting stuck feel really bad to
you like you wasted a bunch of time?

The work in CS70 is relatively a marathon and not a sprint. 16AB aren't
marathons, but they are longer runs than sprints. It is hard to go from
sprints to a marathon without going through longer runs in between. At least
this is how it feels to students when they start. From the perspective of a
senior who is graduating, CS70 should feel easy.

## How to find summer research

2017-04-19
I'm trying to find research this summer, but I don't have a lot of experience.
What is the best way to get started searching?

### Anant Sahai's answer
Depending on the background, we have some projects that are open to undergrad
participation. A willingness to work hard, learn on your own, etc. is
absolutely required. The same is probably true of many if not most of my
colleagues. As the student says, coming to office hours is usually the best
bet.

## Is it worth taking EE16B if I already took math 54 and plan to take EE16A ?

2017-04-19
I'm not interested in hardware but I've heard EE16B is useful for machine
learning.

I'm debating whether I should take EE16B because circuits are a major part in
16B. Does EE16B help with other CS classes, specifically CS and CS189? (L&S CS
Major)

### Elad Alon's answer
You may find out you are actually interested in "hardware" after taking EE16A
:), but circuits is not any larger fraction of 16B than it is 16A. In other
words, there's about 4-5 weeks of "circuits" in the beginning (I use quotes
because this material is also used to cover differential equations and some
very basic signals and systems), and after that the course focuses essentially
entirely on material that is directly relevant to machine learning/robotics
(control, SVD/PCA, sampling, DFT).

### Followup:
Student:
My only reservations about taking EE16A/B is,

1\. I would like to take EE16A and CS70 over the summer; I have prior Math 54
knowledge but no indication of the summer workload.

2\. As I'm in L&S, EE16B is not a mandatory requirement. And while I am
interested in EE courses, I've talked to many EECS majors who say EE16A/B
turned them off from EE.

Elad Alon:
I'm not quite sure which option you were asking about whether it l's
recommended or not, but the two options we recommend (in order) are:

  

(1) EE16A + EE16B

(2) Math 54 + EE16B

  

In terms of when to take these, I would recommend taking them as early as
possible. (I.e., for 16A, as soon as you have mathematical maturity at the
level of a 5 on the Calculus BC exam, or a semester of math at Berkeley.).
16A/B are designed and targeted as freshman courses that build foundational
knowledge for EECS topics as a whole. Postponing taking these classes in my
opinion is thus really missing out on an opportunity - not just to learn the
specific material itself, but to get early exposure to how to think about and
even design seemingly complex systems.

Student:
Is this recommended? I'm planning on taking CS61B/CS70 over the summer so I'm
trying to determine when to take EE16A or B.

Elad Alon:
This is correct; our recommended path is to take EE16A and EE16B, but you can
also take Math 54 and EE16B. (Currently enrolled Berkeley students are also
allowed to take EE16A and Math 54, but I generally wouldn't recommend that
path.)

## Possible to skip CS70 for CS minor?

2017-04-19
Hi,

I'm considering pursuing a minor in CS, and was wondering if it's generally
permissible to skip CS70 if I have a lot of relevant experience doing well in
courses that cover similar/identical material (Math 55, Stat 134, other upper
div math courses, pursuing a major in math or stats....) Is there a process
for approving or clearing this for a CS minor?  

Thanks for your assistance!

### Anant Sahai's answer
You might want to consider the new course EECS47F that formally exists to
allow students to complete the work in CS70 if they have taken other courses
that cover a very significant chunk of the material. This course exists
formally, but it is intended to be implemented by students talking to the CS70
instructors and doing the exams of CS70 and any other work that is deemed by
the faculty member as necessary to fill the holes in the students background.

## 168 + 194-38(Cyberwar) + EE16A Workload

2017-04-19
I know that nobody really knows what the work load for Cyberwar is since it's
a new course, but could anyone give me advice on how hard this schedule would
be? I will probably take them with just a decal for 13 units, or maybe a
history breadth. I've heard 168 workload isn't too bad, but that 16A is time
consuming, and I assume cyberwar will be on the light-medium side. Any
comments about 168 and 16A workloads would be helpful.

Also, as a senior (and with a very early Phase I and II) would I be safe Phase
II-ing 16A?

Thanks!

### Elad Alon's answer
This isn't quite the question you asked, but have you take Math 54 already? If
so and you felt that you had a strong understanding of the material, then
taking EE16A may not be the best bet - I would instead recommend taking EE16B.
If you're interested in that path, there was a lot more discussion about this
on the pinned thread about the L&S CS EE/Math requirements change; feel free
also to send me a note about this as well.

### Followup:
Elad Alon:
Sure thing. In that case sticking with EE16A is indeed the best bet - 16B does
very much build off of 16A, so you'd want to make sure you've got that solid
foundation.

## Cs 70 vs. Stats

2017-04-17
I am thinking of taking a stats course before CS 70 because I have never had
experience in probability. Does anyone have any suggestions on the most
related or overlapping stats courses, or if this would be a good idea? (CS
intended, currently in Math 1b and 61b)

### Anant Sahai's answer
What you need for 70 is mathematical maturity, not experience with
probability. EE16AB are enough to raise your mathematical maturity to the
right level. Math 1B by itself is almost certainly not enough. Taking Stat 134
without Math 53 is decidedly not advised, and the consensus guidance for all
EECS and LSCS students is to take EE126 after CS70 instead of taking Stat 134.

What is "mathematical maturity"? At the most basic visceral level, it is
comfort in solving problems step by step and maintaining confidence in your
work even as you take steps forward. For 70, you need comfort and familiarity
with doing simple proofs and derivations as well. What we observe even in 16AB
is that when students come in, many are so used to getting answers immediately
(which is what so much of high school and standardized testing have primed you
for) that they freeze up when faced with a problem that does not have an
immediately visible path to the solution. Some students do one level better,
in that they start trying random things but their confidence quickly
dissipates as they take steps that don't land on the answer itself. Where you
need to be emotionally (at a minimum) for 70 coming in is to maintain
confidence, execute simple things correctly, be able to be precise in talking
about concepts, and have some intuitive sense for when progress is being made.
Learning mathematical maturity is sometimes kind of painful, but this is pain
that you must experience to progress. The way that 16AB inflict this good pain
upon you is forcing you to confront multistep problems that you cannot solve
immediately.

Students should not rush into 70 prematurely or they won't be able to fully
benefit from how it takes their basic sophomore mathematical maturity and
forces them to rise to the next level (most visibly in being able to
appreciate and do proofs that require strategy and not just tactics) --- the
level that you need to be at to begin to grow in the manner that courses like
126 and 170 want you to grow.

### Followup:
Student:
I took (and did well in) Math 54 the semester before I took 70, that probably
helped me quite a bit in terms of mathematical maturity. I've heard 54 can be
hit or miss though, I was lucky and had a professor who liked to emphasize
proofs a bit more which was nice.

Student:
^ what math courses had you taken going in? A lot of people have also talked
about "mathematical maturity?" Had you taken 54 prior to the course?

## Am I prepared for CS 70?

2017-04-17
I am taking EE 127 this semester (although I am not doing particularly well).
I got an A in math 54. Didn't do so hot in 16A/16B (got a B+) because I am
pretty bad at the circuit crap.

How prepared would you say that I am for CS 70? Thanks.

### Anant Sahai's answer
Yes. You are almost certainly prepared.

Please feel free to talk to either Prof. Elad Alon or myself (just email
either of us) about what made you feel that the circuits content was
problematic for you. The goal is to have it be synergistic with the rest of
the content from a thinking perspective, and so if you felt that there was a
gap, then either there is some bug in the way that the material was presented
to you or there is some particular mental muscle that hasn't been
appropriately exercised yet. In particular, the circuits content in 16B is so
limited that it is hard to explain a lower grade purely on that basis. This
suggests that there is something else that is the problem. It is good to fix
these kinds of problems as early as possible in your undergraduate career,
which is one of the reasons why 16AB are intended to be taken by freshmen.

## EE121 no longer exists?

2017-04-16
I see that EE121 is no longer even listed as a possible class for the next two
semesters. Is this still a class here? Is it maybe listed under a different
number?

### Anant Sahai's answer
It is still a course, but currently, those of us who can teach it are in high
demand to teach other things that have higher priority.

121 is a great course. I last taught it in Fall 2013. However, some of the
ideas in it have been incorporated into 123, so a bit of the material and
spirit is available that way. But we had added all this interesting material
on using codes for storage in data centers, etc. --- that is nowhere else.

## EE16A/CS70 + R5B in summer?

2017-04-15
Hi, I'm a freshman intending to major in CS. I'm enrolled in EE16A in summer,
but thinking to switch to CS70 if the registration opens up. Would it be too
intense if I also want to take a r5b? (for reference, I'm taking math 53,
cs61a, and a r1a this semester. I have a decent amount of free time and feel
like my workload rn is totally manageable).

Also, I want to take math110 next semester. Would EE16A help with math110? (I
took math54 last semester but didn't do well..)

Thanks so much!

### Anant Sahai's answer
If you didn't do well in Math 54, you really do need to understand the
material in EE16A. Not doing well in Math 54 is also a huge warning sign for
the mathematical maturity required to take CS70, and nobody should take an
upper-division mathematics course without having the skills taught in CS70.
Stated succinctly: Take EE16A in the summer and take 110 only after you have
already completed both 70 and 16B.

## Phrase1 choice: CS168 or EE16A

2017-04-14
I will be a L&S CS senior. If I can only phrase1 one of CS168 and EE16A, which
one should I prioritize? Any help is appreciated.

### Instructor answer
Considering EE16A is needed to graduate, I would phase I that class.

## Any updates on the online / self paced EE16A that people mentioned earlier
this semester?

2017-04-14
I've taken physics 7a, math 54, and cs189 and I'd appreciate getting to move
to 16B. Do we know if it will be offered next fall? Or over the summer?
Thanks!

### Elad Alon's answer
My understanding is that the connector courses (i.e., self-paced class to make
up a subset of material) have been approved, and will be officially available
in the fall. I don't believe they will be offered during the summer, but as
your colleague mentioned, I'd be happy to meet with anyone to form a plan of
action for this nonetheless.

### Followup:
Elad Alon:
Sorry about the out of date websites - my office hours are 10:15-11:15am on
Thursdays in 519 Cory. Please do feel free to swing by.

Student:
Ah I see, I was looking on his EECS website. Yeah that's a good idea to email
him. Thanks for your help.

Student:
According to [his site](https://people.eecs.berkeley.edu/~elad/contact.html):
Tues. and Thurs. 11am-12pm, or by request. Not sure how up-to-date that is so
you should email him as well!

### Followup:
Student:
How many units will EECS 47D be for someone who has taken M54 and wants to
learn the circuits portions of 16A? The course is listed as being 1-3 units.

Student:
Will it have labs? Also will there be resources like office hours available
for self-paced students?

Elad Alon:
Sure - the connector class should be EECS 47D.

## Phase 1: CS 170, STAT 133, Math 54?

2017-04-12
I'm a rising sophomore who applied into the CS major this semester.

I'm already Phase 1-ing my R1B, but I wanted to know which other class to
Phase 1 between CS 170, STAT 133, and Math 54.

### Elad Alon's answer
I know this wasn't your question, but if you haven't already taken EE16A, I'd
like to strongly recommend signing up for that instead of Math 54.

## CS189 without CS70?

2017-04-12
Dear Fellow Students (and Professor Sahai),

I have taken the prerequisites Math 53 and Math 54, but not CS70. I have taken
CE 93 ("Data Analysis for Engineers"), which has some probability, but I felt
it was rather light.  
 **1) Granted I self-study probability topics over the summer (~6 hrs a week,
12 weeks), would you recommend I take CS189 in the Fall with Prof Bartlett and
Prof Sahai?**

My plan was to go through the probability topics listed
[here](http://gwthomas.github.io/docs/mlmath.pdf) (CS 189 TA Garett Thomas'
guide) and whatever past CS70 probability material I can access online. **2)
What are key probability topics you would recommend knowing going into
CS189?**

[I'm also making an assumption the discrete math component of CS70 isn't a
prerequisite for CS189...]

****

Other info: I'm an Energy Engineer completing a minors in EECS/ME. I have
taken EE16A; currently taking EE127, EE16B. I will take three other techs next
semester.

Thank you all in advance for insight and tips! I really appreciate it :)

### Anant Sahai's answer
You need to learn probability well and be comfortable with proofs, etc. at the
level of 70 --- that is, with twists. The polynomials material in 70 is also
very relevant. Having 16B and 127 will be good for you, but you might have to
fill in gaps for 70 material. Probability is notoriously hard to self-study.
There is a way of thinking and reasoning that you need to internalize.

### Followup:
Student:
Hi Garrett,

As someone who is in 70 and will likely be taking 189 before taking 126 or
another rigorous probability course, I'm wondering if you have any resources
that you can recommend that are helpful for practicing continuous probability,
sampling, estimation, and the other topics you mentioned. Would the material
for this be found in, say, the books used for Stat 134/135? Thanks!

Student:
(OP)  
Hi Garrett - thank you for taking the time to answer my question! (And also
many thanks for creating the guide PDF)


I had taken note of your disclaimer on Page 1, which is why I am hoping to
learn from the EE/CS community what they feel are useful concepts to study
that may not be mentioned in the guide. I also recognize the guide serves only
as a introduction to some prerequisite topics; hence, I appreciate any tips on
resources I can use to delve further into the listed material (I'll be sure to
check out the Stanford links Prof Shewchuk posted on his site).

I will look into the topics mentioned in your reply above. Actually feeling
slightly relieved, because CE 93 did teach the all topics you mentioned.
However it was a very straight-forward class and I've heard CS70 has a
reputation to be difficult/rigorous, which is what worried me about my
preparation. I'll make sure to have Gaussian distributions, continuous
probability, density functions, and basic stat concepts properly reviewed and
under my belt by end of summer.

Thanks again!  
(And sorry for misspelling your name in my first post!)

### Followup:
Student:
+1

## EE142, EE143, and EE106A

2017-04-11
I'm trying to decide between these three classes for the fall. Can someone
comment on the workload and difficulty of each?

### Elad Alon's answer
142 is probably (by a good margin) the highest workload out of the three of
those. It's an outstanding class and you will learn a lot, but it is
definitely something you should expect to invest significant time in to if you
take it. As Rachel mentioned below, you should also definitely plan to have
140 under your belt before taking 142.

  

143 and 106A are both great classes as well - I think 143 is probably higher
time commitment than 106A, but the two classes are also pretty different (143
is much more lab oriented).

## Salaries for EECS and CS majors

2017-04-10
Do EECS and CS majors receive the same starting salaries on average?

### Anant Sahai's answer
Salaries tend to depend on the job you get (and your other offers) not the
major that you have.

Jobs depend on the skills and background that you bring, not your major per
se. (To the extent that anyone is screening based on majors, there are only a
few more jobs that EECS would let you pass through the screen than LSCS.)

So your question is not asking what you want to know.

## EE 16A Summer 2017

2017-04-08
How much is the workload for EE 16A over the summer and who will be teaching
it?

### Anant Sahai's answer
There is a dream team of instructors that has been assembled for the first
roll out of summer 16a. All of them were TAs in the pilot or first scale up
offering. So folks who were very involved when key design decisions for the
course were being made and core content was developed.

  

The workload will be like normal 16a, except at double speed. So, a lot of
work but rewarding. Students are not encouraged to take any other course or
significant commitment alongside.

## Math 110 or EE C128 for control theory

2017-04-07
I'm really interested in studying control theory, but I've heard that taking
more math classes (especially linear algebra i presume) pays a lot of
dividends later on. Idk who's teaching 128 yet except it's gonna be someone
from the MechE department and idk what that will mean. On the other hand I
heard the professor for 110 next semester is really good. Both are considered
to be pretty good classes so I'm kinda conflicted.

Thoughts? Is it possible to self learn the material from either of these?

### Anant Sahai's answer
Math 110 is a good course to take after 16B to deepen your understanding of
linear algebra and understand the abstract side of the subject as well.

I believe that 128 has 120 as a prereq so I assume that you have already taken
that? 120 introduces different techniques that allow you to generalize many of
the concepts that you have seen in 16B in the finite-dimensional vector case
to the infinite-dimensional cases of signals in discrete time as well as
signals in continuous time. The concept of circulant matrix in 16B gets
replaced with the idea of an LTI system. The DFT gets generalized to the DTFT,
CTFT, and Fourier Series. The characteristic polynomial and eigenvalues of a
system matrix gets extended to think about the Laplace Transform in which the
poles play the roles that eigenvalues do. And so on. These ideas from 120
enable 128 to introduce ways of thinking about control systems that go further
than the taste provided in 16B.

Another key course for control theory is 127, optimization.

### Followup:
Student:
Huh that's interesting. Granted, 128 didn't use any fourier at all the
semester I took it (though I guess laplace is similar). I feel like if you
have the mathematical maturity to understand transforms and such you could
probably do without 120 (I've taken 128, 106AB without 120, so it's doable) if
you don't care about signal processing as much.

Student:
EE 16A/B don't teach any of the Fourier analysis that was in EE 20 except for
the DFT.

## Recommended Classes for a Second Year LSCS

2017-04-06
I'm currently a freshman taking CS 61B and 70, and hopefully will be declared
at the end of the semester. So far I have also taken CS 61a and EE16a and am
thinking of doing the 16a+b option. What classes are recommended for me to
take in my third semester? I was thinking of between ee16b + cs61c + 188/170,
but am not sure of the workload. These last two semesters have been pretty
relaxed in terms of workload if that helps as a gauge. I'm also not sure how
my priorities work as I am declaring after phase 1 - but what classes should I
phase 1/2. I'm not really sure about taking a 4th class and if I do it will
probably be a p/np breadth.

### Anant Sahai's answer
If you have 16B and 70, then 126 is a good choice alongside 170. You'll get
stronger on the mathematical side of the world. 126 is designed to be taken
after 70 and to keep you challenged and growing.

### Followup:
Student:
@3637

### Followup:
Student:
Not sure how Spring declaration works. Phase 2 doesn't seem to start until
July so there may be a chance? I'd check with an advisor.

## EECS 126 approved for the CS Minor?

2017-04-06
As above. The website says CS upper divs, but since I'm a little confused
about the course-naming conventions, I just wanted to ask here if EECS 126
(Prob and Random Processes) is counted for the CS minor? Thanks!

*pls say yes*

### Instructor answer
Great question

@Lily Zhang

### Followup:
Student:
I would like to add that if you want to learn measure theory, you should take
104/105/202A sequence (or H104/202A). Measure theory is usually not covered in
104, but 104 is a foundational class for 105/202A (which cover a bit measure
theory).

Student:
Thanks for your insight Prof. Sahai!

Anant Sahai:
For computational economics, there are lots of sides. Economics has had a long
and deep relationship to control theory (especially stochastic control theory)
and optimization. So, taking 126 and 127 is clearly going to strengthen the
appropriate muscles in a big way. The modeling aspects of probability are more
important than the algorithm-analysis aspects, so 126 is definitely way more
important than 174. Taking 170 is always good, and it is a prereq to other
courses that will help. It depends on what econometrics type courses you take,
but I think that 189 is another core EECS course that could be good for a
complementary perspective, but 126 and 127 are way more important.

You need to be taking lots of math courses though as well for preparation.
Math 104 is absolutely critical because you're going to need measure theory at
some point (could be taken in graduate school). Economists like continuous
math like classic EEs and Physicists do.

Student:
Thanks for the clarification Prof. Sahai!

As an Econ major with not-so-great coding skills but a great interest in math,
I was hoping to pursue more mathematical classes (like 170, 174, etc.), so
this is a relief. In your opinion, what do you think a good preparation for
research in the field of Computational Economics would be?

## 16B and Math 110

2017-04-05
Given the recent changes to the lower division requirements, to what extent
does 16B cover Math 110 material? Would the math from 16B be enough to take on
courses like CS 189 and EE 221A or would it still be advisable to take 110 in
order to have a better math background and to do better at those courses?

### Anant Sahai's answer
**@ Anant Sahai** **@ Elad Alon**

EE 16B is adequate preparation for CS 189 in the sense that the linear-
algebraic topics in 189 are reachable for someone who understands the material
in 16B. Of course, linear algebra is a deep subject that one constantly gets
better at, and so in 189 you are going to have to work hard. However, this
work is doable and you will grow as you do so, assuming you have other
technical maturity. (So, 189 is not intended to be taken by a 1st semester
sophomore by any means. 189 is a junior/senior course for real. It's not an
entry-level upper-div course.) You will know more linear algebra and know it
better at the end of 189 than at the beginning.

We still recommend people to take Math 110 because the additional abstract
perspective is important to understand --- both for cultural reasons and for
general mathematical maturity.

221A is a true graduate course. It is an entry-level graduate course, but for
Berkeley PhD students. This means that a well-prepared UCB senior can take the
course, but the intensity is quite high. A mastery of 16B is adequate
preparation as far as linear-algebra goes (and in fact, other students from
other places might have even less than that), but you really need to know more
material say from 120, etc. before being able to take 221A.

## Interested in ML (machine learning), but not ready for 189

2017-04-05
I'm currently taking 188 and I think it is sparking an interest in AI/ML. I
want to learn more about ML, but I don't think I'll be able to handle 189 next
semester. Are there any other classes I can take that covers some ML?

### Elad Alon's answer
Have you taken EE16B already? A good chunk of the material there will directly
prepare you for 189.

### Followup:
Student:
+1

Student:
Asking the question in previous reply considering the discrepancy in student
answers above (Soroush is also a TA for 189), and your answer

Student:
Prof Sahai, will your iteration of CS 189 be harder than previous iterations?

Anant Sahai:
Rigor upgrades as the curriculum improves. Linear algebra wise, 16B is
sufficient to start, but you will get stronger by the challenge.

  

In my view for overall technical maturity, 16a is a level 1 course, 16b is
level 2, 70 is level 3. 170 is level 4. 126 and 127 are also level 4, but
might be 4.5 in practice. I view 189 as being a level 4.5 to 5 course.

  

My opinion is that each course should appropriately challenge you and force
you to get sore and grow. In a nice way. You might welcome the break that
winter or summer brings, but in time, the understanding will stay as memories
of being sore fade away.

Student:
^ yea I agree with Aditya. EE 126 and 127 are much more rigorous courses than
189.

Student:
Currently taking CS 189 right now. I found that Math 110 and a good knowledge
of CS 70 probability is sufficient for CS 189. Taking EE 126 and 127 would be
overkill imo

Student:
They would all be very useful. I think if you had to choose one it would be
Math 110 since 189 is super Linear Algebra heavy.

## Good EE upperdivs w/ 16B

2017-04-05
Could anyone recommend any EE upperdivs that would be manageable to take
alongside ee16b?

### Elad Alon's answer
**@ Elad Alon** **@ Anant Sahai**

Elad: Unfortunately I think that all of the classes listed in the student
response actually do require 16B. Out of the three of them, 147 is probably
the most likely to be OK (simply because the most relevant parts of 16B would
be covered in the beginning of the semester), but in general, I wouldn't
recommend trying to do too much "prefetching" by taking upper divs at the same
time at 16B. That said, it really depends on your background - if you'd like,
please feel free to ping me directly and we can chat about specific
suggestions for you.

Please note BTW that 120 is continuing to evolve, and moving forward is highly
likely to be much more strongly leveraging the coverage in 16B.

## EE classes for device physics

2017-04-03
I'm an Engineering Physics major doing an EECS minor and I'm very interested
in the device physics side of things. I'd like some more advice on what
classes to explore.

For reference on the E Phys Major: I've taken math 53+54, E7, 16A+B, 61BL,
C191, and various other physics classes.

I plan to take 117, 118, and 143, and Physics 141A (solid-state)

I was told 130 would be a good addition, but can I get any other advice?
Thanks!

### Anant Sahai's answer
130 for sure and also 147 MEMS. You can also think about taking 230B when
you're ready for it.

## Math54 needed for declaring LS CS major?

2017-04-01
I am currently an intended-CS student.

In order to declare the LS CS major, what are all the courses we need?

I saw in the major declaration form that we need Math1A,B,54,CS61A,B,CS70.

However, it has come to my realisation that we only need 2 courses from
EE16A,16B and Math 54 to finish the CS degree.

So IN ORDER TO DECLARE THE MAJOR, is it required that we take Math 54 at LS?

### Satish Rao's answer
You should take EE16A instead of Math 54.

\---------------------------------------------------------

Though neither 16A nor Math 54 is required before declaration.

See Steven's answer below.

### Followup:
Student:
Yes.

## EECS vs CS

2017-03-31
I'm deciding between whether to pursue EECS + Statistics or CS + Statistics.

My biggest concern is the natural science requirements for EECS (which I have
not taken yet). Are these worth taking if I am primarily focused on pursuing
machine learning or data science?

Otherwise, what would be the recommended path? EECS or CS (with Statistics, of
course)?

Edit: Currently a Berkeley student, currently in EECS.

### Anant Sahai's answer
The natural science requirements are extremely important if you want to go
into the broad area of ML and really understand it. Actually, I would advise a
student to go beyond and actually take statistical mechanics from Physics to
understand that different way of thinking. Courses and their content matter
way more than majors.

### Followup:
Student:
Exactly

Student:
Oh so you're considering switching to CS?

Student:
Currently a student at Berkeley

### Followup:
Student:
The way I see it,

1\. You can take a light class like Nutri Sci 10 and get away with it for L&S
bio breadth

2\. 3 - 4 natural sciences (and hard ones, that is) for CoE is a lot, given
that I would prefer taking them as a 4th tech if I were to take them.

Unrelated question:  
Do Engineering Math and Stats majors get priority for enrollment in upper
division stats courses?

Student:
Wouldn't you have to do a natural science anyways as part of the biological
sciences breadth in L&S?

Student:
OP here. I'm trying to figure out how important the natural science
requirements are for my interests, and whether they are really worth it for
me.

Student:
Thanks. But I still have to do the natural science requirements with that
route

## EE16A vs EE100

2017-03-31
I received an email from my department (ME) today stating that EE100 will be
re-continued starting Spring 2018. Looking through the syllabus from older
years, it seems that it has more of an emphasis on circuits/computer
architecture topics while EE16A covers much of the same material from Math 54.
Currently I am planning on taking 16A next semester, but I would be open to
waiting one more semester to take 100. Does anyone have any experience with
EE100 or any input regarding which class would be more suitable for someone
with very little EE background?

### Anant Sahai's answer
The EE100 (note the number might change) being developed for ME is very
different from what the old EE100 was - the class is essentially brand new.
The name of the course will be "Electronics for the Internet of Things"; a
draft description is below.

Electronics has become a powerful and ubiquitous technology supporting
solutions to a wide range of applications in fields ranging from science,
engineering, healthcare, environmental monitoring, transportation, to
entertainment. The objective of this course is to teach students majoring in
these and related subjects how to use electronic devices to solve problems in
their areas of expertise. Through the lecture and laboratory, students gain
insight into the possibilities and limitations of the technology and how to
use electronics to help solve problems. Students learn to use electronics to
interact with the environment through sound, light, temperature, motion using
sensors and actuators, and how to use electronic computation to orchestrate
the interactions and exchange information wirelessly over the internet.

\--- To add to Elad's description above ---

The new course is a course that is still very much in development. The goals
and nature of the course is very different than 16AB. 16AB are first and
foremost *freshman* courses intended to provide a grounding in how to think
systematically about systems, including both mathematical modeling and
connecting to/from the physical world. *Information* and in particular,
linear-algebraic perspectives on its nature, are at the core of the subject
matter in 16AB, and 16AB are intended to form a foundation upon which a great
deal more can be built --- courses like 189, 70, 105, 120, 127, 106AB, etc....
While in a parallel universe, ME students could conceivably also take 16AB
early in their careers (as freshmen and/or sophomores) and the ME curriculum
could adapt to rely on the material and perspectives taught there (e.g.
feedback control is also a core concern in ME so the material in 16B is
conceptually very relevant), just taking 16A as a junior is really not a great
idea for serving the needs of an ME student who needs to work with mechatronic
systems. A service course that is aimed at being the first-and-last course
that someone might take in an area is very different than a foundational
course.

## Any ECON double major about STAT requirement?

2017-03-30
After taking CS 70, is it a waste of time to take STAT 20 or Data 8 + STAT 88
(already taken CS 61A)? Is EE 126 better than STAT 134? Has anyone tried to
petition to use CS 70 or EE 126 to satisfy the statistics requirement of ECON
major before?

### Anant Sahai's answer
We had a meeting of some selected faculty across Stat and EECS. The general
recommendation is that our students who have taken CS70 should be taking EE126
unless they didn't really understand the probability parts of 70. 126 is the
best way to deepen your understanding of Probability while also understanding
how it applies. The small set of topics that are covered in 134 but not in 126
should be easy for students to self-study after they have internalized the
material in 126. Stat 134 essentially should be treated as being sunsetted ---
140 is designed to be a better course.

Come and talk to me ([sahai@eecs](mailto:sahai@eecs)) if you want a faculty
member's signature on a petition saying that 70+126 should be able to
substitute for Stat 20 for another major. But it is the other major's call. At
Berkeley, we definitely have to do some work to do in getting these sort of
substitutions to be standardized for folks who are joint majors or minors.

### Followup:
Anant Sahai:
The course is being expanded in response to demand.

Student:
So STAT 134 is a lot easier than EE 126?

Student:
I don't think EE126 is generally hard to get into? It's not a large course
because there's not that much interest in it, as far as I can tell.

Student:
Another reason (at least why I don't plan on EE126) is that compared to CS70,
there are very few students (I don't think this has to do with capacity given
that many drop the class), so doing well will be ridiculously hard even if you
were a good student in CS70, e.g., as a rough approximation, if you had the
60th highest score on the final in 70, that's really good and it's a solid A,
but given only 60-70 people take EE126, assuming EE126 is taken by the top
CS70 students, you'd be at the bottom of the class... (of course you can
always improve, but this is just an approximation)

### Followup:
Student:
As the anon in the first follow-up notes, CS70 misses quite a bit of the
topics in Stats20. EE126 doesn't really address those missing topics either,
but I would expect someone who has taken both courses to be able to pick the
rest up on their own reasonably quickly.

In either case, this is something to ask the econ department about; it's their
decision.

## Possible to Take CS 161 and CS 261 Concurrently?

2017-03-29
I'm interested in taking both of these courses next semester. Both are
security courses, but I completed the prerequisites for CS 261 already (CS
162).

### Anant Sahai's answer
Graduate courses often have unspoken prerequisites. It is fair to assume
everything from undergrad (for someone who is in the stratosphere enough to
get into Berkeley for grad school) when someone is teaching a grad course. So
in general, you have to ask the instructor.

## Delaying 61C

2017-03-29
I'm a CS major wondering how important taking 61C as early as possible is. I
finished other lower division classes but chose to skip 61C this semester in
favor of upper-div classes (170, 188, 191) this semester. I originally planned
to do 189+61C next semester (Fall 2017), but with the offering of 159 (NLP)
I'm considering dropping 61C in favor of 159, as it is a class I find
interesting that isn't offered consistently. Is this a wise choice skipping
61C two semesters in a row? I'm worried the semester after (Spring 2018) might
be a little awkward because a lot of upper division courses seem to expect
knowledge from 61C, of which I will have none. I would prefer to have another
class alongside 61C, as I don't want to take it solo. Any suggestions?

### Anant Sahai's answer
There is a reason that the EECS department strongly encourages all students to
complete the complete six course lower-division (the 61ABC trilogy and the
16AB+70 trilogy) before entering the upper division.

The courses that you seem to be gravitating towards are more on the
theoretical side (things building off of 16AB+70 like 170, 188, 189, 126, 127,
etc.). It is true that 61C in particular is the least directly connected to
that side of the world. However, it is very important background. Furthermore,
if you want to work in Industry at any point, knowledge of the material in 61C
is going to assumed by everyone around you. And you probably should take at
least one course that is more software-engineering oriented, all of which
depend on 61C.

## Is EE126 worth the intensity, or is Stat 134 sufficient to give background for
ML?

2017-03-28
I'd probably have to drop a breadth class that isn't required but I'm
interested in to accommodate the workload of EE126, is it worth the time?

### Anant Sahai's answer
You should take 126. There's a reason we offer it.

### Followup:
Student:
Thanks!

Student:
I think you should be fine. I took both 189 and I'm taking 127 right now, and
while 127 mentions some concepts taught in 189 such as support vector
machines, it doesn't really build on top of 189 that much. You might be
familiar with some of the things taught in the beginning of 127 if you took
189 (i.e. SVD), but they're not too difficult to learn.

Student:
Any downsides to taking 127 before 189? I wanted to take 188 before 189, so I
planned to do 127 alongside 188.

Student:
For the record: I've taken 188 and 189, and I'm currently taking 126 and 127.

127 vs 189? I think 127 is a harder course than 189, but remember that also
depends on the teacher for the course. Most people I know take 189 before
taking 127. (also note that 188 is largely unrelated to 126, 127, and 189.)
127 is more general than 189 -- machine learning uses convex optimization as
an application.

127 vs 126? They are completely unrelated. 126 covers probability, 127 covers
convex optimization and linear algebra.

126 vs 134? 126 is the harder course, because it covers more topics, is more
accelerated, and has the sharpest cs students taking it. It is very
competitive. It will take a substantial amount of time. The hws are weekly and
take 10 hours each for me (not alone, with working with other students). if
you have the time, go for it.

I have found all of these courses to be amazing. You can't go wrong with any.
Take all if you're in the AI/ML track.

## Is CS 61C sufficient for CS?

2017-03-25
I'm taking CS 61C right now, but I feel that I'll have a lot of gaps in my
knowledge once I'm done. I _do not_ want to become a hardware engineer.
However, understanding the hardware is important especially for systems and
low-level programming - and I want to be equipped for those tasks. Am I?

For example, I don't know how computers work below the logic gate level. I
don't know any hardware description language, or how to design hardware in
general. Is CS 150 worth taking considering I don't want to become a hardware
guy? What do you suggest?

### Anant Sahai's answer
First, 150 is no more. There is just 151 and 152, both of which are apparently
awesome courses. Back when I was an undergrad, 150 was de-facto required if
not actually required.

I'm a little confused by some of your statements though. In 16B, you should
have learned a little something about how logic-gates themselves work ---
assuming the simplified transistor models presented to you. But yes, you don't
know hardware description languages. Does everyone need to know that? Not
really. but if you want to do systems programming, then knowing 151/152 is
probably essential along with 149 and 162. To have a solid foundation, you
need to have a better grounding in the hardware than 61C alone. But 61C is
probably enough for someone who isn't going to end-up in hard-core
performance-oriented computing.

### Followup:
Anant Sahai:
You should have 16B and 61C before taking them. 151 is definitely not about
how transistors work. It is about digital design --- how to design digital
systems (digital means that the transistors are used basically as switches)
with an eye to implementing them in custom hardware (whether instantiated in
an FPGA or in an ASIC). 152 is more focused on microprocessors specifically.

Talk to students in 151. They can weigh in.

## EE16A Tutoring?

2017-03-24
Hi! I'm currently a freshman in EE16A. I've already taken Math 54 so I found
the linear algebra part of the course fairly easy, but I'm having a lot of
trouble with circuits (I don't really have an extensive physics background and
I don't understand most of the concepts). I know there are office hours and
also drop-in tutoring from HKN, but are there any more structured tutoring
sessions available? I really need someone to explain the concepts to me in
more depth.

Thanks in advance!

### Instructor answer
In addition to what the above student suggested:

You can try tutoring at the Center for Access to Engineering Excellence:
<http://engineering.berkeley.edu/student-services/academic-support/tutoring-
schedule>

Or try HKN: <https://hkn.eecs.berkeley.edu/tutor/>

You could also contact **@ Nicole Evans McIntyre** for the private tutor list
if you are willing to pay for individual tutoring.

## PNP MATH 53

2017-03-23
Can L&S CS student PNP MATH 53? Also, what parts of MATH 53 are used in CS
189?

### Anant Sahai's answer
yes, math 53 is not a requirement for your major.

The maturity from Math 53 is very important. In terms of specific material,
things like partial derivatives (and what it means to differentiate a scalar
valued function with respect to a vector, a vector valued function with
respect to a vector, etc...), as well as gradients, and the method of Lagrange
multipliers are absolute bread/butter parts of background for 189 because they
are critical aspects of optimization. The limited coverage of this material in
EECS16AB is not enough maturity for sure.

## How to best learn Natural Language Processing on my own?

2017-03-22
Seeing as CS 288 might not be offered soon, I'm wondering what is the best way
for me, as a CS student, to learn NLP. My thinking was that I should learn (1)
probability and statistics, (2) algorithms, (3) machine learning, and (3)
syntax and semantics here at Berkeley. I finish phases 1 and 2 this semester
(though not deeply).

Then, when I have time, I can read a NLP book like "Foundations of Statistical
Natural Language Processing" and understand how these concepts are applied to
NLP.

**Is this the best way to go?** Another idea is to self-study past CS 288
materials. Prof. Sahai mentioned in a earlier thread that Professors have
insight into learning students don 't, and he is absolutely correct. We have
Prof. Denero, among others, on this Piazza, who are NLP experts.

Also, just to be clear, I'm not focused on NLP as my career. I feel that it's
a supremely useful area of CS to know, though. Thank you!

### Instructor answer
Do you have any suggestions, **@ John DeNero** ?

### Followup:
Student:
Hi Professor DeNero,

I saw on the draft schedule that you'll be co-teaching CS288 in Spring 2018.

I'm trying to plan ahead a little, and so I wanted to ask: I know CS188 is
listed as a pre-requisite, but do you think CS189 is equally necessary or
useful as a foundation for 288?

Thank you!

### Followup:
John DeNero:
Yes, there's a chance. We're aware that there is a lot of demand. However, CS
288 is a graduate course. Historically, very few undergraduates have chosen to
stay in the course beyond the first two weeks. And of course, graduate
students will have enrollment priority for the course if it is offered.

### Followup:
John DeNero:
If you are concerned about your preparation for the course, please contact the
instructor directly. It's a new course, so only he can answer that question.
dbamman@berkeley.edu

### Followup:
Student:
Morphology (and phonology) is Ling115, while syntax (and semantics) is
Ling120. Ling115 has a reasonably important prereq of Ling100, although Ling5
would probably be sufficient as well. Ling120 is probably manageable without
the prereq, although I'm not sure how much the course varies based on
professor.

Typology would be Ling122, but that course assumes a reasonable linguistics
background (e.g. 110 (phonetics) and others); I was enrolled in it for a few
weeks, but had to drop it because I couldn't follow along, having not taken
110 yet.

John DeNero:
A linguistics course in natural language syntax or morphology would be useful.
A linguistic typology course would also be great. I'm not sure what the course
numbers are at Berkeley. For math and stat, I'd recommend numerical
optimization (e.g. EE 127) , linear algebra, and stochastic processes (e.g.,
EE 126). Taking more linguistics and philosophy is interesting and fun, but
perhaps not directly related to your career.

## EE 120 without EE 16B

2017-03-21
Is it possible to take EE 120 without having taken EE 16B? Is it possible to
self study the relevant material in EE 16B for EE 120 and then go straight to
EE 120?

### Anant Sahai's answer
The feasibility of this is going to constantly wane as 120 adjusts to steady
state. (As students who have taken 20 leave the system and the course can
start to lean heavily on 16B.) The effects of the introduction of 16AB will
ripple through the curriculum (189, 126, 127, 70, etc.) as time goes on.

### Followup:
Student:
Thank you for your detailed response, Prof Sahai!

Anant Sahai:
It is always possible in principle to self-study every single thing in a
course on your own. This does not make it advisable or the most likely path to
success in the long term. What material in 16B is not relevant to 120? At the
moment, I think that the SVD and PCA-related material isn't likely to make an
appearance in 120. Everything else can be built upon to different degrees
depending on exactly how 120 realigns.

The curriculum isn't some buffet where the lower-division courses provide
certain condiments that make upper-division more enjoyable or provide you with
some rice to eat the other dishes with. This shows a fundamental
misunderstanding of the conceptual connections between courses and ways of
thinking. The goal of our courses is to enable you to think about things
better, not to teach you X, Y, and Z. The specific topics are mere vehicles to
help us achieve our real goals.

Student:
I mean, material in EE 16b relevant to EE 120

## Questioning the EE 16A Requirement for L&S CS

2017-03-20
Why do L&S CS majors have to take EE16A?

I'm currently enrolled in this class and I see little use for 2/3 of this
class (i.e. anything outside of linear algebra) for a majority of L&S CS
majors who will most likely not deal with circuits in their futures.

I have heard the following opinions on why this is the case and provided a
series of counter points to them:

1) EE16A and EE 16B prepare students for other CS courses, specifically CS 70

A broad majority of L&S CS majors don't end up taking EE 16A nor EE 16B before
they are able to declare, since it would be useless to most of them if they
weren't able to get into the major. Therefore, since CS 70 is part of our
declaration requirement, we anyways end up taking it before EE 16A and EE 16B,
which makes it useless. In regards to prepping us for other courses, a
majority of CS upper division courses either don't require any knowledge of
circuits or require a knowledge of circuits that runs tangential to the course
material. This can be seen from the fact that 16a and 16b are very sparsely,
if at all, listed as prerequisites to any CS upper division course.

2) A basic amount of knowledge of circuits is essential to a proper CS
education.

I disagree with this entirely. There definitely do exist fields within CS for
which a knowledge of circuits would be useful but there also exists numerous
fields in CS (esp. with industrial application) that require absolutely no
knowledge of circuits. And if this is the case, it seems that imposing a
requirement that ALL students must know a basic amount of knowledge on
circuits would be unfair to those who have no need to use it in the future.
This is the same point that I would make as to why CS 170 and CS 162 are not
required for all CS majors, even though they are extremely useful in a large
proportion of fields within CS.

3) EE 16A gives students a better understanding of linear algebra that Math 54
that would be essential for CS majors when taking classes in the future

If this is a concern, students should be offered the option of taking Math 54
+ Math 110 instead of Math 54 + EE 16A since Math 110 also imposes a higher
  understanding of linear algebra.

I argue that EE 16A should either be entirely removed as a L&S CS major
requirement or, as mentioned in my last point, should be
replaced/substitutable with Math 110.

I would love to hear any followup discussions regarding this topic; my goal in
posting this is to spark a discussion on why exactly we have this requirement
for L&S CS majors and hopefully either get it removed for future L&S CS majors
or hear a solid explanation as to why EE 16A needs to be a requirement for all
L&S CS majors as opposed to an optional class that L&S CS majors could take if
their academic interests align with material taught in the class.

### Anant Sahai's answer
**@ Anant Sahai** **@ Elad Alon**

Anant Sahai:

Hi, I will write a more detailed answer later but first will say that I
encourage you to come and talk to me to understand this better. 16AB were
designed to be fundamental to the needs of all of our students in preparation
for a 40-year career going forward, and L&S CS students in particular. We in
the faculty have a bit more experience than you do about both how fields are
evolving intellectually as well as just how much things can change with time.
As a student, you don't really understand the bigger picture, especially the
scope of change and the need for a robust development of different ways of
thinking. Which is to be expected --- otherwise, you wouldn't need the
university and could just go and read books and do projects on your own to
learn. The answer so far (I have to go to a meeting) is basically of the
"trust us" variety, and there is a strong case that such trust is actually
fundamental to the student/teacher relationship. Everything we say will always
have a dimension of "trust us" to it, because you do not understand or
appreciate what you cannot yet fathom. In the words of Donald Rumsfeld, it's
the unknown unknowns that get you. One of our goals is to make you more ready
for them.

### Followup:
Elad Alon:
I guess that Anant's and my responses crossed each other, but fortunately, (I
think :) we emphasized the same fundamental idea (about the importance of
linear algebra) while covering some other orthogonal points. Just to re-
emphasize though, I have no doubt that there are things that can be improved
in both 16A and 16B, so I'd like to make the same offer as Anant did. If
something doesn't seem to be working in either of those classes, please feel
free to email me as well - a huge amount of thinking and work has gone in to
these courses, but that doesn't mean that there aren't still improvements to
be made. Constructive feedback is hence always highly welcomed.

Elad Alon:
Responding to both of your follow-ups here, approximately in order, although
in many ways your questions/comments are related.

  

Would I argue that any possible introduction to EE must by definition include
linear algebra? No, certainly not - this wasn't the way I learned things
originally, and this isn't how things are taught in most other schools (at
least not yet). That's a pretty weak criteria though - as a student, I
distinctly remember wondering to myself why in the world I was learning the
things that I was (especially in my intro circuits class, but even well after
that), and I perservered despite that.

  

This leads to one of the main reasons I would however argue that including
linear algebra in an intro EE(CS) class is absolutely important - and perhaps
even almost necessary. Including linear algebra allows us to show with
relatively little prior background just how powerful the tools and techniques
that underly modern EE (and CS) really are in enabling real-world applications
that students (particularly freshman) will not only recognize, but have a
visceral feeling about/interest in. I really can't take the credit for that
particular realization BTW - it was really much more the product of Gireeja
Ranade's and Anant's thinking than my own (at the time) - but having now
worked this through (along with the two of them and many others), linear
algebra really is the one conceptual area I can think of that finds
substantial importance and use across pretty much the entire spectrum of EE
endeavors (including the more physicsy side, as you mentioned). As already
mentioned, it is also something that can be taught to students coming out of
high school (of course with appropriate math maturity) while simultaneously
exposing them to the application (and hence making them feel "empowered").

  

I certainly agree with you that an integrated approach to teaching physics 7B
like material would be extremely worthwhile as well. Physics 7B itself however
requires more math background than what can be expected from incoming
freshman, and so this is one of the reasons why we made the choice to
partition things the way we did. (Another reason for this is that for better
or for worse, in general, students entering from high school tend to have less
background in or opportunities to learn physics than they do math.)

  

I'm now dipping into a much more highly speculative topic, but to follow up a
bit further on your point about an integrated approach to Physics 7B, there
have actually been some discussions amongst the faculty about creating a "16C"
(naming along with everything else TBD) that could serve as an alternative
option for Physics 7B. This (currently hypothetical) course would more
directly expose students to the applications/motivations for the 7B material,
as well as more generally the "physicy" side of EECS. This class could then
also leverage the linear algebra (as well as of course circuits and basic
sensor ideas) from 16A/B. In case it wasn't obvious from how I started this
paragraph, it isn't at all yet clear when or even if this will happen - the
discussions are still highly preliminary. Based on my experience from 16A/B,
standing up a course like this will take (tens of) thousands of hours of work,
and so it's not a task that anyone will be taking on lightly. I do believe
it's an exciting possibility however, and am doing what I can to help support
this eventually happening (but again, absolutely no guarantees at all at this
time).

  

  

  

Anant Sahai:
Please come and talk with me about any concerns that you have about 16A. It is
meant to be taken by freshmen in their first semester in parallel with 61A.
That is firmly the intended audience and recommended scheduling by students,
and the course is designed for that. Clearing the backlog of students during
the transition who have not taken it as freshmen creates some degrees of
mismatch here and there, but it is our goal that even those students should
get a lot out of taking 16A. (I'll be honest, when I taught it, both me and my
TAs got a lot out of it. And we all supposedly know all this stuff perfectly
by comparison --- so it should reward contemplation for pretty much everyone.)

Our goals for 16A are to asymptotically achieve perfection in the course ---
and this means that we welcome any and all bug reports. Send me an email. The
goal is that the course should be fundamentally inclusive and that every
single concept taught in the course should be clear, integrated, and obviously
relevant. Just like students, we Profs will fall short of the high goals that
we set for ourselves, but that doesn't mean that we stop trying. :-)

In terms of linear algebra, yes, we believe that linear algebra is absolutely
fundamental to EECS and that students need to learn *why* things are defined
the way they are and to really understand the connections between these
fundamental concepts. This isn't about symbol pushing or some calculating
tricks.

Student:
Also, to discuss your middle two paragraphs, I believe it is possible to teach
circuitry in your integrated fashion while still including (at least basic)
material on electric and magnetic fields and forces as taught in Physics 7B.
In fact, I think this will extend the integration to one more level, in the
sense of understanding how the different electrical components work under the
hood (in terms of how they move electrons and affect electromagnetic fields).

Student:
So to clarify, you believe it is absolutely important and necessary to include
Linear Algebra in any incarnation of an introductory EE course?

Elad Alon:
I do appreciate your concrete suggestion and for starting a constructive
dialog - I hope that my following comments/discussion will be read in that
spirit as well.

  

I have to admit that I'm somewhat puzzled by your comments regarding the
content/structure of 16A (especially relative to the recent offerings), but
it's probably not worth dwelling on that. More importantly, there are a number
of additional (in my opinion substabtial) issues with your proposal, one of
the most important of which (again, in my opinion) is that this approach will
explicitly de-emphasize that designing efficient systems involves optimizing
(and hence understanding) across multiple (all) layers of hierarchy
simultaneously, and that often times, things you do at one level can make your
life dramatically simpler (or harder) at the others. The silo'ed approach you
are proposing is exactly what I have seen over and over in my career (both in
academic and industrial contexts) lead people down highly sub-optimal
approaches to solving the problems that faced them. For almost all intents and
purposes, this would go back to the 20/40 model we had before (although
granted it would be a very different version of 20), which was very clearly
not working (both overall and specifically in highlighting the above).

  

As I tried to describe in my response above, learning about how to design
circuits - and especially the way we present that in 16 - is really not some
fundamentally different beast than learning how to apply mathematical
techniques to solve problems in other domains (such as machine learning,
robotics, medical systems, ...). Making this intellectual link clear
throughout all of the modules (in 16A and 16B) is something we are constantly
striving to improve, but splitting the content up (as you proposed) in to
separate courses certainly won't help with this.

  

Also, as a fully practical matter, 16B (which follows the same integrated
approach described in the first paragraph) really wouldn't work in the general
case for the target audience without the build-up and introduction (both in
terms of content as well as way of thinking) from 16A. While we are allowing
L&S students moving forward (for now) to fullfil their requirements with Math
54 and 16B (mostly for reasons that I hope will be transient, as I'll explain
below), that is not the path we recommend by any means, and is not something
that would work in general without the existence of 16A.

  

To clarify the above and address an indirect point I believe you are raising,
we are currently in discussions with both Math and Statistics about getting
them to accept the combination of 16A+B as replacements for Math 54 (both in
terms of course prereqs as well as for their majors). This is by no means a
done deal and we can't yet make any guarantees, but my hope is that this will
address some of the practical issues that are driving some students to delay
taking 16 (which again, I definitely don't recommend).

Student:
In my honest opinion, I agree with Sahai about EE 16B being a vital
introduction to electrical engineering, but from what I know, EE 16A just
doesn't have the same quality, and seems more like a mishmash of linear
algebra (which is mostly covered in Math 54), and circuitry (which is already
somewhat, if not mostly, covered in Physics 7B). I propose the following as an
alternative setup:

Introducing a CS 70-Math 55 (as in "Linear Algebra with Emphasis in Theory and
Applications in Computation") analogue for Math 54, carrying over all the
properties of the relationship between CS 70 and Math 55 (e.g. acceptability
for Math/CS double major, major requirement for CS and EECS, etc.),

replacing the Physics 7B major requirement for EECS with a new
"Electromagnetism and its Applications for Computation" class required for
both L&S and EECS graduation, which will in teach op-amps and the remainder of
circuitry in 16A not already covered in lieu of most (or all) of the
thermodynamics unit,

phasing out EE 16A,

and keeping EE 16B as is.  

In this scenario, the unit requirement for EECS students will drop, and that
of L&S CS students will stay the same (as they are not required to take
Physics currently, resulting in the new E&M class replacing the units vacated
by 16A).

The only drawback I see in this arrangement is the possible slight increase in
faculty for the [EE]CS department, but I think the benefit of reducing and/or
streamlining the courseload would outweigh this cost.

Elad Alon:
I think that Anant largely hit the points that I would have made, but I'd like
to also offer to speak with anyone in person about why I believe the material
in EE16A and EE16B are indeed fundamental to your education as a CS student.

  

To follow up on one specific aspect that Anant hinted at however, if you look
at where the major innovations/advancements have happened in the last decade
(starting arbitrarily from e.g. the iPhons), almost all of them have involved
optimization and co-design among multiple levels of the system stack (from
applications and algorithms all the way down to the circuits and devices).
Even if you end up as a purely "software" engineer, our goal at Berkeley is to
try train you to be one of the ninjas who has at least a basic understanding
of how issues at layers both above and below where you work can not only
influence what you are doing, but provide opportunities for optimization of
the system as a whole.

  

Another point I'd like to make is that many of the skills you exercise in
circuit design are actually essentially identical to skills you would exercise
in software or system design as a whole (as well in linear algebra). I can
dive in to the details if you'd like, but debugging, modularity, modeling, and
using structured methods to do design and even analysis are all common across
the board. As a final note, there are actually many mathematical concepts
underlying circuits, and gaining intuition about those same concepts but with
physical quantities you may not be as familiar with is a great way to make
sure you really understand the math.

Anant Sahai:
Very coarsely speaking, there are three major ways that information is
processed and information processing is itself understood, and their relative
importance changes with time and application.

1) Procedure-orientation: this is the standard Turing/Von-Neumann
"computation" approach that is represented by most programming languages used
today.

2) Circuit-orientation: this is what is behind the operation of neural
networks as well as analog circuitry.

3) Optimization-orientation: these are where minimalist principles and
constraints are important. Many databases also fall into this category.

It is absolutely vital for a CS student to know and be comfortable with
reasoning about all three modes. The 61ABC series is heavily weighted towards
(1) with a little bit of (3) mixed in during 61A. 16AB bring more of (2) and
(3) into the mix, and it is vital that this happen as early as possible in
students' development so that their mental muscles are more balanced in their
development. This is why we absolutely urge 16AB to be taken by freshmen.

Within (2), there are many aspects to analog information processing. In 16A
you see a little bit as well as how it connects via constraints to
optimization-oriented thinking. However, in 16B the dynamic aspects also come
into play. While today's deep neural networks tend to use circuits for
information processing (circuits emulated by programs running SIMD cores for
now, but more specialized cores in the future) in a way that doesn't involve
time, there is every indication that biological neural networks do indeed
invoke time dynamics in nontrivial ways. So it would be absolutely
irresponsible of us to not give students some inclination of time-dynamic
behavior of circuits as a part of their foundational training for a 40 year
career. This is why the department wants everyone taking 16A and 16B.

Fundamentally, EECS has two pillars: information and computation. All students
need grounding in both even if they may choose to specialize in one more than
the other. But they need to start with mental balance to the extent possible
so that they don't misunderstand informational issues as being computational
nor vice-versa. You're going to have to learn and adapt. It's our job to give
you the foundation so that you can do so.

## P/NP EECS Technical Course

2017-03-20
Does P/NPing a technical course look bad for grad school? I'm having a lot of
trouble in one of my upper div EECS courses (completed my major requirements,
I'm taking it out of pure interest); however, this class is turning out to be
really difficult, and I don't think I'll end up doing that well in it.

I was planning on using the green form to either P/NP or drop the course. I
would rather do it P/NP because I still want to learn the material, just
without the worry of having to do really well, but I heard P/NPing technical
courses could look bad when applying to grad school. Is this the case? And if
so, should I just drop the course?

Also, in case this information is useful, if I do end up going to grad school
I want to focus more on systems (and I've been doing pretty well in systems
classes over here). The class I'm having trouble in is a theory-heavy course.

### Anant Sahai's answer
Purely from a grad school admissions perspective, having a P in a course that
is far outside your area is not going to hurt you.

## EE16A P/NP for L&S CS?

2017-03-19
In @3105 it's mentioned that receiving a grade of P in a lower division
requirement will count as a C-.

Can L&S CS students then P/NP EE16A, considering it's a graduation requirement
and not counted for purposes of declaration? If not, will receiving a P in
EE16A bar you from graduating because you can't retake the class?

### Instructor answer
All major requirements must be taken for a letter grade and an overall 2.0 is
needed to graduate for LSCS.

### Followup:
Student:
A D- and up is a passing grade, but you also need an overall 2.0 and semester
GPA to graduate.

Elad Alon:
I'd like to *very strongly* discourage you from putting EE16A off until your
senior year. 16A is designed and run as a freshman level course, and if you've
taken math 54 and really deeply understood it by then (which if you're going
to take classes like 189, will be very important), you're basically setting
yourself up to spend ~70% worth of a semester repeating material. As discussed
in the thread about the recent change in L&S requirements, there are way
better options out there (either taking 16A early on and following it up with
16B, or if you've taken 54 and really understood it well, taking 16B along
with doing some self-studying for the circuits material from 16A.)

Student:
LOL this is going to be me when I'm senior taking EE16a

Student:
You have to pass

## CS189 Preparation for EE127

2017-03-17
I'm currently taking 189 and I find it manageable. I've taken math 54 and both
of EE16A/B, but not math 110. Is this math preparation from 189 enough for
EE127?

Thanks

### Anant Sahai's answer
Yes.

## EE16A and B for LSCS Math Double Major

2017-03-16
Can students thinking about doubling in LSCS and Math take EE16a and EE16b in
replacement for Math 54 since under the new policy students can opt to take
16a AND 16b in place of 54? In other words, can 16a and 16b satisfy the 54
requirement for math major (double with cs)? Asking this because also
interested in doing some EE upper divs so I'm pretty certain about taking both
16 courses instead of just 16a/54 or 16b/54 under the new policy! Or is this a
question I should direct towards the math department?

### Instructor answer
To clarify, are you asking if EE 16AB will sub for 54 in the Math major? I am
not aware that they will accept this, but you should definitely check with
your math adviser.

Sarah

### Followup:
Student:
Thank you professor!

## cs61C

2017-03-15
How is this class useful for programming?

### Anant Sahai's answer
61C is arguably the most important course in the lower-division for
programming (narrowly understood), with only 61B potentially rivaling it. As
the student answer points out, you have to know how things work to understand
the impact of the choices that you make. A good artist needs to understand
their tools.

### Followup:
Student:
OP's question was "How is this class useful for programming?" I'm don't
understand how you get the tone of "when am I ever going to use CS 61C?" from
that...

Student:
No I just don't know much about 61c. I thought it was just areas that are
abstracted away from programmers and that what you mostly focus on is binary
and stuff and didn't know programmers can use these things to make more
efficient code. I also didn't know we learn C

Student:
OP's tone comes off as "when am I ever going to use CS 61C?" The answer is:
maybe never, especially if you do say front end web development or even most
types of software development. That doesn't make it irrelevant.

Student:
Who's upset? No one here has indicated being upset by anything. The OP was
simply asking how cs61c is useful for programming..

Student:
Well if you come expecting to learn computer programming, you can hardly be
upset when a computer science department teaches computer science.

Student:
" **Computer science** is theoretical, it takes a scientific and mathematical
approach to information and it 's computation. **Computer programming** is
practical, it is the process of designing, writing, testing, debugging, and
maintaining the source code of **computer** programs. They are different, but
related fields. "

\- <http://softwareengineering.stackexchange.com/questions/137103/whats-the-
difference-between-computer-science-and-programming>

Student:
Sorry this might be a stupid question but what's the difference?

Student:
Then again, we shouldn't imply that studying programming is inferior. Not
everybody comes to Berkeley CS to someday becomes a "computer scientist". Some
people come to simply be well-versed and excellent programmers in the future,
and there is absolutely nothing wrong with having that goal in mind.

Student:
It is still a valuable comment, to point out that there is a difference
between learning programming and learning computer science. 61C is needed for
a healthy understanding of computer science.

  

I'd guess that someone could get away with programming without 61C knowledge
(though even then, we do learn and use C in 61C).

Student:
Why does this matter? CS61C can still have relevance to just programming,
which is what OP asked about.

## How to learn to effectively read academic papers?

2017-03-14
I'm currently online-auditing a course taught at a different school. In the
class, the professor assigns a a research paper for reading before class, and
then leads a discussion of the paper's ideas in class. Although not all of the
lectures are online, the professor does upload a rough outline of what he
intends to talk about in class, basically in a txt file containing the
pertinent questions he wants the class to talk about.  

In the cases where the lecture videos aren't available, I've often found
myself confused by the questions listed, and wonder how and why the professor
seems to be able to pick up on minute details/edge cases and is able to ask
compelling questions to ask about a given paper, or a new idea.(i.e. why do
writes become much faster than reads according to figure 4c). I guess I was
wondering how I can learn to ask the right questions and efficiently
understand academic papers.

### Anant Sahai's answer
Take an in-person special topics course and then ask the professor to walk you
through the process.

Basically, you read a paper like you have a conversation as a curious and
inquisitive student. Lots of back and forth. You need to take notes and ask
questions of the paper. And then read the paper to see what it has to say. And
then ask more questions. And read it again. And again. And again.

## Incredible amounts of stress from taking a class

2017-03-14
I'm a junior EECS student taking an upper-div EECS class that is _not_
required for graduation. I personally find that the difficulty of the material
has markedly increased. This has been sucking up all of my time as of late,
causing me insane amounts of stress, and has hurt my mental health.

Every day it becomes more clear that I simply can't keep up with the class I'm
currently taking. The stress is literally consuming every minute of my life.
Is there _any way_ at all to drop the class? I just feel an impending sense of
doom now. It is clear to me that I won 't be able to improve no matter how
hard I try or how much help I try to get.

**Edit:** Could someone tell me how the new policy in the _follow-up_ to
@2554 relates? If I'll have completed 45 technical units (20 upper-div) by the
end of this semester, will I be able to P/NP this upper-div course?

### Instructor answer
I'm sorry that you're having such a hard time this semester. As the students
have referenced below, you will need to speak with your ESS advisor. You could
have three options, but again your ESS advisor would know for sure.

Option 1) Since you will complete your degree requirements this semester
without this class, check with your ESS advisor if you should submit [this
petition](http://engineering.berkeley.edu/sites/default/files/docs/changes-
after-deadline.pdf) to change the grade to P/NP after the deadline due to
circumstance A. Documentation is required so it would be a good idea to visit
the Tang Center or Dr. Christine Zhou in 241 Bechtel,
[christinez@uhs.berkeley.edu](mailto:christinez@uhs.berkeley.edu) or (510)
643-7850. I think her drop-in hours are Tues and Wed. or

Option 2) Submit [this
petition](http://engineering.berkeley.edu/sites/default/files/docs/changes-
after-deadline.pdf) to drop the course after the deadline due to circumstance
A. Documentation is required so it would be a good idea to visit the Tang
Center or Dr. Christine Zhou in 241 Bechtel,
[christinez@uhs.berkeley.edu](mailto:christinez@uhs.berkeley.edu) or (510)
643-7850. I think her drop-in hours are Tues and Wed, or

Option 3) Ask your ESS advisor about the green petition, the new policy that
allows students to drop a class after the deadline **one time** **.**
Information about this petition is not available online.

### Followup:
Student:
If it is CS 189 please consider sending me or the other TAs an email. I am
willing to help you personally if it's for this class.

Student:
Am I allowed to P/NP?

I would rather not say which class it is. It's just a CS upper div.

### Followup:
Anant Sahai:
Go and talk to the professor privately. In every course I have taught, there
have been occasions when students would need to talk to me privately because
they felt that they couldn't do it. Sometimes this is true and sometimes it is
not. Mostly, it is not true. But through an interactive conversation with the
professor, you can get much more than you can by ruminating about it yourself.
Because they've seen many many students go through the material while you have
only seen yourself, and that too not very clearly.

Student:
Have you tried those things? I was seriously a mess until I started going to
OH every day.

Student:
The only reason I'm posting is because I am supremely confident I _can 't_ do
it. I just can't - I wish I never tried.

### Followup:
Student:
The policy I'm referring to is the "green petition" mentioned by Lydia.

Student:
I would love more details about this new policy if possible. Do you have any
links to the policy? Why do you think I might still be able to drop?

### Followup:
Student:
I think it depends...you should talk to your ESS adviser about your needs and
they can figure out whether the green petition makes sense for you or not.

## Advice for dropping out of college as an EECS major

2017-03-12
Not sure if there are any previous posts regarding this so I decided to make
my own. My circumstances right now:

\- I am a first-year transfer majoring in EECS

\- This is my second semester and I have taken or am taking CS61A, B, and C,
70, and EE16A

\- I am a full-time student also working two part-time jobs and the ocassional
freelance work

\- I am from a _very_ low-income family and I am the main source of income

My source of stress and the reason why I am considering this at all is because
of the last point listed above. I currently receive full financial aid for my
classes (besides the summer semester, for some reason) and the extra money I
get from grants/loans along with the money from working is crucial to my
family's survival. Forgive me if it sounds like I'm dramatizing that, but I
can't really think of a better way to put it.

This May, I will not have enough money to support my family lest we resort to
living in a shelter or cramped apartment. Even then, we would not have enough
money for a lot of the necessities we pay for every month. The only options I
can think of are to drop out/take a semester off or attend school part-time,
all in order to have time for a full-time job as a software engineer. I
believe I have the necessary experience and side projects already for landing
such a job, but naturally I'm afraid to just drop out. The problem with taking
a semester off or attending part-time is that, since I'm a transfer in the
engineering department, I believe I only have a limited number of semesters
here before I can no longer enroll. I suppose I could petition to stay longer
as another option, though.

In summary, I'm considering dropping out to support my family before we go
homeless. If I have the experience and confidence in my skills to land a
software engineering job right now, should I go for it? Some clarification for
how long an EECS transfer can attend would also be appreciated.

### Instructor answer
Email one of your profs, or Chris Hunn, or Lilly Zhang, or perhaps Susanne
Kauer.

They can talk this out at least.

We may only be sounding boards, but we are happy to do so.

\-----

I think this has already been addressed with this specific student, but since
it stirred a lot of conversation, I thought I'd clarify for anyone else
curious. Typically, UC Berkeley allows any student to leave for as much time
as they need. There's a process to take time off, and some paperwork to come
back. The time away does not count towards your 4 years (2.5 for a transfer).
However, this may not be the case if you study at another institution while
you're away.

It's pretty common for students to "withdraw", it's just not something we hear
alot about. While Cal isn't always great at supporting and embracing any sort
of "non-traditional student", it really does allow alot of flexibility for
taking time off. The Advisers in your department or college are happy to talk
more about if if you need.

[Taking time off](http://registrar.berkeley.edu/registration/cancellation-
withdrawal) & [returning to
Cal](http://registrar.berkeley.edu/registration/re-admission)

### Followup:
Student:
+1 I would be happy to help, but definitely makes sense if you're not
comfortable publicly sharing your info. Good luck OP!

Student:
OP here, thank you for this suggestion. While I wouldn't be too comfortable
with sharing the reasons for my situation publicly, I will still consider this
as an option.

Student:
+1 I would be happy to help.

Student:
+1

Student:
I would too.

Student:
+1 I would definitely help out.

### Followup:
Student:
OP here. Thank you for the kind words. An internship has certainly been one of
my options. Unfortunately, it may only be a temporary fix if I continue to
attend school full-time in the next academic year.

### Followup:
Student:
OP here. Thank you for this information! I wasn't aware of any postponement
policies, so I'll confirm this with an advisor very soon.

### Followup:
Student:
(I'm the author of the initial response thread). Oh, one more clarification I
have to make. My decision to open these credit cards were carefully planned
and I had written up a detailed plan on how I was going to manage the money.
If done haphazardly, credit cards could be cause more problems than it solves.

Student:
(I'm the author of the initial response thread). By going into debt, I mean
using it to make ends meet while you work towards graduating. My situation was
probably different from yours in that I had built up a credit score and was
eligible to apply for credit cards that gave 0% interest for 15-21 months.
This allowed me to get access to about $20k in 0% interest (of course, I
didn't use it all but it was something useful to have to pay for important
expenses that financial aid didn't cover). Having a full time job also helped
my chances of getting a credit card.

One plan that could work for you is taking one year off of school to work as a
software developer. Then while you're there, save enough to help you get
through for the next two years. And perhaps, if your credit score is okay,
then you could even get 0% interest credit cards. With 15-21 months of no
interest (Citi Simplicity; Chase Slate; Discover 18 months), you will be able
to focus on school while also being able to survive. Then you will have only
paid a few months of interest before you get a job hopefully making a decent
salary.

Oh, I think i'm writing in circles, but I hope this clarified things without
making things more confusing. Feel free to ask more questions.

Student:
Thank you for sharing this. Could you clarify what you mean by going into
debt? I'm already taking out federal loans and, aside from borrowing from
people I personally know, I don't see how private loans would have 0%
interest. My initial plan was to rely on my federal grants/loans and I was
fairly confident I could land a decent job right after graduating to pay them
off asap, but my circumstances have changed such that I now would need to take
out more loans to go down that same route (something I consider riskier than
just trying to find a job now and finishing school later).

### Followup:
Student:
Why is this relevant or helpful? Please, try to be sensitive. This should be a
supportive space; please try to be helpful and kind. The admins can see your
names and we will not tolerate trolling.

Student:
Asians aren't a monolithic group, either. Some groups are overall
underprivileged, like southeast Asians.

Student:
At the risk of getting dragged into a fruitless debate, perhaps we should be
mindful of the fact that everybody's personal situation and experiences are
different. Trying to stereotype people, assign characteristics to arbitrary
groups of people, and otherwise deny people their individual identities,
thoughts, and feelings is unhelpful and harmful. This is regardless of whether
it's done for comedic effect, to make a political point, or whether it
stereotypes "whites", "asians", "the left", "the right", "LGBQT people".

Student:
Not sure how you assumed the OP was Asian. Also, it may be true the left views
Asians and whites in the way you described. In fact, many posters in the "Town
halls too politically correct" expressed that view. So that may be correct.
However, by bringing this up, you're using the OP's plight to make a political
point, which is not related to the discussion at all.

Student:
What does this have to do with anything? OP is just asking for advice, and not
once mentioned privilege or anything like that.

Student:
I think it's relevant though. I have a slight feeling that the OP is Asian.
He/she should know how the left views them: as overprivileged, monotonous
automatons.

Student:
Let's please not make jokes here. This person (and the commmenter above) is
revealing some highly personal information, and we should be mature about it.
I, too, am not a fan of political correctness but this is the wrong forum to
attack political correctness.

Student:
Glad this page is not totally anonymous so at least staff members could know
who this ridiculous person is ;)

Student:
Not a troll. Whites and Asians are privileged. They don't need help. Only
minorities, LGBQT, etc. are victims.

Student:
are you serious? No point to be a troll under this post

## EE16A and CS61B (Summer)

2017-03-08
Can anyone share their experiences taking one or both of these classes during
the summer? Maybe general advice or tips for CS summer classes in general?

### Instructor answer
EE 16a has never been offered over summer before so i'm afraid no one will be
able to share personal experiences from that.

### Followup:
Student:
If a student took Math 54 already, is it still advised against to take EE16A
and CS61BL during the summer?

## Advice for CS70 second time around?

2017-03-06
I will preface this by saying yes I have read a lot of posts about CS70 on
this Piazza, but I am still at a loss as to what to do to prepare for retaking
70.

I attempted to take CS70 this semester, but after getting around 1 standard
deviation below the mean on the midterm I decided to drop the course. What's
troubling is I dedicated a huge amount of time to 70, understood and got high
grades on the homework, read the notes carefully many times, went to lecture,
watched lecture webcasts, went to 4 discussions a week, looked at all the
extra resources, and did past exams.

I currently have a 4.0 GPA (already took 61A and B), so I could have declared
if I stuck with it, but I felt too shaky with the concepts to continue. I am
well aware I do not have mathematical maturity required for the class, and it
doesn't help that I am a freshman who wasn't ever good at math and has not
taken any math courses at Cal yet. However, some such freshmen I know passed
the course easily (even some who came in with at most AB calculus math
experience). I don't think I'm ready to take Math54 either. I'm just horrible
at math.

My plan would be taking the course this summer, while self studying 70
material and other math material this semester before the summer starts. I
only have 13 units so I would have some time to self study. What would people
recommend? Will it be any easier in the summer if I only take CS70? Is there
going to be a CSM section for summer? If not, would that negatively impact me?
I don't want to get an A, I just want to get something that is not a C or
lower like I would've gotten if I continued in the course. Thank you in
advance!

### Satish Rao's answer
If you feel like you are horrible at math, then this is a real warning sign
for 70. Self-studying is a very hard way to build mathematical maturity.
Classes are better for that. You need to take something that will take you
from where you are, and improve your mathematical maturity. EE16A might help
you in that direction (assuming you have already done the equivalents of Math
1A and 1B). As freshman-oriented courses, they are more gentle with their
slope of mathematical difficulty.

The math in CS70 is not some magic or esoterica. It is accessible to everyone,
provided that you train for it. (Think of it like being able to run 3 miles.
That is something that most humans can do, even if some people might be really
out of shape when they start. They just have to train for longer and at a pace
that will let their body adapt to the rising difficulty.) Without talking to
you, what you described sounds like someone who was stymied by the difficulty
slope in 70 relative to your mathematical equivalent of athletic conditioning.
Take EE16A and 16B first. Then the slope in 70 should be more accessible.
There's no getting around working hard, but you have clearly shown that you
are willing to do that.

Good luck!

\---------------------------------------------------------------------------------------------------------------------------------------------------

Hello OP,

I am the current professor of CS70. Moreover, I interacted with you a bit on
piazza. Let me first say, I am sorry to see that you have gone.

I am a Dad for what its worth to kids roughly your age. So, I will give a
"Dad" story to hopefully address your question. My kids embark on eye-rolling
at this point, please feel free to do so.

I was in a seminar once where Terry Tao was speaking. He was a prodigy and now
is an incredibly accomplished and also incredibly generous mathematician
through his blog. He was describing at a fairly high level his work with Green
regarding arithmetic progressions. He was writing fairly quickly on the board,
but then stopped, for a while, thirty seconds perhaps even a minute. He
concentrated, perhaps even rocked slightly. He then nodded, perhaps remarked
something like "OK", and continued his explanation.

What was he doing?

Who knows?

But I will speculate. He was perhaps thinking about his explanation and how it
fit in with the details of the proof of this epic theorem. To maintain
integrity, the explanation had to be faithful to the actual proof, he could
not go on without ensuring that. Moreover, he focused enough to get the
details sorted in his mind and confirm that his explanation was indeed on
solid ground. He did this in front of an audience that patiently awaited.

This focus and integrity is perhaps a view of what math is, and what doing it
takes. He wasn't comfortable with communicating much less having a soft
understanding of what was going on, he had to ensure that what he understood
and communicated was true. Certainly, many details were not there, but a plan
whose parts could actually be executed was laid out. Second, he was able to
focus and bring these things together in those moments, in front of an
audience. The combination of the desire to communicate accurately and the
ability to focus to gather what context he needed into his mind to verify his
explanation was amazing.

In CS70, one needs to do this on some level. For example, think about a proof
of Fermat's theorem; or $$a^{p-1} = 1 \pmod{p}$$ for non-zero $$a$$. Here, one
needs to gather some ideas. Any non-zero $$a$$ has an inverse $$\pmod p$$, as
$$gcd(a,p)=1$$ when $$p$$ is prime. Thus, we can say that the set
$$\\{a,2a,3a,\ldots,(p-1)a\\}$$ consists of distint elements and thus must be
the same set as $$\\{1,\ldots,(p-1)\\}$$ modulo $$p$$. Then, we proceed by
noting the product of the elements of the "two" sets are the same, but have
different form. From here, can you finish?

In some sense, this isn't even enough to just know the basic proofs. We then
ask questions like show that $$a^{(p-1)(q-1)} = 1 \mod{pq}$$ on the exam!
Here, the proof is the same, one needs to work with the set $$\\{x
\in\\{1,\ldots pq-1\\} | gcd(x,pq) = 1\\}$$ as they have inverses and do a bit
more work. Oh my! But this is fine. You can do it! Just play with the ideas, a
little bijection, a little bit about inverses. Turn over the proof a couple of
times to see how it works. Teach someone the proof to see if you have it. But
do try to have it completely, if not then, eventually. Indeed, I sometimes sit
up in the middle of the night because I got some aspect of some explanation
wrong to some student.

One thing though that makes this very difficult, would be doing all this while
thinking about how "not good" at math one is. One needs to use your
significant mental resources to play with the ideas not to engage in fear or
self doubt.

I should note even Terry Tao had doubts at times; indeed, he was once led out
of an exam room in tears. [See
here.](https://www.nytimes.com/2015/07/26/magazine/the-singular-mind-of-terry-
tao.html?_r=0)

Given your performance in 61A and 61B, these ideas are easily within your
grasp. Just approach them calmly, and engage, you will do fine. You are
welcome to continue to come to office hours and at least listen. The
interactions among students, and between students and TA's may well be more
fun and instructive now that the pressure is off. Choose ideas to really get
and ensure you get them. Better to solidly have some than sketchily have many.
It should be fun, even.

TL;DR. For math, one should try to own the why. Focus on that, leave out
yourself and specifically doubts about yourself, however hard that is. Some
days we just don't get it, that's fine too. There is always another day.

Cheers,

Satish Rao

### Followup:
Anant Sahai:
Just EE16A and EE16B are enough to prepare you in terms of mathematical
maturity for CS70. These courses form a trilogy of sorts.

L&S CS students are not required to take 53 and 54 if they take EE16A and
EE16B.

Math 53 and 54 also can give the requisite level of mathematical maturity if
you take them seriously.

Trying to take CS70 with just Calculus 1A and 1B is not a good idea. The
prerequisite is "sophomore mathematical maturity" not "freshman mathematical
maturity."

Student:
If I had to take both EE courses AND Math 53 and 54 I would not be able to
take CS70 on time. What should I do?

Anant Sahai:
Have you already taken Math 53, 54?

Going into 70 with just Math 1AB is a bad idea.

### Followup:
Student:
Student groups like HKN, CSM are typically not offered during the summer,
however our classes will always have office hours. Many often also have HW
parties as well.

Student:
Also, I am considering the EE courses. I will have to try to fit them into my
schedule somehow.

### Followup:
Satish Rao:
Hello,

My apologies on the crowds. We have a new Oral Quiz queue which one can sign
up for where we have

course staff who can review concepts with students.

Some office hours are busier than others, I will try to get an idea

of where extra time is in our next staff meeting.

Satish Rao

### Followup:
Student:
Just wanted to say thanks for posting this! I read the reply over break but
didn't get a chance to come back and respond till now.

And the timing of the latest homework WRT to the midterm is really beneficial
to letting us study more breadth/speed for the exam, so I know many of us also
appreciate that decision by the instructors.

Satish Rao:
Sorry about the length of the homeworks. We did try to ease up a bit between
the midterms, with a bit of a ramp.

For this midterm the homework is not due for a week after the midterm, so you
will have more time to focus on

preparing for the tests.

The strategy on the midterms is to give more smaller problems. This is for a
few reasons, first is that more questions

increases the amount of data from which to "measure" a students knowledge and
ability to work with the materials, another

being that a "large" question like what you see on homework is problematic in
that the piecing together of various concepts

at that level is too much to expect on an exam and very noisy in that even for
the same student on some days

the insight comes quickly on another it just doesn't. We do try to design them
to capture the pieces of the

puzzles that you put together in the homeworks. For example, testing the proof
of Fermat's theorem may unwind

into smaller questions about inverses, bijections, and reorganizing terms
within a modular arithmetic framework.

The idea is that you worked with all of these pieces in your homework, so the
time spent on your homework

should be helpful for exam. Still, the pacing for homework is truly very
different than what we can test

on the exam; read problems, digest, play with the ideas, be creative, etc.
Measuring student performance fairly is a difficult

problem that Professors constantly struggle with.

As for advice, perhaps the above context is useful. In some sense, knowing the
design principles around the exams

may well help you better understand how to approach the exam.

Studying old exams is good. Other instructor exams are great for content, but
maybe to attune to my style use my

exams perhaps later in your studying cycle. Discussions have more smaller idea
problems that are akin to exams.

Study those. Finally, do at least understand the solutions to homeworks. We do
have difficult homeworks in that it

is difficult to come up with the solutions, but often the solutions are short
(annoyingly so, I would imagine) so do at

least try to scan over and understand the solutions to the homeworks; I
wouldn't try to come up with them again

necessarily though as that would likely take a lot of time.

## Do we need to have taken math54 to take cs70?

2017-03-04
Hi I'm thinking of taking cs 70 over the summer but I haven't taken math 54.
Will i be ok?

### Anant Sahai's answer
You need the mathematical maturity. EE16AB are the gold standard for the
"Sophomore Mathematical Maturity" that CS70 expects. Math 53, 54 also do the
trick.

### Followup:
Student:
70 also covers the notion of one-to-one, onto, and bijective functions which
is covered in math 54 too.

Student:
Markov chains are covered in 70. There's a faster solution if you can solve
linear equations in matrix form, which you learn in Math 54. But you also
might have learned that in high school. Other than that, 70 doesn't depend on
54.

## What is the ultimate goal of our CS classes? How are they designed?

2017-03-02
I was talking to an alum who graduated in the early 2000s, and he was talking
about being a good software engineer vs. computer scientist.

I don't fully understand the distinction between the two. Can someone explain
it, and what the school classes are geared towards?

What are the professors' expectations when teaching? Do they simply want us to
become better at the topic, or do they want us to become a better X through
taking courses Y and Z?

What does the school want us to become/earn after we graduate besides the
degree itself?

### Anant Sahai's answer
guide.berkeley.edu maintains student learning goals for every major on campus

\-----------

[Anant Sahai's opinion]

The point of the classes that EECS offers is to, collectively, help you become
a better engineer (and scholar, should you go on for graduate study) over the
course of a 40+ year career. Ideally, a Berkeley style engineer who can work
on things that push the boundaries and not just filling in the blanks.
Engineers who can contribute to make society better and advancing the state of
knowledge, while learning. How classes do this is by helping you think about
things more clearly. When I was an undergraduate, there were things said in
lecture that were never on an exam or a HW that still ended up helping me
years later. If a student thinks that a class is about doing well on the
homework or on exams or getting a good grade, the student is missing the
point. If the student thinks the point of the course is to teach them a
particular tool that they can use in industry, they are also missing the
point. They should be paying attention and trying to internalize how we are
thinking.

A Bachelor's degree is meant to prepare you for being an apprentice --- to
learn productively from masters who are working in the field. There are going
to be many practical skills associated with both software engineering in
general as well as particular application domains that you will have to learn
in the field. In general, the time at Berkeley is precious and what you could
learn better in industry should be left to be taught to you there. Details
(and particular tools) are easy to learn in industry, but big pictures are
harder. This is because real life has lots of details. Knowing how to remove
the details and see the essence is the skill that is hard to learn in industry
precisely because the essence alone is never enough. But the essence is
critical for making strategic decisions. However, when people start out, they
don't usually get to make strategic decisions. So there is a gap --- a time
during which you are learning a lot in industry and not seeing the full
advantage of your Berkeley education. This is fine from our point of view ---
we are teaching you with the time-scale of decades in our mind.

### Followup:
Student:
I didn't mean to imply a wrote a program that could generate english. That
would probably be beyond my abilities (at least, if I wanted it to be
coherent....). The course was History of Information (a great course
overall!), and we were talking about the effects of the dictionary on the
development of language and how that affected word choice. I was in 61A at the
time, and we had just learned to use dictionaries (the Python kind, of course)
and so I though it would be fun to do things like word count on a couple texts
we were given as well as some basic statistics and to find data to explore the
same topics. It was nothing super rigorous, but I found it to be a good way to
practice Python (of which I needed lots of practice them!) and to explore the
topic in a way that I figured most people would not. Based on what I learned
from messing around I used that to write the reading response which gave me a
bit more depth and thus made the word count thing easier. :) I mean, I can BS
my way to a word count any day [hello AP courses!] but assignments are much
more fun when you can complete them without needing to do that.

Student:
Mr. Ball,

I was interested in your comment that you wrote code to write a reading
response for you. Am I understanding this correctly? You wrote a program to
write an essay for one of your classes. How did you do this project?

## Computer science careers for Cognitive science Majors

2017-02-28
I'm a cognitive science major and I know that they usually end up going into
Artificial intelligence, but I won't end up taking Machine learning before I
graduate and I haven't taken math 1b, math 53 or math 54. I will end up taking
intro to AI and cs70 though, is that enough? Is it really difficult for CogSci
majors to land a successful career as a software applications developer after
college? What other CS fields do cogsci majors usually end up in and what
upper divs would I need in order to be successful in it? With the time I have
left I most likely will only be able to take intro to AI, efficient
algorithms, and user interface design and development, but I think I can maybe
fit in another one depending on what its prerequistes are. This is just kinda
worrying me because I dont want to end up stuck in an area I am not all that
interested in. Also, how important is cs61C? I heard its not very important
for most programmers, is that true?

### Anant Sahai's answer
"Sophomore mathematical maturity" is a prerequisite for CS70. This practically
means the mathematical maturity acquired by taking EE16AB and/or Math 53/54.
In our experience, students who lack the appropriate level of mathematical
maturity tend to find CS70 excruciatingly painful and CS70 is a reasonably
hard course even for those who have the mathematical maturity it expects.

The EECS department believes that all the lower division courses are pretty
vital. It's not even so much about the specific technical details that you
learn, although those are important and useful. It is about the perspectives,
context, and ways of thinking. That is what really helps you in the long term.
Taking these courses is about helping you ask questions as much as it is about
helping you answer them. Others can often help you answer questions when you
are working. Fewer folks are available to help you ask questions.

That said, there are a vast range of software development jobs out there and
knowing 61AB, 70, 170, 160, and 188 is actually not a very weak foundation, as
long as you work hard to keep on learning. The lack of 61C would be a pretty
glaring hole though. 61C and 162 are very important perspectives for a
practical software developer, especially if they are ever want to be engaged
in work that demands high performance. Real-world performance is often less
about Big-O issues and more about cache misses.

## How do Professors learn new topics?

2017-02-27
I am interested in learning how Professors master new topics they weren't
originally educated in.

It seems like every EECS faculty member knows machine learning, from Prof.
Shewchuck to Prof. Sahai and Prof. Wagner. The first two is/will teach CS 189,
while Prof. Wagner uses ML techniques in his research. This is just an
example. I don't think all EECS professors learned machine learning in
undergrad / PhD years, hence they must have had to learn on their own. How did
they achieve this?

I ask because learning to learn is one of the most useful skills ever.
Considering Professors have to constantly absorb large amounts of knowledge
(entire fields) without taking courses, I want to know what techniques they
suggest for us. Thank you in advance.

### Anant Sahai's answer
"Sophomore mathematical maturity" is a prerequisite for CS70. This practically
means the mathematical maturity acquired by taking EE16AB and/or Math 53/54.
In our experience, students who lack the appropriate level of mathematical
maturity tend to find CS70 excruciatingly painful and CS70 is a reasonably
hard course even for those who have the mathematical maturity it expects.

The EECS department believes that all the lower division courses are pretty
vital. It's not even so much about the specific technical details that you
learn, although those are important and useful. It is about the perspectives,
context, and ways of thinking. That is what really helps you in the long term.
Taking these courses is about helping you ask questions as much as it is about
helping you answer them. Others can often help you answer questions when you
are working. Fewer folks are available to help you ask questions.

That said, there are a vast range of software development jobs out there and
knowing 61AB, 70, 170, 160, and 188 is actually not a very weak foundation, as
long as you work hard to keep on learning. The lack of 61C would be a pretty
glaring hole though. 61C and 162 are very important perspectives for a
practical software developer, especially if they are ever want to be engaged
in work that demands high performance. Real-world performance is often less
about Big-O issues and more about cache misses.
## CS Town Halls too politically correct

2017-02-26
I attended the CS town hall meeting on Tuesday. Minutes:
<https://docs.google.com/document/d/1i9hiXp6bgFLsSe6i91gy7HaGVTpCiUw2gJi-
aZDVPLE/edit>

Why is everyone so politically correct at these town hall meetings? We have so
many more important things to discuss. How can we more regularly offer courses
[like CS 288]? How can we deal with long waitlists? How can we afford more
tuition waivers for TAs? These are the real issues CS students want to
discuss. Open forums with Professors are rare. I, and most CS students, would
rather not waste the chance on safe spaces/playing victim card/dividing people
by race, gender, sexuality.

\------------------------------------------------------------------------------------------------------

**" EECS Master Race” is offensive/hurtful to those inside and outside of our
department"**

Relax, it's just a joke. No one ever meant harm.

**" As a female and a minority I definitely feel like I don't belong when none
of my TAs or professors look like me.”**

This is a non-issue. TAs and Professors are hired on their merits, not on
gender or color of their skin. Also, it's not all about race. People can be
similar without having the same skin color.

"When [a female student] suggested including a woman on the interview board
for one of these organizations **she was told that "men and women don't
interview differently" so there’s no need to include a woman on the board, and
that she should "stop pulling the girl card for everything**."

What's so controversial here? People should be chosen based on merits, not
gender. ALL people are created equal. This includes people of all genders,
sexualities and ethnic backgrounds.

**" TAs are dismissive or lack understanding/empathy, this can be especially
difficult for those who come in without CS backgrounds or underrepresented
students"**

I've been at Cal 3 years and not once have I had a bad TA. In any of my CS
courses. Not once. Our TAs are the most energetic, enthusiastic, and
intelligent people I've ever known at Cal. These are people that write books
for students (like Sinho Chewi, Alvin Wan), respond to Slack/text messages at
all hours of the day, and answer your piazza questions without even being
students (Steven Bi). Please find someone else to blame. We CS students love
our TAs.

"Students from [BESSA](http://ucbessa.berkeley.edu) (Black Engineering and
Sciences Student Association) expressed that they feel that enough is not
being done.... **Reported that BESSA lacks the resources to provide services
like tutoring, given their few numbers. "**

Okay....Whose fault is that?

\----------------------------------------------------------------------------------------------------------------------------------------------------

I propose students vote on the topics discussed at these town halls. We CS
students have our frustrations, but they are NOT what the department believes
they are. The complaints described above do not represent the CS student body.

### Anant Sahai's answer
Different town halls have focused on different topics. Think about it
logically. If the department wanted to understand the full breadth and scope
of student concerns, and wanted to do so over the course of multiple town
halls, then what would be a better strategy?

A) Having each town hall be completely open and free-form as to topic, thereby
getting lots of people voicing the same issues over and over again.

B) Having a general town hall, student surveys, followed by topic-specific
town hall meetings so that a broader scope of student concerns can be heard.

(Optional technical exercise: in what ways is this like or unlike the use of
linear vs nonlinear signaling for communicating over a noisy channel? If you
get to use a noisy channel repeatedly to communicate a single Gaussian random
variable, how does the performance scale with linear approaches? What scaling
can you get with nonlinear approaches?)

The issue of course offerings and increasing the TA budget have already been
discussed. There are things being done trying to resolve this and
fundamentally, those are about getting campus to give faculty slots and TA
money to the department. Inclusivity, on the other hand, is incredibly
important and had not been discussed nearly enough. EECS values inclusion.
Language like "victim card" and the like might seem like mere rhetorical
flourishes to some of you, but such language and behavior acts as a way to
exclude many people. Humans have feelings and are social creatures.
Exclusion/inclusion is not some third-order effect for systems of interacting
humans.

(Optional technical exercise, in case simple decency of being inclusive isn't
enough: when one is designing a control system that has multiple state
dimensions and dynamics that couple them, is the optimal control strategy
going to be to only consider the dimension of the state that you care about?
Why or why not?)

The rigor of thinking that the EECS department wishes to inculcate in its
students is not limited to questions involving software or circuits or devices
or mathematical models that we give you. The goal is for you to be able to
think critically and rigorously about problems in general. One of the
important principles here is not assuming that everyone else is a fool. It's
alright to not understand something. That's normal. You might question
something because it doesn't make sense to you. That's also good. But to jump
from there to assume that the people in charge are in the grips of something
nefarious like "Political Correctness" isn't logical. It's arrogant.
*Humility* is a vital attribute for engineers. Approach questions sincerely.
*Arrogance* can be fatal in practice.

It is good that you appreciate your TAs. And it is good that you have high
esteem for your faculty. But you should also have some trust that these same
good TAs and faculty are trying to achieve something when we want to
understand how to improve inclusivity. Just because you have not experienced
something doesn't mean that it does not exist.

### Followup:
Student:
Students did vote on which topics were discussed; in several surveys.

### Followup:
Student:
@OP who asked "And what's the alternative? Hire under-qualified people based
on their race or gender?"

Actually, no, but sadly that's a prevalent misconception. There are definitely
constraints you can relax without compromising on "qualifications" to address
this issue, which AFAIK the department already does. One example of such a
requirement is compensating via the faculty's research area. You can adjust
quotas for hiring faculty in areas A vs. B to compensate for factors like this
without compromising on qualifications or merits at all.

To put it into mathematical terms, this is a dynamic multi-objective problem
with lots of soft constraints, not a static single-objective problem with only
hard constraints. So solutions like the above do exist.

Student:
+1 meritocracy is a myth

Student:
America has made mistakes. So let's learn from them instead of reinstating
discrimination.

Student:
tbh the whole merit argument is built on the assumption that everyone has the
same starting point and therefore is a self-serving meritocracy. The truth is
that we do not due to many historical reasons and whatsoever we were just not
enlightened and deprived people of right to education and equal opportunities
coz we were dumb.

While one could easily argue that political correctness has been
"overwhelming" on campus, colleges across the country, like Caltech, started
admitting female students till 1970 which is like not so long ago. The point I
am trying to make is that to break the perpetuating historical stereotypes,
one needs to have certain favorable policies or programs to make up for the
gap and I agree, it is super hard to draw the line of being "fair" and make up
to the minorities just "right", but the whole idea of "OH YOU SUCK THAT'S WHY
WE DO NOT WANT YOU" is harmful, unhelpful and ultimately unfair: if there was
no equal opportunities granted in the first place how would there be fair
competitions anyway?

Everyone likes meritocracy but plz, not a self-serving one.

Student:
"select a faculty and staff of TAs thats as brilliant and diverse as the group
of students they hope to teach."

Is this compatible with evaluating people ONLY based on their merits? Not
based on any other criteria such as their skin color? If so, I support the
idea.

Student:
There's this thing called implicit bias that has played a huge role in why
women/minority groups have had such a difficult time growing in number in
tech, or even rising to positions of leadership. Implicit bias takes form in
the subtle stereotypes or judgements that we hold about groups of people. For
example when we don't see many women in STEM fields, both at student and
professor levels, we believe that its because women are less qualified or may
not be smart enough to pursue those fields in great numbers. This notion
carries forward in how we interact with women in these environments later on,
as our first impression of them may be subconsciously clouded by this idea we
have.

So while a female professor may be just as, if not more, qualified as her male
counterpart, perhaps the individuals interviewing her had their perspectives
colored in this same way and didn't take her as seriously because she was a
woman. Representation is extremely important, not only for other girls to see
so that they understand that STEM isn't just a field for guys, but also
because it helps fight against the idea that only certain groups of people are
qualified to do something.

So no. The alternative isn't to hire under-qualified people based on their
gender. Quite the opposite in fact. We need to take into account how our
perspectives may be colored by subconscious biases, and actively look for ways
to select a faculty and staff of TAs thats as brilliant and diverse as the
group of students they hope to teach.

Student:
OP Here. Thank you Daniel for your comment.

**" It can become very easy to think  "well maybe CS just isn't for girls" if
you don't see female professors or TAs. And that point follows similarly for
other minority groups in CS."**

****

True. And what's the alternative? Hire under-qualified people based on their
race or gender? We students are paying a lot of money for a good education
here. A good education, not a politically correct one. Gender or minority
status should not be part of the equation at all. Merit is the only thing that
should matter.

### Followup:
Student:
In response to:  
"I agree diversity is important. But why are people obsessed about racial
diversity? There's also intellectual diversity and diversity of opinion which
are far more important than the color of someone's skin. Also, let's judge
people based on their merits, not the color of their skin. Racial
discrimination is illegal and immoral, and this includes reverse
discrimination. If the males on the interview board were more qualified than
the female, choose the males. Is that so controversial?"

Due to implicit bias, the interview panel may determine the underrepresented
minority candidate to be less qualified not because of his/her CV, but because
of his/her appearance. It's already shown that in academic hiring situations,
a CV with a male sounding name is more likely to be chosen for an interview
than a CV with a female sounding name, despite the rest of the CVs being
identical. Even the most "woke" among us can suffer from implicit biases based
on gender/race/accent/dress/etc. that we must constantly challenge and put
into question when interacting with others, especially during faculty
interviewing processes.  

I am nearing the end of my PhD here at Berkeley, preparing to enter the
Silicon Valley work force. I am also a petite female. When I walk into any
sort of professional situation with new people, I know that the first thing
I'm going to have to do is work extra hard to project experience,
intelligence, and authority. I love wearing dresses that look like they came
from Claire Underwood's closet, but I'm an engineer, so I should stick to
pants so that I don't come off as too feminine and get taken less seriously
(note the second half of this sentence - case and point right there). I can't
be too assertive or they might think I'm bossy; no, much better to phrase
ideas as passive suggestions with an extra shot of humility. I can't write an
efficient email listing action items without running the risk of rubbing
someone the wrong way. On my first day of EE375, I was asked (by another
woman) if I was a reader for my course. I was in fact a 5th year PhD student
and Head GSI, but based on nothing but my appearance she assumed that I was on
the bottom rung of pedagogical the totem pole. Implicit bias exists (this is
covered nicely in EE375 by the way) and we can be guilty of applying it even
to people who look like us. Thus, interview committees need to acknowledge
their own implicit biases and take them into account when weighing candidates'
qualifications, so race, ethnicity, and gender can't be ignored.

Student:
Students voted on which topics were discussed in several surveys.

Student:
CSM sections and HKN office hours are not explicitly held by TAs... get your
facts straight.

Student:
"Maybe 5-10 students in the major of hundreds are arrogant."

A disagree with almost everything you're trying to express but this is the
first thing that made me lol.

Student:
OP Here.

**EECS Master Race**

I don't know of a single EECS major who has acted condescendingly towards
another student based on his major. Maybe 5-10 students in the major of
hundreds are arrogant. It's inevitable. It's not an actual problem.

**Minority Representation**

Second off, while I agree that people should be chosen based off merits, an
important aspect to consider is perspective. People with different backgrounds
and life experiences can have vastly different perspectives that give them
insight into different problems. This is why striving to be more diverse can
strengthen the community."

I agree diversity is important. But why are people obsessed about racial
diversity? There's also intellectual diversity and diversity of opinion which
are far more important than the color of someone's skin. Also, let's judge
people based on their merits, not the color of their skin. Racial
discrimination is illegal and immoral, and this includes reverse
discrimination. If the males on the interview board were more qualified than
the female, choose the males. Is that so controversial?

**TAs**

"TAs are dismissive or lack understanding/empathy, this can be especially
difficult for those who come in without CS backgrounds or underrepresented
students"

****

TAs can always improve. But the complaint implies that TAs don't do enough for
people without CS backgrounds / underrepresented students. This is
categorically false. Do the complainers not see the review sessions that TAs
put on? Do they not see CSM sections? Do they not see HKN office hours? Do
they not see homework parties? Do they not see project parties? You cannot
complain TAs are not doing enough. Underrepresented students have the same, in
fact more, opportunities than the rest of us (they have affirmative action
internships like Facebook University).

### Followup:
Student:
@OP lmaooooo. Quote from other comment saying "the world is an unfair place,
let's give everybody more opportunities"

OK, so we had an EECS town hall about diversity and giving underrepresented
people more opportunities. But oh noooooo, now that's being too "politically
correct", those issues "don't really matter"... so the question I have is,

what does your ideal solution look like? I agree that in this situation, where
resources are limited and the world is an unequal place, sometimes lifting
people up requires some sacrifices. It's not a perfect solution. But do you
have any better ones in mind? The alternative you mention in which we ignore
these issues and focus on "merit" is so hollow. There doesn't exist a single
merit-based system in the world that doesn't favor the rich and disadvantage
the poor.

Even Asian education systems, especially in China, which started out being
very merit-based and allowing for a lot of economic mobility are now falling
apart. The nouveau rich in China afford better tutors and better schools, and
inequality is growing rapidly there. In the US, those economic stressors are
split even more among racial groups, due to a long and complicated history
with race and immigration in the US. If you think a "merit based system"
somehow decreases inequality from an economic or racial standpoint, I have a
bridge to sell you.

It really boils down to this. Is the current system equal? Obviously not. Can
it be made equal? We can try. Does a merit-based system fix this? No, it has
never worked anywhere. So what should we do? Well, let's talk about it...
maybe at a town hall...

Student:
But diversity is important, because different people have different needs
based on their background. Here's a great example: in the original release of
the Health app on iPhone's, Apple didn't include a menstrual cycle tracker.
You could track any amount of obscure vitamins/minerals/healing crystals, but
you couldn't keep track of your reproductive health. (Here's a good
[article](http://fusion.net/story/100781/apple-ios-update-new-version-of-
healthkit-still-doesnt-track-periods/) on the issue.)

Student:
OP Here.

1\. Yes, we should provide BESSA with proper funding and resources.
Absolutely. But they have no right to complain about "not having enough
students" as if that's the department's fault.

1.5. I think diversity should not be a factor at all in recruiting. Maybe more
diversity is a good thing but imagine if you were the totally qualified
student constantly turned away because clubs/companies wanted to impose some
racial quotas? Discrimination is illegal and immoral.

2\. My bad. I didn't mean "not a single student" but rather "not many
students". This is why I propose having a survey for EECS students to vent
their concerns. These PC problems will appear at the very bottom of your list.

3\. I know what affirmative action is about. It has a good purpose in mind.
But it's immoral and ought to be illegal. How can you tell someone you're
rejecting them only based on their skin color and feel happy about it?

Student:
1\. Okay, but BESSA is one such group, and you don't want to listen to their
complaints about not having enough resources. So we should expand BESSA and
provide them with more funding and resources correct?

As someone in that position, yes. I am in charge of recruiting for certain
clubs, and I still believe in taking diversity into account when deciding what
candidates to accept. It sucks, but the reality is that the various
perspectives brought in due to diversity far outweighs the difference between
a 3.5 and a 4.0 in the candidates.

2\. You are complaining about students complaining about diversity in EECS. So
obviously students in EECS have complained about the lack of diversity,
otherwise we wouldn't even be having this conversation.

3\. Yes, affirmative action is about giving disadvantaged people more
opportunities.

Student:
OP Here.

1\. True, merit only works for equal opportunity. So let's work on giving
people equal opportunities instead of punishing people who are not of a
underrepresented group / had well-off parents. We have Women in Tech, Black
Girls Code, etc movements that provide resources for women, African Americans,
etc. Let's expand those programs.

Tell me this. If you're an Asian EECS major, 4.0, aced all the interviews, but
keeps getting rejected due to the color of your skin, would you still support
affirmative action then?

2\. I have not heard a single student complain about diversity in EECS.
However, I always hear students complain about long waitlists/not being able
to take classes they want/no tuition waiver as a TA. In fact, browse the past
history of this EECS 101 piazza and compare the number of these complaints to
complaints of "not enough diversity / pro-affirmative action"

3\. And not everyone has the same opportunity to be a lawyer. Or a doctor. The
world is an unfair placd. The way we make it fairer is to give everyone more
opportunities rather than snatch opportunities from people.

Student:
1\. How do you even define merit. How do you compare the 'merit' of 2 people
if one of them went to a rich private school and has been taking coding
classes for 5+ years while the other couldn't even afford a computer? Merit
only works if everyone has equal opportunity, which is not the case.

2\. Where is your data that a majority of students don't care about these
problems? Have you managed to create an accurate/representative poll of
undergrad EECS/CS majors? And just because the problems presented only affect
a (sizable) minority of students, we should completely ignore them? A problem
is still a problem even if it affects <50% of the students.

3\. Not everyone has the same opportunities to enter tech, which is what leads
to the lack of diversity in the first place.

Student:
1\. This is off topic but why should the admissions office consider economic
status? Merit, and only merit, should be considered. Not wealth, not race, not
anything else. Diversity is nice but merit comes first every time.

2\. As I mentioned, this issue doesn't affect me and most CS students. Most
students want the department to focus on the problems that actually exist and
affect our education rather than solving politically correct problems which
aren't actually problems.

3\. Lack of diversity is real, the numbers don't lie. But so what? If everyone
has the same opportunities to enter tech, then why does it matter if most
people in tech are male or Asian/white? Lack of diversity is not a problem.

Males are disproportionately represented amongst construction workers. Does
that mean discrimination against women?

Females are disproportionately represented among teachers. Does that mean
discrimination against men?

No, it's just people gravitating towards fields they're interested in. No need
to politicize everything.

Student:
1\. How do you determine who is qualified enough to get acceptance into
Berkeley EECS? Based on what people did in high school? What about the people
(mostly underrepresented minority students) who didn't have the opportunity to
do any CS or EE in high school? The admissions office doesn't even consider
race, but it does consider economic status, which is strongly correlated with
race. And that leads to more diversity. And it starts from the bottom up: less
diversity in undergrads --> less diversity in TAs.

2\. Who are you to decide what the professors spend their time on? We just had
a town hall last semester about the lack of funding for EECS (covered course
shrinkage, long waitlists, etc). And just because this issue doesn't affect
you doesn't mean that it doesn't matter.

3\. HKN doesn't even get money from the department. " _for a problem that
doesn 't exist"_ what problem are you referring to? The lack of diversity?
Because that is a very real and well-documented problem in tech.

Student:
We complain about it for three reasons.

1\. **Their arguments aren 't logical. **I don't see how Berkeley EECS has a
diversity problem. We choose the most qualified students, TAs, and Professors.
If that means less diversity, fine, but there's no problem. And most of their
concerns are frankly absurd, like the BESA thing. Please pinpoint an _actual_
problem first.

2\. **Don 't waste town halls. **If you have legimitate concerns, you should
be welcome to bring them up. But you don't need a town hall with Professors.
We don't have town halls on the issues EECS students care about, but we have
town halls on this. Faculty time is limited and should be spent on the issues
that matter.

3\. **It 's not a zero sum game. **If the problems brought up in these town
halls are "solved", you hurt 99% of students. Taking money from HKN and giving
it to BESA _for a problem that doesn 't exist _means HKN doesn't offer
tutoring, provide cookies after exams, or shuts down its exam archive. Hiring
TAs based on their skin color rather than merit _for a problem that doesn 't
exist_, not only is illegal and immoral, but it also deprives us of a good
education.

So yeah, we care. Because it hurts us all.

Student:
So. The first time I _ever_ see an EECS department townhall dedicated to
addressing marginalized folks ' concerns, someone has to post a complaint
about it. Your complaints about class sizes and tuition are valid, of course,
but dragging underrepresented folks down too? The many times I've seen people
request classes be expanded, on Piazza or elsewhere, I've _seen_ staff do it.
They 've LISTENED to you. Expanded classes. Answering demands on future
classes offered. But this is the first time I ever hear **anyone** talk about
diversity. Not even concrete plans to do anything. Just a townhall to
**talk**. But this post blows it up as though we were donating half the
department 's funding towards a student group. How selfish, to begrudge us
that.

### Followup:
Student:
i don't see any other major which has as much demand as CS, especially one
with as much sudden _increase_ in demand, so what 's your point?

Student:
I don't see any other major which has such a huge waiting list problem as
EECS. Look it up, it was documented in the Daily Cal.

Student:
You should read more about that protest a few months ago. I'm usually against
the extreme liberalism of Berkeley, but those student groups had very valid
complaints.

I don't really know what the Milo incident has to do with this post. A large
majority of them aren't affiliated with Berkeley.

EECS is no less underfunded than all of the other departments at Berkeley. We
might actually be better off than most; at least admin didn't try to dissolve
our college like they did with College of Chem. A department town hall isn't
going to do anything when the problem is at a much higher (regents, state)
level.

Student:
Thank you for your comment.

"How can we more regularly offer courses [like CS 288]? How can we deal with
long waitlists? How can we afford more tuition waivers for TAs?"

**I wish these problems were discussed more as well. If you asked these
questions at a town hall, I bet a good chunk of the audience would think to
themselves, "what stupid, annoying questions".**

****

I disagree with this, however. A good chunk of the audience would be delighted
to hear their actual concerns being addressed. EECS students are tired of the
political correctness taking over Berkeley.

Few months ago, we had protesters block Sather Gate because they wanted a
"sexuality center" or waste of money like that. Then they stormed the Student
Store. And guess what? They succeeded. Meanwhile we our department is
underfunded, we can't even get into the classes we want, and the classes we
want to take aren't available for us.

Then, earlier this month, antifa's / anarchists destroyed our Amazon ASUC
because they couldn't deal with someone exercising their right to free speech.
Later on, these groups justified their violence in the Daily Cal.

### Followup:
Student:
steven, here is the full citation

National hiring experiments reveal 2:1 faculty preference for women on STEM
tenure track  
Wendy M. Williams and Stephen J. Ceci  
Department of Human Development, Cornell University, Ithaca, NY 14853

which i cite only with respects to the study which you cited (at least the one
which i believe you cited, since if you did post a link, i cannot see it
either) which in my view suffered from methodological flaws

Science faculty’s subtle gender biases favor male students  
Corinne A. Moss-Racusina,b, John F. Dovidiob, Victoria L. Brescollc, Mark J.
Grahama,d, and Jo Handelsmana,1  
Yale University, New Haven, CT 06520

Student:
Can't see that link / use the Berkeley proxy anymore, since my CalNet account
expired.

I can't talk personally about discrimination about women professors, because
I'm not one. I'll note that I haven't taken a single CS course with a female
professor, which does say something about the department.

Otherwise, see all of anon's comments above.

And we're _currently_ in a world where people equally qualified of other races
and genders never even get to develop their skills and change the world,
because they aren 't represented and given that opportunity.

Student:
It's unproductive to say that some method has not shown perfect results, hence
we should end that strategy and instead do nothing.

Discrimination against female professors is not easy to prove on such a small
level but we know that there is unconscious (and some conscious) bias against
women across STEM fields therefore there is unconscious bias against women in
CS, and unless you can actually argue otherwise, there is the same bias
present at UC Berkeley. This is something that is large and institutional and
takes place at many levels.

You discuss qualifications like they are an objective standard. Minority
groups benefiting from affirmative action often will not be evaluated equally.
No single decision will be obviously sexist, but the net result will be that
female professors almost always end up not being chosen if qualifications are
basically equal, and a choice of either candidate would be defensible.

Student:
OP Here.

Thank you for posting that link. It shows that even with affirmative action in
place, we don't have too many women as professors. So affirmative action is
clearly not the solution.

UC Berkeley doesn't discriminate against women professors. Give me a single
example of discrimination against women professors here. It doesn't exist. We
choose the most qualified people and that's it. Berkeley won't be the greatest
public university if we start focus on creating a politically correct
education rather than a good education. Do you want a world where the Sahai's,
Papadimitriou's, Patterson's and Denero's of the world can't get tenure
because they weren't "underrepresented" enough?

Student:
"National hiring experiments reveal 2:1 faculty preference for women on STEM
tenure track"

<http://www.pnas.org/content/112/17/5360>

dunno the degree to which this generalizes to the private sector or to our
subfield but even on this forum i've heard the claim this institution
discriminates against female faculty both in hiring practices and career
progression

### Followup:
Student:
1) This doesn't violate the constitution. Fisher v. University of Texas at
Austin

2) Decentralizing a process makes something naturally diverse. If SWE can hold
interview boards separately from HKN that already improves the diversity
without diluting HKN's quality.

Student:
OP Here.

There is a limited number of positions on interview boards and course staff.
So we have to deal with this scarcity somehow. The way Berkeley currently does
it is chose the people most qualified for the position. What most people are
suggesting here is "let's have qualified people, but also add women/minorities
even if they're not qualified."

No. This is discrimination against men/Asians/whites based on
gender/ethnicity. It is immoral and illegal under the US Constitution.

Student:
But there's a difference between affirmative action in tenuring Professors and
having women/minorities on interview boards and on auxiliary course staff.
Diversity is not some binary thing where it exists or doesn't exist. There are
clear areas where introducing diversity doesn't diminish quality that we can
improve on.

Student:
OP Here. I sympathize for your experience growing up. I do. But affirmative
action doesn't solve the problem you describe. Do you think people of other
races are going to like you more if they are rejected for jobs _they are more
qualified for_ , just to meet some racial quota?

I understand the value of diversity like everyone else here. But I don't want
to force diversity upon students and diminish the education they are paying so
much for. Do you want a world where the Sahai's, Papadimitriou's, Patterson's
and Denero's of the world can't get tenure because they're not
"underrepresented"?

### Followup:
Student:
One poster claimed that Asians are "extremely well-represented in tech". While
that may be true for entry-level or low-level jobs it's not true for
management or executive positions (see
<http://www.csmonitor.com/Business/2016/0928/In-its-drive-for-diversity-is-
the-tech-industry-neglecting-Asians>). I had the chance to sit in on a Google
executive meeting and about 70% were white males, 29% were white women, and 1%
were Asians/other minorities. For whatever reason even white women outnumber
Asian males in tech management / executive positions.

Student:
**There are ways to improve diversity without diluting talent**

****

I disagree. Either you value diversity the most or you value talent the most,
there's no "middle ground". I choose talent the most because I (along with the
majority of people) believe people should be chosen on their merits and not on
their skin color.

**Because we are not in construction or teaching or law. We are in tech. This
distinction should be simple enough.**

Fair enough. My point is, I've never heard for "Men in Teaching" or "Women in
Construction" movements. So there is some hypocrisy.

Student:

    But it's not about helping them, is it? It's about some people who play the victim card for self gain. It's easier to complain "my group is underrepresented in tech so hire me though I'm not qualified" than do the work and get the job fairly.

That is not happening in 99% of tech companies. There are ways to improve
diversity without diluting talent.


​    
    Instead of harassing Asians in tech based on their skin color why don't you help these underrepresented groups too? 

Because we are not in construction or teaching or law. We are in tech. This
distinction should be simple enough.

Student:
OP Here.

Post above isn't mine but I strongly agree with it.

1\. It's not "alarmist rhetoric". The student is just expressing non-PC
opinions. If people have the right to speak for gender + race discrimination,
so do people who don't support affirmative action.

2\. So what if Asian males are well represented in the tech community? These
are people who work hard to get into top schools, work hard to get
internships, work hard to become TAs, and work hard to become software
engineers. It's not discrimination. Why don't people mention the fact that
women are underrepresented in construction? Or men in teaching? Or Asians in
farming? Or Hispanics in lawyers? Instead of harassing Asians in tech based on
their skin color why don't you help these underrepresented groups too?

But it's not about helping them, is it? It's about some people who play the
victim card for self gain. It's easier to complain "my group is
underrepresented in tech so hire me though I'm not qualified" than do the work
and get the job fairly.

Student:
Way to hijack this post with your alarmist rhetoric. Asian Males are still
extremely well represented in the tech community, and that doesn't look to be
changing anytime soon.

### Followup:
Student:
if you want more black students in computer science, then you should go to
poor high schools and tell kids that they will be able to double or
potentially triple their family's household income by going to a community
college and then transferring and getting a degree in computer science. speak
my language by telling me what's in it for me. i think it's superficial and
extremely condescending to say that people need to see people who look like
them (but otherwise have absolutely nothing in common with them) to recognize
that this is a great (if challenging) path to walk in life.

Student:
No they are not.

1) More interview boards can established and hosted by different
organizations, so at least some of the boards are diverse naturally be
decentralizing the process

2) But this person wasn't asking for a Minority Women professor to be hired
immediately. It just expresses a feeling that they have. Feelings aren't
action items alone.

Student:
"When [a female student] suggested including a woman on the interview board
for one of these organizations **she was told that "men and women don't
interview differently" so there’s no need to include a woman on the board, and
that she should "stop pulling the girl card for everything**."

**" As a female and a minority I definitely feel like I don't belong when none
of my TAs or professors look like me.** **"**

****

These statements clearly suggest people want to choose
professors/TAs/interviewers/etc based on the color of their skin or gender
rather than their qualifications.

Student:

    And making it more equitable doesn't require discriminating against people based on their gender or race.

People keep saying that, but none of the proposals taken seriously suggested
this. There are ways to be more inclusive without affecting the quality of
something

Student:
The world can be made more equitable. It can never be made completely fair.

And making it more equitable doesn't require discriminating against people
based on their gender or race.

Student:

    That's the way the world is and it can't be changed. 

If that's a fundamental view of yours, then you'll never understand the point
of any of these culture town halls. And there is no further use explaining it
to you. But a lot of us don't hold that belief, and believe the actions we do
here are Berkeley can break this cycle.

Student:
Look, the fact is the world isn't a fair place. Barron Trump has advantages
I'll never have. And I have advantages an African American student in inner
city Chicago doesn't have. That's the way the world is and it can't be
changed. We can provide more opportunities to people, like "Black Girls Code",
"One Hour of Code", etc, (which by the way are well-funded and promoted by top
politicians including the POTUS, so you can't complain there aren't role
models) but we can never create a fully level playing field.

Ultimately, success in life comes from self motivation. Even if there aren't
many role models for Black students, if they truly like CS, they can learn
themselves. You have middle school kids these days making top 100 App Store
apps. You have to try. Don't expect anyone to force you to.

Student:
And why is it that Black students feel discouraged from pursuing CS. It's
because there aren't role models in the US for them. This is a long term,
cyclical issue.

Student:
It's society's fault. Look at high schools that are majority Asian/white
compared to those that are majority African-American/Hispanic. Look at which
ones have computer science programs that can get high school students
interested in CS. You can't be interested in CS if you were never exposed to
it in the first place.

Student:
Still, whose fault is that? Whose fault is it that African American students
are not so interested in CS? It's no one's fault. So instead of them blaming
the department for not discriminating, we could be discussing issues students
care about.

Student:

    "Students from BESSA (Black Engineering and Sciences Student Association) expressed that they feel that enough is not being done....Reported that BESSA lacks the resources to provide services like tutoring, given their few numbers."

This complaint isn't to due with their specific organization. They feel there
aren't enough Black Students period for them to recruit from in the first
place. There is a difference between playing a victim card, and demonstrating
that an issue is out of your hand.

### Followup:
Student:
Empirically speaking based on this post, diversity is clearly a concern that
EECS students do have.

Student:
I will defer to you as I didn't organize the budget town hall :)

I'm not insisting on more budget town halls at all. I just want these town
halls to address what students actually care about. If students care about
BESA's problems or TAs being not sympathetic, while personally I believe these
are non-issues, I support discussing them in town halls.

But the topics of town halls should not be forced onto students. The CS
advisors, who are some of the greatest people I've met here, by the way, sent
out a "culture survey". My point is, our discussion shouldn't be restricted to
"EECS culture" but whatever concerns EECS students have.

Student:
To be honest, as one of the organizers from HKN, I think the "budget" town
hall was a waste of time. That issue is completely outside of our (and the
department's) control, and just talking about it isn't going to accomplish
anything.

On the other hand, students and the department can actually do something to
help improve the culture in EECS, meaning these town halls can have tangible
results.

Student:
Why do these need to be mutually exclusive?

### Followup:
Student:
+1, you tell 'em :)

Student:
https://www.scientificamerican.com/article/how-diversity-makes-us-smarter/

Student:
Anon:

I'm the author of this post.

First of all, I mentioned I'm a CS and Physics double major because I wanted
to refute OP's argument that I don't want to work hard and get the job fairly
so I'm complaining that I should be hired despite not being qualified just
because I belong to an underrepresented group.

You said yourself that I'm "probably already in the top 1% of Berkeley
students" — so that means I'm qualified. And as for working hard: there's no
affirmative action for SAT scores or GPA, and Berkeley does not practice
affirmative action in admissions. I myself got the test scores needed to get
into Berkeley with a scholarship, despite having a weak educational background
(my formal education ended with the second grade), then the GPA needed to
declare the CS major and the skills needed to get research positions and an
internship. How did I work any less hard to get where I am than any of those
white/Asian males you're talking about in your last paragraph? Do you still
want to imply that all of them are working harder than I am and I'm still just
playing the victim?

Second of all, when did I ever say that women and underrepresented minorities
are the ONLY ones who can be disadvantaged? I'm Asian-American myself, so I
definitely aware that there have been cases of racism against Asians in tech
(see the U.S. Department of Labor suing Palantir for anti-Asian
discrimination, and Trump's top advisor, Steve Bannon, saying that there are
too many Asian CEOs in Silicon Valley, when in fact Asians are
underrepresented in management — and you're still advocating for re-electing
Trump?). I also know that many Asian-Americans come from impoverished families
with parents who may be refugees or who haven't even completed high school
degrees, and that people of all genders and races can come from poor
backgrounds with lack of educational opportunities. I'm not saying that if
someone is a white/Asian male, they automatically face 0 problems, ever.

However, as a white/Asian guy in tech, you will never get comments from your
coworkers about what you're wearing, or messages from your boss harassing you
for sex. You will never get coworkers telling you how unfair it is that you
get a "vacation" when in fact you're taking maternity leave to have a child.
You will never get your classmates or GSIs assuming that you're less
competent, ignoring what you're saying, interrupting you to tell you things
you already know, and asking you whether you're sure you're in the right
classroom, just because you're a girl in a dress. You will never look around
the room and feel like you're the odd one out and like you shouldn't even be
here.

Is it true that some women and underrepresented minorities don't make it in
tech because they're not interested or don't work hard enough? Definitely. But
are you really going to say that white/Asian males just naturally have _so_
much more interest and _so_ much better of a work ethic that it 's the ONLY
reason why they make up the majority of tech? If you think about it, wouldn't
it be more logical to conclude that there are also other factors at play —
such as gender/racial biases, feeling unwelcome in tech, and some races being
statistically more likely to be disadvantaged than others?

Lastly, whether or not the majority thinks "my group is underrepresented in
tech so hire me though I'm not qualified" is the right way to go (and how do
you know that's true; where are your statistics?) — I don't care. My opinion
here is that no one gets a free pass. Everyone has to work hard if they want
to succeed. But what you're failing to recognize here is that it's not a level
playing field. It's not true that everyone has completely equal chances of
succeeding, and that if someone doesn't succeed it's always because they
didn't work hard enough, and never because of other factors. I'm not devaluing
hard work. I'm saying that we need to acknowledge these inequities exist and
take steps to solve them, so that every person's hard work can be properly and
fairly recognized.

Student:
It's clear that your definition of a successful society is very narrow and
shows your limited worldview. When you have people who all come from the same
background and all think the same way, how can you expect them to truly
understand the other 90% of the world? When they choose the kinds of products
and services to design and implement, when they decide what is necessary to be
created to improve society, naturally they will only relate to their own
experiences, like you are doing right now, and use them as basis to form
judgments of what technology should be created and how society should operate.
Japan, although strong economically and in tech, still cannot compare to the
innovation of diverse America and will never come close to the worldwide
impact of America with only homogeneous and singular views. If you want
technology that only benefits a specific group of people and doesn't fully
consider the needs of others, continue with your fixed mindset that the world
will never be equal and that diversity is useless and doesn't contribute to a
successful society. It's pitiful that you've adopted such a pessimistic and
narrow-minded view.

"If they want to do tech, then do tech." Again, you're ignoring all of the
social factors that discourage people from even wanting to do tech in the
first place. And even when they decide tech is something worth their time to
pursue a career in, they face obstacles that pull them away from the field.
Which you should perceive as a bad thing, unless you're still stuck to the
ideology that diversity is useless.

Student:
There's little to no evidence to suggest that racial diversity is necessary or
better for tech or society in general. Japan is one of the most homogeneous
countries in the world, but have one of the largest economies and leads in
science and discovery. Nobody is asking women to go into medicine or nursing.
If they want to do tech, then do tech. You people have to stop being special
snowflakes and accept that the world isn't equal. And yes, it's a sick
narrative, because it doesn't exist.

Student:
The fact that she's succeeded only STRENGTHENS her argument. What is there to
complain about if she's successful? That should mean there's no problems, and
everything is fine, right? Wrong... so wrong.

Women face biases all the time. Immediately, when you see a female in tech,
especially a stereotypically attractive and feminine woman, you judge that
she's less competent than a man. Intelligence and competence are highly
associated with masculinity. Beauty and brains don't go together. When girls
grow up, they feel this pressure all the time--the pressure to choose between
being beautiful and being smart. Our society still objectifies women and
attaches their physical beauty to their value as people, more so than men. And
this is made worse by the relative lack of female leaders and role models in
tech. Girls grow up thinking they don't belong in tech, and this is why they
choose other, more stereotypically feminine careers such as medicine or
nursing, over tech. This is why there are programs to encourage females to
stay in tech. Because technology plays such a large role in defining how our
society works, and diverse perspectives are needed to help shape society.

Please open your mind to perspectives and experiences that aren't yours. It's
not bullshit or some "sick narrative of victimhood." The statistics showing
the lack of diversity in tech aren't bullshit. If you agree that no one gender
or race should dominate any single field, then be supportive of attempts to
integrate varying perspectives into tech. No one is hurting your ability to
succeed in your tech career away by encouraging others, who didn't grow up
with parents or friends or role models in tech, to consider tech.

Student:
The fact that you have succeeded as a Physics and CS major detracts from your
argument. You are probably already in the top 1% of Berkeley students. You can
play the victim card all you want, it's the popular thing to do nowadays. I
will never be convinced that you, because you are a woman, have been
significantly affected because of it. Is there sexism and racism? Of course,
but I'm not convinced that here in the Bay Area, it's this huge problem.
There's this notion that minorities, women, have it so bad, worse than other
genders or races. It's just not true.

"I am not, as OP is saying, "complaining 'my group is underrepresented in tech
so hire me though I'm not qualified'"" That's a load of BS. If you look
around, you will see that's exactly what they (the majority) want.

There's really no point continuing this argument. You and all the others here
have swallowed the sick narrative of victimhood, and I don't blame you, the
recent election must have really gotten a lot of people on the edge. But he
wasn't elected because of racism or biases, he was elected because of things
like this sick narrative of victimhood. But keep pushing it! It worked so well
last time.

To all the current students who feel disenfranchised here, whether you be
white or Asian or something else, I sympathize with you. Just remember to vote
in the next election. if you think these people have your interests in mind,
forget it. Remember these people want to kick you out because of you work too
hard. Your hard work doesn't matter. Asians aren't diverse. Poor whites are
privileged. For our vendetta we can only hope that Trump gets reelected.

Student:
+1!

Student:
+1 !!!!

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1 Wya OP

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
BOOST.

Student:
+1

Student:
Thank you so much for writing this. +1!

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
4 hours and still no rebuttal?

Student:
+1

Student:
Would like to hear OP's response to this

Student:
+1 <3

Student:
+1

Student:
+1

Student:
+1

Student:
+1

### Followup:
Student:
Prof. DeNero I would love to take CS 288 with you!

Student:
Professor, thank you for taking the time to personally respond to this thread.
It shows how world-class EECS faculty members are. They make you suffer a lot
to make you learn but students grow stronger due to it. So thanks.

Professor, please do consider teaching CS 288 in the near future! We are all
dying to learn Natural Language Processing. I saw your enthusiasm while
teaching language translation at the end of CS 61A. I would give my right
kidney to take CS 288 with you.

### Followup:
Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

Student:
+1

### Followup:
Student:
Several thoughts @ latest anon:  


> Sure, you might get to argue the merits of Aristotle's vs Kant's views of
> morality...

It doesn't seem like you've taken an ethics course! Engineering ethics aren't
frequently taught in abstract utilitarianism/deontology debates (especially
those as anachronistic as Aristotle & Kant), but rather via more recent
scholarship and various case studies. CS 195, for example, does a great job of
this.

> ...but does that make you a good person?

This is a straw-person argument. Nobody (in this thread or otherwise) is
making the claim that requiring an understanding of ethics makes everyone good
people automatically––clearly even engineers who understand ethics can and do
make unethical decisions.

Ethics courses offer a combination of frameworks (e.g.
deontological/utilitarian thought) and postmortems that are helpful for people
who want to be good. When we, in our careers, ask ourselves "am I making the
ethical decision? am I a _good person_ if I build this tool?, " ethics
requirements will have built the skills necessary to answer those questions to
our own satisfaction. Feel free to make the claim that this thinking is
trivial and can be achieved via some good ol' fashioned engineering
intuition––the thousands of years of moral philosophy you cite, an extremely
dense recent interest in STEM ethics (esp. bioethics), and various ongoing
violations of ethical standards in STEM indicate otherwise

Whatever "good" means, that is.

> If that was the case, politicians across America would be scrambling to
> offer this magic solution to their criminals.

This is a red herring. Ethics classes exist to make engineering students more
ethical engineers; if whatever "criminals" you're referring to are engineering
students (they very well might be), then engineering ethics classes make a lot
of sense for them!

Furthermore, even if we take your extension as valid/logical, there are lots
of programs teaching moral philosophy and ethics in American prisons as part
of rehabilitation/education programs.

And, finally, since when are politicians experts on engineering ethics? Why do
you defer to their authority? This impulse seems misguided, especially given
the various violations of engineering ethics that have been and continue to be
commissioned by a number of governments.

> You want more ethical people, I get it, but my point is forcing someone to
> take a ethics class defeats the point.

Yes, it is good when people are ethical. Is your argument that exposing people
to ethics will cause them to be unethical? That it'll have no impact on their
personal ethics? You haven't indicated either, even in your fallacious
comparison.

Student:
I don't think taking an ethics course makes someone a better person per se.
Sure, you might get to argue the merits of Aristotle's vs Kant's views of
morality but does that really make you a good person? No. Making someone a
good person isn't as simple as having them take a class. If that was the case,
politicians across America would be scrambling to offer this magic solution to
their criminals. You want more ethical people, I get it, but my point is
forcing someone to take a ethics class defeats the point.

Student:
+1

Student:
+1

and better curriculum in general (I heard LSCS does not even have the 1-unit
ethics requirement as EECS major does)

Student:
+1

Staff has the most responsibility to establish the culture, educate students,
and broaden their worldviews.

Student:
+1

Thank you Chonyi, I hope that what you've mentioned materializes into concrete
action items from the department's end & are institutionalized with a
transparent timeline.

From my experience as serving as an ASUC senator, the fact of the matter is
that student's come and go, they graduate, we graduate - but the one constant
that will always remain is the Department, the one constant that can be shaped
to reflect the impact & culture that we want to have lies in the Department
which has a large role in our education from inside & outside the classroom.
The Department is in a position to implement these ideas that Chonyi has
mentioned, we have dedicated roles within the administration to spearhead
these issues - when can we begin?

Student:
and since this is such a common sentiment and we have already recognized that
people are not content with the current climate, I think it makes sense for
the department to take some responsibility in educating people within the
department because these people largely contribute to the climate.

### Followup:
Student:
Merhdad is right about the fact that the goal here is to correct systemic and
historical biases. But, I think the goal of programs directed at certain
individuals go beyond affirmative action practices.

When I said it removes tensions, I meant in the context of that particular
environment, not across society. However, I sincerely doubt that these
programs do increase racial, economic or other divides in a meaningful way.
Why is OK to group 'disadvantaged' into one large group or to not consider
race? I would agree that socioeconomic status is probably a better indicator
of disadvantage, but it's so intertwined with race, that I don't think it
matters much in aggregate.

But furthermore, 'disadvantaged' is a catch-all term, like marginalized that
captures dozens and dozens of different disadvantages. While the blind and
visually impaired have instances of discrimination and microaggressions,
they're not same struggles that black youth, or Latinxs, or any other group
face, even though they're in a similar category.

Specific programs give people a place to share and grow and hopefully include
support without the discomfort of needing to explain to others the struggles
they've encountered. For example, while I would to teach CS at many of them,
my presence would be an active distraction for many of the students.  

If as a society, we segregated ourselves all the time, in every way, then
you're right that'd we probably be in a worse position overall. But programs
that address a specific group aren't designed to replace people's interaction
with others - they're a temporary. Someone who goes through an internship
targeted at women, will almost certainly be working with and interacting with
and possibly even dating men then or in the future. Additionally, people are
intersectional, I don't believe that individuals in these programs see
themselves as only that adjective.

Finally-- the the quote "people don't see race". People absolutely notice
people who don't look or act like them. It doesn't matter whether you think
you're an enlightened person; we all have unconscious biases we are (by
definition) we are unaware of. What do you think when you walk by a homeless
person, or see a group of African American dancers on BART, or someone using a
red and white cane, etc, etc? Some of these things you and I probably think
are normal, but for some of them we have instinctive reactions we probably
don't even notice. It's very difficult to become aware of these things, but
damn, I've carried around some very ill-conceived thoughts and reactions.

Student:
@^Anon: Affirmative action is not aimed at the individual, or at the present
for that matter.

What a _lot_ of people seem to miss is the fact that the point of affirmative
action is to attempt to compensate for _historical_ , systematic
oppression/discrimination against a people. The idea is, when you oppress a
group of people for hundreds of years and then realize you've been doing
something morally wrong, you can't just stop, apologize, and then pretend as
if that is sufficient to right your wrong... you actually need to compensate.
This may or may not involve some intermediate effects such as increasing
diversity or helping the needy/poor, and one might argue those are themselves
noble goals worth pursuing, but they are side effects, not the goals
themselves here. The goal is to right a historical moral wrong, and its scope
and effects extend beyond individuals or the current generation. If the
present was similar but the history wasn't there, affirmative action could
very well not be there either.

Student:
Michael, thank you for writing such a detailed answer.

I would disagree that the programs you mention remove racial/gender/economic
tensions. They increase them. People don't usually look at people based on
their race but when you divide people into groups like this, and give specific
groups opportunities, then you interracial anger that never even existed in
the first place. There should be special programs for the disadvantaged in
general, so dividing along economic lines is fine, however let's not make
assumptions like "he's a Latino student, hence we need to help him out instead
of this poor white student".

Student:
Ok to the questions:

Edit: mixing up my piazza posts. lol. Just like the ol' days.

Perverse Incentives to Lie.

I like to think of this the same way I deal with cheating as a TA/Instructor.
My experience is that most people don't cheat, and most cheating doesn't tip
the scales in a significant way. Regardless of whether you add race or gender
to the mix, what we're talking about is people cheating an application system.
People can (and do) do this already. However, the question is about prevalence
and the how effective the cheating is. Most people don't lie, and those who do
lie about their race or socioeconomic status or fabricate essays for college
were probably not as strong of applicants to being with. I also very much
fundamentally believe that most people are well intentioned and not evil. That
helps me stay grounded at times..because:

People lying to gain an advantage is a real problem. Turns out, for a nominal
sum of cash (say $1500) it's pretty easy to get certified as having ADHD.
Aside from the access to prescription drugs, this enables people to unfairly
apply for disability accommodations. 150% time on a test can certainly be an
advantage when you're not using it to overcome a disability. The result of
this, is that getting accommodations can be excessively difficult. It took
nearly a year (and letters and phone calls from my parents to many people at
the College Board) to get approved, and they still eff'd up my SATs and AP
tests many times.  

So, the consequences of these actions are real. To me, the solution is that if
you find someone is lying or cheating, you punish them. When it comes to race
(and even more so, gender identity) is can be difficult and touchy to verify,
but if a company has a problem that is so bad to the point where they need to
take these measures, I think they can communicate with applicants about their
process. I would much rather see process try to adapt to be equitable, and
then correct their mistakes instead of trying nothing at all. In my view: if
an application asks for a gender, and it's progressive enough to even include
an option for transgender, I just can't fathom that many people (I just say
it...) are fucked up enough to co-opt the incredible struggles of the trans
community for their own gain? I'm not saying it won't happen, but until it
happens on a big scale, I personally think the impact that you make by being
equitable would outweigh the potential costs.

However, the other option is to change the incentive structure. Getting a job
will always have a high financial incentive to it, but I think it just means
that we have to adjust the process to lower the stakes. I read that the
average American now has 10 jobs before they're 40. This hopefully means that
landing in the wrong first job won't be such a deal. It's part education and
part process change that I think can ultimately solve the problems.  

On programs that are only for a certain race or group:  
I don't personally have strong feelings about these overall. My personal
belief is that the more we interact with others not like us, the more we will
collectively understand each other better. However, programs that cater to a
specific demographic and be extremely successful. In the space on early-CS
education there are a number of programs such as CODE2040, Black Girls Code,
AppCamp for Girls, Level the Playing Field Institute. These programs are, in
part, able to achieve success by simply removing the racial, gender, economic
and other tensions so so they can focus on their goals of teaching
programming. In think internship and scholarship programs that are structured
the same way are also a necessary component of progress. They give people
opportunities they otherwise wouldn't have. And in terms of resources, I don't
think those programs typically take away spots from everyone else - I think
they're more of an additive thing. Like "we're going to do this extra effort
because we believe in this case", such that if not centered around a
gender/ethic/etc issue, then there wouldn't be a replacement program.

Student:
_The last section that was cut off:_

It's possible, in fact I'd say extremely likely, almost certain, that the
resource allocation is biassed towards the majority. This isn’t necessarily
nefarious, more a byproduct of societal and system imbalances. It’s true that
there may be some “give and take” in terms of what needs to change to be
better supportive of more groups and individuals. We are all (or were)
struggling college students and trying to get into classes. The unfortunate
reality is that some groups experience disadvantages that others do not. You
can claim this is natural, and to an extent you’d be right. However, what’s
not natural are the extreme gender and racial imbalances in our program (and
others). What’s not natural, is recognizing that discrimination exists, but
ignoring to do anything about it.  

What’s different about the issues now, is that there are a critical mass of a
bunch of different marginalized groups. Keep in mind that not everyone at
these town halls and social hours is experiencing the same struggles and
difficulties. It’s a wide range of issues, but there are very common unifying
elements that I believe demand the attention of everyone in our community.
While I was not at this town hall, I was at the one immediately prior, and so
far these have been the two best attended town halls in my recent memory. The
have been better attended by faculty, staff, students, and administrators.
There were a couple years not too long ago where the department didn’t have a
town hall because attendance was so low.

Finally, I wanted to reiterate that these topics are tough and I truly mean
that my inbox is open if you’d like to send a message.

Thanks for reading. <3.

—

Follow Up:

It was brought to me that my comparison to advocating for diverse political
view points on campus is an unfair comparison. I was not trying to convey nor
imply that those with traditionally conservative viewpoints have faced the
system biases that other marginalized groups have. That’s not fair comparison.
I was trying to convey that we ought to have diversity in many ways. People
are intersectional - “the isms” cross many different boundaries that can apply
to people in many ways. We need to make sure that those who are not like us,
are included in our communities.

Student:
Also, Michael, how would you suggest we deal with people lying about their
race to gain advantage in tech? This has been happening in university
admissions for a while and also in politics (see Elizabeth Warren). Based on
the increasing advantages being a minority student in tech holds today, just
based on recruiters actively reaching out to you, the incentive to lie about
one's race is growing.

Student:
Michael, thank you for your post. You mentioned tech companies are reaching
out to minority groups more, which is great. What are your thoughts on
internship / job programs that only accept minority students, however. Some
internship programs are reserved for minority students, just based on their
race, which is a large cause of the anger felt by the OP and others.

Student:
Omg...did I hit a piazza post limit. This got cut off. That's embarrassing.

And frustrating. :( I'll re-add the rest later.

Student:
+1!

## Can CS Town Hall meetings be webcasted?

2017-02-26
I have a lecture conflict on Tuesday.

Thank you!

### Anant Sahai's answer
Different town halls have focused on different topics. Think about it
logically. If the department wanted to understand the full breadth and scope
of student concerns, and wanted to do so over the course of multiple town
halls, then what would be a better strategy?

A) Having each town hall be completely open and free-form as to topic, thereby
getting lots of people voicing the same issues over and over again.

B) Having a general town hall, student surveys, followed by topic-specific
town hall meetings so that a broader scope of student concerns can be heard.

(Optional technical exercise: in what ways is this like or unlike the use of
linear vs nonlinear signaling for communicating over a noisy channel? If you
get to use a noisy channel repeatedly to communicate a single Gaussian random
variable, how does the performance scale with linear approaches? What scaling
can you get with nonlinear approaches?)

The issue of course offerings and increasing the TA budget have already been
discussed. There are things being done trying to resolve this and
fundamentally, those are about getting campus to give faculty slots and TA
money to the department. Inclusivity, on the other hand, is incredibly
important and had not been discussed nearly enough. EECS values inclusion.
Language like "victim card" and the like might seem like mere rhetorical
flourishes to some of you, but such language and behavior acts as a way to
exclude many people. Humans have feelings and are social creatures.
Exclusion/inclusion is not some third-order effect for systems of interacting
humans.

(Optional technical exercise, in case simple decency of being inclusive isn't
enough: when one is designing a control system that has multiple state
dimensions and dynamics that couple them, is the optimal control strategy
going to be to only consider the dimension of the state that you care about?
Why or why not?)

The rigor of thinking that the EECS department wishes to inculcate in its
students is not limited to questions involving software or circuits or devices
or mathematical models that we give you. The goal is for you to be able to
think critically and rigorously about problems in general. One of the
important principles here is not assuming that everyone else is a fool. It's
alright to not understand something. That's normal. You might question
something because it doesn't make sense to you. That's also good. But to jump
from there to assume that the people in charge are in the grips of something
nefarious like "Political Correctness" isn't logical. It's arrogant.
*Humility* is a vital attribute for engineers. Approach questions sincerely.
*Arrogance* can be fatal in practice.

It is good that you appreciate your TAs. And it is good that you have high
esteem for your faculty. But you should also have some trust that these same
good TAs and faculty are trying to achieve something when we want to
understand how to improve inclusivity. Just because you have not experienced
something doesn't mean that it does not exist.
## CS 70 Off Campus

2017-02-22
Is it possible to take cs 70 at another UC or a community college over the
summer? If so, which ones?

### Anant Sahai's answer
Essentially, no. Nothing articulates to 70.

### Followup:
Student:
This is only applicable for CS and Math double majors

## Stat Courses for CS 70

2017-02-20
Are there any statistics courses that have a good amount of overlap with CS 70
and/or can help students prepare for CS 70?

Would Stat 134 or Stat 140 be helpful for CS 70, or would CS 70 only be
helpful for Stat 134 and Stat 140?

Asking this as I am planning to double major with CS and Statistics/Data
Science.

### Anant Sahai's answer
The hope is that EE16AB will help prepare students for CS70. The problem with
CS 70 (from the perspective of someone who has repeatedly taught the course)
is that many students come in not satisfying the assumed prerequisite of
mathematical maturity vis-a-vis both manipulation and modeling, as well as
understanding (as opposed to pattern matching to be able to solve problems).
It isn't about needing prior exposure to the concepts. The concepts are
introduced in 70 one at a time. (If anyone disagrees, please do email
[sahai@eecs.berkeley.edu](mailto:sahai@eecs.berkeley.edu) to let me know.) The
pacing in 70 is admittedly a bit fast --- we expect students to actually skim
notes ahead of lecture, attend lecture (paying attention and taking notes) and
participate actively in discussions, go back and reread notes carefully, and
then attack the homework problems with full dedication (not while
multitasking) and working through their confusion, possibly with the help of
interacting with other students. We expect all students to get stuck every
week, but we want them to get stuck on the specific concepts and techniques
that we are teaching them, not to get stuck because they are having trouble at
a more basic level.

### Followup:
Student:
Btw Adhikari said she is NOT planning to replace 134 with 140. This is because
134 is better suited for someone without a programming/Data 8 background.

Student:
reading for stat140 right now (after have taking 134). The probability you
learn is pretty equivalent, but you also learn a bit of numpy/scipy stats to
do simulations or calculate probabilities you wouldn't be able to do on pencil
and paper.

stat140 has a lab section which 134 does not have, so that could be a
consideration in differentiating the courses

in terms of probability overlap between 70 and 134/140, i would agree with the
student answer. i took 70 and 134 the same semester and it was a lot of help
to already be familiar with probability by the time 70 got to it.

Student:
Prof. Adhikari is also the current 134 Professor.

Student:
Tbh 140 and 134 are supposed to be very directly comparable; Adhikari (current
140 prof and frequent 134 prof) says that's it's the same material and intends
to replace 134 with 140 permanently within the near future. She has said the
only difference is the ability to use Python to simulate events and calculate
things that are intractable by hand. Plus, course readings/practice problems
all come from Pitman. I doubt anybody can say for sure exactly how much
they're the same, as nobody can take both, but I'd suspect they're pretty darn
similar.

As for relevance to 70, pretty much all the probability notes in 70 have
already been taught in 140.

## Can Professors please mention Berkeley achievements?

2017-02-16
0\. When I first came to Cal, I honestly didn't see why we were so highly
ranked. I realized we get a great education, but what made our school first in
the world? I didn't see it.

Now, I'm starting to understand. Just look at all the achievements of Berkeley
researchers.

Guess where IPython notebook was created? Berkeley. In fact its creator works
in Doe Library.

Guess where Apache Spark was created? Soda Hall, in fact you walk past it
every day to get to the Woz.

Guess where GNU/Linux was created?

1\. I wish Professors would emphasize these achievements more. It really helps
students appreciate their education more.

2\. Honestly, Professors should at least talk about their own achievements.
Not to show off, but to inspire students. Students (myself included) don't
realize how hard it's to become a Berkeley Professor. Of a thousand graduate
students, they choose 1-2 per year.

**These Professors - Hilfinger, Sahai, Satish Rao, Sanjit Seshia - are the top
2-3 in their field.** Think about that. You're interested in signal
processing? Well, the guy teaching your CS 70 class is the world leader.

My point is, Professors don't talk about themselves, but how can we feel pride
in our institution if you won't?

Thanks :)

### Anant Sahai's answer
The hope is that EE16AB will help prepare students for CS70. The problem with
CS 70 (from the perspective of someone who has repeatedly taught the course)
is that many students come in not satisfying the assumed prerequisite of
mathematical maturity vis-a-vis both manipulation and modeling, as well as
understanding (as opposed to pattern matching to be able to solve problems).
It isn't about needing prior exposure to the concepts. The concepts are
introduced in 70 one at a time. (If anyone disagrees, please do email
[sahai@eecs.berkeley.edu](mailto:sahai@eecs.berkeley.edu) to let me know.) The
pacing in 70 is admittedly a bit fast --- we expect students to actually skim
notes ahead of lecture, attend lecture (paying attention and taking notes) and
participate actively in discussions, go back and reread notes carefully, and
then attack the homework problems with full dedication (not while
multitasking) and working through their confusion, possibly with the help of
interacting with other students. We expect all students to get stuck every
week, but we want them to get stuck on the specific concepts and techniques
that we are teaching them, not to get stuck because they are having trouble at
a more basic level.
### Followup:
Student:
Yeah definitely confused with FreeBSD - https://www.wikiwand.com/en/FreeBSD

Student:
Maybe confused with BSD?

### Followup:
Student:
:O)

## Summer EE16A. Lecture mandatory?

2017-02-08
Recently announced that STAT134 would change its lecture time and now
conflicts with EE16A lecture in the summer. Has EE16A lecture ever been
mandatory?

### Anant Sahai's answer
Not attending lecture is not a good idea.

Summer policy has not been set. But not attending lecture in summer is an even
worse idea than not attending lecture during the semester. In summer,
everything is going twice as fast. You're not expected to be able to take any
more than a single course at a time.

## Inadequacy after learning concepts

2017-01-23
After learning most concepts, I feel inadequate because I know in the real
world, they're not using this concept: They're using something much more
sophisticated.

For example, Error Correcting Codes (CS 70): The ECCs we learn were discovered
in the 1970s. Today's ECCs use much more complex techniques involving abstract
algebra.

Why learn these basic concepts if in the real world, I'll need to use
something much more complex? And knowing the basic case won't help me (I'll
need to learn abstract algebra which this approach doesn't require)

### Anant Sahai's answer
The basics are what are the most important over a long career. You need to
understand the core idea of something before you can understand other
manifestations of the idea as well as extensions. EECS courses aren't
cookbooks with recipes for you to follow. And in the lower-division at least,
many things are taught to you in a way that does double or triple duty --- you
are not just being taught about X, but also how to think more generally, as
well as learning ideas that are more broadly applicable.

For error correcting codes themselves, EE229B talks about them in more detail
and brings you closer to the state of the art. This is not to say that the
codes taught in 70 aren't useful today --- many modern implementations take
the ideas of Reed Solomon codes taught in 70 and make things more efficient by
exploiting ideas of extension fields (taught in EE229B and Math 114 I
believe). There are also other qualitatively distinct code families, namely
the polar codes, LDPC codes, and turbo codes, that are increasingly popular
today in cutting-edge applications. To understand LDPC and Turbo code
constructions and implementations, you need to understand more about message-
passing inference algorithms as well as things like linear programming and
optimization. To understand polar codes, you need more information theory
(EE229A) as well. These modern families build more directly on the material in
*core* EECS courses like 126, 127, etc. rather than on the algebra and
algebraic geometry underlying other codes in the Reed Solomon style.

Remember, a Bachelor's degree gives you the education you need to be an
apprentice that learns on the job, and can keep on learning for the next 4+
decades. It cannot make you a master at anything without sacrificing your
long-term future for an ephemeral gain in the present. Lower-division is
designed to help you build a solid foundation to prepare you for *learning*
more advanced material.

## Change EE147 into a 4-unit class

2017-01-19
This might not be the right place to ask but last semester I took EE147 as one
of my upper div requirements for EECS major. However, since it was only
3-unit, I had to take one additional class to fulfill the 20 unit upper div
requirement (usually 5 upper divs). So I looked back on the structure of EE147
and found that it had 3 hours of lectures and 1 hour of discussion weekly,
which was exactly the same as most of 4-unit CS upper divs. The amount of
workload was, at least to me, same as the other 4-unit classes. Why is it
3-unit instead of 4-unit? Is there anyone that's in charge of class
administration? Who should I write to?

### Instructor answer
Courses are carefully evaluated by COCI (Committee on Courses of Instruction)
and the Academic Senate. According to the Course Management System, this
course meets for 3 hours of lecture and 1 hour of discussion/week, but it has
no lab. This may be why it is 3 units instead of 4.

## Undergraduate Research

2017-01-19
I am a sophomore and was wondering if there are any research opportunities for
a person with my level of experience. (Taken 61A, 61B, 70, Currently taking
188)

### Instructor answer
there is a helpful handout on various ways to find research located outside of
205 Cory.

### Followup:
Kris Pister:
exactly.

Student:
How does an undergraduate student get an invitation to these meetings? Is this
something that would come about as a result of asking professors about
research opportunities?

## EE105 v CS170

2017-01-19
Which is bigger workload

### Instructor answer
there is a helpful handout on various ways to find research located outside of
205 Cory.
## GPA to get into grad school?

2017-01-11
What GPA do I need to get into a decent grad program (top 10)?

### Instructor answer
there is a helpful handout on various ways to find research located outside of
205 Cory
### Followup:
Student:
Agreed^ professors are looking for people they want to do research with and
would perform that research well, not someone only made up of numbers.

Student:
Everything I've heard from professors is that letters of rec >>>>>>>
everything else, including grades. Stellar letters can make up for any
deficiency in other areas. But a 4.0/amazing extracurriculars are not going to
make up for mediocre letters.

Student:
Letters of rec, GRE score, research, extracurriculars

### Followup:
Student:
Not if OP has very high standards...

### Followup:
Student:
I know this is an old thread, but I'd just like to add that several top
engineering graduate programs require having three letters of recommendation.
Building strong bonds with faculty members in the span of an undergraduate
career can be quite challenging!

Student:
Thanks professor!

## Is 61A/70 Tutor hiring done already?

2017-01-05
I know these classes typically release offers very late, but are they done
hiring for tutors/readers? If so, do you get an email if you are not selected?

### Satish Rao's answer
70 has not started hiring tutors/readers. It is generally done near the
beginning of

the semester, after upper division readers are hired.

### Followup:
Student:
Depends on the semester. The hiring is done by a faculty member so the
professor.

## Practical Math/Stats Courses

2017-01-04
I really love "practical" math courses. In other words, math courses that
teach you to solve real world problems.

For example, CS 70 and EE 126 give you the tools (Markov Chains, Expectation,
etc) to model a lot of real world phenomena. On the other hand, Math 54 is
really theoretical: Vector spaces, basis, rank, null space. Math 54 is useful
but only in EE 16A did I appreciate linear algebra.

**So, my question is, what other practical math courses do you suggest?** They
don 't need to be in Math DepartmentThey don't even need to be math courses:
Game Theory isn't math but (1) its practical and (2) it's analysed like math.

Here are some I'd like, please suggest more!

\- STAT 150: Stochastic Processes  
\- STAT 153: Intro to Time Series  
\- STAT 155: Game Theory

\- INDENG 166: Decision Analysis

\- INDENG 267: Queueing Theory

\- PUB POL 259: Cost Benefit Analysis

\- PHIL 143: Modal Logic

### Satish Rao's answer
70 has not started hiring tutors/readers. It is generally done near the
beginning of

the semester, after upper division readers are hired.
### Followup:
Student:
"Math 54 is useful but only in EE 16A did I appreciate linear algebra."

I think Math 54 is useful, but its not applications focused. EE 16A teaches
you a lot of the same material, but teaches you applications of each linear
algebra topic as well.

### Followup:
Student:
OP Here. Looks interesting! Added it to my classes to take list!

### Followup:
Student:
OP Here. Same question. Seems interesting but I have no idea what to expect.

## Intuition behind Machine Learning.

2017-01-03
I am TAing for CS 189 next semester. Before that, I thought I should properly
understand what ML actually IS. I help lead Machine Learning at Berkeley and
currently research in Prof. Wagner's lab. I've also published several papers
on deep learning. Over the summer, I interned on Google's self driving car
team. But I never truly grasped what ML is. So I present this question, which
has been eating at me for months.

If machines can learn, why can't they teach? Why can't they think? Reason?
Worship? Why are we focusing on Machine LEARNING instead all of these other
possibilities? A machine that can think is far more intelligent than one that
can simply learn. So we should be focusing on that instead.

### Anant Sahai's answer
Never confuse an argument about linguistics with an argument about the world.
The following koan was taught to me by Chomsky in the context of Turing and
Searle, and who was referring to wisdom passed down from Dijkstra. (I'm
adapting it.)

A disciple approached Basho and inquired about the nature of artificial
intelligence.

Basho: "Do birds fly?"

Disciple: "Yes."

Basho: "Do airplanes fly?"

Disciple: "Yes."

Basho: "Do fish swim?"

Disciple: "Yes."

Basho: "Do submarines swim?"

Disciple: "No."

Basho: "Why do airplanes fly but submarines don't swim?"

Upon hearing this, the disciple was enlightened. He proceeded to do something
useful like learn linear algebra, optimization, and probability.

Reflect upon this and you will pass the zeroth gate of modern AI.

### Followup:
Student:
Taken together, don't the koan and Steven Bi's response imply that the OP is
Steven Bi?

Student:
The OP is a CS God. Look at his achievements. He is in the top 0.1% of
Berkeley students. I wouldn't be surprised if he's a billionare at 25.

Steven Bi is also a CS God.

Therefore, Steven Bi might be OP.

Student:
I have no idea what part of this post (either in the author's background or
writing style) suggests that I made the post, or why I would acknowledge
making a post that I had made anonymously if I _had_ done so.

### Followup:
Student:
People have edited the OP's post, use the history slider to see.

Student:
I would prefer to stay anonymous.

### Followup:
Student:
If a computer program is so good that it for all purposes seem to think and
respond intelligently, then we may as well call it thinking, even if it's just
algorithms underneath. People don't say a sub "swims", but since it can
achieve the same purpose, it basically swims. (Just as we say the airplane
"flies".)

  

Sorry if that was long-winded, English is not my native language. Does it make
more sense now?

## Why don't Professors discuss their background & research?

2016-12-31
I'm a sophomore here, I've taken CS 61A, CS 61B, EE 16A and CS 70. None of my
professors mention their background even though most of them are in the top 5
of their fields in the world.

The biggest benefit of going to such a great school is the top professors, but
if the professors just focus on teaching and don't mention all the other
things they know, what's the point of having such great professors?

Why not just hire some undergrads like Alvin Wan, Sinho Chewi, Yujie, Michael
Zhang, Soroush, Kunal Mishra and Steven Bi as professors?

### Anant Sahai's answer
Come to office hours and ask. Not everything fits in a large lecture. :-)

Our research perspective infuses all the courses, but in ways that are
sometimes too subtle for the as yet untrained eye to perceive. (Faculty who
visit from elsewhere often give us comments though, because they can see what
we are doing underneath the surface that you perceive.) For example, 16AB were
literally put together with cutting-edge research in mind (and new ways were
developed research-style for the course itself), and the goal of innoculating
students with the right patterns of thought to be able to participate and
absorb the things that are coming down the pike. Not just 16AB --- some of the
problems in CS70 as well are abstracted from ideas that arose in research
contexts. DS8 is the same way. However, the connections between the research
and the problems are sometimes obscured because the first duty of homework and
lecture is to be digestible by students and help them grow (even if this
growth sometimes leaves you a bit sore).

The connections to research become slightly more visible in upper-division
courses like 126, 127, 121, 123, 189, etc... (To speak about a few that I
directly know about.) They are quite visible in graduate courses and
completely out in the open in special topics courses (like the 194/294 course
I will teach next semester).

But as in all fields, there is a difference in perspective between a master
and one who is beginning their education. Senior musicians and dancers will
often go on and on about the importance of the foundations, because their
mastery gives them a different perspective on the basics than the beginner
has. It is no different in Engineering. That is why a high degree of faith and
trust in your instructors is so important in education.

Anyway, the fastest way to get access to a bit of the feel of the integration
between research and teaching in the lower division is to join the content
team for a course. There, you will see things more in the open as well.

### Followup:
Student:
Is Prof. Seshia the world leader in computational proofs? I knew he was really
smart but the world leader? As my professor for CS 70? Boy, Berkeley has a
serious problem. Students need to be aware of this.

Kris Pister:
Your point is a good one. Prof. Sahai correctly explained out that our
research and startup experiences have a big

impact on what and how we teach, but to your point we may not be doing a good
job of pointing that out during

lecture. Often a short comment or parenthetical clause is all that it takes,
but I think that sometimes the faculty

forget to do that.

I always try to throw references like that into my lectures and course
material. If you take ee140 from me, you'll do

your CMOS designs for the fictional startup Golden Bear Circuits, and you'll
have a clear startup-relevant chip design task straight

from something that I've had exposure to through my consulting.

If you take ee147 from me, you'll get a lot of comments like "and that simple
idea is what launched the billion dollar

MEMS accelerometer industry" or "and those five boxes drawn just right got me
a PhD in '92."

In addition to going to office hours to ask questions, I would encourage you
to ask questions in lecture periodically

as well, either before or during class, about how what you are learning is
related to research and commercial practice.

## Why is Math 110 useful in Machine Learning?

2016-12-29
I don't see anything in Math 110 that's not taught in Math 54. Further, I
don't see how anything beyond the basics of solving systems of equations is
useful in ML. What's the point of eigenvalues, null space, subspaces, vector
spaces, etc.?

### Anant Sahai's answer
Linear algebra is critical conceptually to understand what is actually going
on in Machine Learning. This is one of the major reasons that 16A and 16B were
built the way they are. The student answer is pretty good, to which I can just
add that the discussion of the spectral theorem (eigenvalues/eigenvectors for
symmetric matrices) and the SVD in 16B is also relevant. For EECS people,
linear-algebra is not just a bag of tools. It is an important component of how
we think.

The idea is that 16B + hard work should get people to where they need to be.
Math 54 by itself is not enough for most.

### Followup:
Student:
So 110 is 1) more challenging than 54, 2) way more rigorous than 54, 3) (well
I took h110) but much more geometrically focused and geometry is pretty good
for math maturity.

Student:
(not Garrett but) Basically the more you do math / proofs / challenging
problems the more mathematically mature you get. Think of it as math
intuition. It's something that's not really taught, but it's something you
gain by studying more math.

### Followup:
Student:
Didn't even know Hug was teaching it... from what I've heard, he was a pretty
good 188 prof this past semester (I took it with Abbeel tho so I can't say for
myself), but ultimately, 188 is actually quite different from 189 (way more
concept based and waay less math). I think you should take it with Shewchuk
though... just reading his notes on it give me a good impression of the way he
taught the class.

Yeah I had Prof. Recht last semester. The class was really interesting, but to
be quite blunt, it was the most disorganized CS class (or maybe just class in
general) I've ever taken. Most people had to rely on student's notes or
Shewchuk's notes because nothing was easy to find, lectures were in general
kinda hard to understand and a little too simplistic at times. Idk if the TAs
or the profs made the exams, but the midterm was brutal, and the final was
pretty tough too (although imo way easier).

Student:
Who's better, Hug or Shewshuck for ML?

Also, were you get rekt by Prof. Rect?

Student:
Different offerings of the course have different emphases on math. Fall 2016
was more mathy because the professors (specifically Prof. Recht) believed that
CS 189 = EE 126 + EE 127 + some notes on backprop, which is ultimately just a
bunch of math.

If you take it next semester with Shewchuk, I believe you'll have a bit of a
different experience. There is still def. alot of math, but I think the ML
concepts are emphasized more.

Student:
@Anon from 3 replies ago. Idk, that's a question for you. You signed up for
this major, so you must of had your reasons, right? I'm not sure how it didn't
dawn on you from 70, 170, and 188 that cs is a mathy discipline. At this point
you just sound bitter.

Student:
Well, I like the mathy aspects of ML, but I like coding and software
engineering too.

Student:
yeah, exactly - that's my point.

Student:
lol tons of CS PhDs working in the AMPLab are math undergrads.

Student:
What's the point of studying Computer Science then? Why don't we all just
study math?

Student:
AI/ML is especially mathy. Also graduate students also take it and graduate
level cs is lots and lots of math.

Student:
Yeah, but ML (like many/most CS subfields) is just applied math.

Student:
Why is linear algebra so important though? This is a Machine Learning course.
Not a Linear Algebra course.

### Followup:
Student:
Probably, although not by much. The repetition of the material would obviously
help and an argument could definitely be made that, being able to see
applications of the sometimes overtly conceptual subject matter in 110 (as you
would in 189) would also help, but all in all, I doubt it'd do too much good
for 110 to take 189 at the same time.

I think the reverse is definitely true though - I took 110 before 189 and felt
that it helped me immensely. Can't imagine taking (and perhaps more
importantly, doing particularly well in) 189 without the prior exposure to 110
or 110-esque material (don't know too much about 16B myself).

Student:
Maybe this is a better question: does it help **for math 110** to take 189 at
the same time?

Student:
Yes, the later parts of 110 are really useful in the early parts of 189.

Student:
Is that your explanation as to why you shouldn't take it at the same time as
CS189?

Student:
Math 110, especially the later parts, are used extensively in CS 189.

Student:
Why Anon?

Student:
No, take it before.

### Followup:
Student:
He responded!

Student:
+1 Please answer Sir

Student:
+1 Really looking forward to your response Professor Sahai

Student:
+1 Professor, please answer this! It will help all students.

Student:
+1 Please answer this

## [ADVICE] Getting A's on exams

2017-07-07
CS major here. I need some advice: **How to perform** **above average on
exams.** In all my technical classes here, I 'm always

+\- .5 STDs from the mean. Consequently, I'm a solid B student.

No matter how hard I study, I always perform around the same. The problem is
that I'm not studying the right way. There's always problems on the final I
just don't know how to do. **I 'm not mastering the material** like I should.

_**How should I be studying?**_

This is what I do currently.  
1\. Write down everything I need to know.  
2\. Re-do all discussion WSs, cross off items.  
3\. Practice weak areas from old exams.  
4\. Do (untimed) practice exams.

I'm taking 61C and 170 next semester. I'd especially appreciate if Yujie,
Steven Bi and other TAs replied.

### Anant Sahai's answer
Student posters, do you do old exams timed or untimed? Whole thing at once, or
question by question with answer key?

From Prof. Sahai:

1) The most important thing to remember is that everone is different in how
they learn, but the most direct path to doing well on exams is to actually
understand the material well, understand how it connects to everything else
that you have learned, and to have sufficient practice with the underlying
technical skills to be able to execute on demand.

2) For many students, getting adequate sleep and rest is extremely important.
Relatedly, the general ability to concentrate and not be distracted for three
hours straight is really important. So, don't shoot yourself in the foot by
going into sleep debt, not eating properly, or allowing yourself to cultivate
habits of distraction. Being able to do one thing at a tiMaking your own me
for a long time isn't something that will just work on exams when you've spent
all the time earlier in 3 minute work bursts interrupted by texts, youtube
videos, etc... Marathoners don't train by just doing sprints.

3) Don't try to learn everything at the last minute. Really try to understand
everything as the homeworks flow week by week. Don't just assume that you'll
understand things better later. Ask the TAs and Profs for help earlier rather
than later.

4) In furtherance of your underlying understanding, the following approaches
are woefully underused:

  * Making your own problems about the material, solving them, and sharing them with others.
  * It is often said that the best way to really learn something is to teach it. So, in general, doing versions of what the TAs and Profs do is a good idea. Make your own exam. Think about the concepts in the course, how they connect to other material in prereq courses and follow-on courses (ask your TAs or Prof if you do not understand this), and then try to make questions that hit those connections. After doing the practice exams as practice, deconstruct the problems and ask how you could make a similar question yourself? 
  * Pretend you are inside the material and understand how it fits together from the perspective of the computer or the math itself. Engage your artistic and imaginative side: try to escape the bounds of your individual human experience by stretching your ability to identify with the subject. Don't be afraid to be silly. And don't be cynical --- every time you are cynical, you are just putting emotional distance between yourself and the material. That is not going to help you. The material has to become like a close friend --- you can get mad at it and frustrated at times, but you have to let yourself care and be vulnerable if you are going to really get close.
  * Play "stump your friend" with someone you care about and trust --- test each other about the material in a way that helps them understand better but don't destroy their confidence. If you end up stumping yourself, this is fine. Figure it out together. 
  * Don't be restricted to what you can see on the computer screen. Print stuff out and write stuff out by hand. Lay out the material in your own way so that it spatially spans many pages and you can see it all together spread out around you. The computer screen is too small to fully engage your visual memory.

### Followup:
Student:
a. Try to learn the week's material over the weekend, before the week starts.

b. If there is a textbook or recommended supplement, read it because it will
be helpful. Just going over the lecture slides is not enough...

Hope these help :)

Student:
Not OP but for b, if material is harder to consume and understand, it will
"stick" more and you'll end up understanding it better. When someone is making
concepts clear and easy to understand, its easy to fool yourself into thinking
you've learned them.

### Followup:
Student:
Also, sometimes it helps to learn or know some of the material beforehand. You
still have a month.

Student:
By going to lectures / discussions? They take only a few hours...

And asking yourself the question: "How much of your 'studying' time are you
actually studying?"

I'm sometimes shocked by the answer myself lol...

### Followup:
Student:
I think that the listing of the sorts of activities that are useful to do on a
regular basis (e.g. actually reviewing the solutions to previous homeworks
instead of just being satisfied with getting full points on a problem, first
trying the homework on your own for a few hours and _then_ work on the
problems with your study group) is more useful than the actual time allotted
for each of the activities.

That is, scale the numbers down if you want, but the list of activities is
pretty reasonable.

Student:
I think this probably is a little much... I don't know anyone who actually
spends this much time on a single class consistently

Student:
Sure, that's more or less the same idea as the answer above.

### Followup:
Student:
I noted above the suggestion of first trying studying alone, and then meeting
with your group, when you've already tried some ideas (whether or not they
work). See if your groupmates had the same ideas, and brainstorm more together
if none of them work.

But if you're pretending that you understand something when in your group,
then that's probably not going to be very effective / a separate problem to
handle (e.g. if it's a confidence/embarrassment issue).

Student:
Also when studying alone, your mileage may vary. When studying in a group,
some people will ask questions that will really test the extent of your
knowledge. If you don't think you can get that kind of coverage on your own,
study in a group.

### Followup:
Student:
Not particularly, he got a B in CS 61A.

Student:
is he a CS God?

Student:
I think when you sleep and get up is completely irrelevant to your grade as
long as you get enough sleep... I know someone who got an A in CS 70 who slept
at 6 am every day during dead week (and got up at like 2 pm).

### Followup:
Student:
Wow. What an mind-blowing answer. Steven Bi is THE CS God.

Student:
Upper div office hours are certainly smaller than those for lower divs (or
more specifically: office hours for smaller courses have fewer people), and
the timing of the week matters quite a bit as well. Certainly, the earlier the
office hours (with respect to when the assignment is due), the less crowded
it'll be.

For 170, my office hours were generally earlier in the week (i.e. I don't like
holding office hours right on the day the homework is due, so I usually
don't), and I can't recall a single occasion when I felt that I didn't have
enough time to respond to all of the students (barring the OH right before the
exam).

170 is also not a coding-based class, and so I didn't have to spend time
trying to read/debug students' code. I think OH for that class is generally
unlikely to be too rushed.

I've had students who only appear once or twice, and I've had regulars who
just met with their study groups at my office hours. I think that the
difference is more based on your personal preference.

Piazza can handle some (many) questions, but if the question is more involved
(as some conceptual questions tend to be), I'll fairly strongly advocate
asking in office hours. As an instructor, being able to gauge the student's
understanding in real time and working on a whiteboard for visualizing are
immensely useful in explaining concepts. (There have definitely been questions
on Piazza that I've ignored because they're too tedious to explain there, but
which would have been straightforward to answer in person. Also, some students
aren't very good at asking questions and it's hard to figure out what the
source of their confusion is via Piazza.)

Student:
Try going to office hours when there is no homework/projects due. It's pretty
fun to pick at the TAs brains.

Student:
Office hours for CS classes in my experience tend to be rushed and unhelpful
because the TA's have limited time and lots of people to deal with. On Piazza
you'll usually get a thoughtful answer promptly.

Student:
I just ask on piazza

### Followup:
Student:
I'm rarely worried about not finishing an exam, so I never timed myself. If I
was concerned about this, I would probably time only the last exam or two, at
the very end of my preparation, to get a sense of pacing.

Whether or not I do it by-question is depending if I'm still in the learning-
phase of studying (esp. in courses when I haven't really been following the
course/doing the homework properly, and I'm using exams to figure out what I
was supposed to have learned) or if I'm actually testing myself.

If it's the former, I'll usually read individual questions, think for a bit,
and then go straight to reading the solution, since I presumably can't solve
the problems.

If it's the latter, I'll write out semi-full solutions to all of the problems
before checking my answers.

Student:
As a freshman who got an A in 61A and an A+ in 70, I'll chime in here - I do
them untimed because I find that removing the pressure from the clock really
helps. Keep in mind that there's often a common thread to test questions
because there's only so many things that they can test, so once you find that
common thread, tests become that much easier. As for the answer key, I like
having immediate feedback, especially since one question doesn't really help
or hinder the next, but I can see how individual preferences might vary.  

Best of luck!

### Followup:
Student:
"Don't be restricted to what you can see on the computer screen. Print stuff
out and write stuff out by hand. Lay out the material in your own way so that
it spatially spans many pages and you can see it all together spread out
around you. The computer screen is too small to fully engage your visual
memory"

This is _poetic._ This is why Berkeley EECS is #1 in the world, we have the
best professors like Prof Sahai, who turned down Stanford and MIT for us. I
still don't get why.

Student:
+1 the god himself has descended and given us spiritual revelations

### Followup:
Student:
You guys should watch Prof Sahai's first cs 70 lecture from Fall 2014. Its
pretty inspiring because he talks about his background and also explains the
motivation behind 70. If I remember correctly, he does go over why he chose
Berkeley.

Student:
+1 I had you in CS 70 in Spring 2014 but forgot to ask. Thank you sir!

Student:
+1 I'd love to hear your response Sir

Student:
+1 Please answer this Sir!

Student:
+1 Looking for an inspirational story or message

Student:
+1 Need your life advice Professor

Student:
+1 I've always wondered this

## Is CS169 cancelled for next semester?

2016-10-14
Noticed I could no longer load CS169 in calcentral scheduleplanner for next
semester. Has this class been cancelled?

### Satish Rao's answer
Yes. Apologies. Perhaps look at 164 or 160, both have significant design
projects.

## Math 54: EECS requirement and Math Minoring

2016-08-25
I'm a second-year EECS major who's wondering about the current status of Math
54 as a degree requirement, whether it will be removed by the time I graduate,
and whether it will apply retroactively to me. With that said, even if that
requirement is removed I am considering doing a Minor in Mathematics, which
still does require Math 54. So I'm wondering what I should be doing at this
point, and if there is any possibility that the Math Department would take
EE16A/B as substitutes as well (long shot, I know...)

### Instructor answer
The answer remains the same as a year ago (please find those posts). This
requirement has not been removed and all students are encouraged to complete
it.

The only change is that students who have completed EE16A & 16B may now
complete Math 110 instead of Math 54. (EECS only)

### Followup:
Elad Alon:
For EECS majors, you can indeed take Math 110 instead Math 54 (since you will
have taken both EE16A and EE16B).

  

For L&S majors, if you take EE16B, you can use that to fulfill the requirement
for Math 54 (i.e., you can use 16B to replace Math 54).

Student:
From @1350:

"To give some more general advice/summarize, if you feel like you have gotten
a good grasp on linear algebra from 16A/B, there shouldn't be any need for you
to take Math 54."

Does this mean that Math 54 isn't required for EECS majors if we have taken
both EE16A and 16B?

Student:
+1 I can't access the post.

Student:
I'm not able to access that post; it says "Not Permitted"

Student:
@1426 Professor Sahai

## Phasing out Math 54/EE16A and 16B

2016-05-30
I've read from several sources on Piazza and Facebook that Math 54 may be
phased out for L&S CS students. If so, will both EE 16A and 16B be
requirements for L&S CS majors? I am going to be a freshman next year,
intending to declare CS; should I plan to enroll in 16A for fall and 16B for
spring in my first year? Even if 54 is not phased out for next year, is there
a large possibility that I will not have to take it before I graduate? Thank
you!

### Elad Alon's answer
EDIT: I made a small but important typo in my original response - I meant to
say that is likely that you will *not* need math 54 by the time you graduate.
Sorry about any confusion!

  

We are in the process of getting approval to have the combination of
EE16A+EE16B serve as an option to fulfill the math 54 requirement for LS CS
students. So, I believe it is indeed likely that you will *not* need math 54
(assuming you have taken 16A and B) by the time you graduate.

  

My personal recommendation (not necessarily speaking on behalf of the
department or anyone else) would indeed be to try and sign up for 16A this
fall (and probably 16B in the spring, although you can of course make that
decision when the time comes).

### Followup:
Student:
second bump

Student:
bump, as I'm wondering about this question too :)

Student:
Would you recommend that EECS students take 54 though? Given that it may be
unnecessary.

Elad Alon:
The details of the degree requirements for CoE EECS are slightly different
than for L&S CS, but the advice of signing up for EE16A in the fall (assuming
you have the appropriate math background from high school) and EE16B in the
spring holds for everyone.

Student:
+1

## EE Internships / Research for a Freshman

2016-05-06
Like the title states, I took EE 16A and thought it was a bomb class.
Unfortunately, I have only taken EE 16A. Obviously, it's extremely late, but
would there be any companies interested in taking on a Freshman for an EE
internship? Or any EECS professors who would be willing to accept a Freshman
into their lab? I think the circuit design and signal processing stuff is
really cool, but given my limited knowledge, it's probably be difficult.

I really want to explore some of the cool stuff that was presented in 16A,
because I kind of am considering pursuing EE as a career path.

If you know any Freshman receptive EE professors / companies, please tell me.

Thanks

### Elad Alon's answer
I think most EE faculty would actually be happy to get freshman involved in
their research groups one way or another, so as your colleague pointed out,
I'd definitely recommend reaching out to some of the professors directly. (Now
that it's summer it may be a harder to catch people, but during the semester
swinging by office hours is a good bet.) Feel free to ping me directly if
you'd like advise about who you might try speaking to first based on your
interests.

## EE 105 Popularity?

2016-05-03
Just curious, why does everyone want to take EE 105 suddenly?

Comment your reason below..?

### Elad Alon's answer
I think most EE faculty would actually be happy to get freshman involved in
their research groups one way or another, so as your colleague pointed out,
I'd definitely recommend reaching out to some of the professors directly. (Now
that it's summer it may be a harder to catch people, but during the semester
swinging by office hours is a good bet.) Feel free to ping me directly if
you'd like advise about who you might try speaking to first based on your
interests.
### Followup:
Elad Alon:
I would also like to challenge the original statement about 16A/B not teaching
circuits as rigorously or in depth as 40. 16A/B actually cover essentially all
of the same circuits-related topics that 40 did, and in fact expand beyond 40
somewhat in terms of design thinking and connections to linear algebra. It is
true that there is less absolute time spent in 16A/B purely on circuits, but
to put it in the words of one of my GSIs, what is mostly given up (at least in
lecture) relative to 40 are some of the "tricks". If anyone is interested, I
would be happy to walk through more of the details/nuances in terms of the
differences, but we committed from very early on in the course design to cover
the topics we did include in EE16 deeply and rigorously, and circuits is no
exception.

Student:
105 is being remodeled to fit students coming out of 16 and into 105.

## How important is CS 188 for taking CS 189?

2016-05-01
I'm wondering how much material from CS 188 will be used in CS 189, because I
may not take them in back to back semesters - i.e. I may wait a couple of
semesters after taking 188 to take 189.

### Elad Alon's answer
I think most EE faculty would actually be happy to get freshman involved in
their research groups one way or another, so as your colleague pointed out,
I'd definitely recommend reaching out to some of the professors directly. (Now
that it's summer it may be a harder to catch people, but during the semester
swinging by office hours is a good bet.) Feel free to ping me directly if
you'd like advise about who you might try speaking to first based on your
interests
### Followup:
Student:
thanks, Elad!

Elad Alon:
EE16A will help to prepare for 189, but EE16B will help even more so. (One of
the early topics/concepts we cover in 16B is SVD/PCA, which are both very much
core to 189.)

Student:
what type of linear algebra is used in 189 though?

Student:
ee16 is easier than math 54 in terms of math

Student:
so I should be brushing up on 54 material - would taking EE 16A help prepare
for 189?

Student:
Different anon, but a lot of linear algebra and some basic 53 stuff.

## Taking EE 105 without 16B?

2016-05-01
Hi,

I am planning on taking EE 16B and CS 61C next semester.

I want to take EE 105 for my last 4 units, but I since I'll be taking it
concurrently, I'm not sure how much of a disadvantage I'd be in? I have a
friend who said 16A is enough for EE 105, but I'm not sure how true that
statement is...

If I'd be at a disadvantage, I'll just fulfill one of the HSS requirements.

### Elad Alon's answer
I also would not recommend taking 105 without having first taken EE16B.

  

From speaking with students from the 16AB pilot (who are the only ones at this
point who could have taken the 16 sequence and now be in 105), my
understanding is that they felt well prepared for the content itself, but
experienced some difficulties with the (newly added to 105) SPICE labs. (I
don't know if this sentiment was shared by those who had taken 40, so this may
not be a differentiator between 16/40). All of that said, as mentioned above,
105 is being redesigned to build on the style and specifics of 16A/B, so in
the long term 16B is (by design) what you will need to succeed.

## Difference between EE143 and EE147?

2016-04-27
What is the main difference between EE143 and EE147? seems like they are quite
similar?

### Clark Nguyen's answer
Aside from the actual fabrication experience 143 offers that has already been
mentioned, 143 presently has more of a semiconductor transistor focus, where
MOS devices serve as the main vehicle for discussion of wafer-level
fabrication technology.

147, on the other hand, focuses more on micromechanical (MEMS) devices, such
as used in today's accelerometers, gyroscopes, and timing devices, found in
smart phones, cars, etc. It not only covers wafer-level fabrication methods
for MEMS that can be quite different from those used for transistors, but also
covers methods for designing MEMS devices and appications. You'll learn to
work with masses, springs, forces, and velocities, instead of inductors,
capacitors, voltage, and currents.

Both are cool classes.

### Followup:
Student:
thank you! I've actually taken 130, 143 already. I just wanted to learn about
MEMS but wanted to not waste time if they were the same. but looks like
worthwhile to take 147. Thanks!

Student:
I've taken both; they are very much different. 147 covers maybe 3-4 weeks of
fabrication (though it does a great job of it)- and only those pertinent to
MEMS. The rest of the class is very much into how MEMS structures work etc.
143 is almost completely about the fabrication process, specifically about the
intricacies & annoying non-idealities that pop up during the process. In the
lab you build some devices (none of which work), and you have to write a lab
report about how they work (take 130 concurrently to make this easy), but very
little of the actual design/working of devices is covered. I personally
preferred 147, (also Pister is great), but if you want to be a process
engineer take 143.

## Math 54 major req for EECS

2016-04-26
Hey just wanted to check up on the status of Math 54 for EECS. I've heard that
it may be phased out if you took 16A/B, but will that apply retroactively? I'm
a current freshman, graduating 2019.

### Elad Alon's answer
The short answer is that we are in the process of getting approvals to make
this happen, and I do believe it will be in place by the time you graduate. To
give a bit more detail, for the EECS degree requirements, we are currently
working on getting approval to have Math 110 serve as a substitute for Math
54. Longer term, we are considering expanding flexibility further to make it
   so that if you have taken EE16A/B, you can take any upper div. math course, or
   "math equivalent" upper-div. courses like EE126, EE127, or CS174. (This latter
   idea is still very early however, so please don't count on it just yet.)

To give some more general advice/summarize, if you feel like you have gotten a
good grasp on linear algebra from 16A/B, there shouldn't be any need for you
to take Math 54.

### Followup:
Elad Alon:
For L&S CS, we are in the process of getting approval to have 16A + 16B
replace the need for Math 54. So, assuming you're planning to take 16B after
16A, there probably isn't a need for you to sign up for 54.

## BioE / EECS joint major?

2016-04-23
I have heard that BioE/EECS is a fairly popular double major amongst students
in CoE, and have heard rumors that CoE is planning on having a BioE/EECS joint
major as an option in the next few years. How true is this rumor, and when
would this possibly be implemented?

### Elad Alon's answer
Actually there a number of efforts currently underway to attempt to establish
a simplified system for joint majors as a whole, and BioE-EE/CS is one of the
main targets in mind for this effort. It's still too early in the process to
"count" on this happening, but I'm sure there will be announcements when/if
this gets worked out.

## Is this doable? I'm Eecs.

2016-04-16
Is EE 126, EECS 151, EE 140 and CS 176 for fall semester doable?

Thanks.

### Elad Alon's answer
That sounds like a very heavy workload to me. As your colleague indicated, 151
has a very substantial lab and more importantly final project component. 140
also has a lab and project, and although they may not be quite as time
consuming as 151, it definitely isn't a light load either. I'm not familiar
with the load for 176, but 126 most likely wouldn't be as bad as the previous
two in terms of sustained workload, however it can be a conceptually very
challenging course, and so you'd to make sure you have enough time to
assimilate that material as well.

  

Long story short - while I don't think this is absolutely impossible, this
does sound like a pretty crazy schedule. If you'd like, I'd be happy to sit
down with you and chat about your course/career plans to see what some
alternatives might look like/whether you really need to attempt this schedule
- just send me a note.

## Class help

2016-04-11
How doable is taking EE140 and CS170 plus two non technical courses?

What about CS162 and EE140?

### Elad Alon's answer
You'll certainly be busy, but either of those options seem quite feasible to
me.

## Academic probation last semester?

2016-04-09
What happens if, during your last semester, you get straight D-s in your
classes (or some combination of letter grades such that your GPA is below 2),
but your cumulative GPA remains above 2, and you've completed all required
courses with at least a D-? According to the EECS website, this would put you
on academic probation - does it matter if that happens during your last
semester?

### Satish Rao's answer
Dude. Seriously. Buck up. Try harder. The instructors/TAs/read4er, your fellow

students are super there for you!!!

Ping any, ping all, they will help.

### Followup:
Satish Rao:
The intention of the answer wasn't to deny the BS. But to say there may be
value in trying...

Satish Rao:
An acceptable question, certiainly...

Perhaps larger questions loom.....

## Upper div EE as replacement for EE16a

2016-03-31
I'm going to be a senior CS major and I need to satisfy the EE16a requirement.
As I understand the class is actually for freshman. Is it at all acceptable to
replace the EE requirement (ee16a) with a (harder) upper division electronics
class, such as EECS149 or EE126?

### Instructor answer
As you said, EE 16A is a major requirement, so I don't see an exception being
granted for this. CS juniors and seniors took EE16A this semester. You may
want to speak with them to get their perspective on the class. I would also
recommend speaking with your CS advisor.

EE 16A&B are pre-reqs for EE 126 and EE 16A&B or instructor permission are
required for EECS 149.

## Specializing in EE and jobs..

2016-03-19
Ok, this is probably going to seem like a very stupid question, but what are
the job prospects if you specialize in EE? I am a Freshman EECS major, and
ever since I came here, I found out that I absolutely abhor coding. However,
after taking EE 16A, I have taken a liking to the EE / hardware side...
However, some of the stories I have heard about EE specialization kind of
scare me... I have heard about some EECS majors "defaulting" to CS
specialization because it's hard to find jobs in EE.. I have also heard about
some people who have Ph.D's in EE who are having difficulty finding jobs.. It
doesn't seem like Berkeley emphasizes EE (as opposed to CS) too much (Though
this perception is probably due to my own ignorance)...

How hard is it to get internships in EE? GPA minimum requirements?

EDIT:

First of all, thank you for all the responses. It is very encouraging to know
that so many people are willing to answer my questions.

A clarification to the line "I absolutely abhor coding": This might be a bit
of an overstatement. I just am not particularly adept at some of these CS 61B
esque style questions, which has in turn caused me to dislike it. I'm not sure
if EE is concerned with finding the max distance between 2 nodes in a Binary
Search Tree (?). I am perfectly fine with coding that for example, is
presented in E7 (i.e. practical applications). I actually enjoy writing the
code for the iPython notebooks we have to do in EE 16A. I am perfectly fine
with using something like MatLab for mathematical modeling.

Furthermore, my original post heavily implies that I only want to do EE
because I don't want to do CS. I have many interests in EE that I want to
explore (i.e. fiber optics, solid state), and overall prefer the designing and
integration of multiple concepts that EE requires. I believe that if I had
been exposed to EE before taking a CS class, I would have still wanted to do
it. I think having to come up with a design for a circuit given a specified
problem (and actually getting it right) is extremely satisfying.

### Instructor answer
Here are some responses from our EE faculty:

Randstat has a nice analysis of the perks of EE jobs; EE was one of their "hot
jobs" for 2015.  

The numbers are here: <https://www.randstadusa.com/workforce360/jobs-the-
economy/engineering-jobs-in-demand-for-2015/255/>  

Salient points:  
\- geographic supply and demand imbalance: too many EE's in some places and
too few in others  
\- >10 jobs for every EE graduate  
\- there appear to be >20,000 job openings across the country for EE's at any
given time (I added up the demand circle in the report)

\- The national average starting pay for an electrical engineer with three to
10 years’ experience is $90,295. (This figure is national- Berkeley's grads
tend to make more)

\- EE's have among the highest salary increases year-to-year. An Electronics
Engineer had the highest annual increase at >8%  
\- these jobs are hard to fill so a Berkeley EE is a goose that lays golden
eggs  
\- Our Ph.d.'s have no trouble finding very high paying jobs. There are always
more internships than students available at Berkeley.  


### Followup:
Student:
lel I am a filthy CS major

Student:
I agree with the above anon. Even as a hardcore EE major, I have to give
sufficient credit to my CS peers because they are just different
specializations. I can do things that amaze my CS peers and sometimes I'm
amazed by what they can do. Instead of looking for differences, how about some
synergy? After all, we are in EECS.

Student:
There are many software engineers who take EE classes (like my CS friend who
took classes like EECS 150) and there are many EE who take CS classes. There
are EE who do not take CS classes beyond CS61C and there are many CS people
who do not take any EE beyond 16a (or b). The point is that it depends on what
the person is interested in.

Silly presumptuous statements such as the ones above are ridiculous supposed
ego stoking. Is it really necessary to look down on software engineering just
because they don't want to do EE? Please study what you want and what is
interesting to you! But don't look down on other disciplines just because you
didn't specialise in CSE or CS vs EE vs CE ... etc.

smh

Student:
Someone who finished a 3 month coding bootcamp can be a software engineer. You
don't need to spend 4 years at Berkeley to be one.

Student:
Take the average software engineer. Ask them to build a low-pass filter and do
the correct digital signal processing to complete the control loop on a
microprocessor.

Take an EE. Ask them to write a website/backend. They will for sure be able to
figure it out.

Student:
I think that this is extremely presumptive. There is nothing stopping CS and
CSE from taking EE classes and many do so.

## EE120 and EE105

2016-02-07
I'm thinking of taking these classes next semester, but the thing that makes
me hesitant to is the fact I took 16A/B instead of 20/40. Will people who took
20/40 have a considerable advantage because those classes are taught in an
approach more similar to 105/120?

### Elad Alon's answer
The short answer is that you will be totally fine in EE105/EE120 having taken
EE16A/B. Both 105 and 120 have been/are being adjusted to match the
coverage/style of 16A/B; 20 and 40 are dead, so it's in no one's interest to
have the follow-on courses match to them instead of to 16A/B.

Best of luck!

## CS70 Reader

2016-01-26
Hi, has anyone gotten a notification about being a CS70 reader yet? (This was
from the forms posted by Satish Rao on 1/11).

### Satish Rao's answer
Sorry. For the delay. We had to wait for upper division hiring first. But we
have made some

offers, and are awaiting responses. There were many great applicants, and
selection processes

are always noisy, so don't take it personally that you have not (yet) recieved
an offer...

## CS70 inconvenient discussion time

2015-12-27
Hello

I am currently enrolled in cs70 for spring 2016. I signed up for a discussion
time that I now realize will not work well for my schedule. Is there a way I
can do this (I don't want to have to put myself on the waitlist for the class
just to change my discussion time).

Thanks for the help

### Satish Rao's answer
More discussions will be added. I would hold on.

Also student answer is correct, though it is nice to get to know a GSI/uGSI.

They are extremely nice people who have their students interests at heart

and can best help when they know their students.

## How to get into EE16A - discussion/lab sections?

2015-12-17
The discussion I'm signed up for is full, but the lab sections is empty. So I
think I need to switch my discussion to be able to get off the WL. Do we have
to attend the discussion/lab section we are officially signed up for or will
we be able to attend a different one?

### Elad Alon's answer
For lab you do need to attend the section you are signed up, but for the
discussions it is flexible. (If we run in to case where a particular
discussion is heavily overloaded we will give priority to those who actually
signed up for that discussion, but that generally hasn't happened in the
past.)

## EE 16A Lab Sections Removed?

2015-12-05
Hi,

During Phase 1, I'd signed up (onto the waitlist) for EE16A, as well as
waitlisting for a lab and discussion section respectively. I was recently
checking Telebears, and for some reason, the lab that I'd signed up for (EE16A
022 LAB) was no longer on there. Was this lab section cancelled? If so, what
are the recommended steps to take to ensure that I can actually be waitlisted
onto a lab section that exists, without losing my spot on the waitlist? I
tried changing only my lab section, but it won't let me select my old
discussion section, which makes me worried as to whether I'll lose my spot on
the waitlist because I had to change both sections.

### Elad Alon's answer
A number of lab sessions had to be cancelled and replaced by new lab sessions
in order to facilitate consolidation of all of the labs in to a single room
(hence helping to make sure that the labs run smoothly). Everyone who was
already enrolled in those sessions should have received an email with
instructions, but let me briefly detail here how those of you who are on the
waiting list should proceed.

  

During Telebears Open Hours, please enroll yourself in a new lab and
discussion section that has plenty of open seats. Note that the Telebears
system unfortunately will force you to change both the lab and the discussion
section. However, once the semester starts you can attend whatever discussion
section you would like to (labs you will need to attend the section you signed
up for), so don't worry about making having had to switch the discussion in
addition to the lab.

  

(For those of you who are already enrolled and are facing the same problem
with needing to switch both lab and discussion, you can rely on the same
approach above.)

### Followup:
Elad Alon:
This change should not directly affect your chance of getting in to the
course. Specifically, if you switch to an open lab section using the "switch
secondary sections" function in Telebears (e.g., during Open Hours), it will
have no affect on your position on the waitlist.

It is very important however that whatever secondary sections (lab or
discussion) you sign up for have open seats. If those sections do not have
open seats, you will not be enrolled and will be skipped over when the
waitlist is processed automatically. So, I would definitely recommend that you
sign up for sections that have a large number of open seats, since if there
are only 1 or 2 open you may end up not getting in.

We completely understand your concern about having used Phase 1 units, and we
are doing everything we can to minimize the impact of the changes we had to
make. As explained above, as long as you switch to secondary sections that
have plenty of open seats, this shouldn't impact your priority on the
waitlist.

### Followup:
Elad Alon:
Sure thing. Please see my response to the follow-up immediately above this
one; my understanding is that as long as the secondary sections you signed up
for have open seats, you will be accepted in the order of the waitlist for the
main class.

## EE 16B discussion sections

2015-11-25
I'm currently enrolled in a discussion section that I cannot attend, because
the only one that works with my schedule is already full (crazy schedule).

Professors Sahai and Maharbiz, do you know yet what your discussion attendance
policy is going to be? Is there a possibility that I could arrange to attend
the discussion section that I can actually attend?

On a related note, I wanted to put myself on the waitlist, but TeleBears
actually won't let me because I'm already enrolled. If I drop the course, will
TeleBears keep me from adding it again (i.e. can I drop the course and then
stick myself on its waitlist)?

### Anant Sahai's answer
Discussion sections are really important. If your schedule is crazy, you will
have problems beyond this issue. Crazy schedules are not generally a good
idea.

In general, our discussion policy is going to be similar to the policy for 16A
this term. Attend a section that works for you, but people registered have
priority for that section.

## EECS vs CS

2015-11-13
Hi everyone,

I am a new Freshman to Berkeley and got in as Pre-CS.

So here is my dilemma I recently heard a professor (Prof. Sahai) and many
students suggest that EECS is better than LSCS in terms of employers/graduate
school. However I am really interested in pursuing a double major in Pure Math
and CS/EECS. I also am currently doing very well in Math 54 and CS 61a. Is it
worth starting the transfer process to COE for EECS? I think I can get the GPA
necessary to transfer but I really would like to study pure math. If it makes
a difference I want to do the minimum level of EE possible in either majors. I
simply do not like circuits or hardware but am willing to do it if EECS is
better.

Should I stay or attempt to switch. A lot of people think LSCS is not a strong
major cap or not.

Also just out of curiosity why is LSCS a BA but Environmental Economics and
Policy a BS. It makes almost no sense!

### Instructor answer
First of all, congratulations on your admission to UC Berkeley! Both of our
programs are excellent. Students in EECS and LSCS take the same classes with
the same faculty. As the student above mentioned, if you plan to pursue a
double major, LSCS has the same breadth requirements as math, so you will not
need to complete extra breadth requirements. In addition, it can be very
difficult to transfer into COE. The requirements for transfer can be found
here: <http://engineering.berkeley.edu/admissions/undergrad-admissions/change-
college>

As Professor Sahai states, there are some differences in priority for the two
majors. If you have questions about how this will impact you, please don't
hesitate to email me
([svannostrand@eecs.berkeley.edu](mailto:svannostrand@eecs.berkeley.edu)). As
Professor Sahai and others have mentioned, it's important to do what is right
for you and for your education. For folks in industry and graduate schools, it
doesn't matter whether you pursue EECS or LSCS.

## CS61C vs EE16B next semester

2015-11-04
I am an EECS sophomore who has not taken CS61C or EE16B and does not have a
strong preference of CS vs EE yet. I was wondering if I had to choose which
would be more beneficial to take first.

Also, is there an update on whether CS61C could offer another final time for
people taking both EE16B and CS61C?

Thanks!

### Elad Alon's answer
There certainly isn't a "right" answer to this one, but if I had to choose one
of the two, I would probably recommend taking 16B first. The main reasons for
this are that (1) 16B is a somewhat broader intro course, so it would open
more doors for you (61C opens doors to classes as well, but less broadly so),
and (2) 16B covers at a somewhat more basic level some material that also
shows up in 61C. (There are no changes in 61C planned/expected because of
this, but over the long term, we expect that people will in all likelihood
have taken 16B before or at most concurrently with 61C.)

  

I'm not sure about a 61C alternate final, but will ping the instructors to
ask.

## Taking CS 70 as a freshman in EECS

2015-11-03
Math 54 Lecture 1 is very quickly filling up, and since my telebears is not
until tomorrow - it is likely that I may not get in. As a substitute, I may
take CS 70 - however, I have not taken any Berkeley math yet. How good of an
idea is it to take CS 70 as a freshman without Berkeley Math experience?

### Anant Sahai's answer
You take a sophomore course as a freshman at your own peril.

It is in general a very bad idea to take 70 without meeting its official
prereq: sophomore mathematical maturity (from the perspective of the EECS
department). Getting a 5 on the Calc BC exam is definitely not enough, by
itself, to have sophomore mathematical maturity. Taking Math 1A and 1B in some
cases (for students who pay attention, actually read the book carefully, pay
attention in lecture, and understand the proofs instead of just doing the HW
and hunting for formulas) is enough to provide sophomore mathematical
maturity, but it sometimes isn't enough. Some people catch up quickly, quite a
few do not. (I have seen more tears in 70 than I care to remember, and this is
a big part of what drove us to create 16AB. We want to stop these tears.) Math
53&54 have historically been better about getting students ready for 70
maturity-wise, but again, can be a bit hit or miss. (Not as much as 1AB, but
still.) Meanwhile, some students get here straight from high school with the
adequate mathematical maturity.

With the advent of EECS 16AB, they represent the definitive sense of what
defines sophomore mathematical maturity. These are what we officially deem to
be the Freshman EECS courses alongside 61AB. And 16AB are on the mathematical
track, just like 70 is as a sophomore course. 70 is the third course in the
mathy sequence, just like 61C is the third course in the software engineering
sequence.

## CS: Do we have to attend the EE16A discussion/lab that we signed up for?

2015-10-30


### Elad Alon's answer
You do need to attend the lab that you signed up for (otherwise we have no way
of managing the space/resource constraints in the lab), but discussion you can
generally choose to attend a different session later (the only caveat is that
if one particular session gets overly crowd for the room it's in, but I don't
expect this to happen).

## CS 61C and EE16B Final Exam Conflict

2015-10-29
I know that the class conflict will not be resolved, but is it guaranteed that
if we take both courses we will be allowed to schedule an alternate final time
so we can take both finals? I've heard varying answers so I'm a bit confused.
If it is guaranteed, who should we contact about the final arrangement?

### Instructor answer
Hi there, Unless you've heard something from one of the faculty, this
definitely is not guaranteed. Last I heard, Professor Katz is working on a
solution, and the EE16B faculty are considering publishing the webcasts a week
behind schedule (to encourage lecture attendance) and don't believe an
alternate final will be possible. Until you hear from the faculty or
department staff that taking both is possible, I would not plan on it.

## Taking EE16B or Not

2015-10-28
Hi, I'm a freshman EECS major with just a few questions.

First, if we are currently enrolled in EE16A, is it required for us to take
EE16B in the Spring of 2016? Or, instead can we choose take our other required
classes, such as Physics 7a and Math 53 (Plus CS61B and an AC requirement)?
And, of course, then proceed to take EE16B in either Fall 2016 or Spring 2017.

However, if that is not required, is it _recommended_ that we take EE16B in
Spring 2016? If so, why? I ask this because I feel that although these courses
are designed as intro courses, I would much rather go into them with a better
understanding and skill level in physics and math. Thus, I am leaning towards
taking my math and physics courses prior to taking EE16B.

Also, is there any update as to whether EE16A and EE16B will account for Math
54? If not, would it better to take Math 53 or Math 54 before EE16B?

Lastly, during our TeleBears appointment, do we have to choose the courses
that we discussed with our faculty advisor? I thought of taking different
courses after having spoke with my faculty advisor.

Thanks!

### Elad Alon's answer
Hi There,

It is not required to take 16B in spring if you are currently enrolled in 16A.
The recommendation is to finish the series within your first 3 semesters.
Faculty may want to chime in about your desire to have more physics and math
before taking 16B. (Edit by Elad: please see my note below with
comments/suggestions on this and other points.)

At this point there is no update on Math 54; it is still a requirement. Please
see post @556 for more information.

### Followup:
Elad Alon:
Getting your lower div. requirements done by the end of sophomore year is
certainly a good idea, but if e.g. one of those courses (particularly one that
doesn't have a specific lead in to material you're interested in learning more
about later) ends up in junior year that isn't to bad. I'd recommend putting
together a "four year plan" and then you'll be able to tell what the
implications of the various choices are.

To be more specific, given the exposure you've already had in 16A and that
you'd like to get some more background in linear algebra, taking 61B, 16B, and
Math 54 should be very manageable (and would certainly keep you on track).

Student:
Oh, and 61C also remains.

Student:
Your response hit it right on the dot - thank you.

I was told in faculty advising, however, that I should be taking 3 technicals.
From what I understand, ideally, by the end of sophomore year, I should have
completed my lower div requirements (remaining: 61B, 16B, 53, 54, 7a, 7b,
CS70). If I was to only take 2 techs (61B and 16B) next semester, would I
still be on track?

Regardless, I would like more practice with linear algebra so I believe taking
54 alongside 16B will be quite beneficial.

Elad Alon:
It's probably worth mentioning that taking just two techs (61B and 16B) is
perfectly acceptable and you shouldn't feel the need to do more than that.
Also, the way I am interpreting your question (please correct me if I'm wrong)
is that you are asking about which of those three classes would have greatest
synergy with EE16B in terms of the content?

If my assumption above is correct, out of the three you mentioned,Math 54 is
by far the most directly relevant. That said, it's largely a question of how
comfortable you feel with the linear algebra material in 16A. If you feel
pretty comfortable with it, then Math 54 will be repetitive and may not be
worth it; but if you would like to get some more practice/etc. with that
material, then by all means that's the class I would go for (out of the three
you mentioned)

Student:
Thank you for those responses. Another question:

If I do take EE16B in the Spring, along with CS61B (and an American Cultures
requirement) what other class should I take with these 3 - regarding Physics
7a, Math 53, and Math 54? Specifically, which of these classes would be the
best to take alongside EE16B and really help me develop my skills?

Thanks again

Anant Sahai:
I'm going to second what my colleague Elad Alon has said.

And I want to add that with this particular full-scale cohort of 16A (folks
taking it this term), we are going to be gently adjusting and balancing the
material across 16A and 16B (and eventually 70). So, this next 16B is going to
pick up pretty much exactly where this 16A leaves off. Our goal is to educate
you and so we will choose to pace the course so that it works. We are also
going to be understanding of the times when there are difficulties that come
from "growing pains" in the course --- and take that into account while
grading. So, you're best off just following through with the sequence along
with your classmates. Future offerings are going to reflect the more fully
stabilized material and depend on the stabilized 16A. So, in later 16Bs, you
might find yourself missing something that your classmates learned in their
16A --- that was inserted there in response to what we learned from this
particular 16A, and that we chose to patch in 16B instead.

Elad Alon:
I should have also noted BTW that if anyone would like to get some personal
advice about EE16B and your course schedule, please feel free to contact me or
simply swing by my office hours.

## EE16B Labs/Discussions

2015-10-26
Can we sign up for different labs and discussions for EE16B like we did for
EE16A? For example, I have a 102 Discussion and 101 Lab for EE16A. Is that how
it is for EE16B too?

### Anant Sahai's answer
Yes.

## Math 54

2015-10-22
How likely is it that Math 54 will be removed from the requirements? Should I
not take math 54 next semester if i was planning to?

### Instructor answer
At this point in time, the faculty have not proposed this change or started
any work to remove the requirement. You should continue to enroll in courses
knowing the Math 54 is a requirement. Once anything official has began, we
will notify students. As Lily said, this will take a number of semesters if
formally proposed.

### Followup:
Student:
Hi,

I'm a freshman and my advisor never mentioned any of this to me, she simply
told me to register for 54. Now I'm in EE16A this semester, but now I'm
worried about the the material that I'm missing out on by skipping 16B. What
should I do? Should I take 16B anyways?

Student:
Cornell CS also isn't accredited

Student:
It just means that Berkeley doesn't try to have CS reviewed by another
organization... it doesn't mean anything though... Carnegie Mellon SCS and
Stanford CS are not accredited as well but Berkeley EECS and MIT EECS are

Student:
What does it mean that L&S CS isn't accredited?

Anant Sahai:
I'm sure I'll teach 70 at some point in the future, though it might be years
from now. Currently, I am focused on getting 16a (this semester) and 16b (next
semester) up to be great courses leading up to 70. The 16ab courses are being
built with lots of the teaching ideas from 70 used throughout. Although the
material can be different, you can think of 16ab as being taught "like 70, but
with labs."

Student:
Hi Prof. Sahai,

There has been a lot of speculation, but is it true that you will not teach CS
70 anymore? People have said that your CS 70 is one of the best taught CS 70s

Thanks,

An Anonymous Student

Anant Sahai:
Spring 16a is going to be running at the maximum possible size. There are
limits on TA availability. (This will get better as more students run through
the new courses and a deeper pool of potential TAs has been trained.)

Our own preference is that Freshmen should take it. However, true seniors who
haven't taken 20 or 40 yet are in a hard place. So, they have to be given
preference. But we believe that the L&S backlog will be clearing out over the
next semester or two. The EECS backlog will be entirely eliminated after next
semester.

I think that there is enough difference in perspective in 54 and 16ab that 16a
will be fun even for them. But yeah, taking a freshman course as a senior
could very well be boring for some. Oh well. In the long run, we really would
like to get both 16ab taken by L&S people before they declare, but we will
have to see what the best way is.

Student:
What about those of us who are Math/Stats/Econ/etc. double majors in L and S
who require Math 54

Student:
Looks like LSCS people who have taken 54 are in for a really boring EE 16a

Student:
Do you think it will be possible that EE 16a can expand like CS61b? the
difference is only 200 students (about 900 in 61b vs 700 in 16a)... currently
the LSCS advisors seem to be pushing LSCS students to all take EE 16a their
senior year, since the new course enrollment procedures have a very very large
amount of seats reserved for LSCS seniors.

Why would the EECS department purposefully try to hamstring half of its
students... :(

Wouldn't the department encouraging EE16a to be taken as sophomores rather
than seniors (since LSCS would be declared by the end of freshman year) be a
better option? (even adding EE16a to the declaration sequence like CS 61a,b,70
since it appears to be a rather important class)

Student:
i am wondering about something similar ^

Student:
Slightly confused - if I'm a LSCS freshman who plans on taking both 16A/16B,
should I hold off on Math 54? Even though it's currently still a graduation
requirement, and it's not guaranteed that I'll even get 16A anytime soon?

Anant Sahai:
First, 70 is not the same as Math 55. They are very different, even though
there is some conceptual overlap.

From our point of view, taking Math 54 and 16a together makes about as much
sense as taking Math 55 and 70 together. Yes, the added practice and different
approaches from Math 55 would definitely help you in 70. Just because more
practice and seeing different approaches helps with anything. But is it the
most effective use of your time? Probably not. So take 16a and 16b first. Then
decide for yourself if you want to take Math 54.

Are Math 54 and 61a adequate prep for 70? In some cases, yes. In other cases,
no. Depends on both the student and who taught them 54. It is in part because
of those "no cases" that 16ab exist.

Student:
Would it make sense, then, to take EE16A and Math 54 concurrently? (if I
intend to take 16B in Fall 2016)

Student:
I've taken Maths 54 not 55

Student:
Isn't CS 70 == Math 55? if so you should be fine

Student:
Thanks for the information!  
Just to be clear, if a person has taken Maths 54 and CS61A, how prepared is
he/she for CS 70?

Student:
Thank you! It seems like getting into EE16a will be much easier once LSCS
people are able to declare (which for most will be around the end of Freshman
year)

Anant Sahai:
The goal of the design of 16a AND 16b is to serve both the EECS and L&S CS
populations as freshmen, or whenever they would be in principle prepared to
take Math 54. (5 on the Calc BC or actually, even having finished Calc 1A at
Berkeley itself.)

So, yeah, we would recommend L&S intended-CS to take 16a and then 16b as soon
as possible. We designed 16a and 16b to be so that 16a, 16b, and 70 form a
sequence like 61a, 61b, and 61c. Both myself and more importantly, Gireeja
Ranade who had given guest lectures in 70 and is a prime force behind the 16
sequence, saw that many students suffered in 70 because of inadequate courses
before that. 16ab solve that.

The problem is that right now, there is so much backlog that we can't open
enough seats for L&S intended CS freshmen. Much to our dismay, but seats are
finite. Oh well. The problem will get fixed once the backlog is cleared.

Student:
Hi Professor Sahai,

So if we are LSCS do you recommend taking EE16a early (possibly so that we can
see the more applied parts of Linear Algebra) ?

I am currently a freshman enrolled in Math 54. However, the class certainly
seems more theory focused, with students focusing on concepts like subspaces
and vector spaces for very long periods of time.

Anant Sahai:
Quite possible in practice, yes... However, you should separate out two
questions. As far as graduation requirements go, they are really only
important when you are about to graduate. There is also the question of
actually needing the material for our courses. So make sure that you take 16AB
as soon as you can. That way, you will have the understanding required to
tackle EECS upper-div courses that need linear algebra.

Student:
Right now I'm planning to take Math 54 spring of my sophomore year. (I'm a
freshman right now). Is it possible the requirement might be changed by then?

Anant Sahai:
Actually, the possibility extends even more strongly to L&S CS. The idea is
that 16a and 16b together will obviate the need for Math 54 prereqs for our
own courses. (And moving the requirement would keep the total number of
courses required neutral.) And given that L&S CS is not an accredited program,
we won't have the requirement to have two math courses from the Math
department. So it is much easier to change the requirements. Having the
department's full lower-div courses being taken by both sets of students, EECS
and L&S CS, will help in aligning both groups together both culturally and
educationally as far as the upper-divs are concerned. 16AB are being built
explicitly with the needs of upper-divs like 184, 189, 170, 127, etc. in mind
as well as for 70.

Student:
Just EECS (The idea behind this is that ee 16a and 16b wil cover enough math
54 material).

## Recitation Sections

2015-10-20
What are recitation sections, specifically for EE 120? How are these sections
different from discussion sections?

### Anant Sahai's answer
They are the same as discussion sections. Just a different name.

## Differences between CS174 and EE126?

2015-10-20
They both seem to cover the same topics, and I'm trying to decide between the
two.

### Anant Sahai's answer
Prof. Sahai: The main difference is the perspective. Both deal with
probability, but in 126, the focus is more on understanding the underlying
concepts, the theory, and how they can be used to model situations and apply
in different settings. By contrast, in 174, the focus is a little bit more on
technical tricks and techniques that can be used to analyze randomized
algorithms. Overall, 126 is the more "core" supported course in the
department. It's offered every term, etc.

My personal perspective is that after taking 126 and 170, you should be able
to get a lot of the value in 174 by reading the truly excellent textbook for
174 and then applying the ideas if you ever need to analyze a randomized
algorithm. The reverse is not true. Your conceptual foundation in probability
after just 70 isn't strong enough. After 126, it should definitely be quite
strong. With 174 alone, it is possible to still have conceptual/intuition
holes if you find yourself just relying on the techniques. Basically, if you
have to take just one, take 126. If you have to take one first, take 126
first.

Lily Zhang: The only additional information I have for you is that CS 174
focuses on randomized algorithms and using probabilistic processes to analyze
algorithms learned in CS170. I would also add that I recommend speaking with
the instructors to determine which course would fit your interests. Office
hours and faculty advising are great places to do this :)

## EE16A Midterm Scheduling

2015-10-15
Hello,

I'm trying to take both CS169 and EE16A next semester. I know they have time
conflicts, but I heard EE16A will at least be webcasted.

From previous years that Fox/Patterson have taught CS169, I've heard there is
no final, but there are in class quizzes. So I think if I do take both, taking
the final for EE16A will be fine, but I was wondering if the midterms for
EE16A were scheduled during class? If so, is it possible to schedule the
midterms to a different time, if we contact ahead of time?

### Instructor answer
I'm not sure that our faculty have scheduled midterms already, so the best
people to ask would be the instructors of the course, especially if you may
need accommodations.

## CS 70 Without EE 16B

2015-10-15
I am planning to take EE 16B in Spring (already finished Math 53/54 and I'm in
16A right now). Could I take CS 70 in Spring as well or does it now depend on
the content from EE 16B?

### Anant Sahai's answer
I posted about this in the 16A Piazza. In general, taking 70 and 16B
concurrently is fine from a material point of view for students who have had
16A --- and especially if they have also taken Math 53. However, you have to
watch the workload for your semester as a whole.

## Reserved Spots for EE 16B and CS 61C (not B!)

2015-10-10
I'm an EECS freshman. Should I be using phase 1 to get into these courses, or
will spots be set aside?

\--

Thanks, Professor Sahai! I suspected that, but wasn't sure how many people who
took 16A in the Spring might have delayed 16B 'til next semester.

### Instructor answer
16B requires 16A as an absolute hard prereq. There are 490 seats in 16B. There
are about 480 people in 16A this term. There are about 10ish other students
out there who took the 16A pilot and did not take the 16B pilot.

What deduction can you make for this regarding the supply vs demand in 16B?

What consequences might this have upon your decision to phase 1 vs phase 2 the
course?

We expect all the EECS students taking 16A this term to take 16B next term.
There will be enough seats for them in 16B.

61C will have spots held through the final date of undergrad phase II
telebears appointments (December 10) for declared EECS majors (see
<http://www.eecs.berkeley.edu/Policies/enrollment.shtml> ).

### Followup:
Student:
61C will have spots held through the final date of undergrad phase II
telebears appointments (December 10) for declared EECS majors (see
<http://www.eecs.berkeley.edu/Policies/enrollment.shtml> ).

## EE16A for LS CS Freshman

2015-10-10
Does the EECS Department believe that for Spring 2016, EE 16A will be able to
accomodate for freshman in L&S CS? Also, will there be spots reserved for L&S
CS Majors (or undeclared) for EE 16A since it is a lower division requirement
for the CS major?

### Anant Sahai's answer
16AB are designed with L&S intended-CS students very much in mind. (As long as
you have a 5 on the Calc BC AP exam or equivalent) It's only because of the
backlog of demand that it has been nearly impossible for them to get in till
next semester.

We are hoping to have some seats available for L&S intended-CS freshmen in 16A
in Spring. The Fall offering was super impacted and we were sadly unable to
let more than a handful of intended-CS freshmen into the course --- or for
that matter, even declared CS students. The Spring offering is both bigger and
we expect that most of the pent-up EECS demand will already have been
satisfied in Fall. So, quite a few seats should be available for L&S students.

However, our initial estimates say that 16A in the Spring might still be
oversubscribed and because of lab-space limits, the size can't grow
significantly beyond what is on the schedule. So if you are L&S intended-CS,
be sure to keep that in mind.

## EE 16A, CS 170 conflict

2015-10-08
I really want to take EE upper divs, but I've been shut out of 16A this
semester as a CS major, and now I have to postpone it again for 170 which is
very frustrating -- I know it's not the department's fault or anything,
especially since I'm not even EECS, but I was wondering if either EE 16A or CS
170 will have provisions for the conflict (in terms of midterms and
webcasting)?

### Instructor answer
I can't give a 100% guarantee of this until the semester is actually under way
and we have fully worked out all of the logistics, but I expect that there
will be an opportunity for a make-up final exam for EE16A next semester.
(EE16A will definitely be webcast, so there won't be a issue with lecture.)
So, I would certainly encourage you to try and sign up for EE16A - please note
that there will still be some limitations on enrollment (mainly due to lab
space availability).

As per the Professors of the course, CS 170 will not be webcast and there will
not be alternate exams.

### Followup:
Student:
CS 170 will not be webcast and there will not be alternate finals

Elad Alon:
Please see above.

Student:
+1

Student:
+1

## EE120 and 16B

2015-10-07
Would it be a good choice to take EE16B and EE120 concurrently after taking
EE16A and Physics7B? I plan to do that next semester but I am a bit worried
about whether this is gonna work out as expected in my 2nd semester of my
sophomore year.

### Anant Sahai's answer
120 really is supposed to be taken after 16B. I guess someone could take them
concurrently, at least right now in the transient period before everyone is
going through 16A and 16B as freshmen.

## Spring 2016 CS 169 and EE16A conflict

2015-10-03
Hi I noticed that EE16A's time got changed to the same time as CS 169, Tu/Th
330-5 pm. Is this finalized or is it going to be changed again and hopefully
accommodate students who wish to take both? =D

Thanks!

### Instructor answer
The time/day slot for EE16A is final - unfortunately there is simply no way
for us to meet all of the other constraints (particularly getting a large
enough room) and avoid all possible class conflicts. 16A will be webcast
however, and it may be possible that arrangements can be made for things like
the final exam. It is completely at the faculty instructors' discretion as to
whether to offer alternate exams so you should not assume this will work out
unless you have one or the other instructor's commitment confirmed in an
e-mail.

### Followup:
Elad Alon:
I believe what's on schedule.berkeley.edu may be out of date - as far as I
know for Spring 2016 we do intend to give highest priority to majors that need
EE16A to graduate. Will check in to that on our end and hopefully get the
online info updated - if you don't see that in the next week or so please feel
free to ping us again.

Student:
Don't fret. The reason you were kicked off the wait list last spring was
likely because it was a very small, limited trial run focused on the classes
target demographic (freshmen/sophomores). The reason for that note is that
moving forward this EE16A/B is supposed to be for lower division standing
students, but the department understands that during the transition from 20/40
to 16A/B it won't quite work out that way.

## spring 2016 EE16A and CS161 conflict

2015-10-02
hi,

i noticed on schedule.berkeley.edu that EE 16A and CS161 are both MWF 11-12P
next semester, which implies same final slot. is there going to be any way to
be able to take both these classes next semester? :(

### Elad Alon's answer
Please see my responses to the follow-up discussions below if there are other
conflicts anyone is worried about.

### Followup:
Elad Alon:
This is indeed the final time for EE16A next semester. We do however hope/aim
that you'll enjoy EE16A just as much (if not even more) as the other classes
you were dreaming about :)

Student:
If this change is final yes thank you thank you thank you!!! My hopes and
dreams felt so crushed when I thought I'd have to sacrifice 161 to graduate.
:D

Student:
it got changed. nice

### Followup:
Elad Alon:
Our apologies for this - this was the only slot we could get with an
appropriately sized room on TuTh. EE16A will be webcast however, and if you
contact the instructors/get their approval you will likely be able to make
arrangements to resolve the final exam conflict.

## EE 16A Spring 2016

2015-10-01
I'm an EECS major with senior standing who hasn't taken EE 16A yet. I noticed
that on the new schedule, EE 16A was restricted to people with a class
standing of Freshman, Soph, or Junior. I was wondering whether this was a
mistake/would be changed? Or am I screwed forever?

### Instructor answer
No information on the campus online schedule should be taken seriously. The
schedule was supposed to go live on Monday and the fact that it is live today
means that departments all across campus who were double-checking information
were caught unawares.

### Followup:
Student:
see @501

Student:
Hello, I am in a similar situation in terms of standing, but I was wondering
if there are going to spots reserved in EE16A for eecs senior standing like
they did with EE 20/40? So, I was pretty much wondering if we could phase 2
EE16A with a relatively safe chance of not getting kicked out. I also want to
take 2 other upper div cs classes and the other cs upper div classes are
pretty competitive too.

Elad Alon:
Ok great - our current plan is indeed to give folks like yourself priority
next semester, so you should be in good shape.

Student:
Thanks! I'm an L&S CS senior. I actually didn't take it this semester because
they told us to wait for next semester.

Elad Alon:
As far as I know, for spring 2016's EE16A we will be prioritizing graduating
majors - hopefully the official channels will be updated to reflect this soon.

One clarification however - are the two of you L&S majors, or CoE? If CoE, you
would need both EE16A and EE16B to graduate, which wouldn't be possible in a
single semester since one requires the other.

## CS61C and EE16B Spring 2016 Conflict

2015-10-02
CS61C and EE16B have the same lecture times and final slots. Will this be
changed?

### Elad Alon's answer
Unfortunately the 16B time/day slot will not be changed - there were simply no
other options available. The class will be webcast however, and I'm sure that
arrangements can be made for things like e.g. the final.

## Graduating a year early

2015-09-23
Thinking about graduating a year early in EECS. I have taken (and will have
taken after Spring 2016 semester):

170, 188, 189, 162, 186, 194-15, 161, 16a, 16b.

I feel like this is a solid enough base for what field I currently plan on
going into (backend SE, systems, etc...), and I am out of state so the
financial burden of another year/semester really doesn't appeal to me if it
only means 1 or 2 classes I am interested in taking.

The primary reason people have given me for staying is "its college do what
you want" and while that would be nice in a perfect world, it just isn't that
way and I cant really justify to myself why it would be worth it to take some
random classes in other departments...I really like EE16A right now, the
concepts of EE are interesting, but I am afraid of taking another semester of
those types of classes and them not living up to my expectations.

Any advice would be great!

### Elad Alon's answer
I'll avoid commenting on the main question for now, but I did want to offer to
suggest EE classes I believe you'd be likely to enjoy if you're interested in
following up on that path further. Feel free to email me or come by my office
hours if you'd like to discuss that further. Regardless, very glad to hear
that you're enjoying EE16A so far!

### Followup:
Student:
Not just 40k. An extra year in school means you're throwing away
[$108,911+](https://career.berkeley.edu/sites/default/files/pdf/Survey/2014EECS.pdf)
in salary the first year and the equity you get from that (which can be a lot
if you're at Google or another good publicly traded company).

Student:
I agree with Anon, you can do a lot with 40k.

Student:
Sure, reflecting on where you life is headed is something nice to do, but you
don't need to pay $40,000 to the university to do that. I am graduating a year
early myself because I already have a job where I would be happy working lined
up, though I probably would stay another year if I still haven't found a job.

Student:
Having another year to reflect on where your life is headed is just as
important. Money isn't everything in life.

## EE105 w/ EE16B

2015-09-26
Would it be ok to take EE16B and EE105 concurrently after taking EE16A and
Physics7B? Or would i be completely lost in 105 without taking 16B beforehand?

### Elad Alon's answer
While I don't think it would be impossible to catch up in 105 having taken
only EE16A, I would definitely recommend waiting to take EE105 after EE16B.

## EE16A: Lab0: Trouble Downloading iPython

2015-08-30
I am using windows 8, and I am having trouble getting iPython to fully
download. After running the installer as an administrator, I used
check_version.py, and I am missing the following packages:

qt 4.8.6

conda 3.15.1

conda-env 2.3.0

jinja2 2.8

mistune 0.7

tornado 4.2.1

jsonschema 2.4.0

matplotlib 1.4.3

numpy 1.9.2

scipy 0.16.0

Should I install each of these packages separately, run the installer again,
or try something else?

### Anant Sahai's answer
Don't post 16A questions outside of 16A's piazza.

## EE16A

2015-08-25
Do we attend lab and discussion sections before the first ee16a lecture?

### Anant Sahai's answer
Yes. You do.

The labs start on Wednesday as do discussion sections.

This is so that we can get everyone ready ahead of HW 0 which is due on the
first Monday and is designed to help get everyone on the same page in terms of
the class logistics before the steady march of technical material....

## Should I sign up for EE16A

2015-08-05
Hi, I unfortunately saw the email about EE16A after my Phase II appointment
ended and I'm thinking about whether or not to enroll. My current schedule is
Math 54, CS 61A, Physics 7B, and Com lit r1b. If I enrolled in EE16A, I'd have
to change my lab and discussion sections for Physics 7B, but everything else
would be okay. I have a few questions while I'm mulling it over:

\- how exactly does EE16A prepare you for Math 54? I've heard that it does,
but is it essential / would my eecs experience suffer if I took EE16A in the
spring as opposed to in the fall?

\- If I decided to enroll, how would I get an add code if there are no more
seats remaining? (I'm an incoming eecs freshman)

Thanks!

### Anant Sahai's answer
Yes, sign up if you have a 5 on the Calc BC exam or equivalent. 16a is
extremely important for EECS. You should take it as early as possible. We want
to bring everyone in line to the new system fast because our goal is for
sophomore and later courses to start reflecting this as soon as possible.

  

We will teach linear algebra, connect it to practical context, with intuition
more deeply rooted than you would get in math 54. Everywhere in EECS that used
to depend on math 54 is going to shift to expecting EECS 16ab instead.

  

Our recommendation is to drop 54 now and think about whether you have to take
it after finishing 16ab and 70.

  

We are letting all EECS freshmen in. Just add it.

## EE 16A what is the right choice

2015-07-28
I have received numerous emails from the Piazza group regarding EE 16A. My
current classes for the fall of my freshman year are CS 61A, Math 1B, English
R1B, and E 98. Would you recommend a change in my schedule with the new
information that they are sending?

### Anant Sahai's answer
Probably, yes. But it depends on why you are taking Math 1B.

  

If you are taking Math 1B to be safe even though you have a 5 on the Calculus
BC exam or equivalent, then you should almost certainly be taking EE16A
instead. Most EECS freshmen will be in 61a and 16a together.

  

If instead you don't really understand basic calculus, then you should indeed
take Math 1B and then take 16A in the Spring alongside 61b. Students in 16a
need to feel comfortable with math and calculus. We don't expect lots of fancy
integration tricks, etc. But it is important to feel comfortable with what a
derivative is, how to do simple integrals, how to maximize a simple function
by taking the derivative, and to be able to follow simple derivations of
formulae.

### Followup:
Student:
Thank you very much for your insight. Your answers are very helpful!

Anant Sahai:
It's up to you. It depends on why you got a 4 on the Calc AB exam and why you
took the AB exam instead of the BC exam.

  

But most likely, the reasons why these two things happened indicate that it is
better for you to take math 1b.

## What does EE 141 function compared to CS 150?

2015-07-29
I heard that EE 141 and CS 150 will share the same lectures in the future, but
different labs. I am focusing on EE field. Could the instructor tell me how
this works? As far as I know, many hardware companies ask their potential
employees to take CS 150. If I just take EE 141, will it fulfill the
requirement from the companies? If I have to take both labs, how does it work?
I know CS 150 and EE 141 are both hard class, and I do want to plan ahead.
Also, does the lab of EE 141 have the same difficulty and same workload as CS
150? Thanks!

### Elad Alon's answer
EE141 and CS150 actually already shared lectures last semester (Spring 2015),
and will continue to do so this semester. Both courses cover key concepts in
digital circuit and system design - the difference is really only that CS150
exercises these concepts (and covers the appropriate tools/flows) by applying
them to FPGA based implementations, whereas EE141 focuses on integrated
circuit implementations (again learning the appropriate tools/flows).

It depends on the specific requirements of the job, but most likely if you
take EE141 you would have the skills needed to do the work of a job that asked
for CS150. (There may be some specific tools/flows you would need to pick up,
but this should be quite do-able.)

Traditionally, the CS150 lab had a more complex project (since the level of
abstraction you needed to specifically engineer was higher than EE141), but
I'd recommend getting in touch with the instructors (Vladimir Stojanovic and
John Wawrzynek) to find out more about their specific plans for this offering.

## Waiting list procedures for EE 16A

2015-07-28
For the manual waitlist for EE 16A, will the enrollment be based off of
waitlist position in discussion, as in automatic waitlists, or will it be
based off of any other other criteria first?

### Anant Sahai's answer
We are saving seats for freshmen EECS. Essentially all of whom should be in
16a alongside 61a. Once they have enrolled, we will enroll by priority. EECS
students who used phase 1 units will get priority to get in. A smattering of
others might also make it. The first midterm is before the drop deadline, and
with some natural attrition, we expect a significant number of those who stick
through to get in.

  

Next semester and beyond, we expect to have more room for non-eecs students
since the eecs backlog will have been reduced by a lot.

### Followup:
Student:
Thanks!

Anant Sahai:
Probably not. But who knows.

### Followup:
Anant Sahai:
Pragmatically, the chances aren't that great. Right now, there are 160
potential seats available. We expect maybe another 20-60 or so EECS freshmen
to sign up. That leaves somewhere between 110-140 seats that can flow to the
waitlist.

There are about 90 EECS people on the waitlist. They'll get priority and it
looks like a pretty safe bet for them.

So, this leaves about 20-50 seats for others. Within that, we will probably
prioritized undeclared intended-CS freshmen (to help align them into the new
system), but there aren't that many of them signed up. So other people are
definitely going to get in from the waitlist. Beyond the waitlist, there will
be some natural attrition as people drop the course ahead of the drop deadline
for random reasons --- probably another 25 seats at least will free up if 5%
drop. So, another set of persistent people will be able to get off of the
waitlist and into the course. But not everyone.

We'd love to be able to get everyone in, but we don't have the lab space, hw
party space, or teaching resources.

Currently, my advice to folks who have a specifically "EE" requirement that
needs to be filled like MechE or BioE or so on is to take EE40 the last time
it is offered. That is a traditional EE course of the type that serves MechE
students well. They should not really be in the 16A waitlist. 16A is not
currently designed to, by itself, serve the needs of those students. It is
designed to be an introductory EECS course that will, together with 16B, serve
the needs of EECS and L&S CS students primarily. These folks should drop off
the waitlist for sure and register for 40.

For experienced L&S CS students who are already taking upper-division EECS
courses and really just want to take one course and graduate --- if you are
viewing 16A as a breadth course, you're probably better off just taking 20 or
40 since it is the last time those are being offered. 16A isn't intended to be
approached as a breadth course for anyone. If you just want to be able to take
105 or 130 or 140 or 142, taking 40 is probably the better option. 16AB are
going to be run and taught and graded assuming that the core set of students
are freshmen --- the way that 61AB are. 40 and 20 are more sophomore-aimed
courses, the way 61C and 70 are.

## Physics 7B

2015-07-27
Does Physics 7B content overlap with the content learned in EE16A? I was
considering taking Physics 7B as a freshman but wasn't sure if I would need to
take a Math 5X course beforehand.

### Elad Alon's answer
I believe there is a small amount of overlap between Physics 7B and EE16A in
terms of circuits-related content. The focus in Physics 7B is (understandably)
the underlying physics of the components and a little bit about how they work
in circuits, whereas in EE16A we will be focusing more on circuits themselves
as a vehicle to expose you to the design process and how to apply it to solve
problems. Note that you don't need any prior knowledge/exposure to circuits
for EE16A - we will be introducing the basics of circuits on an as-needed
basis in the class.

It's worth noting that Physics 7B does use multivariable calculus (mostly for
the E&M portion of the class), so you probably want to have Math 53 under your
belt before taking it.

## Switching into EE16A for Phase 2, worried about being waitlisted and not
getting the class.

2015-07-27
Hello, I received the notice that anyone who got a 5 or higher on the Calculus
BC test should be taking EE16A over something like Math 53 or Math 54. I'm
happy to switch into that if its recommended, but when looking at schedule
builder and the online schedule of classes, it didn't seem like there were
available seats, or in those classes with available seats, the waitlist was
the same size. I'm worried that if I swap into the class in favor of Math 53,
I might not get into the class. (I did notice in the email that was sent out
that you were saving spots for incoming students in a situation like mine, but
would like a second confirmation!)

Any help would be greatly appreciated!!!

### Elad Alon's answer
We are definitely saving seats for students like yourself, so please do go
ahead and switch.

## EE16A and Math 53 final on the same day

2015-07-27
I have switched into EE16A but realized that its final is in the slot right
before my Math 53 (lecture 2) final. The Math 54 class and section 1 of Math
53 class are both full. I could take Physics 7B instead of EE16A, but from all
the discussion about taking EE16A, I think I would rather take EE16A first
semester. So is there anything else I can do to avoid 2 finals on the same
day?

### Elad Alon's answer
I'll let Anant comment on final scheduling options for EE16A, but assuming you
were planning to take three technical courses and that the Physics 7B final
isn't the same day, taking CS61A, EE16A, and Physics 7B is a perfectly
reasonable option. Or, you could take just CS61A and EE6A and fill in the rest
of your schedule with non-technical courses; the vast majority of upper-div.
EECS courses are gated by the CS61/EE16 series (not by math/physics), so if
you choose this option you'd still be in great shape in terms of getting
yourself ready for the rest of the program.

## EE16A Switching Sections

2015-07-26
If I want to switch my discussion section for EE16A during Phase II (I'm
already fully enrolled from Phase I), would I need to be in any waitlists if I
use Change Sections on Telebears or will I be able to immediately switch my
section?

### Elad Alon's answer
You should be able to switch sections without going through the waitlist. That
said, if from whatever reason you run in to trouble with this, don't worry too
much about "officially" changing your section - once the semester starts you
can attend any section you'd like to as long as there is room. (The people who
signed up for that section have priority, but this a form of politeness and in
practice is rarely important.) Please do be sure to sign up for and stick to
the appropriate lab however since the labs are substantially more space and
resource constrained.

## Error Switching Sections for EE16A

2015-07-25
I'm enrolled in EE16A, but I'm trying to switch my discussion section while
keeping my lab section. I've tried doing this multiple times, but when I click
on the lab I'm already enrolled in and the discussion section I'd like to
switch to, tele-Bears gives me a system error and asks me to try again every
time. I've check to make sure that the discussion I'm switching to isn't full,
but the problem persists. Any ideas on how to solve this?

### Anant Sahai's answer
Don't worry so much about discussion sections --- we will let people attend
other sections as long as there is room. (Priority is for people registered in
that section but that is just simple politeness.) The lab section is what
matters since labs are required and more tightly space-constrained.

## General EECS Requirements

2015-07-27
Is Math 1B required to be taken for a letter grade for EECS majors even if
you've gotten a 5 on the AP Calculus BC exam? Is it recommended to take Math
53 concurrently with EECS 16A?

### Anant Sahai's answer
A 5 on the Calc BC gets you out of both Math 1A and 1B.

EE16A is designed to be taken concurrently with CS61A. (Taking CS61A before is
also alright for people who got here before EE16A was available or for those
who did not get a 5 on the Calc BC or equivalent.)

We recommend taking EE16A before Math 5X, but it is up to you. You can take
them concurrently.

## EE 16A Waitlist

2015-07-19
Does anybody know when the waitlist for EE16A will be processed?

Sahai said that it would be sometime during the end of phase 1 and its
currently phase 2 right now and nothing has happened.

### Instructor answer
We are currently talking with Professor Sahai about when to process the wait
list. Per his request, it will happen sometime in the next couple of weeks.

### Followup:
Student:
Thank you for such quick response! Is there an estimate as to much time should
we expect before admission?

Anant Sahai:
Yes, this is still the case. We expect to be able to let in all rising
sophomore EECS students who used phase I units on 16a.

Student:
Is this still the case? I just enrolled in my phase II classes but my schedule
will change a lot if I do not get into EE16A this semester. I am unfortunately
no longer able to enroll in any of my other 5 lower division technical classes
I have to take this year because I used my phase I units on EE as advised. I
am a rising sophomore EECS student planning to declare ECE. Is there any
update on the likelihood of admission to this class?

Anant Sahai:
The problem appears to be partially technical. Our forecasts are that there
will be room for essentially all waitlisted EECS students who spent Phase 1
slots on EE16A. However, there is no way in telebears to reserve seats for the
freshmen in secondary sections (labs and discussions) and so, we can't just
add all the EECS students to the course now. We are concerned that too many of
the secondary sections will fill up and the freshmen won't be able to fit 16A
into their schedules (they also don't realize that in EECS, people can usually
attend other discussion sections, etc....).

We understand that this is annoying, but there appears to be no better
solution.

Student:
Per instruction from the EE 16A faculty team, we are waiting for some
additional freshmen and transfer students to add. We hope to have more
information soon about when the wait list will be processed.

## Becoming a reader without lab assisting

2015-05-30
Hello! How common is it to become a reader for EE classes without lab
assisting? Also, is it possible to read for 16A or 16B, if I took 20 and 40
instead? Thanks!

### Anant Sahai's answer
In the long-run, the hiring pipeline for 16ab will be like the hiring pipeline
for 61ab. But right now at this transition point, it is definitely possible to
become a reader and/or academic intern (what was formerly called lab
assistant) for 16ab without having taken the course.

  

As a member of course staff, you'd be expected to stay very current with
lecture though. So attending in person and/or watching the webcasts carefully.
The material is not some remix of 20 and 40. There is some overlap, but these
are entirely new courses.

## Course route?

2015-03-29
Wondering if there is a route view of all the upper div courses based on
specific areas of study.

If so could anyone tell me what the website is?

### Tsu-Jae King Liu's answer
The HKN course survey site (<https://hkn.eecs.berkeley.edu/coursesurveys>) has
a nice map of upper division courses.

I've created an updated version, which distinguishes more clearly the areas of
study within
EE:[Course_Maps.pptx](https://d1b10bmlvqabco.cloudfront.net/attach/hyq0br1u3kx7dg/hck3jkt89tc5ot/i7ul97f87fdm/Course_Maps.pptx)

## BMail

2015-03-03
I got this email on my berkeley.edu account and I'm not sure if I should click
on the link.

Access tο yοur email is abοut tο expire, we recοmmend that yοu revalidate yοur
accοunt tο avοid been suspended, Click [Revalιdate ](http://bit.ly/18hqULN)tο
update yοur accοunt.

The Mail Team

### Tsu-Jae King Liu's answer
Indeed you should not click on that link!

Please forward this phishing message to Eric Fraser
([fraser@eecs.berkeley.edu](mailto:fraser@berkeley.edu)), Director of
Information Technology for the College of Engineering, so that he can track
down the source.

Thanks in advance,  
Tsu-Jae

### Followup:
Tsu-Jae King Liu:
See "Five Ways to Spot a Phish" at https://security.berkeley.edu/phishing

