*** Settings ***
Library    email_bot.EmailBot

*** Variables ***
${SUBJECT}    Re: Your email
${SENDER_EMAIL}    goyal11.gopal@gmail.com   # replace with the real email

*** Test Cases ***
Draft And Send Email Reply
    Log     Fetching latest email from ${SENDER_EMAIL}
    ${content}=    Get Email Content From Sender    ${SENDER_EMAIL}
    Should Not Be Empty    ${content}

    Log     Drafting reply using OpenAI
    ${reply}=    Draft Email Reply    ${content}
    Log     Sending reply: ${reply}

    Send Email Reply    ${SENDER_EMAIL}    ${SUBJECT}    ${reply}
    Log     Email reply sent successfully!
