---
title: "AI-driven development with bolt"
emoji: "⛳"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["bolt", "AI", "react", "ai driven"]
published: true
publication_name: "nislab"
---
## TL;DR
⛳ Learn how to leverage bolt and Vercel for AI-driven development.
This article explains the steps to build a portfolio site with almost no code. Below is an example of the completed image.
https://masuda-yosuke.vercel.app/

## 使用するツール
- GitHub: Code hosting and version control
- bolt.new: AI-powered development platform
- Vercel: hosting service for easy application deployment

## Introduction
Among the large number of tools available these days to assist development, I tried AI-driven development using a service called “bolt” this time.
My impression is that this service is “very useful.
Although its use is limited, most of the applications can be developed with this service if they are not large scale applications.
Since this service uses React, it is easy to use, especially for those who are familiar with React.
However, if you need back-end processing, you will need to prepare a separate API.
In my opinion, in most cases, the business logic is dependent on the backend, so I think a human should still be responsible for that.
In this article, I will explain step-by-step how to create a portfolio website using this service.
Anyone who has never been good at design or front-end development, or even those who have never developed before, will be able to perform AI-driven development.

## Registering an account
### 1. Github
First, create a Github account.
https://github.com/

### 2. bolt
Next, create a bolt account. At this time, you can smoothly create a repository by linking it to your Github account.
https://bolt.new/

### 3. vercel
Finally, create a vercel account. At this point, you can link it to your Github account to facilitate deployment.
https://vercel.com/

## Creation of portfolio websites
### Configuration
The following is the information for the portfolio we will be creating.
- Header
	- Name: [Enter your name here]
	- Short Introduction: [Enter a brief introduction such as "Software Engineer" here]
	- Navigation Links:
		- About Me
		- Projects
		- Skills
		- Contact
- About Me
	- Expertise and Interests: [Example: Specialized in front-end development with a keen interest in the latest UI/UX design trends]
	- Key Skills: [Example: React, TypeScript, AWS, CI/CD]
	- Personal Background: [Example: Enjoys music production and is passionate about intuitive usability in UX design]
- Experience:
	- Title: [Example: Backend Development for Large-scale Systems]
		- Position: [Example: Software Engineer]
		- Job Description: [Example: Responsible for designing the system architecture of an app called 〇〇]
		- Company: [Example: ABC Technology]
	- Title: [Example: Backend Development for Large-scale Systems]
		- Position: [Example: Software Engineer]
		- Job Description: [Example: Responsible for designing the system architecture of an app called 〇〇]
		- Company: [Example: ABC Technology]
- Projects
	- Project Name: [Example: Task Management App]
		- Description: [Example: An application that simplifies task sharing and progress tracking among team members]
		- Links:
			- GitHub: [GitHub link]
			- Live URL: [Live website URL]
		- Image URL: [Project screenshot URL]
	- Project Name: [Example: IoT Home Security System]
		- Description: [Example: A system that enhances home security using IoT devices]
		- Links:
			- GitHub: [GitHub link]
			- Live URL: [Live website URL]
		- Image URL: [Project screenshot URL]
- Skills
	- Front-end: [Example: HTML, CSS, JavaScript, React, Tailwind CSS]
	- Back-end: [Example: Node.js, Express, Python, SQL, MongoDB]
	- Tools: [Example: Git, Docker, Terraform]
	- Others: [Example: AWS, CI/CD, Test Automation]
- Links
	- Email Address: [Example: yourname@example.com]
	- GitHub: [GitHub URL]
	- Zenn: [Zenn URL]
	- X (formerly Twitter): []
	- Instagram: []
	- LinkedIn: []


:::details Copy
```markdown
- Header
	- Name: [Enter your name here]
	- Short Introduction: [Enter a brief introduction such as "Software Engineer" here]
	- Navigation Links:
		- About Me
		- Projects
		- Skills
		- Contact
- About Me
	- Expertise and Interests: [Example: Specialized in front-end development with a keen interest in the latest UI/UX design trends]
	- Key Skills: [Example: React, TypeScript, AWS, CI/CD]
	- Personal Background: [Example: Enjoys music production and is passionate about intuitive usability in UX design]
- Experience:
	- Title: [Example: Backend Development for Large-scale Systems]
		- Position: [Example: Software Engineer]
		- Job Description: [Example: Responsible for designing the system architecture of an app called 〇〇]
		- Company: [Example: ABC Technology]
	- Title: [Example: Backend Development for Large-scale Systems]
		- Position: [Example: Software Engineer]
		- Job Description: [Example: Responsible for designing the system architecture of an app called 〇〇]
		- Company: [Example: ABC Technology]
- Projects
	- Project Name: [Example: Task Management App]
		- Description: [Example: An application that simplifies task sharing and progress tracking among team members]
		- Links:
			- GitHub: [GitHub link]
			- Live URL: [Live website URL]
		- Image URL: [Project screenshot URL]
	- Project Name: [Example: IoT Home Security System]
		- Description: [Example: A system that enhances home security using IoT devices]
		- Links:
			- GitHub: [GitHub link]
			- Live URL: [Live website URL]
		- Image URL: [Project screenshot URL]

- Skills
	- Front-end: [Example: HTML, CSS, JavaScript, React, Tailwind CSS]
	- Back-end: [Example: Node.js, Express, Python, SQL, MongoDB]
	- Tools: [Example: Git, Docker, Terraform]
	- Others: [Example: AWS, CI/CD, Test Automation]
- Links
	- Email Address: [Example: yourname@example.com]
	- GitHub: [GitHub URL]
	- Zenn: [Zenn URL]
	- X (formerly Twitter): []
	- Instagram: []
	- LinkedIn: []
```
:::

### creation procedure
1. Open [bolt.new](https://bolt.new/).
2. Enter the following prompt.
```bash
Create a portfolio website for engineers and programmers using React. Use the details below to construct each section and design a professional, simple, and intuitive layout.  
Base the design on the attached image.

# Section Details

### 1. Header
- **Name**: Display the person's name in the header (e.g., `[Enter your name here]`).
- **Short Introduction**: Provide a brief self-introduction (e.g., `[Example: Software Engineer]`).
- **Navigation Links**:
  - Include links to easily navigate to each section of the website.
  - Example links: About Me, Projects, Skills, Contact.

### 2. About Me
- **Expertise and Interests**: Highlight your expertise and areas of interest in technology (e.g., `[Specialized in front-end development with a keen interest in the latest UI/UX design trends]`).
- **Key Skills**: List programming languages and tech stacks you are proficient in (e.g., `[React, TypeScript, AWS, CI/CD]`).
- **Personal Background**: Write about hobbies, inspirations, and what drives you (e.g., `[Enjoys music production and is passionate about intuitive usability in UX design]`).

### 3. Experience
Include the following information for each experience:
- **Title**: The title or role of the experience (e.g., `[Backend Development for Large-scale Systems]`).
- **Position**: The position you held (e.g., `[Software Engineer]`).
- **Job Description**: Details about your responsibilities (e.g., `[Designed the system architecture of an app called 〇〇]`).
- **Company**: The company you worked for (e.g., `[ABC Technology]`).

### 4. Projects
Present details for each project in the following format:
- **Project Name**: Provide the project title (e.g., `[Task Management App]`).
- **Description**: Briefly describe the project's purpose and features (e.g., `[An application that simplifies task sharing and progress tracking among team members]`).
- **Links**: Include links, if available.
  - GitHub link (e.g., `[GitHub link]`).
  - Live website URL (e.g., `[Live website URL]`).
- **Image URL**: Add a link to a screenshot of the project (e.g., `[Project screenshot URL]`).

### 5. Skills
Categorize and list your technical skills. Use `react-icons/fa` or `react-icons/si` to display icons for each skill where applicable.
- **Front-end**: [Example: `HTML, CSS, JavaScript, React, Tailwind CSS`]
- **Back-end**: [Example: `Node.js, Express, Python, SQL, MongoDB`]
- **Tools**: [Example: `Git, Docker, Terraform`]
- **Others**: [Example: `AWS, CI/CD, Test Automation`]

### 6. Links (Contact and Social Media)
- Email Address: (e.g., `[yourname@example.com]`)
- GitHub: (e.g., `[GitHub URL]`)
- Zenn: (e.g., `[Zenn URL]`)
- X (formerly Twitter): Add if applicable.
- Instagram: Add if applicable.
- LinkedIn: Add if applicable.

---

# Output Format

Create a data structure designed for building the portfolio in HTML or JSX. The structure should be readable as React components and organized into individual sections.

# Output Example (JSX Format)

```jsx
export default function Portfolio() {
  return (
    <>
      <Header
        name="[Enter your name here]"
        intro="[Example: Software Engineer]"
        links={["About Me", "Projects", "Skills", "Contact"]}
      />
      <About
        expertise="[Example: Specialized in front-end development with a keen interest in the latest UI/UX design trends]"
        skills={["React", "TypeScript", "AWS", "CI/CD"]}
        background="[Example: Enjoys music production and is passionate about intuitive usability in UX design]"
      />
      {/* Add other sections in a similar structure */}
    </>
  );
}
\```
# Notes
Since some information may not always be available, implement flexible rendering for each section. For optional fields that are empty, consider hiding those fields in the output.

# Information
<Enter the details from the above structure here.>
```
3. Attach a screenshot of your favorite design.
:::message
Please ensure that the uploaded file is less than 5MB.
:::
4. After a while, bolt will start creating the project.
:::message alert
When errors occur, fix them yourself or have bolt resolve them for you!
In the free version, 150,000 tokens can be used per day.
Try to resolve errors that you can resolve yourself.
:::
5. If successful, the following will be displayed
![](/images/2024-11-21-portfolio-with-bolt/bolt-1.png)
:::message
If it does not appear, please press the reload button in bolt.
:::
6. Click on “Open in StackBlitz” in the upper right corner to open the project in StackBlitz.
7. Click on “Create a Repository” under PROJECT on the left to create a repository.
![](/images/2024-11-21-portfolio-with-bolt/bolt-2.png)
8. Enter a repository name and click “Create a Repository”.
:::message alert
If you are using Vercel for free, be sure not to make it Private.
:::
![](/images/2024-11-21-portfolio-with-bolt/bolt-3.png)
9. Once created, you will see the StackBlitz project associated with the repository.
![](/images/2024-11-21-portfolio-with-bolt/bolt-4.png)
10. Go to [Github] (https://github.com/) and verify that the repository has been created.
![](/images/2024-11-21-portfolio-with-bolt/github-1.png)
11. Click on the created repository
![](/images/2024-11-21-portfolio-with-bolt/github-2.png)
12. README.md contains a link to the StackBlitz project.
![](/images/2024-11-21-portfolio-with-bolt/github-3.png)
13. Having reached this point, proceed to the next step of deploying to [VERCEL] (https://vercel.com/).
14. Click on “Add New Project” in the upper right corner.
![](/images/2024-11-21-portfolio-with-bolt/vercel-1.png)
15. Import the repository you just created
![](/images/2024-11-21-portfolio-with-bolt/vercel-2.png)
16. Enter the Project Name and click “Deploy” with the default settings.
![](/images/2024-11-21-portfolio-with-bolt/vercel-4.png)
17. If the deployment is successful, the following will be displayed. Click “Continue to Dashboard” to confirm the deployed site.
![](/images/2024-11-21-portfolio-with-bolt/vercel-5.png)
18. The dashboard of the deployed site will be displayed.
![](/images/2024-11-21-portfolio-with-bolt/vercel-6.png)
19. Domainsの右側にあるURLをクリックすると、デプロイされたサイトが表示されます。
![](/images/2024-11-21-portfolio-with-bolt/app-0.png)

## Finally
This is how to perform AI-driven development.
Anyone could easily develop front-end applications.
We hope you will use this service to give shape to your own ideas.
If you have any questions or feedback, please let me know in the comments!