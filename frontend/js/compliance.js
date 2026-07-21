// ==========================================
// Compliance Intelligence JavaScript
// frontend/js/compliance.js
// ==========================================

const API = "http://localhost:8000/api/compliance";


// ==========================================
// Upload Multiple Policy PDFs
// ==========================================
async function uploadPolicies() {

    const files = document.getElementById("policyFiles").files;

    if (files.length === 0) {
        alert("Please select one or more policy PDFs.");
        return;
    }

    let formData = new FormData();

    for (let i = 0; i < files.length; i++) {
        formData.append("files", files[i]);
    }


    document.getElementById("policyStatus").innerHTML =
        "Uploading policies...";


    try {

        const response = await fetch(API + "/upload-policies", {

            method: "POST",

            body: formData

        });


        const data = await response.json();


        document.getElementById("policyStatus").innerHTML =
            `${data.uploaded} policy file(s) uploaded successfully.`;

    }


    catch (err) {

        console.log(err);


        document.getElementById("policyStatus").innerHTML =
            "Upload failed.";

    }

}



// ==========================================
// Upload Complaint
// ==========================================
async function uploadComplaint() {


    const file = document.getElementById("complaintFile").files[0];


    if (!file) {

        alert("Please select a complaint file.");

        return;

    }


    let formData = new FormData();


    formData.append(
        "file",
        file
    );


    document.getElementById("complaintStatus").innerHTML =
        "Uploading complaint...";



    try {


        const response = await fetch(API + "/upload-complaint", {


            method: "POST",


            body: formData


        });



        const data = await response.json();



        document.getElementById("complaintStatus").innerHTML =
            "Complaint uploaded successfully.";

    }



    catch (err) {


        console.log(err);


        document.getElementById("complaintStatus").innerHTML =
            "Upload failed.";

    }

}



// ==========================================
// Analyze Complaint
// ==========================================
async function analyzeComplaint() {


    document.getElementById("analysisResult").value =
        "Analyzing complaint...\nPlease wait...";


    try {


        const response = await fetch(API + "/analyze", {


            method: "POST"


        });



        const data = await response.json();



        document.getElementById("analysisResult").value =
            data.report || JSON.stringify(data, null, 2);

    }



    catch (err) {


        console.log(err);


        document.getElementById("analysisResult").value =
            "Analysis failed.";

    }

}



// ==========================================
// Compliance Chat
// ==========================================
async function askCompliance() {


    const question =
        document.getElementById("chatQuestion").value;



    if (question.trim() === "") {

        return;

    }



    document.getElementById("chatAnswer").value =
        "Thinking...";



    try {


        const response = await fetch(API + "/chat", {


            method: "POST",


            headers: {


                "Content-Type": "application/json"


            },


            body: JSON.stringify({


                question: question


            })


        });



        const data = await response.json();



        document.getElementById("chatAnswer").value =
            data.answer;



    }



    catch (err) {


        console.log(err);



        document.getElementById("chatAnswer").value =
            "Unable to get response.";

    }

}