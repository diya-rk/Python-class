
let students = JSON.parse(localStorage.getItem("students")) || [];

const form = document.getElementById("studentForm");
const table = document.getElementById("studentTable");
const message = document.getElementById("message");
const average = document.getElementById("average");
const emptyState = document.getElementById("emptyState");
const studentCount = document.getElementById("studentCount");

// Save student data in localStorage
const saveStudents = () => {
    localStorage.setItem("students", JSON.stringify(students));
};

// Display student records in the table
const displayStudents = () => {
    table.innerHTML = "";

    students.forEach((student) => {
        const row = document.createElement("tr");

        if (student.marks < 50) {
            row.classList.add("fail");
        } else {
            row.classList.add("pass");
        }

        const nameCell = document.createElement("td");
        const subjectCell = document.createElement("td");
        const marksCell = document.createElement("td");
        const resultCell = document.createElement("td");

        nameCell.textContent = student.name;
        subjectCell.textContent = student.subject;
        marksCell.textContent = student.marks;

        const badge = document.createElement("span");
        badge.classList.add("result-badge");

        if (student.marks >= 50) {
            badge.textContent = "Pass";
            badge.classList.add("result-pass");
        } else {
            badge.textContent = "Fail";
            badge.classList.add("result-fail");
        }

        resultCell.appendChild(badge);

        row.append(
            nameCell,
            subjectCell,
            marksCell,
            resultCell
        );

        table.appendChild(row);
    });

    emptyState.style.display =
        students.length === 0 ? "block" : "none";

    studentCount.textContent =
        students.length + (students.length === 1 ? " student" : " students");

    saveStudents();
};

// Display a temporary message
const showMessage = (text, type) => {
    message.textContent = text;
    message.className = "message " + type;

    setTimeout(() => {
        message.textContent = "";
        message.className = "message";
    }, 3000);
};

// Add a student
form.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const subject = document.getElementById("subject").value.trim();
    const marksValue = document.getElementById("marks").value;

    if (name === "" || subject === "" || marksValue === "") {
        showMessage("Please fill in all fields.", "error");
        return;
    }

    const marks = Number(marksValue);

    if (!Number.isFinite(marks) || marks < 0 || marks > 100) {
        showMessage("Marks must be between 0 and 100.", "error");
        return;
    }

    const student = {
        name: name,
        subject: subject,
        marks: marks
    };

    students.push(student);

    displayStudents();
    form.reset();

    showMessage("Student added successfully!", "success");
});

// Calculate average using reduce()
document.getElementById("averageBtn")
    .addEventListener("click", () => {

        if (students.length === 0) {
            average.textContent = "--";
            showMessage("No student records available.", "error");
            return;
        }

        const total = students.reduce(
            (sum, student) => sum + student.marks,
            0
        );

        const averageMarks = total / students.length;

        average.textContent = averageMarks.toFixed(2);
    });

// Remove a student by name using filter()
document.getElementById("removeBtn")
    .addEventListener("click", () => {

        if (students.length === 0) {
            showMessage("There are no records to remove.", "error");
            return;
        }

        const name = prompt("Enter the student name to remove:");

        if (name === null || name.trim() === "") {
            return;
        }

        const originalLength = students.length;

        students = students.filter(
            (student) =>
                student.name.toLowerCase() !== name.trim().toLowerCase()
        );

        if (students.length === originalLength) {
            showMessage("Student not found.", "error");
        } else {
            displayStudents();
            average.textContent = "--";
            showMessage("Student record removed successfully!", "success");
        }
    });

// Callback function example
function processStudents(callback) {
    callback();
}

// Load saved records when the page opens
processStudents(displayStudents);
