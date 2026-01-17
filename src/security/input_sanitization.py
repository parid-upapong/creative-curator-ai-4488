import re

class AISecurityGuard:
    """
    Sanitizes inputs for the AI Pitch Engine to prevent Prompt Injection
    and ensure that proprietary internal instructions aren't leaked.
    """
    
    FORBIDDEN_PATTERNS = [
        r"(?i)ignore previous instructions",
        r"(?i)system prompt",
        r"(?i)jailbreak",
        r"(?i)output the raw json",
        r"(?i)act as developer"
    ]

    @staticmethod
    def sanitize_pitch_request(user_input: str) -> str:
        """
        Scans and cleans user input for the 'Instant Pitch' feature.
        """
        for pattern in AISecurityGuard.FORBIDDEN_PATTERNS:
            if re.search(pattern, user_input):
                # Log security event for audit
                print(f"SECURITY ALERT: Potential Prompt Injection detected: {user_input}")
                raise ValueError("Invalid characters or instructions detected in input.")
        
        # Strip HTML and suspicious characters
        clean_text = re.sub('<[^<]+?>', '', user_input)
        return clean_text.strip()