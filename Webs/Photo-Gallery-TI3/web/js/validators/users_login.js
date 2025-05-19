"use strict";

const userValidator = {
    validateRegister: function (formData) {     
        let errors = [];
        
        let username = formData.get("username");
        let password = formData.get("password");

        if (username.length < 3) {
            errors.push("Name al menos 3 caracteres");
        }
    
        return errors;
    }
};

export { userValidator };