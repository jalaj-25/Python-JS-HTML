document.getElementById('add-btn').addEventListener('click', function() {
    const taskText = document.getElementById('todo-input').value;

    if (taskText !== "") {
        const todoList = document.getElementById('todo-list');
        const listItem = document.createElement('li');
        const taskSpan = document.createElement('span');
        taskSpan.textContent = taskText;

        // Append the task text to the list item
        listItem.appendChild(taskSpan);

        // Create delete button for the list item
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = '×';
        deleteBtn.className = 'delete-btn';
        
        // Append the list item to the to-do list
        todoList.appendChild(listItem);

        // Append delete button to the list item
        listItem.appendChild(deleteBtn);

        // Clear the input field
        document.getElementById('todo-input').value = '';

        // Add event listener to delete the item when the delete button is clicked
        deleteBtn.addEventListener('click', function() {
            todoList.removeChild(listItem);
        });

        // Add event listener to toggle the 'completed' class only when clicking the task text
        taskSpan.addEventListener('click', function() {
            taskSpan.classList.toggle('completed');
        });
    }
});
