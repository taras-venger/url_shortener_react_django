import React, { useState, useRef } from 'react';
import { Form, Button } from 'react-bootstrap';
import axios from 'axios';

function CustomForm() {
  const [state, setState] = useState({
    originalURL: '',
    shortURL: '',
    lifetimeDays: 90
  });
  const urlRef = useRef(null);
  const timeRef = useRef(null);

  const handleSubmit = e => {
    e.preventDefault();
    const url = urlRef.current.value;
    const time = timeRef.current.value;
    axios
      .post('http://127.0.0.1:8000/api/create/', {
        original_url: url,
        lifetime_days: time
      })
      .then(res =>
        setState({
          originalURL: url,
          shortURL: res.data.short_url,
          lifetimeDays: time
        })
      )
      .catch(err => console.log(err.message));
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group>
        <Form.Label>Original URL address</Form.Label>
        <Form.Control
          ref={urlRef}
          className='original'
          type='text'
          placeholder='Input URL address here'
        />
      </Form.Group>
      <Form.Group>
        <Form.Label>Active, days</Form.Label>
        <Form.Control
          ref={timeRef}
          type='number'
          min={1}
          max={365}
          defaultValue={state.lifetimeDays}
        />
      </Form.Group>
      <Form.Group>
        <Form.Label>Short URL</Form.Label>
        <Form.Control type='text' defaultValue={state.shortURL} />
      </Form.Group>
      <Button variant='primary' type='submit'>
        Submit
      </Button>
    </Form>
  );
}

export default CustomForm;
