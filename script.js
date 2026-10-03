document.getElementById('loginForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const regNumber = document.getElementById('regNumber').value;
  const password = document.getElementById('password').value;

  // OAuth2PasswordRequestForm requires URL-encoded body
  const formData = new URLSearchParams();
  formData.append('username', regNumber);
  formData.append('password', password);

  try {
    const response = await fetch('http://localhost:8000/api/v1/auth/exam-login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || 'Login failed');
    }

    // Store JWT token for subsequent protected API requests
    localStorage.setItem('token', data.access_token);
    alert('Login successful!');
    
  } catch (error) {
    alert(error.message);
  }
});

async function getAllStudents() {
  const token = localStorage.getItem('token');

  if (!token) {
    alert('No token found. Please log in first.');
    return;
  }

  try {
    const response = await fetch('http://localhost:8000/api/students/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    if (response.status === 401) {
      // Token invalid or expired
      localStorage.removeItem('token');
      alert('Session expired. Please log in again.');
      return;
    }

    if (!response.ok) {
      throw new Error(`Server returned status: ${response.status}`);
    }

    const students = await response.json();
    // for (let i = 0;i<= 400; i++){
    //   document.querySelector('.students-list').innerHTML +=`<li>${students[i]['full_name']}  -  ${students[i]['reg_number']}</li>`
      
    // }
    
    // return students;
    // return students

  } catch (error) {
    console.error('Error fetching students:', error);
  }
}

// Call the function
// getAllStudents();


async function displayStudents() {
  const students = await getAllStudents();
  if (!students) return;

  const listContainer = document.getElementById('studentList');
  listContainer.innerHTML = ''; // Clear existing content

  students.forEach(student => {
    const li = document.createElement('li');
    // Adjust field names according to your StudentModel (e.g., student.reg_number, student.name)
    li.textContent = `${student.reg_number} - ${student.full_name || 'Student'}`;
    listContainer.appendChild(li);
  });
}

displayStudents();