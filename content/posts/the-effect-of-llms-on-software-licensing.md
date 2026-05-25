+++
title = "The effect of LLMs on software licensing"
date = 2025-08-25
lastmod = 2025-08-25
tags = ["AI"]
+++

Here's something I'm thinking of lately: I think that open source SaaS and restrictive OSS licenses are in for a rocky road now that agentic coding is taking off.

If your software is straightforward and it's open source and you're using licensing to enforce freemium, or if you are using freemium add-ons that aren't open source, then you had better hope your moat is deep enough- either through patents or sheer difficulty of the problem space.  Similarly, if you're trying to use GPL3 or other licensing to try to keep other people from commercializing your OSS, you're likely also going to be disappointed.

It's fairly straightforward to point an agent at a GitHub repo and tell an agent: "translate this to Python/Go/Rust/whatever in a new repo here in my account".  The simpler the project (i.e. the "shallower your moat"), then the easier it is for someone to use this technique to build something that does what your software does.

 Yes, it will be buggy, but agents will continue to get better and if your problem space doesn't involve huge complexity or performance sensitivity, then the generated code might not need much work.  And of course the tooling will get better as people flock to this use case.

I also think that the same capability will largely invalidate the GPL for the same reasons, as people point agents at the source and write new equivalent software that performs the same function but with a more permissive license.

My reasoning is this: the only reason that people use OSS versions of software that has restrictive licensing terms, is because it’s not worth the effort to them to rewrite.

Similarly, attempts to use licensing to prevent clouds from profiting from OSS are likely doomed to fail.  Hyperscalers will be able to point an agent (or 1000 agents), and in a day or two come back to a mostly-functional (new software package that does most of what the original did, but now they have a brand new software that they control completely and are not beholden to or restricted by anyone.

Next time someone tries to pull an Elastic Search license trick on AWS, AWS will just agent themselves up a brand new work-alike in a week written in their language du jour, and have it fully functional in a couple of months.

Note that this doesn’t circumvent patent or trademark issues but it’ll be hard to assert that it’s not a new work, esp. if it’s in an entirely different language.
