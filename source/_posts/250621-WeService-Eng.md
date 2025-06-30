---
title: "When AI Meets Teen Mental Health: A Journey of Two 16-Year-Old High Schoolers"
abbrlink: cbf91797
date: 2025-06-30 17:38:16
tags:
---

![Header Image](/assets/0621header.png)

Imagine this scenario: It's 2 AM, and a high school student lies awake, anxious and confused after a family argument. Traditional counseling appointments require weeks of waiting, plus notifying parents and teachers—making an already vulnerable teen even more hesitant to seek help. But what if there was a professional yet warm AI assistant that could provide immediate emotional support, help them sort through their thoughts, and when necessary, smoothly guide them toward professional help?

This isn't a sci-fi plot—it's the reality that the ReachIn mental health support platform is working to create.

## Background Research: The Problem is Worse Than You Think

### The Overlooked Teen Mental Health Crisis

Our research revealed a shocking reality: In our survey of 36 high school students, 69.4% are experiencing identity confusion, 66.7% face academic pressure, and 61.1% are affected by family conflicts. This means 7 out of every 10 teenagers have been found to be quietly suffering from psychological distress, with likely even more in the silent majority.

What's more concerning is that despite such widespread mental health struggles, 38.9% of students know nothing about their school's Psychological Counseling Center (PCC), and 47.2% show low willingness to seek traditional counseling (scoring 1-2 points). The average willingness to seek traditional help was only 2.44 points (out of 5), showing clear room for improvement in existing mental health support systems.

<!-- 0621Img1 -->
![Survey Results](/assets/0621Img1.png)

*Figure 1: Teen Mental Health Survey Results*

### The "Triple Barriers" of Traditional Counseling

Through in-depth research, we found that students' reluctance to seek psychological help can be summarized as "triple barriers":

1. **Privacy Barriers**: School counseling appointment processes usually require notifying teachers and parents, making students feel exposed and unsafe
2. **Cultural Barriers**: Especially in Asian cultural contexts, discussing mental health issues is still seen as a sign of "weakness"
3. **Access Barriers**: Complex appointment procedures, limited counseling hours, and the conflict between 24/7 emotional support needs and limited working hours

It was against this background that the ReachIn mental health support platform was born.

## A Story of Self-Growth: When Two 16-Year-Olds Met AI

ReachIn's story begins in a drama rehearsal room. Project co-founder Jason, while participating in the drama club, found himself naturally becoming a listener for his peers—when friends shared family tensions, social anxiety, or academic pressure, he helped them identify emotional patterns through affirming feelings and asking clarifying questions. This informal peer support often brought unexpected positive results.

However, when Jason tried to transform this informal experience into a structured peer counseling model, he encountered real setbacks. Discussions with psychology clubs and teachers showed that in tight-knit school communities, keeping secrets is difficult, and students—even with good training—cannot reliably identify signs of serious psychological risk.

Meanwhile, another member, Leo, often dealt with emotional issues. As an ENFJ in MBTI personality types, he's particularly sensitive to emotional changes in people around him and himself, so he often gets caught in emotional whirlpools. He was also one of Jason's regular counseling clients.

As a tech guy who often interacts with AI, one day when he was feeling down, he experimentally turned to AI to express his sadness. The results were surprisingly good. The AI model not only helped him analyze the causes of his current situation but also gave him many practical and effective methods for emotional regulation. Leo returned to his dorm with a wealth of insights.

This made him realize AI models' natural advantages in precisely managing emotions and response speed. However, most Chinese AI products don't do well in user experience—models only have context within the current conversation, lacking local and global memory functions. This isn't very useful for psychological counseling, as users have to resend their background information and struggles to the AI every time.

In one conversation, as a developer proficient in Python, Java, and other programming languages, Leo proposed a bold idea: Could they build a model that combines peer-like empathy with structured technical support—a digital platform that maintains the warmth of human connection while providing instant responses and more effective risk management?

<!-- 0621GroupPhoto.png -->
![Team Photo](/assets/0621GroupPhoto.png)
*Figure 2: ReachIn team photo on presentation day, Jason on the left, Leo on the right*

## Technical Architecture: Not Just a Chatbot, But an Intelligent Companion

The ReachIn platform goes far beyond traditional chatbot concepts. From a technical perspective, it's a full-stack solution with modern architecture:

**Frontend Tech Stack:**
 - Vue.js + TypeScript: Provides responsive user interface for efficiency
 - Pinia state management: Ensures smooth user experience, improving performance and maintainability
 - TailwindCSS: Creates clean and warm design, reducing CSS redundancy and improving access speed

**Backend Tech Stack:**
 - FastAPI + Python: High-performance asynchronous API service supporting high concurrency
 - SQLAlchemy: Reliable data management, with Java-written core startup scripts
 - Milvus vector database: Core of AI memory system, supporting efficient vector storage and retrieval
 - MongoDB: Flexible conversation storage supporting complex queries and analysis, plus full-text storage

<!-- 0621Vue.png -->

![Frontend Architecture](/assets/0621Vue.png)
*Figure 3: ReachIn Frontend Architecture*

But if that's all, it would just be another "wrapper" chatbot. ReachIn's core lies in its intelligent agent design:

1. **Ultimate Trust and Control**
    - We don't want users to feel monitored. To provide a safe space, users can choose the AI agent's name, personality response style, etc.
    - Users can also upload their "resume" to help the AI system understand them faster
    - Users can delete conversation records anytime or lock conversations that require password access (backend uses AES encryption for text data, referencing **Privacy Vault**)
    - Users can choose AI context or what human counselors can see, ensuring privacy remains firmly in their control
    
2. **Smart Memory System**:
    - Divided into short-term and long-term memory, users can manage all memories
    - AI based on vector database can remember user preferences, important people and events, naturally referencing them in future conversations
    - Users can reference any memory anytime or adjust and delete memories

<!-- 0621LeoTrial.png -->
![Leo Trial](/assets/0621LeoTrial.png)
*Figure 4: Showing ReachIn platform's customization features*

3. **Character and Event Cards**:
    - Users can track key people or moments, and AI will use them as relevant reference points
    - This feature allows users to easily mention events or people in new conversations and continue discussions without re-explaining background each time

4. **Multi-Model Selection**:
    - Users can choose the AI model that best suits them, customizing interactions to match their comfort zone
    - Choose models based on user preferences, like DeepSeek for better Chinese writing, GPT-4.1 for more rational objectivity, Claude for better care

<!-- 0621ModelSelect.png -->
![Model Selection](/assets/0621ModelSelect.png)
*Figure 5: Showing ReachIn platform's multi-model selection feature*

5. **Privacy Vault**:
    - Users can set password protection for specific conversations, with all data deletable or exportable anytime
    - Through AES encryption technology and six-digit numeric passwords, ensuring users feel privacy security while providing technical protection

6. **Seamless Handoff**:
    - When professional intervention is detected as needed, the system can smoothly guide users toward human counselors
    - Users can choose what context counselors see, ensuring privacy and trust
    - When emergencies occur (like suicide risk), the system automatically triggers emergency response mechanisms, communicating with user-set emergency contacts to ensure safety
    - User safety always comes first

<!-- 0621HumanHandoff.png -->

![Human Handoff](/assets/0621HumanHandoff.png)
*Figure 6: Showing ReachIn platform's human handoff feature*

## Development Journey: From Idea to Reality in Four Weeks

ReachIn platform development coincided with the school's final project, giving the two teens four complete weeks to dedicate to product research and development. By combining AI-assisted programming and using pre-written components and reusing previously developed code, the development team created an MVP product in four weeks.

### Week 1: Basic Architecture Setup
The team first clarified the core problems to solve and target users, began building basic backend architecture including user registration/login and basic conversation features. They also completed frontend user interface design and single conversation interaction implementation. During this time, Leo and Jason had extensive discussions, determining the product's core features and problems the MVP version needed to solve.

<!-- 0621MindMap.png -->
![Mind Map](/assets/0621MindMap.png)
*Figure 7: Showing ReachIn platform's mind map*

<!-- 0621DiscussionRecording.png -->
![Discussion Recording](/assets/0621DiscussionRecording.png)
*Figure 8: Discussion records about software features during the discussion process*

<!-- 0621OldUIDesign.png -->
![Old UI Design](/assets/0621OldUIDesign.png)
*Figure 9: Old UI design, later replaced*

### Week 2: AI Intelligence Upgrade
This week was the key period for technical breakthroughs. We optimized backend code execution, taught AI to call tools and store memories, and optimized prompts to make AI respond to user confusion from a warmer, more professional perspective. We also built vector databases and MongoDB databases, transforming local testing into deployable multi-user form.

<!-- 0621FastAPI.png -->
![FastAPI Architecture](/assets/0621FastAPI.png)
*Figure 8: ReachIn platform using FastAPI and SQLAlchemy architecture*

<!-- 0621Backend.png -->
![Backend Logs](/assets/0621Backend.png)
*Figure 9: Testing platform backend logs*

<!-- 0621MongoDB_display_and_python_debugging.png -->
![MongoDB and Python Debugging](/assets/0621MongoDB_display_and_python_debugging.png)
*Figure 10: MongoDB database display and Python debugging, development process screenshots*

### Week 3: User Experience Optimization
The team focused on frontend optimization, ensuring frontend features adapted to backend updates, implementing user information customization, multi-conversation management, memory rendering, thinking rendering, and various card rendering features.

<!-- 0621RefineSS.png -->
![User Experience Optimization](/assets/0621RefineSS.png)
*Figure 9: MVP platform frontend user experience optimization*

### Week 4: Testing and Iteration
The final week involved small-scale testing and fixing key bugs, including frontend-backend communication inconsistencies and data inconsistencies. The team used strict Git workflow management, completing a total of **18K lines of frontend code and 33K lines of backend code**.

![Github Screenshot](/assets/S_20250529_001.png) 
*Figure 10: Backend GitHub repository*
![Commits Screenshot](/assets/S_20250529_002.png) 
*Figure 11: Backend GitHub commit records*
![Contribution Screenshot](/assets/S_20250529_004.png)
*Figure 12: Frontend contribution records*

## Community Validation: Let the Data Speak

After four weeks, on the school's product presentation day, we introduced our product and released a survey about school counseling platform usage.

### Surprising User Research Findings

Results showed AI platform acceptance significantly exceeded traditional counseling:
- AI mental health support platform usage willingness average: **3.28 points**
- Traditional counseling help-seeking willingness average: **2.44 points**
- Students showing high willingness (4-5 points) for AI platform: **52.8%**

<!-- 0621AiWilling.png -->
![AI Platform Usage Willingness](/assets/0621AIWilling.png)
*Figure 13: AI mental health support platform usage willingness survey results*

Meanwhile, among the 40 valid survey responses collected, we found over 60% of students believe their main emotional distress causes include identity and self-worth confusion, excessive academic pressure, and family conflicts with parent-child communication issues. Over 50% also chose interpersonal relationship conflicts.

We analyzed users' main concerns in depth:

- **Privacy Security Concerns**: 50% of users worry about data security
- **AI Empathy Ability Doubts**: 66.7% of users think AI lacks human counselors' empathy
- **Professional Credibility Questions**: 36.1% of users question the professionalism and reliability of AI advice

Addressing these concerns, ReachIn adopted the following solutions (which further validated our ideas):

- **Implement anonymous registration and data encryption with global control** to maximize user privacy protection
- **Through warm conversation design and personalized memory**, enhance AI's emotional connection capability while using RAG technology to provide AI with professional psychological counseling knowledge base
- **Establish collaboration mechanisms with professional counselors** to ensure advice professionalism and reliability, while ensuring professionals can intervene when necessary

### Community Response and Beta Recruitment

**38.9% of research participants voluntarily signed up for beta testing**, a number far exceeding our expectations. User feedback showed ReachIn successfully solved key pain points of traditional mental health services:

> "This platform really makes me feel safe, completely without worrying about others' opinions, able to express my true feelings without fear of judgment."
> —— Anonymous user (Grade 11)

> "I just uploaded my personal resume, and the AI actually remembered my previously mentioned family situation, naturally referencing my past struggles in subsequent conversations. This made me feel like talking with a close friend."
> —— Anonymous user (Grade 10)

## Going Further: Our Mission and Global Impact

### Model Innovation: From "Replacement" to "Bridge"

Unlike many AI applications on the market that try to replace traditional counseling, ReachIn has clearly positioned itself as a **"pre-counseling interface"** from the beginning—not to replace professional counselors, but to become a warm bridge connecting students with professional help.

This positioning solves a core contradiction in mental health services: **How to provide support to students at the exact moment they need help most—not weeks later during an appointment?**

<!-- 0621mermaid-diagram-final.png -->
![ReachIn Architecture Diagram](/assets/0621mermaid-diagram-final.png)
*Figure 14: Bridge model diagram*

**ReachIn's "bridge function" specifically manifests in:**

1. **Emotional Preparation Phase**: Helping students organize thoughts and identify problem cores before seeking professional counseling
2. **Memory Building Process**: Helping students build clear emotional records and pattern recognition through AI conversations
3. **Lowering Psychological Barriers**: Letting students adapt to "talking about mental health" in a pressure-free environment
4. **Seamless Referral Mechanism**: When AI detects need for professional intervention, smoothly guiding students to seek human counseling

### Global Applicability and Localization Potential

Our research found that while teen mental health problems manifest differently globally, core barriers are highly similar:

- **Cultural Level**: In Asian cultural contexts, mental health issues are often seen as signs of "weakness," with discussion heavily stigmatized (many students think: I'm not sick, why should I get counseling?)
- **Resource Level**: In developed Western countries, professional counseling resources are scarce, with appointment wait times lasting weeks or even months
- **Capacity Level**: In developing regions, there's a lack of sufficient trained professionals (like Africa, Southeast Asia, etc.)

ReachIn's technical solution has high **replicability and cultural adaptability**. The platform's core architecture can be customized for different regions' cultural backgrounds, language environments, and educational systems, while maintaining unified standards for underlying AI technology and privacy protection mechanisms.

<!-- 0621PreperationBeforePresentation.png -->
![Preparation Before Presentation](/assets/0621PreperationBeforePresentation.png)
*Figure 15: Material preparation before the presentation*

### Deep Collaboration with Professional Institutions

Our collaborative dialogue with the school's Psychological Counseling Center (PCC) brought an important turning point in project development. This conversation gave us deep understanding of professional mental health service boundaries and responsibilities, and redesigned ReachIn's role positioning.

**The new collaboration model isn't competitive but complementary ecosystem:**

- **AI's Responsibilities**: 24/7 emotional support, daily stress relief, preliminary risk screening, user education guidance
- **Professional Counselors' Focus Areas**: Complex psychological problem diagnosis, crisis intervention, deep therapy, long-term recovery guidance
- **Collaboration Mechanisms**: Establish standardized referral processes, share desensitized user insights, create clear ethical boundaries

We call this model **First Step Communication**—that is, before communicating with professional counselors, first receiving preliminary emotional support and problem identification through AI. Or in day-and-night companionship, helping users relieve daily small emotions (we believe emotions accumulate and eventually become mental illness), thereby reducing professional counselors' workload.

This model's greatest value lies in: **It creates incremental value for the mental health service ecosystem, rather than zero-sum competition.** AI handles large amounts of daily, repetitive emotional support needs, allowing professional counselors to invest limited time and energy into complex cases that truly require human professional judgment.

<!-- 0621OurResearchPaper.png -->
![Our Research Paper](/assets/0621OurResearchPaper.png)
*Figure 15: Our research survey report (in paper form)*

## Reflection and Learning: Young Innovators' Growth Journey

### Challenges and Breakthroughs

**Time Management Lessons:**
As a two-person team, Leo took on almost all programming work, including frontend and backend development. Although the team made work plans, they often faced delays due to misjudging workload and time requirements. This experience taught them to more carefully assess time needs in future projects.

**Communication Collaboration Optimization:**
In the second week of development, the team experienced an important communication crisis. Jason was responsible for information gathering, Leo for coding, but they lacked close communication (like daily meetings), causing Leo's implemented features to not match Jason's research findings. By establishing daily meetings and communication mechanisms, the team quickly resolved this issue.

**Technical Architecture Evolution:**
From the initial simple local application to the final distributed cloud architecture, the team also experienced important growth in technical choices. Using Docker containerization, independent database deployment, frontend-backend separation, and other technologies gave them experience with real software development processes serving society.

## Conclusion

Although the 4-week Capstone ended, our project and WeService continue. We will keep going, working to make ReachIn a mental health support platform with local community, national, and even international impact.

ReachIn is just the beginning. We believe that with more young innovators joining, and with further integration of technology and humanistic care, mental health support will become more accessible, timely, and effective. What matters isn't how advanced the technology is, but whether it can truly serve human wellbeing.

Experience ReachIn platform: http://chat.mura.ink/ (Not yet open)

Project open-source address will be released soon, please stay tuned for our updates.

If this article inspires you, please share it with more friends who care about teen mental health. Every share might reach that young heart searching for light in the darkness.

Last edited: 2025-06-30 18:46