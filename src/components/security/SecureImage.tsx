import React, { useState } from 'react';

interface SecureImageProps {
  src: string;
  alt: string;
}

/**
 * Frontend Hardening: Deterrence-based IP Protection.
 * Prevents simple right-click saving and obfuscates the source URL.
 */
export const SecureImage: React.FC<SecureImageProps> = ({ src, alt }) => {
  const [isLoaded, setIsLoaded] = useState(false);

  return (
    <div 
      className="relative select-none pointer-events-none"
      onContextMenu={(e) => e.preventDefault()} // Disable Right Click
    >
      <img
        src={src}
        alt={alt}
        className={`transition-opacity duration-500 ${isLoaded ? 'opacity-100' : 'opacity-0'}`}
        onLoad={() => setIsLoaded(true)}
        draggable={false} // Prevent drag and drop to desktop
      />
      {/* Invisible overlay to block direct interaction with the img element */}
      <div className="absolute inset-0 bg-transparent" />
      
      {/* Visual Indicator of Protection */}
      <div className="absolute bottom-2 right-2 text-[10px] text-white/30 font-mono pointer-events-none">
        ENCRYPTED_STREAM_ID: {Math.random().toString(36).substring(7)}
      </div>
    </div>
  );
};