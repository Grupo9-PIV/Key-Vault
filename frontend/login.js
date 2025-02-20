document.getElementById('request-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const token = Math.random().toString(36).substr(2); // Gerar token

    // Enviar email com token via EmailJS
    emailjs.send("SEU_SERVICE_ID", "SEU_TEMPLATE_ID", {
      to_email: email,
      token: token
    })
    .then(function(response) {
      alert('Email enviado com sucesso!');
      // Salve o token no LocalStorage (para simplicidade) ou em algum armazenamento seguro
      localStorage.setItem('reset_token', token);
    }, function(error) {
      console.error('Erro:', error);
    });
    
  });