const express = require('express');
const app = express();

const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// POST endpoint
app.post('/your-endpoint', (req, res) => {
  console.log('POST /your-endpoint called');
  console.log('Body:', req.body);

  res.json({ message: 'POST received', data: req.body });
});

app.listen(port, () => {
  console.log(`Express server running on port ${port}`);
});

