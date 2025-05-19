"use strict";

const userValidator = {
    validateRegister: function (formData) {     
        let errors = [];
        
        let firstName = formData.get("firstName");
        let lastName = formData.get("lastName");
        let password = formData.get("password");
        let password2 = formData.get("password2");

        if (firstName.length < 3 || lastName.length < 3) {
            errors.push("Name al menos 3 caracteres");
        }
    
        if (password != password2) {
            errors.push("Password debe coincidir");
        }
        return errors;
    }
};

export { userValidator };