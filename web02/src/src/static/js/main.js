async function submit() {
    const u = btoa(window.username.value);
    const p = btoa(window.password.value);
    // Fetch users
    let response = await fetch("/api/users.php");
    const users = await response.json();
    // Check credentials
    possible_users = users.filter((x) => x.username === u && x.password === p);
    if (possible_users.length > 0) {
        const user = possible_users[0];
        document.cookie = `username=${atob(user.username)};SameSite=Strict;`;
        document.cookie = `password=${atob(user.password)};SameSite=Strict;`;
        window.location.href = "/";
    } else {
        alert("Invalid credentials");
    }
}
