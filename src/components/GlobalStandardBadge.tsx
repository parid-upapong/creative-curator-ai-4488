/**
 * GlobalStandardBadge.tsx
 * A UI component representing the 'Standardized' status for the platform.
 */

import React from 'react';

interface BadgeProps {
  score: number;
  level: 'Elite' | 'Standard' | 'Pro';
}

export const GlobalStandardBadge: React.FC<BadgeProps> = ({ score, level }) => {
  return (
    <div className="flex items-center p-2 rounded-lg bg-black text-white border-gold border-2">
      <div className="mr-3">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="gold">
          <path d="M12 2L1 21h22L12 2zm0 4.5l7.5 13H4.5L12 6.5z"/>
        </svg>
      </div>
      <div>
        <p className="text-xs uppercase font-bold tracking-widest text-gray-400">AI-Verified Standard</p>
        <p className="text-lg font-black">{level} - {score}% Match Rate</p>
      </div>
    </div>
  );
};

export default GlobalStandardBadge;