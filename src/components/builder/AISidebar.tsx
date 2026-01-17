'use client';
import React from 'react';
import { motion } from 'framer-motion';
import { Activity, Zap, CheckCircle2, BarChart3 } from 'lucide-react';

export const AISidebar = ({ assets }: { assets: any[] }) => {
  const isAnalyzing = assets.some(a => a.status === 'analyzing');
  const completedAssets = assets.filter(a => a.status === 'completed');

  return (
    <aside className="w-80 border-l border-white/10 p-6 flex flex-col gap-6 overflow-y-auto">
      <div className="glass-panel p-4 border-indigo-500/30 bg-indigo-500/5">
        <div className="flex items-center gap-2 mb-3">
          <Zap className="text-indigo-400 w-5 h-5" />
          <h3 className="font-bold text-sm">AI ANALYSIS ENGINE</h3>
        </div>
        <div className="space-y-3">
          <div className="flex justify-between text-xs text-gray-400">
            <span>Schema Alignment (JSON-C)</span>
            <span>{isAnalyzing ? 'Processing...' : '100%'}</span>
          </div>
          <div className="w-full bg-white/10 h-1.5 rounded-full overflow-hidden">
            <motion.div 
              initial={{ width: 0 }}
              animate={{ width: isAnalyzing ? '70%' : '100%' }}
              className="h-full bg-indigo-500"
            />
          </div>
        </div>
      </div>

      <div className="space-y-4">
        <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider">Project Insights</h4>
        {completedAssets.length > 0 ? (
          completedAssets.map((asset, i) => (
            <motion.div 
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              key={i} 
              className="glass-panel p-4 text-sm"
            >
              <div className="flex items-center gap-2 mb-2 text-indigo-300">
                <BarChart3 size={14} />
                <span className="font-medium">Style: {asset.aiMetadata.style}</span>
              </div>
              <div className="grid grid-cols-2 gap-2 mt-3">
                {asset.aiMetadata.tags.map((tag: string) => (
                  <span key={tag} className="text-[10px] bg-white/5 border border-white/10 px-2 py-1 rounded text-gray-300 capitalize">
                    # {tag}
                  </span>
                ))}
              </div>
            </motion.div>
          ))
        ) : (
          <div className="text-center py-12 border-2 border-dashed border-white/5 rounded-xl">
            <Activity className="w-8 h-8 text-white/20 mx-auto mb-2 animate-pulse" />
            <p className="text-xs text-gray-500 px-4">Upload assets to begin AI scoring</p>
          </div>
        )}
      </div>
    </aside>
  );
};