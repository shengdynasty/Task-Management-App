import React, { useState } from 'react';

const TaskList = ({ tasks, onUpdateTask }) => {
  const [draggedTask, setDraggedTask] = useState(null);

  const handleDragStart = (e, task) => {
    setDraggedTask(task);
    e.dataTransfer.effectAllowed = 'move';
  };

  const handleDrop = (e, status) => {
    e.preventDefault();
    if (draggedTask && draggedTask.status !== status) {
      onUpdateTask(draggedTask.id, { 
        status,
        updatedAt: new Date().toISOString()
      });
      setDraggedTask(null);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
  };

  return (
    <div className="task-board">
      {['todo', 'in-progress', 'done'].map(status => (
        <div
          key={status}
          className="task-column"
          onDrop={(e) => handleDrop(e, status)}
          onDragOver={handleDragOver}
        >
          <h3 className="column-header">
            {status.replace('-', ' ').toUpperCase()}
            <span className="task-count">
              ({tasks.filter(task => task.status === status).length})
            </span>
          </h3>
          {tasks.filter(task => task.status === status).map(task => (
            <TaskCard
              key={task.id}
              task={task}
              onDragStart={handleDragStart}
              draggable
            />
          ))}
        </div>
      ))}
    </div>
  );
};

export default TaskList;
