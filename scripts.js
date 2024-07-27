document.addEventListener('DOMcontentloaded',() => {
   const form = document.getElementaryById('todo-form');
   const todoList = document.getElementaryById('todo-list');

   const loadTodos = async () => {
      const response = await fetch('/todos');
      if (response.ok) {
         const todos = await response.json();
         todos.forEach(todo => {
            const listitem = document.createElement('li');
            listitem.textcontent = todo;
            todoList.appendchild(listitem);
         })
      }
   }
})

form.addeventlistner('submit',async (event) => {
   event.preventdefault();
   const newtodo = document.getElementaryById('new-todo').value;

   const response = await fetch('/add',{
      method: 'POST',
      headers: {
         'content-type': 'application/x-www-form-urlencoded'
      },
      body: 'new-todo=${encodeURLComponent(newTodo)}'
   });

   if (response.ok) {
      const todoitem = await response.text();
      const listitem = document.createElement('li');
      listitem.textcontent = todoitem;
      todolist.appendchild(listitem);
      form.reset();
   }
});

loadTodos();