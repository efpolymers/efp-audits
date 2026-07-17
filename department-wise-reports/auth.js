(function() {
    const PASSCODE = "EFPolymer2026";
    const AUTH_KEY = 'reports_auth_expiry';
    const AUTH_DURATION = 2 * 60 * 60 * 1000; // 2 hours

    function checkAuth() {
        const expiry = localStorage.getItem(AUTH_KEY);
        if (expiry && Date.now() < parseInt(expiry)) {
            localStorage.setItem(AUTH_KEY, Date.now() + AUTH_DURATION);
            return true;
        }
        return false;
    }

    function initAuthUI() {
        const authDiv = document.createElement('div');
        authDiv.id = 'auth-overlay';
        authDiv.style.cssText = 'position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #EDEFF1; z-index: 2147483647; display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: "Segoe UI", system-ui, sans-serif;';
        
        authDiv.innerHTML = `
            <div style="background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); text-align: center; max-width: 400px; width: 90%; border: 1px solid #D8DEE5;">
                <h2 style="color: #3F4B5C; margin-bottom: 8px; font-size: 20px; font-weight: 600;">Restricted Access</h2>
                <p style="color: #6B7785; margin-bottom: 24px; font-size: 14px;">Please enter the passcode to view this document.</p>
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <input type="password" id="auth-passcode" placeholder="Enter Passcode" style="padding: 10px 14px; border: 1px solid #D8DEE5; border-radius: 4px; font-size: 14px; outline: none;" onfocus="this.style.borderColor='#6b4fc8'" onblur="this.style.borderColor='#D8DEE5'">
                    <button id="auth-submit" style="padding: 10px 14px; background: #3F4B5C; color: white; border: none; border-radius: 4px; font-size: 14px; font-weight: 500; cursor: pointer;">Unlock Document</button>
                    <div id="auth-error" style="color: #A32E24; font-size: 13px; display: none; margin-top: 8px;">Incorrect passcode. Please try again.</div>
                </div>
            </div>
        `;
        
        // Hide all original content
        Array.from(document.body.children).forEach(child => {
            if(child.id !== 'auth-overlay') child.style.display = 'none';
        });
        
        document.body.appendChild(authDiv);
        document.documentElement.style.display = ''; 
        
        const submitBtn = authDiv.querySelector('#auth-submit');
        const inputField = authDiv.querySelector('#auth-passcode');
        
        const attemptUnlock = () => {
            if (inputField.value === PASSCODE) {
                localStorage.setItem(AUTH_KEY, Date.now() + AUTH_DURATION);
                window.location.reload();
            } else {
                authDiv.querySelector('#auth-error').style.display = 'block';
                inputField.value = '';
            }
        };

        submitBtn.addEventListener('click', attemptUnlock);
        inputField.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') attemptUnlock();
        });
    }

    if (!checkAuth()) {
        document.documentElement.style.display = 'none'; 
        document.addEventListener('DOMContentLoaded', initAuthUI);
    }
})();
