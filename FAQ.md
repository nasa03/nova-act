# Frequently Asked Questions

## Getting Access

### Question 1: How do I get access to Nova Act?
You can request access to Nova Act through: https://nova.amazon.com/act. Sign in with your amazon.com account and click the button Sign up. You will be included in the waitlist; our team is actively working to allowlist all users in the waitlist. Currently, Nova Act is only available for US-based users.

### Question 2: I signed up yesterday and it said something like "check back in an hour" for the Api Key. However, it still says "Signed up" and I still haven't received any type of email. About how long did you all have to wait for access?
We are actively allowlisting users mostly during business hours. If you signed up during business hours, you should be allowlisted within couple hours. If you signed up after business hours, you should expect to be allowlisted in the next business day. Note that the email confirmation may take longer to reach.

### Question 3: Can I connect Nova Act with my AWS account?
No, Nova Act is not available as an AWS product, but AWS employees are more than welcome to try it out. During this experimental phase, you need to sign up using your amazon.com account. Refer to Question 1 to check how to access Nova Act. 

### Question 4: I have an external customer. Can my customer join the Nova Act preview?
Yes, everybody can join Nova Act preview. Ask you customer to request sign up following the steps described in Question 1.

### Question 5: Do we have details about pricing?
Nova act is a research preview which is free to use. Customers get a daily quota of requests.

## Technical Questions

### Question 6: Can Nova Act handle authentication and passwords?
For security reasons, Nova Act has guardrails that prevent it from handling password inputs or sensitive authentication data. We recommend to use PlayWright APIs for these cases. Check the section about how to enter sensitive information in our documentation: Entering sensitive information.

### Question 7: Can this model be used for general computer use style use cases as well?
Currently, Nova Act is limited to browser automation only. We do not support direct computer use yet. However, we have been able to do simple things by launching a browser window pointed to a remote desktop OS VM and then actuating the window. 

### Question 8: Is Nova Act compatible with LangChain or other tools?
Nova act is an independent agentic system in itself so it works end-to-end from act() call to the model. It is not intended to be integrated with LangChain nor do I think you need it here! 

## Capabilities

### Question 9: What can Nova Act do?
Below are few things that Nova Act can do:

* Interact with web interfaces
* Extract information from web pages
* Perform automated UI tasks

### Question 10: Did the Nova Act team publish any performance metrics using the standard public benchmarks?
Yes, you can refer to the benchmark metrics we published in your blog post (link). We've focused on scoring >90% on internal evals of capabilities that trip up other models, like date picking, drop downs, and popups, and achieve best-in-class performance on benchmarks like ScreenSpot and GroundUI Web which most directly measure the ability for our model to actuate the web.

## Documentation & Resources

### Question 11: I created a workflow with Nova Act, how can I share this with the community?
We highly encourage users to share your workflow with others in the community. Please make a Pull Request (PR) with your script in the Nova Act GitHub sample folder (https://github.com/aws/nova-act/tree/main/src/nova_act/samples). Our team will analyze your workflow and, if approved, it will be merged in our repository.

### Question 12: Where can I find more information?
Resources available include:

* Nova Act Web Page: https://nova.amazon.com/act
* Nova Act Blog Post: https://labs.amazon.science/blog/nova-act
* GitHub repository: https://github.com/aws/nova-act
* Code samples: https://github.com/aws/nova-act/tree/main/src/nova_act/samples

